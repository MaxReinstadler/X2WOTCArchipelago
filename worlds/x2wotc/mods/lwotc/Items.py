from BaseClasses import ItemClassification as IC

from ...ItemData import X2WOTCItemData, get_new_item_id, tech_item_prefix, pcs_item_prefix


# For the full definition of X2WOTCItemData, see worlds/x2wotc/ItemData.py
lwotc_items: dict[str, X2WOTCItemData] = {
    "LaserWeaponsCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Laser Weapons",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"weapon"},
        power = 50.0,
        normal_location = "LaserWeapons"
    ),
    "AdvancedLasersCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Advanced Laser Weapons",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"weapon"},
        power = 50.0,
        normal_location = "AdvancedLasers"
    ),
    "CoilgunsCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Coilguns",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"weapon"},
        power = 150.0,
        normal_location = "Coilguns"
    ),
    "AdvancedCoilgunsCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Advanced Coilguns",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"weapon"},
        power = 150.0,
        normal_location = "AdvancedCoilguns"
    ),
    "ProgressiveRifleTechLwotcCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Progressive Rifle (LWOTC)",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"weapon", "progressive"},
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
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"weapon", "progressive"},
        stages = [
            "ModularWeaponsCompleted",
            "LaserWeaponsCompleted",
            "MagnetizedWeaponsCompleted",
            "CoilgunsCompleted",
            "PlasmaRifleCompleted",
        ]
    ),
    "ProgressiveAdvancedWeaponTechLwotcCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Progressive Advanced Weapons (LWOTC)",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"weapon", "progressive"},
        stages = [
            "AdvancedLasersCompleted",
            "GaussWeaponsCompleted",
            "AdvancedCoilgunsCompleted",
        ]
    ),
    "ProgressiveHeavyArmorTechLwotcCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Progressive Heavy Armor (LWOTC)",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"armor", "progressive"},
        stages = [
            "EXOSuitCompleted",
            "WARSuitCompleted",
        ]
    ),
    "ProgressiveLightArmorTechLwotcCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Progressive Light Armor (LWOTC)",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"armor", "progressive"},
        stages = [
            "SpiderSuitCompleted",
            "WraithSuitCompleted",
        ]
    ),
    "AutopsyDroneCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "ADVENT Robotics",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"weapon"},
        power = 50.0,
        normal_location = "AutopsyDrone"
    ),
    "ProgressiveGREMLINTechLwotcCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Progressive GREMLIN (LWOTC)",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"utility", "weapon", "progressive"},
        stages = [
            "AutopsyDroneCompleted",
            "AutopsySectopodCompleted",
        ]
    ),
    "AutopsyMutonEliteCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Muton Elite Autopsy",
        id = get_new_item_id(),
        classification = IC.progression,
        type = "TechCompleted",
        tags = {"weapon"},
        power = 60.0,
        normal_location = "AutopsyMutonElite"
    ),
    "EXOSuitCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Battle Armor",
        id = get_new_item_id(),
        classification = IC.progression,
        type = "TechCompleted",
        tags = {"armor"},
        power = 120.0,
        normal_location = "EXOSuit"
    ),
    "WARSuitCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Battlesuits",
        id = get_new_item_id(),
        classification = IC.progression,
        type = "TechCompleted",
        tags = {"armor"},
        power = 200.0,
        normal_location = "WARSuit"
    ),
    "SpiderSuitCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Mobile Armor",
        id = get_new_item_id(),
        classification = IC.progression,
        type = "TechCompleted",
        tags = {"armor"},
        power = 120.0,
        normal_location = "SpiderSuit"
    ),
    "WraithSuitCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Shadow Armor",
        id = get_new_item_id(),
        classification = IC.progression,
        type = "TechCompleted",
        tags = {"armor"},
        power = 200.0,
        normal_location = "WraithSuit"
    ),
}

lwotc_filler_items: dict[str, X2WOTCItemData] = {
    "DepthPerceptionPCS:1": X2WOTCItemData(
        display_name = pcs_item_prefix + "Depth Perception",
        id = get_new_item_id(),
        type = "Resource",
        classification = IC.useful,
        tags = {"filler", "pcs", "depth_perception"},
    ),
    "HyperReactivePupilsPCS:1": X2WOTCItemData(
        display_name = pcs_item_prefix + "Hyper-Reactive Pupils",
        id = get_new_item_id(),
        type = "Resource",
        classification = IC.useful,
        tags = {"filler", "pcs", "hyper_reactive_pupils"},
    ),
    "CombatAwarenessPCS:1": X2WOTCItemData(
        display_name = pcs_item_prefix + "Unwavering Stance",
        id = get_new_item_id(),
        type = "Resource",
        classification = IC.useful,
        tags = {"filler", "pcs", "combat_awareness"},
    ),
    "CombatRushPCS:1": X2WOTCItemData(
        display_name = pcs_item_prefix + "Combat Rush",
        id = get_new_item_id(),
        type = "Resource",
        classification = IC.useful,
        tags = {"filler", "pcs", "combat_rush"},
    ),
    "DamageControlPCS:1": X2WOTCItemData(
        display_name = pcs_item_prefix + "Damage Control",
        id = get_new_item_id(),
        type = "Resource",
        classification = IC.useful,
        tags = {"filler", "pcs", "damage_control"},
    ),
    "AbsorptionFieldsPCS:1": X2WOTCItemData(
        display_name = pcs_item_prefix + "Absorption Fields",
        id = get_new_item_id(),
        type = "Resource",
        classification = IC.useful,
        tags = {"filler", "pcs", "absorption_fields"},
    ),
    "BodyShieldPCS:1": X2WOTCItemData(
        display_name = pcs_item_prefix + "Body Shield",
        id = get_new_item_id(),
        type = "Resource",
        classification = IC.useful,
        tags = {"filler", "pcs", "body_shield"},
    ),
    "EmergencyLifeSupportPCS:1": X2WOTCItemData(
        display_name = pcs_item_prefix + "Emergency Life Support",
        id = get_new_item_id(),
        type = "Resource",
        classification = IC.useful,
        tags = {"filler", "pcs", "emergency_life_support"},
    ),
    "IronSkinPCS:1": X2WOTCItemData(
        display_name = pcs_item_prefix + "Iron Skin",
        id = get_new_item_id(),
        type = "Resource",
        classification = IC.useful,
        tags = {"filler", "pcs", "iron_skin"},
    ),
    "SmartMacrophagesPCS:1": X2WOTCItemData(
        display_name = pcs_item_prefix + "Smart Macrophages",
        id = get_new_item_id(),
        type = "Resource",
        classification = IC.useful,
        tags = {"filler", "pcs", "smart_macrophages"},
    ),
    "CommonPCSDefense:1": X2WOTCItemData(
        display_name = pcs_item_prefix + "Basic Defense",
        id = get_new_item_id(),
        type = "Resource",
        tags = {"filler", "pcs", "basic", "defense"},
    ),
    "RarePCSDefense:1": X2WOTCItemData(
        display_name = pcs_item_prefix + "Advanced Defense",
        id = get_new_item_id(),
        type = "Resource",
        tags = {"filler", "pcs", "advanced", "defense"},
    ),
    "EpicPCSDefense:1": X2WOTCItemData(
        display_name = pcs_item_prefix + "Advanced Defense",
        id = get_new_item_id(),
        type = "Resource",
        classification = IC.useful,
        tags = {"filler", "pcs", "superior", "defense"},
    ),
    "CommonPCSPsi:1": X2WOTCItemData(
        display_name = pcs_item_prefix + "Basic Psi",
        id = get_new_item_id(),
        type = "Resource",
        tags = {"filler", "pcs", "basic", "psi"},
    ),
    "RarePCSPsi:1": X2WOTCItemData(
        display_name = pcs_item_prefix + "Advanced Psi",
        id = get_new_item_id(),
        type = "Resource",
        tags = {"filler", "pcs", "advanced", "psi"},
    ),
    "EpicPCSPsi:1": X2WOTCItemData(
        display_name = pcs_item_prefix + "Advanced Psi",
        id = get_new_item_id(),
        type = "Resource",
        classification = IC.useful,
        tags = {"filler", "pcs", "superior", "psi"},
    ),
    "CommonPCSHacking:1": X2WOTCItemData(
        display_name = pcs_item_prefix + "Basic Hacking",
        id = get_new_item_id(),
        type = "Resource",
        tags = {"filler", "pcs", "basic", "hacking"},
    ),
    "RarePCSHacking:1": X2WOTCItemData(
        display_name = pcs_item_prefix + "Advanced Hacking",
        id = get_new_item_id(),
        type = "Resource",
        tags = {"filler", "pcs", "advanced", "hacking"},
    ),
    "EpicPCSHacking:1": X2WOTCItemData(
        display_name = pcs_item_prefix + "Advanced Hacking",
        id = get_new_item_id(),
        type = "Resource",
        classification = IC.useful,
        tags = {"filler", "pcs", "superior", "hacking"},
    ),
}

items: dict[str, X2WOTCItemData] = {
    **lwotc_items,
    **lwotc_filler_items
}
