from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld, World
from worlds.LauncherComponents import Component, components, launch_subprocess, Type
from .Items import X2WOTCItem, item_table, item_display_name_to_key, disable_item
from .Locations import location_table, disable_location
from .Regions import create_regions
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
        # Disable Alien Hunters
        if self.options.disable_alien_hunters:
            for loc_name, loc_data in location_table.items():
                if loc_data.dlc == "AH":
                    item_name = loc_data.normal_item
                    self.disable_loc_item_pair(loc_name, item_name)

        # Disable Integrated DLC
        if self.options.disable_integrated_dlc:
            self.disable_loc_item_pair(
                "ExperimentalWeapons",
                "ExperimentalWeaponsCompleted"
            )

    def create_item(self, name: str) -> X2WOTCItem:
        item_name = item_display_name_to_key[name]
        return X2WOTCItem(self.player, item_name)
    
    def create_items(self):
        for item_data in item_table.values():
            if item_data.type not in ["Event", "Disabled"]:
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

    def disable_loc_item_pair(self, loc_name: str, item_name: str):
        disable_location(loc_name)
        disable_item(item_name)
