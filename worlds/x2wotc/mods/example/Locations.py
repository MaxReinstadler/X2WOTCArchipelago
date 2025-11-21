from worlds.x2wotc.LocationData import X2WOTCLocationData, get_new_location_id


# For the full definition of X2WOTCLocationData, see worlds/x2wotc/LocationData.py
example_mod_locations: dict[str, X2WOTCLocationData] = {
    "ExampleModLocation": X2WOTCLocationData(
        display_name = "Example Mod Location",
        id = get_new_location_id(),
        layer = "Strategy",  # Or "Tactical"
        type = "ExampleType",
        tags = {"example_tag_1", "example_tag_2"},
        difficulty = 12.34,
        normal_item = "ExampleModItem"
    ),
}

locations: dict[str, X2WOTCLocationData] = {
    **example_mod_locations,
}
