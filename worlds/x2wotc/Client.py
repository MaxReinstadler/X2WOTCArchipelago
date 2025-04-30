import asyncio
import os

from CommonClient import (
    ClientCommandProcessor,
    server_loop,
    get_base_parser,
    gui_enabled,
    logger
)
import settings
try:
    from worlds.tracker.TrackerClient import TrackerGameContext as SuperContext  # type: ignore
except ModuleNotFoundError:
    from CommonClient import CommonContext as SuperContext

from .Proxy import run_proxy
from .Version import client_version, recommended_mod_version

from .mods import mods_data, mod_names


class X2WOTCCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: SuperContext):
        super().__init__(ctx)

    def _cmd_version(self) -> bool:
        """Print the version of the client."""
        self.output(f"Client version: {client_version}\nRecommended mod version: {recommended_mod_version}")
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

    def __init__(self, server_address: str | None, password: str | None):
        super().__init__(server_address, password)
        self.locations_checked = set()
        self.locations_scouted = set()

        self.connected = self.DualEvent()
        self.scouted = self.DualEvent()

        self.proxy_port = 24728
        self.proxy_task = None

        # Retrieved from slot_data on connection
        self.goal_location: str = "Victory"
        self.active_mods: list[str] = []

        self.game_path: str = settings.get_settings()["x2wotc_options"]["game_path"]
        # Check for the mod config file in the manual installation path first,
        # then fall back to the Steam installation path if it doesn't exist
        manual = "/XCom2-WarOfTheChosen/XComGame/Mods/WOTCArchipelago/Config/XComWOTCArchipelago.ini"
        steam = "/workshop/content/268500/3281191663/Config/XComWOTCArchipelago.ini"  # after /steamapps
        self.config_file: str = self.game_path + manual
        if not os.path.isfile(self.config_file):
            self.config_file = self.game_path.split("/common/")[0] + steam
        if not os.path.isfile(self.config_file):
            error = (
                "X2WOTCClient: Config file not found in game folder or Steam workshop folder. "
                "Please check the game_path setting in your `host.yaml` and make sure the mod is installed."
            )
            logger.error(error)
            raise FileNotFoundError(error)

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super().server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    async def disconnect(self, allow_autoreconnect: bool = False):
        await super().disconnect(allow_autoreconnect)
        self.locations_scouted = set()
        self.connected.clear()
        self.scouted.clear()

    def on_package(self, cmd: str, args: dict):
        super().on_package(cmd, args)
        if cmd == "Connected":
            slot_data = args["slot_data"]

            if "goal_location" not in slot_data:
                logger.warning("X2WOTCClient: slot_data missing goal_location, falling back on Victory")
                self.goal_location = "Victory"
            else:
                self.goal_location = slot_data["goal_location"]

            if "active_mods" not in slot_data:
                logger.warning("X2WOTCClient: slot_data missing active_mods, falling back on empty list")
                self.active_mods = []
            else:
                self.active_mods = sorted(slot_data["active_mods"])

            self.connected.set()
            self.patch_config()

    def make_gui(self):
        ui = super().make_gui()
        ui.base_title = "Archipelago XCOM 2 War of the Chosen Client"
        return ui

    def start_proxy(self):
        if self.proxy_task:
            self.proxy_task.cancel()
        self.proxy_task = asyncio.create_task(run_proxy(self), name="proxy")

    def patch_config(self):
        CLASS_PREFIX = "[WOTCArchipelago."
        CLASS_SUFFIX = "]"
        AUTO_CODE_BEGIN = "; AUTOGENERATED CODE BEGIN\n"
        AUTO_CODE_END = "; AUTOGENERATED CODE END\n"

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
        await ctx.shutdown()

    import colorama

    parser = get_base_parser()
    args = parser.parse_args()

    colorama.init()
    asyncio.run(main(args))
    colorama.deinit()
