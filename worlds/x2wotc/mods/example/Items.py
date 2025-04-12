from BaseClasses import ItemClassification

from ...ItemData import X2WOTCItemData, base_id


mod_base_id = base_id + 1000  # Make sure IDs are unique to each mod

# For the full definition of X2WOTCItemData, see worlds/x2wotc/ItemData.py
example_mod_items: dict[str, X2WOTCItemData] = {
    "ExampleModItem": X2WOTCItemData(
        display_name = "Example Mod Item",
        id = mod_base_id,
        classification = ItemClassification.progression,
        layer = "Strategy",  # Or "Tactical"
        type = "ExampleType",
        tags = ["example_tag_1", "example_tag_2"],
        power = 12.34,
        normal_location = "ExampleModLocation"
    )
}

example_mod_filler_items: dict[str, X2WOTCItemData] = {
    "ExampleModFillerItem": X2WOTCItemData(
        display_name = "Example Mod Filler Item",
        id = mod_base_id + 1,
        layer = "Strategy",  # Or "Tactical"
        type = "ExampleType",
        tags = ["example_tag_1", "example_tag_2"],
    )
}

# NOTE: items must include filler as well
items: dict[str, X2WOTCItemData] = {
    **example_mod_items,
    **example_mod_filler_items
}

# Mod filler items will be treated like resource items
filler_items: dict[str, X2WOTCItemData] = {
    **example_mod_filler_items
}
