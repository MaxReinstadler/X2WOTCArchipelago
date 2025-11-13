import asyncio
import os
import re
from typing import Any
import zipfile

from CommonClient import (
    ClientCommandProcessor,
    server_loop,
    get_base_parser,
    gui_enabled,
    logger
)
import settings
from Utils import async_start, open_filename, tuplize_version
try:
    from worlds.tracker.TrackerClient import TrackerGameContext as SuperContext  # type: ignore
except ModuleNotFoundError:
    from CommonClient import CommonContext as SuperContext

from .EnemyRando import EnemyRandoManager
from .Options import HintResearchProjects
from .Proxy import run_proxy
from .Version import client_version, minimum_world_version, minimum_mod_version

from .mods import mods_data, mod_names


class X2WOTCCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: SuperContext):
        super().__init__(ctx)

    def _cmd_version(self) -> bool:
        """Print client version info."""
        self.output(
            f"Client version: {client_version}\n"
            f"Minimum world version: {minimum_world_version}\n"
            f"Minimum mod version: {minimum_mod_version}"
        )
        return True

    def _cmd_proxy(self, port: str = "") -> bool:
        """Start the proxy server with a specific port number."""
        if port == "":
            self.output(f"Current proxy port: {self.ctx.proxy_port}")
            return False

        try:
            port = int(port)
        except ValueError:
            self.output("Invalid port number (not an integer).")
            return False

        if port < 0 or port > 65535:
            self.output("Port number out of range (0 to 65535).")
            return False

        self.ctx.proxy_port = port
        self.ctx.start_proxy()
        self.output("Config updated. Please restart your game if it is already running.")
        return True

    def _cmd_mods(self) -> bool:
        """List all installed and active mods."""
        if mod_names:
            self.output("Installed mods:")
            for mod_name in mod_names:
                self.output(f"- {mod_name}")
        else:
            self.output("No installed mods found.")

        if self.ctx.active_mods:
            self.output("Active mods:")
            for mod_name in self.ctx.active_mods:
                self.output(f"- {mod_name}")

            missing_mods = [mod_name for mod_name in self.ctx.active_mods if mod_name not in mod_names]
            if missing_mods:
                self.output("These mods are active but not installed:")
                for mod_name in missing_mods:
                    self.output(f"- {mod_name}")
                self.output("Please use the same apworld that was used to generate the multiworld.")
        else:
            self.output("No active mods found.")

        return True

    def _cmd_install_mod(self) -> bool:
        """Install a mod. Never install mods from untrusted sources and without prior inspection."""
        mod_path = open_filename("Select mod file", [("x2wotc mod", [".py", ".zip"])])
        if not mod_path:
            self.output("No file selected.")
            return False

        apworld_path = f"{__file__.split(".apworld")[0]}.apworld"
        arcname = f"x2wotc/mods/{os.path.basename(mod_path)}"
        with zipfile.ZipFile(apworld_path, "a") as apworld_file:

            # If the mod is a .py file, add it directly to the archive
            if mod_path.endswith(".py"):
                apworld_file.write(mod_path, arcname=arcname)

            # If the mod is a .zip file, extract its contents and add them to the archive
            if mod_path.endswith(".zip"):
                with zipfile.ZipFile(mod_path, "r") as mod_zip_file:
                    for file_name in mod_zip_file.namelist():
                        arcname = f"x2wotc/mods/{file_name}"
                        with mod_zip_file.open(file_name) as file:
                            apworld_file.writestr(arcname, file.read())

        self.output("Mod installed. Please restart the client.")
        return True

    def _cmd_clear_mods(self) -> bool:
        """Uninstall all mods."""
        apworld_path = f"{__file__.split(".apworld")[0]}.apworld"
        temp_path = f"{apworld_path}.tmp"

        with zipfile.ZipFile(apworld_path, "r") as apworld_file:
            with zipfile.ZipFile(temp_path, "w") as temp_file:
                for file_name in apworld_file.namelist():
                    if not file_name.startswith("x2wotc/mods/") or file_name == "x2wotc/mods/__init__.py":
                        with apworld_file.open(file_name) as file:
                            temp_file.writestr(file_name, file.read())
        os.replace(temp_path, apworld_path)

        self.output("All mods uninstalled. Please restart the client.")
        return True


class X2WOTCContext(SuperContext):
    command_processor = X2WOTCCommandProcessor
    game = "XCOM 2 War of the Chosen"
    items_handling = 0b111  # full remote
    tags = {"AP"}

    class DualEvent:
        def __init__(self):
            self._set_event = asyncio.Event()
            self._clear_event = asyncio.Event()
            self._clear_event.set()

        def set(self):
            self._set_event.set()
            self._clear_event.clear()

        def clear(self):
            self._set_event.clear()
            self._clear_event.set()

        def is_set(self):
            return self._set_event.is_set()

        def wait(self):
            return self._set_event.wait()

        def wait_clear(self):
            return self._clear_event.wait()

    connected: DualEvent
    scouted: DualEvent

    proxy_port: int
    proxy_task: asyncio.Task | None

    slot_data: dict[str, Any]
    active_mods: list[str]

    def __init__(self, server_address: str | None, password: str | None):
        super().__init__(server_address, password)
        self.locations_checked = set()
        self.locations_scouted = set()

        self.connected = self.DualEvent()
        self.scouted = self.DualEvent()

        self.proxy_port = 24728
        self.proxy_task = None

        self.slot_data = {}
        self.active_mods = []

        self.enemy_rando_manager = EnemyRandoManager()

        self.game_path: str = settings.get_settings()["x2wotc_options"]["game_path"]

        # Check for the mod config file in the manual installation paths first,
        # then fall back to the Steam installation path if it doesn't exist
        manuals = [
            "/XCom2-WarOfTheChosen/XComGame/Mods/WOTCArchipelago/Config/XComWOTCArchipelago.ini",
            "/XCom2-WarOfTheChosen/XComGame/Mods/3281191663/Config/XComWOTCArchipelago.ini",
        ]
        steam = "/workshop/content/268500/3281191663/Config/XComWOTCArchipelago.ini"  # after /steamapps

        for manual in manuals:
            self.config_file = self.game_path + manual
            if os.path.isfile(self.config_file):
                break
        else:
            self.config_file = self.game_path.split("/common/")[0] + steam

        self.spoiler_file = self.config_file.replace("XComWOTCArchipelago.ini", "XComWOTCArchipelago_Spoiler.ini")
        self.encounters_file = self.config_file.replace("XComWOTCArchipelago.ini", "XComEncounters.ini")
        self.encounter_lists_file = self.config_file.replace("XComWOTCArchipelago.ini", "XComEncounterLists.ini")

        if (not os.path.isfile(self.config_file) or not os.path.isfile(self.spoiler_file)
            or not os.path.isfile(self.encounters_file) or not os.path.isfile(self.encounter_lists_file)):
            raise FileNotFoundError(
                "X2WOTCClient: Config file not found in game folder or Steam workshop folder. "
                "Please check the game_path setting in your `host.yaml` and make sure the mod is installed."
            )

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super().server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    async def disconnect(self, allow_autoreconnect: bool = False):
        await super().disconnect(allow_autoreconnect)
        self.locations_scouted = set()
        self.slot_data = {}
        self.active_mods = []
        self.connected.clear()
        self.scouted.clear()
        self.reset_config()

    def on_package(self, cmd: str, args: dict):
        super().on_package(cmd, args)

        if cmd == "Connected":
            self.slot_data = args["slot_data"]
            if not self.validate_versions():
                async_start(self.disconnect())
                return

            self.active_mods = sorted(self.slot_data.get("active_mods", []))
            self.enemy_rando_manager.set_enemy_shuffle(self.slot_data["enemy_shuffle"])
            self.connected.set()
            self.patch_config()
            self.update_config()
            self.patch_encounters()
            logger.info("Client connected and config updated. Please restart your game if it is already running.")

        if cmd == "LocationInfo":
            scouted_locations = set(item.location for item in args["locations"])
            if self.locations_scouted == scouted_locations:
                self.scouted.set()

    # Client only compares world and client versions;
    # mod and client versions are compared by the mod.
    def validate_versions(self) -> bool:
        world_version = self.slot_data["world_version"]
        minimum_client_version = self.slot_data["minimum_client_version"]

        if tuplize_version(world_version) < tuplize_version(minimum_world_version):
            logger.error(
                f"Client version {client_version} requires "
                f"at least world version {minimum_world_version}, "
                f"but world was generated with version {world_version}. "
                "Please revert to an older version of the client."
            )
            return False

        if tuplize_version(client_version) < tuplize_version(minimum_client_version):
            logger.error(
                f"World version {world_version} requires "
                f"at least client version {minimum_client_version}, "
                f"but client is version {client_version}. "
                "Please update to a newer version of the client."
            )
            return False

        return True

    def make_gui(self):
        ui = super().make_gui()
        ui.base_title = "Archipelago XCOM 2 War of the Chosen Client"
        return ui

    def start_proxy(self):
        if self.proxy_task:
            self.proxy_task.cancel()
        self.proxy_task = asyncio.create_task(run_proxy(self), name="proxy")
        self.update_config({"ProxyPort": str(self.proxy_port)})

    def patch_config(self):
        CLASS_PREFIX = "[WOTCArchipelago."
        CLASS_SUFFIX = "]"
        AUTO_CODE_BEGIN = "; MOD ENTRIES BEGIN\n"
        AUTO_CODE_END = "; MOD ENTRIES END\n"

        with open(self.config_file, "r") as file:
            config = file.read()

        insert_dict = {
            line[len(CLASS_PREFIX):-len(CLASS_SUFFIX)]: ""
            for line in config.splitlines()
            if line.startswith(CLASS_PREFIX) and line.endswith(CLASS_SUFFIX)
        }

        for mod_data in mods_data:
            if mod_data.name in self.active_mods:
                for key, value in mod_data.config.items():
                    if key not in insert_dict:
                        logger.error(
                            f"X2WOTCClient: Class {key} for mod {mod_data.name} "
                            "not mentioned in config file, skipping"
                        )
                        continue
                    insert_dict[key] += f"{value}\n"

        for key, value in insert_dict.items():
            class_index = config.find(CLASS_PREFIX + key + CLASS_SUFFIX)

            auto_code_begin_index = config.find(AUTO_CODE_BEGIN, class_index) + len(AUTO_CODE_BEGIN)
            auto_code_end_index = config.find(AUTO_CODE_END, class_index)

            if auto_code_end_index != -1:
                config = config[:auto_code_begin_index] + value + config[auto_code_end_index:]

        with open(self.config_file, "w") as file:
            file.write(config)

    def update_config(self, config_values: dict[str, str] = {}):
        if not config_values:
            campaign_completion_requirements = self.slot_data.get("campaign_completion_requirements", [])
            hint_research_projects = self.slot_data.get("hint_research_projects", HintResearchProjects.default)
            skip_mission_types = self.slot_data.get("skip_mission_types", [])
            disable_covert_action_risks = self.slot_data.get("disable_covert_action_risks", [])
            config_values = {
                "ClientVersion": client_version,
                "MinimumModVersion": minimum_mod_version,
                "ProxyPort": str(self.proxy_port),
                "bRequirePsiGate": str("PsiGateObjective" in campaign_completion_requirements),
                "bRequireStasisSuit": str("StasisSuitObjective" in campaign_completion_requirements),
                "bRequireAvatarCorpse": str("AvatarCorpseObjective" in campaign_completion_requirements),
                "DEF_AP_GEN_ID": f"{"".join(self.slot_data["seed_name"].split())}_{self.slot_data["player"]}",
                "DEF_HINT_TECH_LOC_PART": str(hint_research_projects == HintResearchProjects.option_partial),
                "DEF_HINT_TECH_LOC_FULL": str(hint_research_projects == HintResearchProjects.option_full),
                "DEF_SKIP_SUPPLY_RAIDS": str("SupplyRaid" in skip_mission_types),
                "DEF_SKIP_COUNCIL_MISSIONS": str("CouncilMission" in skip_mission_types),
                "DEF_SKIP_FACTION_MISSIONS": str("ResistanceOp" in skip_mission_types),
                "DEF_DISABLE_AMBUSH_RISK": str("Ambush" in disable_covert_action_risks),
                "DEF_DISABLE_CAPTURE_RISK": str("Capture" in disable_covert_action_risks),
                "DEF_SKIP_RAID_REWARD_MULT_BASE": str(float(self.slot_data.get("supply_raid_reward_base", 0)) / 100.0),
                "DEF_SKIP_RAID_REWARD_MULT_ERR": str(float(self.slot_data.get("supply_raid_reward_error", 0)) / 100.0),
                "DEF_EXTRA_XP_MULT": str(float(self.slot_data.get("extra_xp_gain", 0)) / 100.0),
                "DEF_EXTRA_CORPSES": str(self.slot_data.get("extra_corpse_gain", 0)),
                "DEF_NO_STARTING_TRAPS": str(self.slot_data.get("disable_day_one_traps", False)),
            }

        with open(self.config_file, "r") as file:
            config = file.read()

        for key, value in config_values.items():
            config = re.sub(rf"{"\n"}{re.escape(key)}=(\S*)", f"\n{key}={value}", config)

        with open(self.config_file, "w") as file:
            file.write(config)

    def reset_config(self):
        self.update_config({
            "ClientVersion": "",
            "MinimumModVersion": "",
            "DEF_AP_GEN_ID": "",
        })

    def patch_encounters(self):
        for file_path in [self.encounters_file, self.encounter_lists_file]:
            with open(file_path, "r") as file:
                old_lines = file.readlines()

            new_text = ""
            for old_line in old_lines:
                if not old_line.startswith("+"):
                    new_text += old_line

                if old_line.startswith("-"):
                    new_line = old_line.replace("-", "+", 1)
                    for placement_index, placed_index in enumerate(self.enemy_rando_manager.enemy_shuffle):
                        placement_enemy = self.enemy_rando_manager.enemy_names[placement_index]
                        new_line = new_line.replace(f"\"{placement_enemy}\"", f"[enemy_{placed_index}]")
                    for placed_index, placed_enemy in enumerate(self.enemy_rando_manager.enemy_names):
                        new_line = new_line.replace(f"[enemy_{placed_index}]", f"\"{placed_enemy}\"")
                    new_text += new_line

            with open(file_path, "w") as file:
                file.write(new_text)

    def fill_spoiler(self, entries: list[dict[str, str | int]]):
        spoiler = "[WOTCArchipelago.WOTCArchipelago_Spoiler]\n"

        # Multiworld item placements
        for entry in entries:
            spoiler += (
                "+Spoiler=("
                f"Location=\"{entry["location"]}\", "
                f"Item=\"{"".join(entry["item"].splitlines())}\", "
                f"Player=\"{"".join(entry["player"].splitlines())}\", "
                f"Game=\"{"".join(entry["game"].splitlines())}\", "
                f"bProgression={bool(entry["flags"] & 0b001)}, "
                f"bUseful={bool(entry["flags"] & 0b010)}, "
                f"bTrap={bool(entry["flags"] & 0b100)})\n"
            )

        # Enemy Rando
        if self.slot_data["enemy_rando"]:
            for placed_enemy in self.enemy_rando_manager.enemy_names:
                placement_enemy = self.enemy_rando_manager.get_placement_enemy(placed_enemy)
                spoiler += (
                    "+EnemyRando=("
                    f"DefaultTemplateName=\"{placement_enemy}\", "
                    f"OverrideTemplateName=\"{placed_enemy}\")\n"
                )

                # Stat changes
                stat_changes = self.enemy_rando_manager.get_stat_changes(placed_enemy)
                for stat_change in stat_changes:
                    spoiler += (
                        f"+CharStatChanges=("
                        f"TemplateName=\"{placed_enemy}\", "
                        f"StatType=\"{stat_change.type}\", "
                        f"Delta={stat_change.delta}, "
                        f"Minimum={stat_change.min}, "
                        f"Maximum={stat_change.max})\n"
                    )

        with open(self.spoiler_file, "w") as file:
            file.write(spoiler)


def launch():
    async def main(args):
        ctx = X2WOTCContext(args.connect, args.password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server_loop")
        ctx.start_proxy()

        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        await ctx.exit_event.wait()
        await ctx.proxy_task
        ctx.reset_config()
        await ctx.shutdown()

    import colorama

    parser = get_base_parser()
    args = parser.parse_args()

    colorama.init()
    asyncio.run(main(args))
    colorama.deinit()
