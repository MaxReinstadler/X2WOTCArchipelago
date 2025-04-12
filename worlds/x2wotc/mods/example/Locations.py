from ...LocationData import X2WOTCLocationData, base_id
from typing import Dict

mod_base_id = base_id + 1000  # Make sure IDs are unique to each mod

# For the full definition of X2WOTCLocationData, see worlds/x2wotc/Data.py
example_mod_locations: Dict[str, X2WOTCLocationData] = {
    "ExampleModLocation": X2WOTCLocationData(
        display_name = "Example Mod Location",
        id = mod_base_id,
        layer = "Strategy",  # Or "Tactical"
        type = "ExampleType",
        tags = ["example_tag_1", "example_tag_2"],
        difficulty = 12.34,
        normal_item = "ExampleModItem"
    )
}

locations: Dict[str, X2WOTCLocationData] = {
    **example_mod_locations
}
