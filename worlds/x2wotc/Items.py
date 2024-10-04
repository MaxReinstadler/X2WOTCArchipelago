from BaseClasses import Item, ItemClassification
from typing import List, Dict, NamedTuple, Optional

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

########################################################################################################################
##                        TECH COMPLETION ITEMS (RESEARCH PROJECTS / SHADOW PROJECTS)                                 ##
########################################################################################################################

tech_base_id = base_id

#=======================================================================================================================
#                                                 BASE GAME
#-----------------------------------------------------------------------------------------------------------------------

vanilla_weapon_tech_items: Dict[str, X2WOTCItemData] = {
    "ModularWeaponsCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) Modular Weapons",
        id = tech_base_id,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["weapon"],
        power = 15.0,
        dlc = None,
        normal_location = "ModularWeapons"
    ),
    "MagnetizedWeaponsCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) Magnetic Weapons",
        id = tech_base_id + 1,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["weapon"],
        power = 100.0,
        dlc = None,
        normal_location = "MagnetizedWeapons"
    ),
    "GaussWeaponsCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) Gauss Weapons",
        id = tech_base_id + 2,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["weapon"],
        power = 100.0,
        dlc = None,
        normal_location = "GaussWeapons"
    ),
    "PlasmaRifleCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) Plasma Rifle",
        id = tech_base_id + 3,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["weapon"],
        power = 170.0,
        dlc = None,
        normal_location = "PlasmaRifle"
    ),
    "HeavyPlasmaCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) Beam Cannon",
        id = tech_base_id + 4,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["weapon"],
        power = 140.0,
        dlc = None,
        normal_location = "HeavyPlasma"
    ),
    "PlasmaSniperCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) Plasma Lance",
        id = tech_base_id + 5,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["weapon"],
        power = 140.0,
        dlc = None,
        normal_location = "PlasmaSniper"
    ),
    "AlloyCannonCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) Storm Gun",
        id = tech_base_id + 6,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["weapon"],
        power = 140.0,
        dlc = None,
        normal_location = "AlloyCannon"
    )
}

vanilla_armor_tech_items: Dict[str, X2WOTCItemData] = {
    "HybridMaterialsCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) Hybrid Materials",
        id = tech_base_id + 7,
        classification = ItemClassification.useful,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["armor"],
        power = 0.0,
        dlc = None,
        normal_location = "HybridMaterials"
    ),
    "PlatedArmorCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) Plated Armor",
        id = tech_base_id + 8,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["armor"],
        power = 85.0,
        dlc = None,
        normal_location = "PlatedArmor"
    ),
    "PoweredArmorCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) Powered Armor",
        id = tech_base_id + 9,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["armor"],
        power = 180.0,
        dlc = None,
        normal_location = "PoweredArmor"
    )
}

vanilla_autopsy_tech_items: Dict[str, X2WOTCItemData] = {
    "AutopsySectoidCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) Sectoid Autopsy",
        id = tech_base_id + 10,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["utility"],
        power = 10.0,
        dlc = None,
        normal_location = "AutopsySectoid"
    ),
    "AutopsyViperCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) Viper Autopsy",
        id = tech_base_id + 11,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["utility"],
        power = 25.0,
        dlc = None,
        normal_location = "AutopsyViper"
    ),
    "AutopsyMutonCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) Muton Autopsy",
        id = tech_base_id + 12,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["weapon"],
        power = 60.0,
        dlc = None,
        normal_location = "AutopsyMuton"
    ),
    "AutopsyBerserkerCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) Berserker Autopsy",
        id = tech_base_id + 13,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["utility"],
        power = 15.0,
        dlc = None,
        normal_location = "AutopsyBerserker"
    ),
    "AutopsyArchonCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) Archon Autopsy",
        id = tech_base_id + 14,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["weapon"],
        power = 55.0,
        dlc = None,
        normal_location = "AutopsyArchon"
    ),
    "AutopsyGatekeeperCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) Gatekeeper Autopsy",
        id = tech_base_id + 15,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["weapon"],
        power = 35.0,
        dlc = None,
        normal_location = "AutopsyGatekeeper"
    ),
    "AutopsyAndromedonCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) Andromedon Autopsy",
        id = tech_base_id + 16,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["weapon"],
        power = 20.0,
        dlc = None,
        normal_location = "AutopsyAndromedon"
    ),
    "AutopsyFacelessCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) Faceless Autopsy",
        id = tech_base_id + 17,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["utility"],
        power = 90.0,
        dlc = None,
        normal_location = "AutopsyFaceless"
    ),
    "AutopsyChryssalidCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) Chryssalid Autopsy",
        id = tech_base_id + 18,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["armor"],
        power = 20.0,
        dlc = None,
        normal_location = "AutopsyChryssalid"
    ),
    "AutopsyAdventTrooperCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) ADVENT Trooper Autopsy",
        id = tech_base_id + 19,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["utility"],
        power = 25.0,
        dlc = None,
        normal_location = "AutopsyAdventTrooper"
    ),
    "AutopsyAdventStunLancerCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) ADVENT Stun Lancer Autopsy",
        id = tech_base_id + 20,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["weapon"],
        power = 75.0,
        dlc = None,
        normal_location = "AutopsyAdventStunLancer"
    ),
    "AutopsyAdventShieldbearerCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) ADVENT Shieldbearer Autopsy",
        id = tech_base_id + 21,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["armor"],
        power = 40.0,
        dlc = None,
        normal_location = "AutopsyAdventShieldbearer"
    ),
    "AutopsyAdventMECCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) ADVENT MEC Breakdown",
        id = tech_base_id + 22,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["weapon", "utility"],
        power = 80.0,
        dlc = None,
        normal_location = "AutopsyAdventMEC"
    ),
    "AutopsyAdventTurretCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) ADVENT Turret Breakdown",
        id = tech_base_id + 23,
        classification = ItemClassification.useful,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["facility"],
        power = 0.0,
        dlc = None,
        normal_location = "AutopsyAdventTurret"
    ),
    "AutopsySectopodCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) Sectopod Breakdown",
        id = tech_base_id + 24,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["weapon", "utility"],
        power = 50.0,
        dlc = None,
        normal_location = "AutopsySectopod"
    )
}

vanilla_goldenpath_tech_items: Dict[str, X2WOTCItemData] = {
    "AlienBiotechCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) Alien Biotech",
        id = tech_base_id + 25,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["facility"],
        power = 0.0,
        dlc = None,
        normal_location = "AlienBiotech"
    ),
    "ResistanceCommunicationsCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) Resistance Communications",
        id = tech_base_id + 26,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["facility"],
        power = 30.0,
        dlc = None,
        normal_location = "ResistanceCommunications"
    ),
    "AutopsyAdventOfficerCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) ADVENT Officer Autopsy",
        id = tech_base_id + 27,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["facility"],
        power = 85.0,
        dlc = None,
        normal_location = "AutopsyAdventOfficer"
    ),
    "AlienEncryptionCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) Alien Encryption",
        id = tech_base_id + 28,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["facility"],
        power = 0.0,
        dlc = None,
        normal_location = "AlienEncryption"
    ),
    "CodexBrainPt1Completed": X2WOTCItemData(
        display_name = "(Shadow Project Completed) Codex Brain",
        id = tech_base_id + 29,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["mission"],
        power = 0.0,
        dlc = None,
        normal_location = "CodexBrainPt1"
    ),
    "CodexBrainPt2Completed": X2WOTCItemData(
        display_name = "(Shadow Project Completed) Encrypted Codex Data",
        id = tech_base_id + 30,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = [],
        power = 0.0,
        dlc = None,
        normal_location = "CodexBrainPt2"
    ),
    "BlacksiteDataCompleted": X2WOTCItemData(
        display_name = "(Shadow Project Completed) Blacksite Vial",
        id = tech_base_id + 31,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["mission"],
        power = 0.0,
        dlc = None,
        normal_location = "BlacksiteData"
    ),
    "ForgeStasisSuitCompleted": X2WOTCItemData(
        display_name = "(Shadow Project Completed) Recovered ADVENT Stasis Suit",
        id = tech_base_id + 32,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = [],
        power = 0.0,
        dlc = None,
        normal_location = "ForgeStasisSuit"
    ),
    "PsiGateCompleted": X2WOTCItemData(
        display_name = "(Shadow Project Completed) Psionic Gate",
        id = tech_base_id + 33,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = [],
        power = 0.0,
        dlc = None,
        normal_location = "PsiGate"
    ),
    "AutopsyAdventPsiWitchCompleted": X2WOTCItemData(
        display_name = "(Shadow Project Completed) Avatar Autopsy",
        id = tech_base_id + 34,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["mission"],
        power = 0.0,
        dlc = None,
        normal_location = "AutopsyAdventPsiWitch"
    )
}

vanilla_other_tech_items: Dict[str, X2WOTCItemData] = {
    "ResistanceRadioCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) Resistance Radio",
        id = tech_base_id + 35,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = [],
        power = 40.0,
        dlc = None,
        normal_location = "ResistanceRadio"
    ),
    "EleriumCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) Elerium",
        id = tech_base_id + 36,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["facility"],
        power = 15.0,
        dlc = None,
        normal_location = "Tech_Elerium"
    ),
    "PsionicsCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) Psionics",
        id = tech_base_id + 37,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["facility", "weapon"],
        power = 80.0,
        dlc = None,
        normal_location = "Psionics"
    )
}

#=======================================================================================================================
#                                               ALIEN HUNTERS
#-----------------------------------------------------------------------------------------------------------------------

alien_hunters_tech_items: Dict[str, X2WOTCItemData] = {
    "ExperimentalWeaponsCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) Experimental Weapons",
        id = tech_base_id + 38,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["weapon", "utility"],
        power = 70.0,
        dlc = "AH",
        normal_location = "ExperimentalWeapons"
    ),
    "AutopsyViperKingCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) Viper King Autopsy",
        id = tech_base_id + 39,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["armor"],
        power = 70.0,
        dlc = "AH",
        normal_location = "AutopsyViperKing"
    ),
    "AutopsyBerserkerQueenCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) Berserker Queen Autopsy",
        id = tech_base_id + 40,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["armor"],
        power = 70.0,
        dlc = "AH",
        normal_location = "AutopsyBerserkerQueen"
    ),
    "AutopsyArchonKingCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) Archon King Autopsy",
        id = tech_base_id + 41,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["armor"],
        power = 80.0,
        dlc = "AH",
        normal_location = "AutopsyArchonKing"
    )
}

#=======================================================================================================================
#                                             WAR OF THE CHOSEN
#-----------------------------------------------------------------------------------------------------------------------

wotc_autopsy_tech_items: Dict[str, X2WOTCItemData] = {
    "AutopsyAdventPurifierCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) ADVENT Purifier Autopsy",
        id = tech_base_id + 42,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["armor"],
        power = 15.0,
        dlc = "WOTC",
        normal_location = "AutopsyAdventPurifier"
    ),
    "AutopsyAdventPriestCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) ADVENT Priest Autopsy",
        id = tech_base_id + 43,
        classification = ItemClassification.useful,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["utility"],
        power = 0.0,
        dlc = "WOTC",
        normal_location = "AutopsyAdventPriest"
    ),
    "AutopsyTheLostCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) The Lost Autopsy",
        id = tech_base_id + 44,
        classification = ItemClassification.useful,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["utility"],
        power = 0.0,
        dlc = "WOTC",
        normal_location = "AutopsyTheLost"
    ),
    "AutopsySpectreCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) Spectre Autopsy",
        id = tech_base_id + 45,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["utility"],
        power = 15.0,
        dlc = "WOTC",
        normal_location = "AutopsySpectre"
    )
}

wotc_chosen_weapon_tech_items: Dict[str, X2WOTCItemData] = {
    "ChosenAssassinWeaponsCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) Assassin Weapons",
        id = tech_base_id + 46,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["weapon"],
        power = 190.0,
        dlc = "WOTC",
        normal_location = "ChosenAssassinWeapons"
    ),
    "ChosenHunterWeaponsCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) Hunter Weapons",
        id = tech_base_id + 47,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["weapon"],
        power = 190.0,
        dlc = "WOTC",
        normal_location = "ChosenHunterWeapons"
    ),
    "ChosenWarlockWeaponsCompleted": X2WOTCItemData(
        display_name = "(Research Project Completed) Warlock Weapons",
        id = tech_base_id + 48,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["weapon"],
        power = 160.0,
        dlc = "WOTC",
        normal_location = "ChosenWarlockWeapons"
    )
}

#=======================================================================================================================
#                                            PROGRESSIVE TECH ITEMS
#-----------------------------------------------------------------------------------------------------------------------

progressive_tech_items: Dict[str, X2WOTCItemData] = {
    "ProgressiveRifleTechCompleted": X2WOTCItemData(
        display_name = "Progressive Rifle Tech",
        id = tech_base_id + 49,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["weapon", "progressive"],
        dlc = None,
        stages = [
            "MagnetizedWeaponsCompleted",
            "PlasmaRifleCompleted"
        ]
    ),
    "ProgressiveMeleeTechCompleted": X2WOTCItemData(
        display_name = "Progressive Melee Weapon Tech",
        id = tech_base_id + 50,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["weapon", "progressive"],
        dlc = None,
        stages = [
            "AutopsyAdventStunLancerCompleted",
            "AutopsyArchonCompleted"
        ]
    ),
    "ProgressiveArmorTechCompleted": X2WOTCItemData(
        display_name = "Progressive Armor Tech",
        id = tech_base_id + 51,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["armor", "progressive"],
        dlc = None,
        stages = [
            "PlatedArmorCompleted",
            "PoweredArmorCompleted"
        ]
    ),
    "ProgressiveGREMLINTechCompleted": X2WOTCItemData(
        display_name = "Progressive GREMLIN Tech",
        id = tech_base_id + 52,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["utility", "weapon", "progressive"],
        dlc = None,
        stages = [
            "AutopsyAdventMECCompleted",
            "AutopsySectopodCompleted"
        ]
    ),
    "ProgressivePsionicsTechCompleted": X2WOTCItemData(
        display_name = "Progressive Psionics Tech",
        id = tech_base_id + 53,
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["facility", "weapon", "progressive"],
        dlc = None,
        stages = [
            "PsionicsCompleted",
            "AutopsyGatekeeperCompleted"
        ]
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

item_table: Dict[str, X2WOTCItemData] = {
    **tech_item_table,
    **event_items
}

item_display_name_to_key = {item_data.display_name: key for key, item_data in item_table.items()}
item_id_to_key = {item_data.id: key for key, item_data in item_table.items() if item_data.id}

total_power: Dict[int, float] = {}
item_count: Dict[int, Dict[str, int]] = {}

def init_item_vars(player: int):
    item_count[player] = {}
    for item_name, item_data in item_table.items():
        if item_data.stages is None:
            item_count[player][item_name] = 1
        else:
            item_count[player][item_name] = 0

    power_values = [item_data.power * item_count[player][item_name] for item_name, item_data in item_table.items()]
    total_power[player] = sum(power_values)

def get_total_power(player: int) -> float:
    return total_power[player]

def get_item_count(player: int, item_name: str) -> int:
    return item_count[player][item_name]

def set_item_count(player: int, item_name: str, new_count: int, adjust_total_power: bool = True):
    old_count = item_count[player][item_name]
    item_count[player][item_name] = new_count

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

    set_item_count(player, item_name, len(stages))
    return True
