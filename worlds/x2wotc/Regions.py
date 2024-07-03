from BaseClasses import MultiWorld, Region
from .Locations import X2WOTCLocation, location_table
from .Rules import has_shadow_chamber
from typing import Dict, Optional

region_table: Dict[str, Dict[str, Optional[int]]] = {
    "Menu": {},
    "Avenger": {},
    "Research Lab": {},
    "Shadow Chamber": {}
}

def create_regions(world: MultiWorld, player: int):
    # Add locations
    for loc_name, loc_data in location_table.items():
        region_name = "Avenger"

        if loc_data.type == "Disabled":
            continue

        if loc_data.type == "Event":
            if loc_name == "Victory":
                region_name = "Shadow Chamber"

        if loc_data.type == "Tech":
            if "shadow" in loc_data.tags:
                region_name = "Shadow Chamber"
            else:
                region_name = "Research Lab"

        region_table[region_name][loc_data.display_name] = loc_data.id

    # Create regions
    for region_name in region_table.keys():
        world.regions.append(create_region(world, player, region_name))

    # Connect regions
    world.get_region("Menu", player).connect(world.get_region("Avenger", player))
    world.get_region("Avenger", player).connect(world.get_region("Research Lab", player))
    world.get_region("Avenger", player).connect(world.get_region("Shadow Chamber", player),
                                        lambda state: has_shadow_chamber(state, player))

def create_region(world: MultiWorld, player: int, name: str) -> Region:
    region = Region(name, player, world)
    region.add_locations(region_table[name], X2WOTCLocation)
    return region
