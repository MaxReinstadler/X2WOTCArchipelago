import dataclasses
from typing import Any, ClassVar, TextIO

from BaseClasses import CollectionState, Item, MultiWorld, Tutorial
from Options import PerGameCommonOptions, OptionError
from settings import Group, UserFolderPath
from worlds.AutoWorld import WebWorld, World
from worlds.LauncherComponents import Component, Type, components, launch_subprocess

from .EnemyRando import EnemyRandoManager
from .Items import X2WOTCItem, ItemManager, item_display_name_to_id, item_groups
from .Locations import LocationManager, loc_display_name_to_id, loc_groups
from .Options import X2WOTCOptions, AlienHuntersDLC, Goal, ChosenWeaponFragments
from .Regions import RegionManager
from .Rules import RuleManager
from .Version import minimum_client_version

from .mods import mods_data


def launch_client():
    from .Client import launch
    
    launch_subprocess(launch, name="X2WOTCClient")

components.append(Component("XCOM 2 War of the Chosen Client", "X2WOTCClient",
                            func=launch_client, component_type=Type.CLIENT))


class X2WOTCWeb(WebWorld):
    theme = "partyTime"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the XCOM 2: War of the Chosen Archipelago mod.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Snyax"]
    )]


class X2WOTCSettings(Group):
    class GamePath(UserFolderPath):
        """Path to your installation of XCOM 2, most likely ending in `/XCOM 2`"""

        description = "XCOM 2 installation folder"

    game_path: GamePath = GamePath("C:/Program Files (x86)/Steam/steamapps/common/XCOM 2")


class X2WOTCWorld(World):
    """
    XCOM 2 is the sequel to the acclaimed turn-based tactics game about defending earth from an alien invasion.
    Outwit your enemy on the battlefield and beyond, hunt the powerful Chosen, and build up an unstoppable
    resistance to save humanity from the occupation of the Elders!
    """

    game = "XCOM 2 War of the Chosen"
    web = X2WOTCWeb()

    settings: ClassVar[X2WOTCSettings]
    options_dataclass = X2WOTCOptions
    options: X2WOTCOptions

    option_names = [
        attr.name for attr in dataclasses.fields(options_dataclass)
        if attr not in dataclasses.fields(PerGameCommonOptions)
    ]

    item_name_to_id = item_display_name_to_id
    location_name_to_id = loc_display_name_to_id

    item_name_groups = item_groups
    location_name_groups = loc_groups

    ut_can_gen_without_yaml = True

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        self.item_manager = ItemManager()
        self.loc_manager = LocationManager()
        self.enemy_rando_manager = EnemyRandoManager()
        self.reg_manager: RegionManager = None
        self.rule_manager: RuleManager = None

    def generate_early(self):
        # Extract slot data for UT re-gen
        re_gen_passthrough = getattr(self.multiworld, "re_gen_passthrough", {})
        if re_gen_passthrough and self.game in re_gen_passthrough:
            slot_data = re_gen_passthrough[self.game]
            for option_name in self.option_names:
                setattr(self.options, option_name, slot_data[option_name])

            # Enemy Rando
            self.enemy_rando_manager.set_enemy_shuffle(slot_data["enemy_shuffle"])

        # Disable inactive mods...
        for mod_data in mods_data:
            if mod_data.name not in self.options.active_mods:
                for item_name, item_data in mod_data.items.items():
                    self.item_manager.disable_item(item_name)
                for loc_name, loc_data in mod_data.locations.items():
                    self.loc_manager.disable_location(loc_name)
            else:
                # ...or enable mod filler items
                for item_name in mod_data.filler_items.keys():
                    self.item_manager.enable_mod_filler_item(item_name)

        # Disable contact techs
        # This always happens for now, while I haven't committed to MCO-ing XComHQ
        # (which currently seems like the only way to fix them)
        self.loc_manager.disable_location("ResistanceCommunications")
        self.item_manager.disable_item("ResistanceCommunicationsCompleted")
        self.loc_manager.disable_location("ResistanceRadio")
        self.item_manager.disable_item("ResistanceRadioCompleted")

        # Set Alien Hunters locations
        if self.options.alien_hunters_dlc == AlienHuntersDLC.option_no_integrated_dlc:
            self.loc_manager.disable_location("ExperimentalWeapons")
            self.item_manager.disable_item("ExperimentalWeaponsCompleted")

        elif self.options.alien_hunters_dlc == AlienHuntersDLC.option_no_alien_rulers:
            for loc_name, loc_data in self.loc_manager.location_table.items():
                if "kill_ruler" in loc_data.tags:
                    self.loc_manager.disable_location(loc_name)
                    if loc_data.normal_item:
                        self.item_manager.disable_item(loc_data.normal_item)

        elif self.options.alien_hunters_dlc == AlienHuntersDLC.option_none:
            for loc_name, loc_data in self.loc_manager.location_table.items():
                if loc_data.dlc == "AH":
                    self.loc_manager.disable_location(loc_name)
            for item_name, item_data in self.item_manager.item_table.items():
                if item_data.dlc == "AH":
                    self.item_manager.disable_item(item_name)

        # Enable progressive tech items
        if "RifleTech+" in self.options.progressive_items:
            if not self.item_manager.enable_progressive_item("ProgressiveRifleTechCompleted+"):
                print(f"X2WOTC: Failed to enable progressive rifle tech+ for player {self.player_name}")
        elif "RifleTech" in self.options.progressive_items:
            if not self.item_manager.enable_progressive_item("ProgressiveRifleTechCompleted"):
                print(f"X2WOTC: Failed to enable progressive rifle tech for player {self.player_name}")
        if "ArmorTech+" in self.options.progressive_items:
            if not self.item_manager.enable_progressive_item("ProgressiveArmorTechCompleted+"):
                print(f"X2WOTC: Failed to enable progressive armor tech+ for player {self.player_name}")
        elif "ArmorTech" in self.options.progressive_items:
            if not self.item_manager.enable_progressive_item("ProgressiveArmorTechCompleted"):
                print(f"X2WOTC: Failed to enable progressive armor tech for player {self.player_name}")
        if "MeleeWeaponTech" in self.options.progressive_items:
            if not self.item_manager.enable_progressive_item("ProgressiveMeleeTechCompleted"):
                print(f"X2WOTC: Failed to enable progressive melee tech for player {self.player_name}")
        if "GREMLINTech" in self.options.progressive_items:
            if not self.item_manager.enable_progressive_item("ProgressiveGREMLINTechCompleted"):
                print(f"X2WOTC: Failed to enable progressive GREMLIN tech for player {self.player_name}")
        if "PsionicsTech" in self.options.progressive_items:
            if not self.item_manager.enable_progressive_item("ProgressivePsionicsTechCompleted"):
                print(f"X2WOTC: Failed to enable progressive psionics tech for player {self.player_name}")

        # Enable tech fragment items
        if self.options.chosen_weapon_fragments == ChosenWeaponFragments.option_two:
            if not self.item_manager.enable_progressive_item("ChosenAssassinWeaponsFragment2"):
                print(f"X2WOTC: Failed to enable Assassin weapon fragments (2) for player {self.player_name}")
            if not self.item_manager.enable_progressive_item("ChosenHunterWeaponsFragment2"):
                print(f"X2WOTC: Failed to enable Hunter weapon fragments (2) for player {self.player_name}")
            if not self.item_manager.enable_progressive_item("ChosenWarlockWeaponsFragment2"):
                print(f"X2WOTC: Failed to enable Warlock weapon fragments (2) for player {self.player_name}")
        elif self.options.chosen_weapon_fragments == ChosenWeaponFragments.option_three:
            if not self.item_manager.enable_progressive_item("ChosenAssassinWeaponsFragment3"):
                print(f"X2WOTC: Failed to enable Assassin weapon fragments (3) for player {self.player_name}")
            if not self.item_manager.enable_progressive_item("ChosenHunterWeaponsFragment3"):
                print(f"X2WOTC: Failed to enable Hunter weapon fragments (3) for player {self.player_name}")
            if not self.item_manager.enable_progressive_item("ChosenWarlockWeaponsFragment3"):
                print(f"X2WOTC: Failed to enable Warlock weapon fragments (3) for player {self.player_name}")

        # Force early proving ground
        if self.options.early_proving_ground:
            self.multiworld.early_items[self.player][
                self.item_manager.item_table["AutopsyAdventOfficerCompleted"].display_name
            ] = 1

        # Disable Enemysanity
        if not self.options.enemy_sanity:
            for loc_name, loc_data in self.loc_manager.location_table.items():
                if loc_data.type == "EnemyKill":
                    self.loc_manager.disable_location(loc_name)

        # Disable Itemsanity
        if not self.options.item_sanity:
            for loc_name, loc_data in self.loc_manager.location_table.items():
                if loc_data.type == "ItemUse":
                    self.loc_manager.disable_location(loc_name)

        # Enable/disable Chosen Hunt-Sanity
        if self.options.chosen_hunt_sanity:
            self.item_manager.enable_chosen_hunt_items()
        else:
            for loc_name, loc_data in self.loc_manager.location_table.items():
                if "chosen_hunt" in loc_data.tags:
                    self.loc_manager.disable_location(loc_name)

        # Handle mod options
        for mod_data in mods_data:
            if mod_data.generate_early and mod_data.name in self.options.active_mods:
                mod_data.generate_early(self)

        # Validate options
        num_filler_items = self.loc_manager.num_locations - self.item_manager.num_items
        if num_filler_items < 0:
            raise OptionError(
                f"X2WOTC: Too many items for player {self.player_name}. "
                f"Disable Chosen Weapon Fragments or enable at least {-num_filler_items} more location(s)."
            )

        # Add filler items
        print(f"X2WOTC: Adding {num_filler_items} filler items for player {self.player_name}")
        self.item_manager.add_filler_items(
            num_filler_items,
            self.options.weapon_mod_share / 100,
            self.options.staff_share / 100,
            self.options.trap_share / 100,
            self.random
        )

        # Shuffle enemies
        if self.options.enemy_rando:
            self.enemy_rando_manager.shuffle_enemies(self.random)

        # RegionManager requires RuleManager which needs to be initialized after generate_early
        self.rule_manager = RuleManager(self)
        self.reg_manager = RegionManager(self)

    def create_item(self, name: str) -> X2WOTCItem:
        item_name = self.item_manager.item_display_name_to_key[name]
        return X2WOTCItem(self.player, item_name)
    
    def create_items(self):
        for item_name, item_data in self.item_manager.item_table.items():
            if item_data.type != "Event":
                for i in range(self.item_manager.item_count[item_name]):
                    item = self.create_item(item_data.display_name)
                    self.multiworld.itempool.append(item)

    def create_regions(self):
        self.reg_manager.create_regions()

        # Place event items
        for loc_data in self.loc_manager.location_table.values():
            if loc_data.type == "Event":
                item_data = self.item_manager.item_table[loc_data.normal_item]
                location = self.multiworld.get_location(loc_data.display_name, self.player)
                location.place_locked_item(self.create_item(item_data.display_name))

    def set_rules(self):
        self.rule_manager.set_rules()

        for mod_data in mods_data:
            if mod_data.set_rules and mod_data.name in self.options.active_mods:
                mod_data.set_rules(self)

    def get_filler_item_name(self) -> str:
        return self.random.choice(self.item_manager.filler_item_names)

    # Invalidate power cache on collect/remove
    def collect(self, state: CollectionState, item: Item) -> bool:
        change = super().collect(state, item)
        if change and item.name in self.rule_manager.power_items:
            state.x2wotc_power_stale[self.player] = True
        return change

    def remove(self, state: CollectionState, item: Item) -> bool:
        change = super().remove(state, item)
        if change and item.name in self.rule_manager.power_items:
            state.x2wotc_power_stale[self.player] = True
        return change

    def fill_slot_data(self):
        slot_data = {
            "world_version": self.world_version.as_simple_string(),
            "minimum_client_version": minimum_client_version,
            "seed_name": self.multiworld.seed_name,
            "player": self.player,
            "goal_location": Goal.value_to_location[self.options.goal.value],
            "enemy_shuffle": self.enemy_rando_manager.enemy_shuffle,
        }

        slot_data |= self.options.as_dict(*self.option_names)
        return slot_data

    # Trigger UT re-gen
    @staticmethod
    def interpret_slot_data(slot_data: dict[str, Any]) -> dict[str, Any]:
        return slot_data

    def write_spoiler(self, spoiler_handle: TextIO):
        if self.options.enemy_rando:
            spoiler_handle.write(f"\n\n=== Enemy Rando for player {self.player_name} ===\n")
            for placement_index, placed_index in enumerate(self.enemy_rando_manager.enemy_shuffle):
                spoiler_handle.write(
                    f"{self.enemy_rando_manager.enemy_names[placement_index]} <- "
                    f"{self.enemy_rando_manager.enemy_names[placed_index]}\n"
                )
