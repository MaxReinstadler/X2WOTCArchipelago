from BaseClasses import ItemClassification

from ...ItemData import X2WOTCItemData, get_new_item_id, tech_item_prefix


# For the full definition of X2WOTCItemData, see worlds/x2wotc/ItemData.py
lwotc_items: dict[str, X2WOTCItemData] = {
    "LaserWeaponsCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Laser Weapons",
        id = get_new_item_id(),
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["weapon"],
        power = 60.0,
        normal_location = "LaserWeapons"
    ),
    "AdvancedLasersCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Advanced Laser Weapons",
        id = get_new_item_id(),
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["weapon"],
        power = 60.0,
        normal_location = "AdvancedLasers"
    ),
    "CoilgunsCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Coilguns",
        id = get_new_item_id(),
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["weapon"],
        power = 140.0,
        normal_location = "Coilguns"
    ),
    "AdvancedCoilgunsCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Advanced Coilguns",
        id = get_new_item_id(),
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["weapon"],
        power = 140.0,
        normal_location = "AdvancedCoilguns"
    ),
    "ProgressiveRifleTechLwotcCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Progressive Rifle (LWOTC)",
        id = get_new_item_id(),
        classification = ItemClassification.progression | ItemClassification.useful,
        type = "TechCompleted",
        tags = ["weapon", "progressive"],
        stages = [
            "LaserWeaponsCompleted",
            "MagnetizedWeaponsCompleted",
            "CoilgunsCompleted",
            "PlasmaRifleCompleted",
        ]
    ),
    "ProgressiveRifleTechLwotcCompleted+": X2WOTCItemData(
        display_name = tech_item_prefix + "Progressive Rifle+ (LWOTC)",
        id = get_new_item_id(),
        classification = ItemClassification.progression | ItemClassification.useful,
        type = "TechCompleted",
        tags = ["weapon", "progressive"],
        stages = [
            "ModularWeaponsCompleted",
            "LaserWeaponsCompleted",
            "MagnetizedWeaponsCompleted",
            "CoilgunsCompleted",
            "PlasmaRifleCompleted",
        ]
    ),
    "ProgressiveAdvancedWeaponTechLwotcCompleted+": X2WOTCItemData(
        display_name = tech_item_prefix + "Progressive Rifle+ (LWOTC)",
        id = get_new_item_id(),
        classification = ItemClassification.progression | ItemClassification.useful,
        type = "TechCompleted",
        tags = ["weapon", "progressive"],
        stages = [
            "AdvancedLasersCompleted",
            "GaussWeaponsCompleted",
            "AdvancedCoilgunsCompleted",
        ]
    ),
    "AutopsyDroneCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "ADVENT Robotics",
        id = get_new_item_id(),
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["weapon"],
        power = 50.0,
        normal_location = "AutopsyDrone"
    ),
    "ProgressiveGREMLINTechLwotcCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Progressive GREMLIN (LWOTC)",
        id = get_new_item_id(),
        classification = ItemClassification.progression | ItemClassification.useful,
        type = "TechCompleted",
        tags = ["utility", "weapon", "progressive"],
        stages = [
            "AutopsyDroneCompleted",
            "AutopsySectopodCompleted",
        ]
    ),
    "AutopsyMutonEliteCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Muton Elite Autopsy",
        id = get_new_item_id(),
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["weapon"],
        power = 60.0,
        normal_location = "AutopsyMutonElite"
    ),
    "EXOSuitCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Battle Armor",
        id = get_new_item_id(),
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["armor"],
        power = 120.0,
        normal_location = "EXOSuit"
    ),
    "WARSuitCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Battlesuits",
        id = get_new_item_id(),
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["armor"],
        power = 200.0,
        normal_location = "WARSuit"
    ),
    "SpiderSuitCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Mobile Armor",
        id = get_new_item_id(),
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["armor"],
        power = 120.0,
        normal_location = "SpiderSuit"
    ),
    "WraithSuitCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Shadow Armor",
        id = get_new_item_id(),
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["armor"],
        power = 200.0,
        normal_location = "WraithSuit"
    ),
}

lwotc_filler_items: dict[str, X2WOTCItemData] = {
}

# NOTE: items must include filler as well
items: dict[str, X2WOTCItemData] = {
    **lwotc_items,
    **lwotc_filler_items
}

# Mod filler items will be treated like resource items
filler_items: dict[str, X2WOTCItemData] = {
    **lwotc_filler_items
}
