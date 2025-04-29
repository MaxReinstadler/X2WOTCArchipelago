import dataclasses

from BaseClasses import MultiWorld, Tutorial
from Options import PerGameCommonOptions
from worlds.AutoWorld import WebWorld, World
from worlds.LauncherComponents import Component, Type, components, launch_subprocess

from .Items import X2WOTCItem, ItemManager, item_display_name_to_id
from .Locations import LocationManager, loc_display_name_to_id
from .Options import X2WOTCOptions, AlienHuntersDLC, Goal
from .Regions import RegionManager
from .Rules import RuleManager

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


class X2WOTCWorld(World):
    """
    XCOM 2 is the sequel to the acclaimed turn-based tactics game about defending earth from an alien invasion.
    Outwit your enemy on the battlefield and beyond, hunt the powerful Chosen, and build up an unstoppable
    resistance to save humanity from the occupation of the Elders!"
    """

    game = "XCOM 2 War of the Chosen"
    web = X2WOTCWeb()

    item_name_to_id = item_display_name_to_id
    location_name_to_id = loc_display_name_to_id

    options_dataclass = X2WOTCOptions
    options: X2WOTCOptions

    ut_can_gen_without_yaml = True

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        self.item_manager = ItemManager()
        self.loc_manager = LocationManager()
        self.reg_manager: RegionManager = None
        self.rule_manager: RuleManager = None

    def generate_early(self):
        # RegionManager requires RuleManager which requires options
        self.rule_manager = RuleManager(self)
        self.reg_manager = RegionManager(self)

        # Set options for UT generation
        if hasattr(self.multiworld, "re_gen_passthrough"):
            if self.game in self.multiworld.re_gen_passthrough:
                slot_data = self.multiworld.re_gen_passthrough[self.game]
                for option_name in dataclasses.fields(self.options_dataclass):
                    if option_name in slot_data:
                        getattr(self.options, option_name).value = slot_data[option_name]

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
        # This always happens for now, while I haven't committed to MCO'ing XComHQ
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
        if "RifleTech" in self.options.progressive_items:
            if not self.item_manager.enable_progressive_item("ProgressiveRifleTechCompleted"):
                print(f"X2WOTC: Failed to enable progressive rifle techs for player {self.player_name}")
        if "MeleeWeaponTech" in self.options.progressive_items:
            if not self.item_manager.enable_progressive_item("ProgressiveMeleeTechCompleted"):
                print(f"X2WOTC: Failed to enable progressive melee techs for player {self.player_name}")
        if "ArmorTech" in self.options.progressive_items:
            if not self.item_manager.enable_progressive_item("ProgressiveArmorTechCompleted"):
                print(f"X2WOTC: Failed to enable progressive armor techs for player {self.player_name}")
        if "GREMLINTech" in self.options.progressive_items:
            if not self.item_manager.enable_progressive_item("ProgressiveGREMLINTechCompleted"):
                print(f"X2WOTC: Failed to enable progressive GREMLIN techs for player {self.player_name}")
        if "PsionicsTech" in self.options.progressive_items:
            if not self.item_manager.enable_progressive_item("ProgressivePsionicsTechCompleted"):
                print(f"X2WOTC: Failed to enable progressive psionics techs for player {self.player_name}")

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

        # Add filler items
        num_filler_items = self.loc_manager.num_locations - self.item_manager.num_items
        print(f"X2WOTC: Adding {num_filler_items} filler items for player {self.player_name}")
        self.item_manager.add_filler_items(
            num_filler_items,
            self.options.weapon_mod_share / 100,
            self.options.staff_share / 100,
            self.options.trap_share / 100,
            self.random
        )

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

    def fill_slot_data(self):
        slot_data = {
            "goal_location": Goal.value_to_location[self.options.goal.value]
        }

        option_names = [attr.name for attr in dataclasses.fields(self.options_dataclass)
                        if attr not in dataclasses.fields(PerGameCommonOptions)]
        slot_data |= self.options.as_dict(*option_names)

        return slot_data
