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

tech_location_prefix = "Research "
shadow_tech_location_prefix = "Research "
enemy_kill_location_prefix = "Kill "
enemy_destroy_location_prefix = "Destroy "

########################################################################################################################
##                            TECH LOCATIONS (RESEARCH PROJECTS / SHADOW PROJECTS)                                    ##
########################################################################################################################

tech_base_id = base_id

#=======================================================================================================================
#                                                 BASE GAME
#-----------------------------------------------------------------------------------------------------------------------

vanilla_weapon_techs: Dict[str, X2WOTCLocationData] = {
    "ModularWeapons": X2WOTCLocationData(
        display_name = tech_location_prefix + "Modular Weapons",
        id = tech_base_id,
        type = "Tech",
        tags = [],
        difficulty = 0.0,
        normal_item = "ModularWeaponsCompleted"
    ),
    "MagnetizedWeapons": X2WOTCLocationData(
        display_name = tech_location_prefix + "Magnetic Weapons",
        id = tech_base_id + 1,
        type = "Tech",
        tags = [],
        difficulty = 15.0,
        normal_item = "MagnetizedWeaponsCompleted"
    ),
    "GaussWeapons": X2WOTCLocationData(
        display_name = tech_location_prefix + "Gauss Weapons",
        id = tech_base_id + 2,
        type = "Tech",
        tags = [],
        difficulty = 25.0,
        normal_item = "GaussWeaponsCompleted"
    ),
    "PlasmaRifle": X2WOTCLocationData(
        display_name = tech_location_prefix + "Plasma Rifle",
        id = tech_base_id + 3,
        type = "Tech",
        tags = [],
        difficulty = 45.0,
        normal_item = "PlasmaRifleCompleted"
    ),
    "HeavyPlasma": X2WOTCLocationData(
        display_name = tech_location_prefix + "Beam Cannon",
        id = tech_base_id + 4,
        type = "Tech",
        tags = [],
        difficulty = 55.0,
        normal_item = "HeavyPlasmaCompleted"
    ),
    "PlasmaSniper": X2WOTCLocationData(
        display_name = tech_location_prefix + "Plasma Lance",
        id = tech_base_id + 5,
        type = "Tech",
        tags = [],
        difficulty = 55.0,
        normal_item = "PlasmaSniperCompleted"
    ),
    "AlloyCannon": X2WOTCLocationData(
        display_name = tech_location_prefix + "Storm Gun",
        id = tech_base_id + 6,
        type = "Tech",
        tags = [],
        difficulty = 55.0,
        normal_item = "AlloyCannonCompleted"
    )
}

vanilla_armor_techs: Dict[str, X2WOTCLocationData] = {
    "HybridMaterials": X2WOTCLocationData(
        display_name = tech_location_prefix + "Hybrid Materials",
        id = tech_base_id + 7,
        type = "Tech",
        tags = [],
        difficulty = 0.0,
        normal_item = "HybridMaterialsCompleted"
    ),
    "PlatedArmor": X2WOTCLocationData(
        display_name = tech_location_prefix + "Plated Armor",
        id = tech_base_id + 8,
        type = "Tech",
        tags = [],
        difficulty = 25.0,
        normal_item = "PlatedArmorCompleted"
    ),
    "PoweredArmor": X2WOTCLocationData(
        display_name = tech_location_prefix + "Powered Armor",
        id = tech_base_id + 9,
        type = "Tech",
        tags = [],
        difficulty = 45.0,
        normal_item = "PoweredArmorCompleted"
    )
}

vanilla_autopsy_techs: Dict[str, X2WOTCLocationData] = {
    "AutopsySectoid": X2WOTCLocationData(
        display_name = tech_location_prefix + "Sectoid Autopsy",
        id = tech_base_id + 10,
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 5.0,
        normal_item = "AutopsySectoidCompleted"
    ),
    "AutopsyViper": X2WOTCLocationData(
        display_name = tech_location_prefix + "Viper Autopsy",
        id = tech_base_id + 11,
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 15.0,
        normal_item = "AutopsyViperCompleted"
    ),
    "AutopsyMuton": X2WOTCLocationData(
        display_name = tech_location_prefix + "Muton Autopsy",
        id = tech_base_id + 12,
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 25.0,
        normal_item = "AutopsyMutonCompleted"
    ),
    "AutopsyBerserker": X2WOTCLocationData(
        display_name = tech_location_prefix + "Berserker Autopsy",
        id = tech_base_id + 13,
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 35.0,
        normal_item = "AutopsyBerserkerCompleted"
    ),
    "AutopsyArchon": X2WOTCLocationData(
        display_name = tech_location_prefix + "Archon Autopsy",
        id = tech_base_id + 14,
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 45.0,
        normal_item = "AutopsyArchonCompleted"
    ),
    "AutopsyGatekeeper": X2WOTCLocationData(
        display_name = tech_location_prefix + "Gatekeeper Autopsy",
        id = tech_base_id + 15,
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 75.0,
        normal_item = "AutopsyGatekeeperCompleted"
    ),
    "AutopsyAndromedon": X2WOTCLocationData(
        display_name = tech_location_prefix + "Andromedon Autopsy",
        id = tech_base_id + 16,
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 65.0,
        normal_item = "AutopsyAndromedonCompleted"
    ),
    "AutopsyFaceless": X2WOTCLocationData(
        display_name = tech_location_prefix + "Faceless Autopsy",
        id = tech_base_id + 17,
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 10.0,
        normal_item = "AutopsyFacelessCompleted"
    ),
    "AutopsyChryssalid": X2WOTCLocationData(
        display_name = tech_location_prefix + "Chryssalid Autopsy",
        id = tech_base_id + 18,
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 55.0,
        normal_item = "AutopsyChryssalidCompleted"
    ),
    "AutopsyAdventTrooper": X2WOTCLocationData(
        display_name = tech_location_prefix + "ADVENT Trooper Autopsy",
        id = tech_base_id + 19,
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 5.0,
        normal_item = "AutopsyAdventTrooperCompleted"
    ),
    "AutopsyAdventStunLancer": X2WOTCLocationData(
        display_name = tech_location_prefix + "ADVENT Stun Lancer Autopsy",
        id = tech_base_id + 20,
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 15.0,
        normal_item = "AutopsyAdventStunLancerCompleted"
    ),
    "AutopsyAdventShieldbearer": X2WOTCLocationData(
        display_name = tech_location_prefix + "ADVENT Shieldbearer Autopsy",
        id = tech_base_id + 21,
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 15.0,
        normal_item = "AutopsyAdventShieldbearerCompleted"
    ),
    "AutopsyAdventMEC": X2WOTCLocationData(
        display_name = tech_location_prefix + "ADVENT MEC Breakdown",
        id = tech_base_id + 22,
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 25.0,
        normal_item = "AutopsyAdventMECCompleted"
    ),
    "AutopsyAdventTurret": X2WOTCLocationData(
        display_name = tech_location_prefix + "ADVENT Turret Breakdown",
        id = tech_base_id + 23,
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 85.0,
        normal_item = "AutopsyAdventTurretCompleted"
    ),
    "AutopsySectopod": X2WOTCLocationData(
        display_name = tech_location_prefix + "Sectopod Breakdown",
        id = tech_base_id + 24,
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 75.0,
        normal_item = "AutopsySectopodCompleted"
    )
}

vanilla_goldenpath_techs: Dict[str, X2WOTCLocationData] = {
    "AlienBiotech": X2WOTCLocationData(
        display_name = tech_location_prefix + "Alien Biotech",
        id = tech_base_id + 25,
        type = "Tech",
        tags = ["goldenpath"],
        difficulty = 0.0,
        normal_item = "AlienBiotechCompleted"
    ),
    "ResistanceCommunications": X2WOTCLocationData(
        display_name = tech_location_prefix + "Resistance Communications",
        id = tech_base_id + 26,
        type = "Tech",
        tags = ["goldenpath"],
        difficulty = 5.0,
        normal_item = "ResistanceCommunicationsCompleted"
    ),
    "AutopsyAdventOfficer": X2WOTCLocationData(
        display_name = tech_location_prefix + "ADVENT Officer Autopsy",
        id = tech_base_id + 27,
        type = "Tech",
        tags = ["goldenpath", "autopsy"],
        difficulty = 5.0,
        normal_item = "AutopsyAdventOfficerCompleted"
    ),
    "AlienEncryption": X2WOTCLocationData(
        display_name = tech_location_prefix + "Alien Encryption",
        id = tech_base_id + 28,
        type = "Tech",
        tags = ["goldenpath"],
        difficulty = 20.0,
        normal_item = "AlienEncryptionCompleted"
    ),
    "CodexBrainPt1": X2WOTCLocationData(
        display_name = shadow_tech_location_prefix + "Codex Brain",
        id = tech_base_id + 29,
        type = "Tech",
        tags = ["goldenpath", "shadow"],
        difficulty = 40.0,
        normal_item = "CodexBrainPt1Completed"
    ),
    "CodexBrainPt2": X2WOTCLocationData(
        display_name = shadow_tech_location_prefix + "Encrypted Codex Data",
        id = tech_base_id + 30,
        type = "Tech",
        tags = ["goldenpath", "shadow"],
        difficulty = 50.0,
        normal_item = "CodexBrainPt2Completed"
    ),
    "BlacksiteData": X2WOTCLocationData(
        display_name = shadow_tech_location_prefix + "Blacksite Vial",
        id = tech_base_id + 31,
        type = "Tech",
        tags = ["goldenpath", "shadow"],
        difficulty = 30.0,
        normal_item = "BlacksiteDataCompleted"
    ),
    "ForgeStasisSuit": X2WOTCLocationData(
        display_name = shadow_tech_location_prefix + "Recovered ADVENT Stasis Suit",
        id = tech_base_id + 32,
        type = "Tech",
        tags = ["goldenpath", "shadow"],
        difficulty = 50.0,
        normal_item = "ForgeStasisSuitCompleted"
    ),
    "PsiGate": X2WOTCLocationData(
        display_name = shadow_tech_location_prefix + "Psionic Gate",
        id = tech_base_id + 33,
        type = "Tech",
        tags = ["goldenpath", "shadow"],
        difficulty = 60.0,
        normal_item = "PsiGateCompleted"
    ),
    "AutopsyAdventPsiWitch": X2WOTCLocationData(
        display_name = shadow_tech_location_prefix + "Avatar Autopsy",
        id = tech_base_id + 34,
        type = "Tech",
        tags = ["goldenpath", "shadow"],
        difficulty = 75.0,
        normal_item = "AutopsyAdventPsiWitchCompleted"
    )
}

vanilla_other_techs: Dict[str, X2WOTCLocationData] = {
    "ResistanceRadio": X2WOTCLocationData(
        display_name = tech_location_prefix + "Resistance Radio",
        id = tech_base_id + 35,
        type = "Tech",
        tags = [],
        difficulty = 15.0,
        normal_item = "ResistanceRadioCompleted"
    ),
    "Tech_Elerium": X2WOTCLocationData(
        display_name = tech_location_prefix + "Elerium",
        id = tech_base_id + 36,
        type = "Tech",
        tags = [],
        difficulty = 35.0,
        normal_item = "EleriumCompleted"
    ),
    "Psionics": X2WOTCLocationData(
        display_name = tech_location_prefix + "Psionics",
        id = tech_base_id + 37,
        type = "Tech",
        tags = [],
        difficulty = 20.0,
        normal_item = "PsionicsCompleted"
    )
}

#=======================================================================================================================
#                                               ALIEN HUNTERS
#-----------------------------------------------------------------------------------------------------------------------

alien_hunters_techs: Dict[str, X2WOTCLocationData] = {
    "ExperimentalWeapons": X2WOTCLocationData(
        display_name = tech_location_prefix + "Experimental Weapons",
        id = tech_base_id + 38,
        type = "Tech",
        tags = [],
        difficulty = 5.0,
        dlc = "AH",
        normal_item = "ExperimentalWeaponsCompleted"
    ),
    "AutopsyViperKing": X2WOTCLocationData(
        display_name = tech_location_prefix + "Viper King Autopsy",
        id = tech_base_id + 39,
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 35.0,
        dlc = "AH",
        normal_item = "AutopsyViperKingCompleted"
    ),
    "AutopsyBerserkerQueen": X2WOTCLocationData(
        display_name = tech_location_prefix + "Berserker Queen Autopsy",
        id = tech_base_id + 40,
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 55.0,
        dlc = "AH",
        normal_item = "AutopsyBerserkerQueenCompleted"
    ),
    "AutopsyArchonKing": X2WOTCLocationData(
        display_name = tech_location_prefix + "Archon King Autopsy",
        id = tech_base_id + 41,
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
        display_name = tech_location_prefix + "ADVENT Purifier Autopsy",
        id = tech_base_id + 42,
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 20.0,
        dlc = "WOTC",
        normal_item = "AutopsyAdventPurifierCompleted"
    ),
    "AutopsyAdventPriest": X2WOTCLocationData(
        display_name = tech_location_prefix + "ADVENT Priest Autopsy",
        id = tech_base_id + 43,
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 20.0,
        dlc = "WOTC",
        normal_item = "AutopsyAdventPriestCompleted"
    ),
    "AutopsyTheLost": X2WOTCLocationData(
        display_name = tech_location_prefix + "The Lost Autopsy",
        id = tech_base_id + 44,
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 15.0,
        dlc = "WOTC",
        normal_item = "AutopsyTheLostCompleted"
    ),
    "AutopsySpectre": X2WOTCLocationData(
        display_name = tech_location_prefix + "Spectre Autopsy",
        id = tech_base_id + 45,
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 35.0,
        dlc = "WOTC",
        normal_item = "AutopsySpectreCompleted"
    )
}

wotc_chosen_weapon_techs: Dict[str, X2WOTCLocationData] = {
    "ChosenAssassinWeapons": X2WOTCLocationData(
        display_name = tech_location_prefix + "Assassin Weapons",
        id = tech_base_id + 46,
        type = "Tech",
        tags = [],
        difficulty = 85.0,
        dlc = "WOTC",
        normal_item = "ChosenAssassinWeaponsCompleted"
    ),
    "ChosenHunterWeapons": X2WOTCLocationData(
        display_name = tech_location_prefix + "Hunter Weapons",
        id = tech_base_id + 47,
        type = "Tech",
        tags = [],
        difficulty = 85.0,
        dlc = "WOTC",
        normal_item = "ChosenHunterWeaponsCompleted"
    ),
    "ChosenWarlockWeapons": X2WOTCLocationData(
        display_name = tech_location_prefix + "Warlock Weapons",
        id = tech_base_id + 48,
        type = "Tech",
        tags = [],
        difficulty = 85.0,
        dlc = "WOTC",
        normal_item = "ChosenWarlockWeaponsCompleted"
    )
}

########################################################################################################################
##                                            ENEMY KILL LOCATIONS                                                    ##
########################################################################################################################

kill_base_id = tech_base_id + 49

#=======================================================================================================================
#                                                 BASE GAME
#-----------------------------------------------------------------------------------------------------------------------

vanilla_enemy_kills: Dict[str, X2WOTCLocationData] = {
    "KillSectoid": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Sectoid",
        id = kill_base_id,
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 5.0
    ),
    "KillViper": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Viper",
        id = kill_base_id + 1,
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 15.0
    ),
    "KillMuton": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Muton",
        id = kill_base_id + 2,
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 25.0
    ),
    "KillBerserker": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Berserker",
        id = kill_base_id + 3,
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 35.0
    ),
    "KillArchon": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Archon",
        id = kill_base_id + 4,
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 45.0
    ),
    "KillGatekeeper": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Gatekeeper",
        id = kill_base_id + 5,
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 75.0
    ),
    "KillAndromedon": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Andromedon",
        id = kill_base_id + 6,
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 65.0
    ),
    "KillAndromedonRobot": X2WOTCLocationData(
        display_name = enemy_destroy_location_prefix + "Andromedon Suit",
        id = kill_base_id + 7,
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 65.0
    ),
    "KillFaceless": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Faceless",
        id = kill_base_id + 8,
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 10.0
    ),
    "KillChryssalid": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Chryssalid",
        id = kill_base_id + 9,
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 55.0
    ),
    "KillAdventTrooper": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "ADVENT Trooper",
        id = kill_base_id + 10,
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 0.0
    ),
    "KillAdventCaptain": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "ADVENT Officer",
        id = kill_base_id + 11,
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 0.0
    ),
    "KillCyberus": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Codex",
        id = kill_base_id + 12,
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 40.0
    ),
    "KillAdventPsiWitch": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Avatar",
        id = kill_base_id + 13,
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 75.0
    ),
    "KillAdventStunLancer": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "ADVENT Stun Lancer",
        id = kill_base_id + 14,
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 15.0
    ),
    "KillAdventShieldBearer": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "ADVENT Shieldbearer",
        id = kill_base_id + 15,
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 15.0
    ),
    "KillAdventMEC": X2WOTCLocationData(
        display_name = enemy_destroy_location_prefix + "ADVENT MEC",
        id = kill_base_id + 16,
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 25.0
    ),
    "KillAdventTurret": X2WOTCLocationData(
        display_name = enemy_destroy_location_prefix + "ADVENT Turret",
        id = kill_base_id + 17,
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 35.0
    ),
    "KillSectopod": X2WOTCLocationData(
        display_name = enemy_destroy_location_prefix + "Sectopod",
        id = kill_base_id + 18,
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 75.0
    )
}

#=======================================================================================================================
#                                               ALIEN HUNTERS
#-----------------------------------------------------------------------------------------------------------------------

alien_hunters_enemy_kills: Dict[str, X2WOTCLocationData] = {
    "KillViperKing": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Viper King",
        id = kill_base_id + 19,
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 35.0,
        dlc = "AH"
    ),
    "KillBerserkerQueen": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Berserker Queen",
        id = kill_base_id + 20,
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 55.0,
        dlc = "AH"
    ),
    "KillArchonKing": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Archon King",
        id = kill_base_id + 21,
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 75.0,
        dlc = "AH"
    )
}

#=======================================================================================================================
#                                             WAR OF THE CHOSEN
#-----------------------------------------------------------------------------------------------------------------------

wotc_enemy_kills: Dict[str, X2WOTCLocationData] = {
    "KillAdventPurifier": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "ADVENT Purifier",
        id = kill_base_id + 22,
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 20.0,
        dlc = "WOTC"
    ),
    "KillAdventPriest": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "ADVENT Priest",
        id = kill_base_id + 23,
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 20.0,
        dlc = "WOTC"
    ),
    "KillTheLost": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "The Lost",
        id = kill_base_id + 24,
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 15.0,
        dlc = "WOTC"
    ),
    "KillSpectre": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Spectre",
        id = kill_base_id + 25,
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 35.0,
        dlc = "WOTC"
    ),
    "KillChosenAssassin": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Chosen Assassin",
        id = kill_base_id + 26,
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 85.0,
        dlc = "WOTC"
    ),
    "KillChosenSniper": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Chosen Hunter",
        id = kill_base_id + 27,
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 85.0,
        dlc = "WOTC"
    ),
    "KillChosenWarlock": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Chosen Warlock",
        id = kill_base_id + 28,
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 85.0,
        dlc = "WOTC"
    )
}

########################################################################################################################
##                                              EVENT LOCATIONS                                                       ##
########################################################################################################################

event_locations: Dict[str, X2WOTCLocationData] = {
    "Victory": X2WOTCLocationData(
        display_name = "Victory",
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

kill_location_table: Dict[str, X2WOTCLocationData] = {
    **vanilla_enemy_kills,
    **alien_hunters_enemy_kills,
    **wotc_enemy_kills
}

location_table: Dict[str, X2WOTCLocationData] = {
    **tech_location_table,
    **kill_location_table,
    **event_locations
}

loc_display_name_to_key = {loc_data.display_name: key for key, loc_data in location_table.items()}
loc_id_to_key = {loc_data.id: key for key, loc_data in location_table.items() if loc_data.id}

enabled: Dict[int, Dict[str, bool]] = {}
num_locations: Dict[int, int] = {}

def init_location_vars(player: int):
    enabled[player] = {loc_name: True for loc_name in location_table.keys()}
    num_locations[player] = len(location_table)

def is_enabled(player: int, loc_name: str) -> bool:
    return enabled[player][loc_name]

def get_num_locations(player: int) -> int:
    return num_locations[player]

def disable_location(player: int, loc_name: str):
    enabled[player][loc_name] = False
    num_locations[player] -= 1
