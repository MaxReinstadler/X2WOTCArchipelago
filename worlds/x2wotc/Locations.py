from copy import deepcopy
from BaseClasses import Location

from .LocationData import location_table

from .mods import mod_locations


class X2WOTCLocation(Location):
    game: str = "XCOM 2 War of the Chosen"


# Add mod locations
for loc_name, loc_data in mod_locations.items():
    if loc_name not in location_table:
        location_table[loc_name] = loc_data
    else:
        print(f"X2WOTC: Duplicate location {loc_name} in mods, skipping")

# Lookup tables
loc_display_name_to_id = {
    loc_data.display_name: loc_data.id
    for loc_data in location_table.values()
    if loc_data.id
}
loc_display_name_to_key = {
    loc_data.display_name: key
    for key, loc_data in location_table.items()
}
loc_id_to_key = {
    loc_data.id: key
    for key, loc_data in location_table.items()
    if loc_data.id
}

# Groups
loc_types = {
    loc_data.type
    for loc_data in location_table.values()
    if loc_data.id
}
loc_groups = {
    loc_type: {
        loc_data.display_name
        for loc_data in location_table.values()
        if loc_data.id and loc_data.type == loc_type
    } for loc_type in loc_types
}


class LocationManager:
    loc_display_name_to_id = loc_display_name_to_id
    loc_display_name_to_key = loc_display_name_to_key
    loc_id_to_key = loc_id_to_key

    loc_types = loc_types
    loc_groups = loc_groups

    def __init__(self):
        self.location_table = deepcopy(location_table)
        self.locked: bool = False

        self.enabled: dict[str, bool] = {loc_name: True for loc_name in self.location_table.keys()}
        self.num_locations: int = len(self.location_table)

    def replace(self, loc_name: str, **kwargs):
        if self.locked:
            raise RuntimeError("Cannot replace location data after location manager has been locked.")

        loc_data = self.location_table[loc_name]
        self.location_table[loc_name] = loc_data.replace(**kwargs)

    def disable_location(self, loc_name: str):
        if self.locked:
            raise RuntimeError("Cannot disable locations after location manager has been locked.")

        if self.enabled[loc_name]:
            self.enabled[loc_name] = False
            self.num_locations -= 1
