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
    location_table = location_table

    loc_display_name_to_id = loc_display_name_to_id
    loc_display_name_to_key = loc_display_name_to_key
    loc_id_to_key = loc_id_to_key

    loc_types = loc_types
    loc_groups = loc_groups

    def __init__(self):
        self.enabled: dict[str, bool] = {loc_name: True for loc_name in self.location_table.keys()}
        self.num_locations: int = len(self.location_table)

    def disable_location(self, loc_name: str):
        if self.enabled[loc_name]:
            self.enabled[loc_name] = False
            self.num_locations -= 1
