from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld, World
from worlds.LauncherComponents import Component, components, launch_subprocess, Type
from .Items import X2WOTCItem, item_table, item_display_name_to_key
from .Items import init_item_vars, get_item_count, disable_item, enable_progressive_item
from .Locations import location_table, init_location_vars, disable_location
from .Regions import init_region_vars, create_regions
from .Rules import set_rules
from .Options import X2WOTCOptions

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

    options_dataclass = X2WOTCOptions
    options: X2WOTCOptions

    def generate_early(self):
        self.init_vars()

        # Disable Alien Hunters
        if self.options.disable_alien_hunters:
            for loc_name, loc_data in location_table.items():
                if loc_data.dlc == "AH":
                    item_name = loc_data.normal_item
                    self.disable_location(loc_name)
                    self.disable_item(item_name)

        # Disable Integrated DLC
        if self.options.disable_integrated_dlc:
            self.disable_location("ExperimentalWeapons")
            self.disable_item("ExperimentalWeaponsCompleted")

        # Enable progressive tech items
        if self.options.enable_progressive_rifle_techs:
            if not self.enable_progressive_item("ProgressiveRifleTechCompleted"):
                print("Failed to enable progressive rifle techs")
        if self.options.enable_progressive_melee_techs:
            if not self.enable_progressive_item("ProgressiveMeleeTechCompleted"):
                print("Failed to enable progressive melee techs")
        if self.options.enable_progressive_armor_techs:
            if not self.enable_progressive_item("ProgressiveArmorTechCompleted"):
                print("Failed to enable progressive armor techs")
        if self.options.enable_progressive_gremlin_techs:
            if not self.enable_progressive_item("ProgressiveGREMLINTechCompleted"):
                print("Failed to enable progressive GREMLIN techs")
        if self.options.enable_progressive_psionics_techs:
            if not self.enable_progressive_item("ProgressivePsionicsTechCompleted"):
                print("Failed to enable progressive psionics techs")

    def create_item(self, name: str) -> X2WOTCItem:
        item_name = item_display_name_to_key[name]
        return X2WOTCItem(self.player, item_name)
    
    def create_items(self):
        for item_name, item_data in item_table.items():
            if item_data.type != "Event":
                for i in range(self.get_item_count(item_name)):
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

    def init_vars(self):
        init_item_vars(self.player)
        init_location_vars(self.player)
        init_region_vars(self.player)

    def get_item_count(self, item_name: str) -> int:
        return get_item_count(self.player, item_name)

    def disable_location(self, loc_name: str):
        disable_location(self.player, loc_name)

    def disable_item(self, item_name: str):
        disable_item(self.player, item_name)

    def enable_progressive_item(self, item_name: str) -> bool:
        return enable_progressive_item(self.player, item_name)
