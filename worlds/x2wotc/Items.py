from BaseClasses import Item, ItemClassification
from typing import List, Dict, NamedTuple, Optional
import random

class X2WOTCItem(Item):
    game: str = "XCOM 2 War of the Chosen"

    def __init__(self, player: int, name: str):
        item_data = item_table[name]
        super(X2WOTCItem, self).__init__(item_data.display_name,
                                         item_data.classification,
                                         item_data.id, player)

class X2WOTCItemData(NamedTuple):
    display_name: str
    id: Optional[int] = None
    classification: ItemClassification = ItemClassification.useful
    layer: str = "Strategy"  # "Strategy" or "Tactical"
    type: str = "Event"
    tags: List[str] = []
    power: float = 0.0  # Relative to other values
                        # (For reference: Magnetic Weapons = 100.0)
    dlc: Optional[str] = None   # None: Base Game,
                                # "AH": Alien Hunters,
                                # "SLG": Shens Last Gift,
                                # "WOTC": War of the Chosen
    normal_location: Optional[str] = None
    stages: Optional[List[str]] = None  # For progressive items

base_id = 2482748367

tech_item_prefix = "[Tech] "
shadow_tech_item_prefix = "[Tech] "
resource_item_prefix = "[Resource] "
weapon_mod_item_prefix = "[Upgrade] "

########################################################################################################################
##                        TECH COMPLETION ITEMS (RESEARCH PROJECTS / SHADOW PROJECTS)                                 ##
########################################################################################################################

tech_base_id = base_id

#=======================================================================================================================
#                                                 BASE GAME
#-----------------------------------------------------------------------------------------------------------------------

vanilla_weapon_tech_items: Dict[str, X2WOTCItemData] = {
    "ModularWeaponsCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Modular Weapons",
        id = tech_base_id,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["weapon"],
        power = 30.0,
        normal_location = "ModularWeapons"
    ),
    "MagnetizedWeaponsCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Magnetic Weapons",
        id = tech_base_id + 1,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["weapon"],
        power = 100.0,
        normal_location = "MagnetizedWeapons"
    ),
    "GaussWeaponsCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Gauss Weapons",
        id = tech_base_id + 2,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["weapon"],
        power = 100.0,
        normal_location = "GaussWeapons"
    ),
    "PlasmaRifleCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Plasma Rifle",
        id = tech_base_id + 3,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["weapon"],
        power = 160.0,
        normal_location = "PlasmaRifle"
    ),
    "HeavyPlasmaCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Beam Cannon",
        id = tech_base_id + 4,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["weapon"],
        power = 160.0,
        normal_location = "HeavyPlasma"
    ),
    "PlasmaSniperCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Plasma Lance",
        id = tech_base_id + 5,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["weapon"],
        power = 160.0,
        normal_location = "PlasmaSniper"
    ),
    "AlloyCannonCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Storm Gun",
        id = tech_base_id + 6,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["weapon"],
        power = 160.0,
        normal_location = "AlloyCannon"
    )
}

vanilla_armor_tech_items: Dict[str, X2WOTCItemData] = {
    "HybridMaterialsCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Hybrid Materials",
        id = tech_base_id + 7,
        classification = ItemClassification.useful,
        type = "TechCompleted",
        tags = ["armor"],
        power = 0.0,
        normal_location = "HybridMaterials"
    ),
    "PlatedArmorCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Plated Armor",
        id = tech_base_id + 8,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["armor"],
        power = 100.0,
        normal_location = "PlatedArmor"
    ),
    "PoweredArmorCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Powered Armor",
        id = tech_base_id + 9,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["armor"],
        power = 180.0,
        normal_location = "PoweredArmor"
    )
}

vanilla_autopsy_tech_items: Dict[str, X2WOTCItemData] = {
    "AutopsySectoidCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Sectoid Autopsy",
        id = tech_base_id + 10,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["utility"],
        power = 20.0,
        normal_location = "AutopsySectoid"
    ),
    "AutopsyViperCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Viper Autopsy",
        id = tech_base_id + 11,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["utility"],
        power = 25.0,
        normal_location = "AutopsyViper"
    ),
    "AutopsyMutonCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Muton Autopsy",
        id = tech_base_id + 12,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["weapon"],
        power = 75.0,
        normal_location = "AutopsyMuton"
    ),
    "AutopsyBerserkerCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Berserker Autopsy",
        id = tech_base_id + 13,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["utility"],
        power = 20.0,
        normal_location = "AutopsyBerserker"
    ),
    "AutopsyArchonCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Archon Autopsy",
        id = tech_base_id + 14,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["weapon"],
        power = 80.0,
        normal_location = "AutopsyArchon"
    ),
    "AutopsyGatekeeperCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Gatekeeper Autopsy",
        id = tech_base_id + 15,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["weapon"],
        power = 50.0,
        normal_location = "AutopsyGatekeeper"
    ),
    "AutopsyAndromedonCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Andromedon Autopsy",
        id = tech_base_id + 16,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["weapon"],
        power = 20.0,
        normal_location = "AutopsyAndromedon"
    ),
    "AutopsyFacelessCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Faceless Autopsy",
        id = tech_base_id + 17,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["utility"],
        power = 80.0,
        normal_location = "AutopsyFaceless"
    ),
    "AutopsyChryssalidCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Chryssalid Autopsy",
        id = tech_base_id + 18,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["armor"],
        power = 20.0,
        normal_location = "AutopsyChryssalid"
    ),
    "AutopsyAdventTrooperCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "ADVENT Trooper Autopsy",
        id = tech_base_id + 19,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["utility"],
        power = 20.0,
        normal_location = "AutopsyAdventTrooper"
    ),
    "AutopsyAdventStunLancerCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "ADVENT Stun Lancer Autopsy",
        id = tech_base_id + 20,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["weapon"],
        power = 70.0,
        normal_location = "AutopsyAdventStunLancer"
    ),
    "AutopsyAdventShieldbearerCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "ADVENT Shieldbearer Autopsy",
        id = tech_base_id + 21,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["armor"],
        power = 30.0,
        normal_location = "AutopsyAdventShieldbearer"
    ),
    "AutopsyAdventMECCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "ADVENT MEC Breakdown",
        id = tech_base_id + 22,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["weapon", "utility"],
        power = 100.0,
        normal_location = "AutopsyAdventMEC"
    ),
    "AutopsyAdventTurretCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "ADVENT Turret Breakdown",
        id = tech_base_id + 23,
        classification = ItemClassification.useful,
        type = "TechCompleted",
        tags = ["facility"],
        power = 0.0,
        normal_location = "AutopsyAdventTurret"
    ),
    "AutopsySectopodCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Sectopod Breakdown",
        id = tech_base_id + 24,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["weapon", "utility"],
        power = 60.0,
        normal_location = "AutopsySectopod"
    )
}

vanilla_goldenpath_tech_items: Dict[str, X2WOTCItemData] = {
    "AlienBiotechCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Alien Biotech",
        id = tech_base_id + 25,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["facility"],
        power = 20.0,
        normal_location = "AlienBiotech"
    ),
    "ResistanceCommunicationsCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Resistance Communications",
        id = tech_base_id + 26,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["facility"],
        power = 0.0,
        normal_location = "ResistanceCommunications"
    ),
    "AutopsyAdventOfficerCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "ADVENT Officer Autopsy",
        id = tech_base_id + 27,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["facility"],
        power = 150.0,
        normal_location = "AutopsyAdventOfficer"
    ),
    "AlienEncryptionCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Alien Encryption",
        id = tech_base_id + 28,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["facility"],
        power = 10.0,
        normal_location = "AlienEncryption"
    ),
    "CodexBrainPt1Completed": X2WOTCItemData(
        display_name = shadow_tech_item_prefix + "Codex Brain",
        id = tech_base_id + 29,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["mission"],
        power = 0.0,
        normal_location = "CodexBrainPt1"
    ),
    "CodexBrainPt2Completed": X2WOTCItemData(
        display_name = shadow_tech_item_prefix + "Encrypted Codex Data",
        id = tech_base_id + 30,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = [],
        power = 0.0,
        normal_location = "CodexBrainPt2"
    ),
    "BlacksiteDataCompleted": X2WOTCItemData(
        display_name = shadow_tech_item_prefix + "Blacksite Vial",
        id = tech_base_id + 31,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["mission"],
        power = 0.0,
        normal_location = "BlacksiteData"
    ),
    "ForgeStasisSuitCompleted": X2WOTCItemData(
        display_name = shadow_tech_item_prefix + "Recovered ADVENT Stasis Suit",
        id = tech_base_id + 32,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = [],
        power = 0.0,
        normal_location = "ForgeStasisSuit"
    ),
    "PsiGateCompleted": X2WOTCItemData(
        display_name = shadow_tech_item_prefix + "Psionic Gate",
        id = tech_base_id + 33,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = [],
        power = 0.0,
        normal_location = "PsiGate"
    ),
    "AutopsyAdventPsiWitchCompleted": X2WOTCItemData(
        display_name = shadow_tech_item_prefix + "Avatar Autopsy",
        id = tech_base_id + 34,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["mission"],
        power = 0.0,
        normal_location = "AutopsyAdventPsiWitch"
    )
}

vanilla_other_tech_items: Dict[str, X2WOTCItemData] = {
    "ResistanceRadioCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Resistance Radio",
        id = tech_base_id + 35,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["facility"],
        power = 0.0,
        normal_location = "ResistanceRadio"
    ),
    "EleriumCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Elerium",
        id = tech_base_id + 36,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["facility"],
        power = 15.0,
        normal_location = "Tech_Elerium"
    ),
    "PsionicsCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Psionics",
        id = tech_base_id + 37,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["facility", "weapon"],
        power = 140.0,
        normal_location = "Psionics"
    )
}

#=======================================================================================================================
#                                               ALIEN HUNTERS
#-----------------------------------------------------------------------------------------------------------------------

alien_hunters_tech_items: Dict[str, X2WOTCItemData] = {
    "ExperimentalWeaponsCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Experimental Weapons",
        id = tech_base_id + 38,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["weapon", "utility"],
        power = 70.0,
        dlc = "AH",
        normal_location = "ExperimentalWeapons"
    ),
    "AutopsyViperKingCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Viper King Autopsy",
        id = tech_base_id + 39,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["armor"],
        power = 120.0,
        dlc = "AH",
        normal_location = "AutopsyViperKing"
    ),
    "AutopsyBerserkerQueenCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Berserker Queen Autopsy",
        id = tech_base_id + 40,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["armor"],
        power = 120.0,
        dlc = "AH",
        normal_location = "AutopsyBerserkerQueen"
    ),
    "AutopsyArchonKingCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Archon King Autopsy",
        id = tech_base_id + 41,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["armor"],
        power = 130.0,
        dlc = "AH",
        normal_location = "AutopsyArchonKing"
    )
}

#=======================================================================================================================
#                                             WAR OF THE CHOSEN
#-----------------------------------------------------------------------------------------------------------------------

wotc_autopsy_tech_items: Dict[str, X2WOTCItemData] = {
    "AutopsyAdventPurifierCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "ADVENT Purifier Autopsy",
        id = tech_base_id + 42,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["armor"],
        power = 20.0,
        dlc = "WOTC",
        normal_location = "AutopsyAdventPurifier"
    ),
    "AutopsyAdventPriestCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "ADVENT Priest Autopsy",
        id = tech_base_id + 43,
        classification = ItemClassification.useful,
        type = "TechCompleted",
        tags = ["utility"],
        power = 0.0,
        dlc = "WOTC",
        normal_location = "AutopsyAdventPriest"
    ),
    "AutopsyTheLostCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "The Lost Autopsy",
        id = tech_base_id + 44,
        classification = ItemClassification.useful,
        type = "TechCompleted",
        tags = ["utility"],
        power = 0.0,
        dlc = "WOTC",
        normal_location = "AutopsyTheLost"
    ),
    "AutopsySpectreCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Spectre Autopsy",
        id = tech_base_id + 45,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["utility"],
        power = 10.0,
        dlc = "WOTC",
        normal_location = "AutopsySpectre"
    )
}

wotc_chosen_weapon_tech_items: Dict[str, X2WOTCItemData] = {
    "ChosenAssassinWeaponsCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Assassin Weapons",
        id = tech_base_id + 46,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["weapon"],
        power = 200.0,
        dlc = "WOTC",
        normal_location = "ChosenAssassinWeapons"
    ),
    "ChosenHunterWeaponsCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Hunter Weapons",
        id = tech_base_id + 47,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["weapon"],
        power = 200.0,
        dlc = "WOTC",
        normal_location = "ChosenHunterWeapons"
    ),
    "ChosenWarlockWeaponsCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Warlock Weapons",
        id = tech_base_id + 48,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["weapon"],
        power = 180.0,
        dlc = "WOTC",
        normal_location = "ChosenWarlockWeapons"
    )
}

#=======================================================================================================================
#                                            PROGRESSIVE TECH ITEMS
#-----------------------------------------------------------------------------------------------------------------------

progressive_tech_items: Dict[str, X2WOTCItemData] = {
    "ProgressiveRifleTechCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Progressive Rifle",
        id = tech_base_id + 49,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["weapon", "progressive"],
        stages = [
            "MagnetizedWeaponsCompleted",
            "PlasmaRifleCompleted"
        ]
    ),
    "ProgressiveMeleeTechCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Progressive Melee Weapons",
        id = tech_base_id + 50,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["weapon", "progressive"],
        stages = [
            "AutopsyAdventStunLancerCompleted",
            "AutopsyArchonCompleted"
        ]
    ),
    "ProgressiveArmorTechCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Progressive Armor",
        id = tech_base_id + 51,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["armor", "progressive"],
        stages = [
            "PlatedArmorCompleted",
            "PoweredArmorCompleted"
        ]
    ),
    "ProgressiveGREMLINTechCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Progressive GREMLIN",
        id = tech_base_id + 52,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["utility", "weapon", "progressive"],
        stages = [
            "AutopsyAdventMECCompleted",
            "AutopsySectopodCompleted"
        ]
    ),
    "ProgressivePsionicsTechCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Progressive Psionics",
        id = tech_base_id + 53,
        classification = ItemClassification.progression,
        type = "TechCompleted",
        tags = ["facility", "weapon", "progressive"],
        stages = [
            "PsionicsCompleted",
            "AutopsyGatekeeperCompleted"
        ]
    )
}

########################################################################################################################
##                                   FILLER ITEMS (RESOURCES / WEAPON MODS)                                           ##
########################################################################################################################

filler_base_id = tech_base_id + 54

#=======================================================================================================================
#                                                RESOURCE ITEMS
#-----------------------------------------------------------------------------------------------------------------------

supplies_items: Dict[str, X2WOTCItemData] = {
    "Supplies:50": X2WOTCItemData(
        display_name = resource_item_prefix + "50 Supplies",
        id = filler_base_id,
        type = "Resource",
        tags = ["filler", "supplies"]
    ),
    "Supplies:75": X2WOTCItemData(
        display_name = resource_item_prefix + "75 Supplies",
        id = filler_base_id + 1,
        type = "Resource",
        tags = ["filler", "supplies"]
    ),
    "Supplies:100": X2WOTCItemData(
        display_name = resource_item_prefix + "100 Supplies",
        id = filler_base_id + 2,
        type = "Resource",
        tags = ["filler", "supplies"]
    )
}

intel_items: Dict[str, X2WOTCItemData] = {
    "Intel:20": X2WOTCItemData(
        display_name = resource_item_prefix + "20 Intel",
        id = filler_base_id + 3,
        type = "Resource",
        tags = ["filler", "intel"]
    ),
    "Intel:30": X2WOTCItemData(
        display_name = resource_item_prefix + "30 Intel",
        id = filler_base_id + 4,
        type = "Resource",
        tags = ["filler", "intel"]
    ),
    "Intel:40": X2WOTCItemData(
        display_name = resource_item_prefix + "40 Intel",
        id = filler_base_id + 5,
        type = "Resource",
        tags = ["filler", "intel"]
    )
}

alien_alloys_items: Dict[str, X2WOTCItemData] = {
    "AlienAlloy:10": X2WOTCItemData(
        display_name = resource_item_prefix + "10 Alien Alloys",
        id = filler_base_id + 6,
        type = "Resource",
        tags = ["filler", "alien_alloy"]
    ),
    "AlienAlloy:20": X2WOTCItemData(
        display_name = resource_item_prefix + "20 Alien Alloys",
        id = filler_base_id + 7,
        type = "Resource",
        tags = ["filler", "alien_alloy"]
    ),
    "AlienAlloy:30": X2WOTCItemData(
        display_name = resource_item_prefix + "30 Alien Alloys",
        id = filler_base_id + 8,
        type = "Resource",
        tags = ["filler", "alien_alloy"]
    )
}

elerium_dust_items: Dict[str, X2WOTCItemData] = {
    "EleriumDust:10": X2WOTCItemData(
        display_name = resource_item_prefix + "10 Elerium Crystals",
        id = filler_base_id + 9,
        type = "Resource",
        tags = ["filler", "elerium_dust"]
    ),
    "EleriumDust:20": X2WOTCItemData(
        display_name = resource_item_prefix + "20 Elerium Crystals",
        id = filler_base_id + 10,
        type = "Resource",
        tags = ["filler", "elerium_dust"]
    ),
    "EleriumDust:30": X2WOTCItemData(
        display_name = resource_item_prefix + "30 Elerium Crystals",
        id = filler_base_id + 11,
        type = "Resource",
        tags = ["filler", "elerium_dust"]
    )
}

elerium_core_items: Dict[str, X2WOTCItemData] = {
    "EleriumCore:1": X2WOTCItemData(
        display_name = resource_item_prefix + "1 Elerium Core",
        id = filler_base_id + 12,
        type = "Resource",
        tags = ["filler", "elerium_core"]
    )
}

#=======================================================================================================================
#                                               WEAPON MOD ITEMS
#-----------------------------------------------------------------------------------------------------------------------

advanced_weapon_mod_items: Dict[str, X2WOTCItemData] = {
    "AimUpgrade_Adv": X2WOTCItemData(
        display_name = weapon_mod_item_prefix + "Advanced Scope",
        id = filler_base_id + 13,
        type = "WeaponMod",
        tags = ["filler", "scope", "advanced"]
    ),
    "CritUpgrade_Adv": X2WOTCItemData(
        display_name = weapon_mod_item_prefix + "Advanced Laser Sight",
        id = filler_base_id + 14,
        type = "WeaponMod",
        tags = ["filler", "laser_sight", "advanced"]
    ),
    "ReloadUpgrade_Adv": X2WOTCItemData(
        display_name = weapon_mod_item_prefix + "Advanced Auto-Loader",
        id = filler_base_id + 15,
        type = "WeaponMod",
        tags = ["filler", "auto_loader", "advanced"]
    ),
    "FreeKillUpgrade_Adv": X2WOTCItemData(
        display_name = weapon_mod_item_prefix + "Advanced Repeater",
        id = filler_base_id + 16,
        type = "WeaponMod",
        tags = ["filler", "repeater", "advanced"]
    ),
    "MissDamageUpgrade_Adv": X2WOTCItemData(
        display_name = weapon_mod_item_prefix + "Advanced Stock",
        id = filler_base_id + 17,
        type = "WeaponMod",
        tags = ["filler", "stock", "advanced"]
    ),
    "FreeFireUpgrade_Adv": X2WOTCItemData(
        display_name = weapon_mod_item_prefix + "Advanced Hair Trigger",
        id = filler_base_id + 18,
        type = "WeaponMod",
        tags = ["filler", "hair_trigger", "advanced"]
    ),
    "ClipSizeUpgrade_Adv": X2WOTCItemData(
        display_name = weapon_mod_item_prefix + "Advanced Expanded Magazine",
        id = filler_base_id + 19,
        type = "WeaponMod",
        tags = ["filler", "expanded_magazine", "advanced"]
    ),
}

superior_weapon_mod_items: Dict[str, X2WOTCItemData] = {
    "AimUpgrade_Sup": X2WOTCItemData(
        display_name = weapon_mod_item_prefix + "Superior Scope",
        id = filler_base_id + 20,
        type = "WeaponMod",
        tags = ["filler", "scope", "superior"]
    ),
    "CritUpgrade_Sup": X2WOTCItemData(
        display_name = weapon_mod_item_prefix + "Superior Laser Sight",
        id = filler_base_id + 21,
        type = "WeaponMod",
        tags = ["filler", "laser_sight", "superior"]
    ),
    "ReloadUpgrade_Sup": X2WOTCItemData(
        display_name = weapon_mod_item_prefix + "Superior Auto-Loader",
        id = filler_base_id + 22,
        type = "WeaponMod",
        tags = ["filler", "auto_loader", "superior"]
    ),
    "FreeKillUpgrade_Sup": X2WOTCItemData(
        display_name = weapon_mod_item_prefix + "Superior Repeater",
        id = filler_base_id + 23,
        type = "WeaponMod",
        tags = ["filler", "repeater", "superior"]
    ),
    "MissDamageUpgrade_Sup": X2WOTCItemData(
        display_name = weapon_mod_item_prefix + "Superior Stock",
        id = filler_base_id + 24,
        type = "WeaponMod",
        tags = ["filler", "stock", "superior"]
    ),
    "FreeFireUpgrade_Sup": X2WOTCItemData(
        display_name = weapon_mod_item_prefix + "Superior Hair Trigger",
        id = filler_base_id + 25,
        type = "WeaponMod",
        tags = ["filler", "hair_trigger", "superior"]
    ),
    "ClipSizeUpgrade_Sup": X2WOTCItemData(
        display_name = weapon_mod_item_prefix + "Superior Expanded Magazine",
        id = filler_base_id + 26,
        type = "WeaponMod",
        tags = ["filler", "expanded_magazine", "superior"]
    )
}

########################################################################################################################
##                                                EVENT ITEMS                                                         ##
########################################################################################################################

event_items: Dict[str, X2WOTCItemData] = {
    "Victory": X2WOTCItemData(
        display_name = "Victory",
        classification = ItemClassification.progression,
        normal_location = "Victory"
    )
}

########################################################################################################################
##                                                TOTAL ITEMS                                                         ##
########################################################################################################################

tech_item_table: Dict[str, X2WOTCItemData] = {
    **vanilla_weapon_tech_items,
    **vanilla_armor_tech_items,
    **vanilla_autopsy_tech_items,
    **vanilla_goldenpath_tech_items,
    **vanilla_other_tech_items,
    **alien_hunters_tech_items,
    **wotc_autopsy_tech_items,
    **wotc_chosen_weapon_tech_items,
    **progressive_tech_items
}

resource_item_table: Dict[str, X2WOTCItemData] = {
    **supplies_items,
    **intel_items,
    **alien_alloys_items,
    **elerium_dust_items,
    **elerium_core_items
}

weapon_mod_item_table: Dict[str, X2WOTCItemData] = {
    **advanced_weapon_mod_items,
    **superior_weapon_mod_items
}

item_table: Dict[str, X2WOTCItemData] = {
    **tech_item_table,
    **resource_item_table,
    **weapon_mod_item_table,
    **event_items
}

item_display_name_to_key = {item_data.display_name: key for key, item_data in item_table.items()}
item_id_to_key = {item_data.id: key for key, item_data in item_table.items() if item_data.id}

total_power: Dict[int, float] = {}
item_count: Dict[int, Dict[str, int]] = {}
num_items: Dict[int, int] = {}

def init_item_vars(player: int):
    item_count[player] = {}
    num_items[player] = 0
    for item_name, item_data in item_table.items():
        if item_data.normal_location is None:  # Progressive and filler items
            item_count[player][item_name] = 0
        else:
            item_count[player][item_name] = 1
            num_items[player] += 1

    power_values = [item_data.power * item_count[player][item_name] for item_name, item_data in item_table.items()]
    total_power[player] = sum(power_values)

def get_total_power(player: int) -> float:
    return total_power[player]

def get_item_count(player: int, item_name: str) -> int:
    return item_count[player][item_name]

def get_num_items(player: int) -> int:
    return num_items[player]

def set_item_count(player: int, item_name: str, new_count: int, adjust_total_power: bool = True):
    old_count = item_count[player][item_name]
    item_count[player][item_name] = new_count
    num_items[player] += new_count - old_count

    if adjust_total_power:
        item_data = item_table[item_name]
        total_power[player] += item_data.power * (new_count - old_count)

def disable_item(player: int, item_name: str):
    set_item_count(player, item_name, 0)

def enable_progressive_item(player: int, item_name: str) -> bool:
    item_data = item_table[item_name]
    stages = item_data.stages
    if stages is None:
        return False
    
    for stage_name in stages:
        if item_count[player][stage_name] != 1:
            return False
        
    for stage_name in stages:
        set_item_count(player, stage_name, 0, False)

    set_item_count(player, item_name, len(stages), False)
    return True

def add_filler_items(player: int, num_filler_items: int):
    num_weapon_mod_items = num_filler_items // 4
    num_resource_items = num_filler_items - num_weapon_mod_items

    for i in range(num_resource_items):
        resource_item_name = random.choice(list(resource_item_table.keys()))
        resource_item_count = item_count[player][resource_item_name]
        set_item_count(player, resource_item_name, resource_item_count + 1)

    for i in range(num_weapon_mod_items):
        weapon_mod_item_name = random.choice(list(weapon_mod_item_table.keys()))
        weapon_mod_item_count = item_count[player][weapon_mod_item_name]
        set_item_count(player, weapon_mod_item_name, weapon_mod_item_count + 1)
