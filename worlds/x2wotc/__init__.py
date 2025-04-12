import dataclasses

from BaseClasses import Tutorial
from Options import PerGameCommonOptions
from worlds.AutoWorld import WebWorld, World
from worlds.LauncherComponents import Component, components, launch_subprocess, Type

from .Items import (
    X2WOTCItem,
    item_table,
    filler_item_table,
    item_display_name_to_key,
    init_item_vars,
    get_item_count,
    get_num_items,
    disable_item,
    enable_progressive_item,
    enable_chosen_hunt_items,
    add_filler_items
)
from .Locations import (
    location_table,
    init_location_vars,
    get_num_locations,
    is_enabled,
    disable_location
)
from .Options import X2WOTCOptions, AlienHuntersDLC, Goal
from .Regions import init_region_vars, create_regions
from .Rules import set_rules

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

    item_name_to_id = {item_data.display_name: item_data.id for item_data in item_table.values()}
    location_name_to_id = {loc_data.display_name: loc_data.id for loc_data in location_table.values()}

    filler_item_names = [item.display_name for item in filler_item_table.values()]

    options_dataclass = X2WOTCOptions
    options: X2WOTCOptions

    ut_can_gen_without_yaml = True

    def generate_early(self):
        self.init_vars()

        # Set options for UT generation
        if hasattr(self.multiworld, "re_gen_passthrough"):
            if self.game in self.multiworld.re_gen_passthrough:
                slot_data = self.multiworld.re_gen_passthrough[self.game]
                for option_name in dataclasses.fields(self.options_dataclass):
                    if option_name in slot_data:
                        getattr(self.options, option_name).value = slot_data[option_name]

        # Disable inactive mods
        for mod_data in mods_data:
            if mod_data.name not in self.options.active_mods:
                for item_name, item_data in mod_data.items.items():
                    self.disable_item(item_name)
                for loc_name, loc_data in mod_data.locations.items():
                    self.disable_location(loc_name)

        # Disable contact techs
        # This always happens for now, while I haven't committed to MCO'ing XComHQ
        # (which currently seems like the only way to fix them)
        self.disable_location("ResistanceCommunications")
        self.disable_item("ResistanceCommunicationsCompleted")
        self.disable_location("ResistanceRadio")
        self.disable_item("ResistanceRadioCompleted")

        # Set Alien Hunters locations
        if self.options.alien_hunters_dlc == AlienHuntersDLC.option_no_integrated_dlc:
            self.disable_location("ExperimentalWeapons")
            self.disable_item("ExperimentalWeaponsCompleted")

        elif self.options.alien_hunters_dlc == AlienHuntersDLC.option_no_alien_rulers:
            for loc_name, loc_data in location_table.items():
                if "kill_ruler" in loc_data.tags:
                    self.disable_location(loc_name)
                    if loc_data.normal_item:
                        self.disable_item(loc_data.normal_item)

        elif self.options.alien_hunters_dlc == AlienHuntersDLC.option_none:
            for loc_name, loc_data in location_table.items():
                if loc_data.dlc == "AH":
                    self.disable_location(loc_name)
            for item_name, item_data in item_table.items():
                if item_data.dlc == "AH":
                    self.disable_item(item_name)

        # Enable progressive tech items
        if "RifleTech" in self.options.progressive_items:
            if not self.enable_progressive_item("ProgressiveRifleTechCompleted"):
                print(f"X2WOTC: Failed to enable progressive rifle techs for player {self.player_name}")
        if "MeleeWeaponTech" in self.options.progressive_items:
            if not self.enable_progressive_item("ProgressiveMeleeTechCompleted"):
                print(f"X2WOTC: Failed to enable progressive melee techs for player {self.player_name}")
        if "ArmorTech" in self.options.progressive_items:
            if not self.enable_progressive_item("ProgressiveArmorTechCompleted"):
                print(f"X2WOTC: Failed to enable progressive armor techs for player {self.player_name}")
        if "GREMLINTech" in self.options.progressive_items:
            if not self.enable_progressive_item("ProgressiveGREMLINTechCompleted"):
                print(f"X2WOTC: Failed to enable progressive GREMLIN techs for player {self.player_name}")
        if "PsionicsTech" in self.options.progressive_items:
            if not self.enable_progressive_item("ProgressivePsionicsTechCompleted"):
                print(f"X2WOTC: Failed to enable progressive psionics techs for player {self.player_name}")

        # Force early proving ground
        if self.options.early_proving_ground:
            self.multiworld.early_items[self.player]["[Tech] ADVENT Officer Autopsy"] = 1

        # Disable Enemysanity
        if not self.options.enemy_sanity:
            for loc_name, loc_data in location_table.items():
                if loc_data.type == "EnemyKill":
                    self.disable_location(loc_name)

        # Disable Itemsanity
        if not self.options.item_sanity:
            for loc_name, loc_data in location_table.items():
                if loc_data.type == "ItemUse":
                    self.disable_location(loc_name)

        # Enable/disable Chosen Hunt-Sanity
        if self.options.chosen_hunt_sanity:
            enable_chosen_hunt_items(self.player)
        else:
            for loc_name, loc_data in location_table.items():
                if "chosen_hunt" in loc_data.tags:
                    self.disable_location(loc_name)

        # Handle mod options
        for mod_data in mods_data:
            if mod_data.generate_early and mod_data.name in self.options.active_mods:
                mod_data.generate_early(self)

        # Add filler items
        num_filler_items = get_num_locations(self.player) - get_num_items(self.player)
        print(f"X2WOTC: Adding {num_filler_items} filler items for player {self.player_name}")
        add_filler_items(self.player, num_filler_items, self.options.weapon_mod_share / 100,
                         self.options.staff_share / 100, self.options.trap_share / 100, self.random)

    def create_item(self, name: str) -> X2WOTCItem:
        item_name = item_display_name_to_key[name]
        return X2WOTCItem(self.player, item_name)
    
    def create_items(self):
        for item_name, item_data in item_table.items():
            if item_data.type != "Event":
                for i in range(get_item_count(self.player, item_name)):
                    item = self.create_item(item_data.display_name)
                    self.multiworld.itempool.append(item)

    def create_regions(self):
        create_regions(self.multiworld, self.player)

        # Place event items
        for loc_data in location_table.values():
            if loc_data.type == "Event":
                item_data = item_table[loc_data.normal_item]
                location = self.multiworld.get_location(loc_data.display_name, self.player)
                location.place_locked_item(self.create_item(item_data.display_name))

    def set_rules(self):
        set_rules(self.multiworld, self.player)
        
        for mod_data in mods_data:
            if mod_data.set_rules and mod_data.name in self.options.active_mods:
                mod_data.set_rules(self.multiworld, self.player, location_table, is_enabled)

    def get_filler_item_name(self) -> str:
        return self.random.choice(self.filler_item_names)

    def init_vars(self):
        init_item_vars(self.player)
        init_location_vars(self.player)
        init_region_vars(self.player)

    def disable_location(self, loc_name: str):
        disable_location(self.player, loc_name)

    def disable_item(self, item_name: str):
        disable_item(self.player, item_name)

    def enable_progressive_item(self, item_name: str) -> bool:
        return enable_progressive_item(self.player, item_name)
    
    def fill_slot_data(self):
        slot_data = {
            "goal_location": Goal.value_to_location[self.options.goal.value]
        }

        option_names = [attr.name for attr in dataclasses.fields(self.options_dataclass)
                        if attr not in dataclasses.fields(PerGameCommonOptions)]
        slot_data |= self.options.as_dict(*option_names)

        return slot_data
