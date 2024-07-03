from BaseClasses import Location
from typing import List, Dict, NamedTuple, Optional

class X2WOTCLocation(Location):
    game: str = "XCOM 2 War of the Chosen"

class X2WOTCLocationData(NamedTuple):
    display_name: str
    id: Optional[int] = None
    layer: str = "Strategy"  # "Strategy" or "Tactical"
    type: str = "Event"
    tags: List[str] = []
    difficulty: float = 0.0   # Relative to total power in percent (0 to 100)
    dlc: Optional[str] = None   # None: Base Game,
                                # "AH": Alien Hunters,
                                # "SLG": Shens Last Gift,
                                # "WOTC": War of the Chosen
    normal_item: Optional[str] = None

base_id = 2482748367

########################################################################################################################
##                            TECH LOCATIONS (RESEARCH PROJECTS / SHADOW PROJECTS)                                    ##
########################################################################################################################

tech_base_id = base_id

#=======================================================================================================================
#                                                 BASE GAME
#-----------------------------------------------------------------------------------------------------------------------

vanilla_weapon_techs: Dict[str, X2WOTCLocationData] = {
    "ModularWeapons": X2WOTCLocationData(
        display_name ="(Research Project) Modular Weapons",
        id = tech_base_id,
        layer = "Strategy",
        type = "Tech",
        tags = [],
        difficulty = 0.0,
        dlc = None,
        normal_item = "ModularWeaponsCompleted"
    ),
    "MagnetizedWeapons": X2WOTCLocationData(
        display_name ="(Research Project) Magnetic Weapons",
        id = tech_base_id + 1,
        layer = "Strategy",
        type = "Tech",
        tags = [],
        difficulty = 15.0,
        dlc = None,
        normal_item = "MagnetizedWeaponsCompleted"
    ),
    "GaussWeapons": X2WOTCLocationData(
        display_name ="(Research Project) Gauss Weapons",
        id = tech_base_id + 2,
        layer = "Strategy",
        type = "Tech",
        tags = [],
        difficulty = 25.0,
        dlc = None,
        normal_item = "GaussWeaponsCompleted"
    ),
    "PlasmaRifle": X2WOTCLocationData(
        display_name ="(Research Project) Plasma Rifle",
        id = tech_base_id + 3,
        layer = "Strategy",
        type = "Tech",
        tags = [],
        difficulty = 45.0,
        dlc = None,
        normal_item = "PlasmaRifleCompleted"
    ),
    "HeavyPlasma": X2WOTCLocationData(
        display_name ="(Research Project) Beam Cannon",
        id = tech_base_id + 4,
        layer = "Strategy",
        type = "Tech",
        tags = [],
        difficulty = 55.0,
        dlc = None,
        normal_item = "HeavyPlasmaCompleted"
    ),
    "PlasmaSniper": X2WOTCLocationData(
        display_name ="(Research Project) Plasma Lance",
        id = tech_base_id + 5,
        layer = "Strategy",
        type = "Tech",
        tags = [],
        difficulty = 55.0,
        dlc = None,
        normal_item = "PlasmaSniperCompleted"
    ),
    "AlloyCannon": X2WOTCLocationData(
        display_name ="(Research Project) Storm Gun",
        id = tech_base_id + 6,
        layer = "Strategy",
        type = "Tech",
        tags = [],
        difficulty = 55.0,
        dlc = None,
        normal_item = "AlloyCannonCompleted"
    )
}

vanilla_armor_techs: Dict[str, X2WOTCLocationData] = {
    "HybridMaterials": X2WOTCLocationData(
        display_name ="(Research Project) Hybrid Materials",
        id = tech_base_id + 7,
        layer = "Strategy",
        type = "Tech",
        tags = [],
        difficulty = 0.0,
        dlc = None,
        normal_item = "HybridMaterialsCompleted"
    ),
    "PlatedArmor": X2WOTCLocationData(
        display_name ="(Research Project) Plated Armor",
        id = tech_base_id + 8,
        layer = "Strategy",
        type = "Tech",
        tags = [],
        difficulty = 25.0,
        dlc = None,
        normal_item = "PlatedArmorCompleted"
    ),
    "PoweredArmor": X2WOTCLocationData(
        display_name ="(Research Project) Powered Armor",
        id = tech_base_id + 9,
        layer = "Strategy",
        type = "Tech",
        tags = [],
        difficulty = 50.0,
        dlc = None,
        normal_item = "PoweredArmorCompleted"
    )
}

vanilla_autopsy_techs: Dict[str, X2WOTCLocationData] = {
    "AutopsySectoid": X2WOTCLocationData(
        display_name ="(Research Project) Sectoid Autopsy",
        id = tech_base_id + 10,
        layer = "Strategy",
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 5.0,
        dlc = None,
        normal_item = "AutopsySectoidCompleted"
    ),
    "AutopsyViper": X2WOTCLocationData(
        display_name ="(Research Project) Viper Autopsy",
        id = tech_base_id + 11,
        layer = "Strategy",
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 15.0,
        dlc = None,
        normal_item = "AutopsyViperCompleted"
    ),
    "AutopsyMuton": X2WOTCLocationData(
        display_name ="(Research Project) Muton Autopsy",
        id = tech_base_id + 12,
        layer = "Strategy",
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 25.0,
        dlc = None,
        normal_item = "AutopsyMutonCompleted"
    ),
    "AutopsyBerserker": X2WOTCLocationData(
        display_name ="(Research Project) Berserker Autopsy",
        id = tech_base_id + 13,
        layer = "Strategy",
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 40.0,
        dlc = None,
        normal_item = "AutopsyBerserkerCompleted"
    ),
    "AutopsyArchon": X2WOTCLocationData(
        display_name ="(Research Project) Archon Autopsy",
        id = tech_base_id + 14,
        layer = "Strategy",
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 60.0,
        dlc = None,
        normal_item = "AutopsyArchonCompleted"
    ),
    "AutopsyGatekeeper": X2WOTCLocationData(
        display_name ="(Research Project) Gatekeeper Autopsy",
        id = tech_base_id + 15,
        layer = "Strategy",
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 80.0,
        dlc = None,
        normal_item = "AutopsyGatekeeperCompleted"
    ),
    "AutopsyAndromedon": X2WOTCLocationData(
        display_name ="(Research Project) Andromedon Autopsy",
        id = tech_base_id + 16,
        layer = "Strategy",
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 70.0,
        dlc = None,
        normal_item = "AutopsyAndromedonCompleted"
    ),
    "AutopsyFaceless": X2WOTCLocationData(
        display_name ="(Research Project) Faceless Autopsy",
        id = tech_base_id + 17,
        layer = "Strategy",
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 20.0,
        dlc = None,
        normal_item = "AutopsyFacelessCompleted"
    ),
    "AutopsyChryssalid": X2WOTCLocationData(
        display_name ="(Research Project) Chryssalid Autopsy",
        id = tech_base_id + 18,
        layer = "Strategy",
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 45.0,
        dlc = None,
        normal_item = "AutopsyChryssalidCompleted"
    ),
    "AutopsyAdventTrooper": X2WOTCLocationData(
        display_name ="(Research Project) ADVENT Trooper Autopsy",
        id = tech_base_id + 19,
        layer = "Strategy",
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 5.0,
        dlc = None,
        normal_item = "AutopsyAdventTrooperCompleted"
    ),
    "AutopsyAdventStunLancer": X2WOTCLocationData(
        display_name ="(Research Project) ADVENT Stun Lancer Autopsy",
        id = tech_base_id + 20,
        layer = "Strategy",
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 15.0,
        dlc = None,
        normal_item = "AutopsyAdventStunLancerCompleted"
    ),
    "AutopsyAdventShieldbearer": X2WOTCLocationData(
        display_name ="(Research Project) ADVENT Shieldbearer Autopsy",
        id = tech_base_id + 21,
        layer = "Strategy",
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 15.0,
        dlc = None,
        normal_item = "AutopsyAdventShieldbearerCompleted"
    ),
    "AutopsyAdventMEC": X2WOTCLocationData(
        display_name ="(Research Project) ADVENT MEC Breakdown",
        id = tech_base_id + 22,
        layer = "Strategy",
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 25.0,
        dlc = None,
        normal_item = "AutopsyAdventMECCompleted"
    ),
    "AutopsyAdventTurret": X2WOTCLocationData(
        display_name ="(Research Project) ADVENT Turret Breakdown",
        id = tech_base_id + 23,
        layer = "Strategy",
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 80.0,
        dlc = None,
        normal_item = "AutopsyAdventTurretCompleted"
    ),
    "AutopsySectopod": X2WOTCLocationData(
        display_name ="(Research Project) Sectopod Breakdown",
        id = tech_base_id + 24,
        layer = "Strategy",
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 75.0,
        dlc = None,
        normal_item = "AutopsySectopodCompleted"
    )
}

vanilla_goldenpath_techs: Dict[str, X2WOTCLocationData] = {
    "AlienBiotech": X2WOTCLocationData(
        display_name ="(Research Project) Alien Biotech",
        id = tech_base_id + 25,
        layer = "Strategy",
        type = "Tech",
        tags = ["goldenpath"],
        difficulty = 0.0,
        dlc = None,
        normal_item = "AlienBiotechCompleted"
    ),
    "ResistanceCommunications": X2WOTCLocationData(
        display_name ="(Research Project) Resistance Communications",
        id = tech_base_id + 26,
        layer = "Strategy",
        type = "Tech",
        tags = ["goldenpath"],
        difficulty = 10.0,
        dlc = None,
        normal_item = "ResistanceCommunicationsCompleted"
    ),
    "AutopsyAdventOfficer": X2WOTCLocationData(
        display_name ="(Research Project) ADVENT Officer Autopsy",
        id = tech_base_id + 27,
        layer = "Strategy",
        type = "Tech",
        tags = ["goldenpath", "autopsy"],
        difficulty = 10.0,
        dlc = None,
        normal_item = "AutopsyAdventOfficerCompleted"
    ),
    "AlienEncryption": X2WOTCLocationData(
        display_name ="(Research Project) Alien Encryption",
        id = tech_base_id + 28,
        layer = "Strategy",
        type = "Tech",
        tags = ["goldenpath"],
        difficulty = 25.0,
        dlc = None,
        normal_item = "AlienEncryptionCompleted"
    ),
    "CodexBrainPt1": X2WOTCLocationData(
        display_name ="(Shadow Project) Codex Brain",
        id = tech_base_id + 29,
        layer = "Strategy",
        type = "Tech",
        tags = ["goldenpath", "shadow"],
        difficulty = 45.0,
        dlc = None,
        normal_item = "CodexBrainPt1Completed"
    ),
    "CodexBrainPt2": X2WOTCLocationData(
        display_name ="(Shadow Project) Encrypted Codex Data",
        id = tech_base_id + 30,
        layer = "Strategy",
        type = "Tech",
        tags = ["goldenpath", "shadow"],
        difficulty = 55.0,
        dlc = None,
        normal_item = "CodexBrainPt2Completed"
    ),
    "BlacksiteData": X2WOTCLocationData(
        display_name ="(Shadow Project) Blacksite Vial",
        id = tech_base_id + 31,
        layer = "Strategy",
        type = "Tech",
        tags = ["goldenpath", "shadow"],
        difficulty = 30.0,
        dlc = None,
        normal_item = "BlacksiteDataCompleted"
    ),
    "ForgeStasisSuit": X2WOTCLocationData(
        display_name ="(Shadow Project) Recovered ADVENT Stasis Suit",
        id = tech_base_id + 32,
        layer = "Strategy",
        type = "Tech",
        tags = ["goldenpath", "shadow"],
        difficulty = 50.0,
        dlc = None,
        normal_item = "ForgeStasisSuitCompleted"
    ),
    "PsiGate": X2WOTCLocationData(
        display_name ="(Shadow Project) Psionic Gate",
        id = tech_base_id + 33,
        layer = "Strategy",
        type = "Tech",
        tags = ["goldenpath", "shadow"],
        difficulty = 70.0,
        dlc = None,
        normal_item = "PsiGateCompleted"
    ),
    "AutopsyAdventPsiWitch": X2WOTCLocationData(
        display_name ="(Shadow Project) Avatar Autopsy",
        id = tech_base_id + 34,
        layer = "Strategy",
        type = "Tech",
        tags = ["goldenpath", "shadow"],
        difficulty = 90.0,
        dlc = None,
        normal_item = "AutopsyAdventPsiWitchCompleted"
    )
}

vanilla_other_techs: Dict[str, X2WOTCLocationData] = {
    "ResistanceRadio": X2WOTCLocationData(
        display_name ="(Research Project) Resistance Radio",
        id = tech_base_id + 35,
        layer = "Strategy",
        type = "Tech",
        tags = [],
        difficulty = 20.0,
        dlc = None,
        normal_item = "ResistanceRadioCompleted"
    ),
    "Tech_Elerium": X2WOTCLocationData(
        display_name ="(Research Project) Elerium",
        id = tech_base_id + 36,
        layer = "Strategy",
        type = "Tech",
        tags = [],
        difficulty = 55.0,
        dlc = None,
        normal_item = "EleriumCompleted"
    ),
    "Psionics": X2WOTCLocationData(
        display_name ="(Research Project) Psionics",
        id = tech_base_id + 37,
        layer = "Strategy",
        type = "Tech",
        tags = [],
        difficulty = 40.0,
        dlc = None,
        normal_item = "PsionicsCompleted"
    )
}

#=======================================================================================================================
#                                               ALIEN HUNTERS
#-----------------------------------------------------------------------------------------------------------------------

alien_hunters_techs: Dict[str, X2WOTCLocationData] = {
    "ExperimentalWeapons": X2WOTCLocationData(
        display_name ="(Research Project) Experimental Weapons",
        id = tech_base_id + 38,
        layer = "Strategy",
        type = "Tech",
        tags = [],
        difficulty = 5.0,
        dlc = "AH",
        normal_item = "ExperimentalWeaponsCompleted"
    ),
    "AutopsyViperKing": X2WOTCLocationData(
        display_name ="(Research Project) Viper King Autopsy",
        id = tech_base_id + 39,
        layer = "Strategy",
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 35.0,
        dlc = "AH",
        normal_item = "AutopsyViperKingCompleted"
    ),
    "AutopsyBerserkerQueen": X2WOTCLocationData(
        display_name ="(Research Project) Berserker Queen Autopsy",
        id = tech_base_id + 40,
        layer = "Strategy",
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 55.0,
        dlc = "AH",
        normal_item = "AutopsyBerserkerQueenCompleted"
    ),
    "AutopsyArchonKing": X2WOTCLocationData(
        display_name ="(Research Project) Archon King Autopsy",
        id = tech_base_id + 41,
        layer = "Strategy",
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 75.0,
        dlc = "AH",
        normal_item = "AutopsyArchonKingCompleted"
    )
}

#=======================================================================================================================
#                                             WAR OF THE CHOSEN
#-----------------------------------------------------------------------------------------------------------------------

wotc_autopsy_techs: Dict[str, X2WOTCLocationData] = {
    "AutopsyAdventPurifier": X2WOTCLocationData(
        display_name ="(Research Project) ADVENT Purifier Autopsy",
        id = tech_base_id + 42,
        layer = "Strategy",
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 25.0,
        dlc = "WOTC",
        normal_item = "AutopsyAdventPurifierCompleted"
    ),
    "AutopsyAdventPriest": X2WOTCLocationData(
        display_name ="(Research Project) ADVENT Priest Autopsy",
        id = tech_base_id + 43,
        layer = "Strategy",
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 25.0,
        dlc = "WOTC",
        normal_item = "AutopsyAdventPriestCompleted"
    ),
    "AutopsyTheLost": X2WOTCLocationData(
        display_name ="(Research Project) The Lost Autopsy",
        id = tech_base_id + 44,
        layer = "Strategy",
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 25.0,
        dlc = "WOTC",
        normal_item = "AutopsyTheLostCompleted"
    ),
    "AutopsySpectre": X2WOTCLocationData(
        display_name ="(Research Project) Spectre Autopsy",
        id = tech_base_id + 45,
        layer = "Strategy",
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 55.0,
        dlc = "WOTC",
        normal_item = "AutopsySpectreCompleted"
    )
}

wotc_chosen_weapon_techs: Dict[str, X2WOTCLocationData] = {
    "ChosenAssassinWeapons": X2WOTCLocationData(
        display_name ="(Research Project) Assassin Weapons",
        id = tech_base_id + 46,
        layer = "Strategy",
        type = "Tech",
        tags = [],
        difficulty = 85.0,
        dlc = "WOTC",
        normal_item = "ChosenAssassinWeaponsCompleted"
    ),
    "ChosenHunterWeapons": X2WOTCLocationData(
        display_name ="(Research Project) Hunter Weapons",
        id = tech_base_id + 47,
        layer = "Strategy",
        type = "Tech",
        tags = [],
        difficulty = 85.0,
        dlc = "WOTC",
        normal_item = "ChosenHunterWeaponsCompleted"
    ),
    "ChosenWarlockWeapons": X2WOTCLocationData(
        display_name ="(Research Project) Warlock Weapons",
        id = tech_base_id + 48,
        layer = "Strategy",
        type = "Tech",
        tags = [],
        difficulty = 85.0,
        dlc = "WOTC",
        normal_item = "ChosenWarlockWeaponsCompleted"
    )
}

########################################################################################################################
##                                              EVENT LOCATIONS                                                       ##
########################################################################################################################

event_locations: Dict[str, X2WOTCLocationData] = {
    "Victory": X2WOTCLocationData(
        display_name ="Victory",
        difficulty = 90.0,
        normal_item = "Victory"
    )
}

########################################################################################################################
##                                              TOTAL LOCATIONS                                                       ##
########################################################################################################################

tech_location_table: Dict[str, X2WOTCLocationData] = {
    **vanilla_weapon_techs,
    **vanilla_armor_techs,
    **vanilla_autopsy_techs,
    **vanilla_goldenpath_techs,
    **vanilla_other_techs,
    **alien_hunters_techs,
    **wotc_autopsy_techs,
    **wotc_chosen_weapon_techs
}

location_table: Dict[str, X2WOTCLocationData] = {
    **tech_location_table,
    **event_locations
}

loc_display_name_to_key = {loc_data.display_name: key for key, loc_data in location_table.items()}
loc_id_to_key = {loc_data.id: key for key, loc_data in location_table.items() if loc_data.id}

def disable_location(loc_name: str):
    loc_data = location_table[loc_name]
    location_table[loc_name] = loc_data._replace(
        type = "Disabled",
    )
