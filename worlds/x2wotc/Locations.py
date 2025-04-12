from BaseClasses import Location
from .LocationData import location_table
from .mods import mod_locations
from typing import Dict

class X2WOTCLocation(Location):
    game: str = "XCOM 2 War of the Chosen"

# Add mod locations
for loc_name, loc_data in mod_locations.items():
    if loc_name not in location_table:
        location_table[loc_name] = loc_data
    else:
        print(f"X2WOTC: Duplicate location {loc_name} in mods, skipping")

loc_display_name_to_key = {loc_data.display_name: key for key, loc_data in location_table.items()}
loc_id_to_key = {loc_data.id: key for key, loc_data in location_table.items() if loc_data.id}

enabled: Dict[int, Dict[str, bool]] = {}
num_locations: Dict[int, int] = {}

def init_location_vars(player: int):
    enabled[player] = {loc_name: True for loc_name in location_table.keys()}
    num_locations[player] = len(location_table)

def is_enabled(player: int, loc_name: str) -> bool:
    return enabled[player][loc_name]

def get_num_locations(player: int) -> int:
    return num_locations[player]

def disable_location(player: int, loc_name: str):
    if enabled[player][loc_name]:
        enabled[player][loc_name] = False
        num_locations[player] -= 1
