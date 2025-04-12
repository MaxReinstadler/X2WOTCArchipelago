from typing import NamedTuple


class X2WOTCLocationData(NamedTuple):
    display_name: str
    id: int | None = None
    layer: str = "Strategy"  # "Strategy" or "Tactical"
    type: str = "Event"
    tags: list[str] = []
    difficulty: float = 0.0  # Relative to total power in percent (0 to 100)
    dlc: str | None = None  # None: Base Game,
                            # "AH": Alien Hunters,
                            # "SLG": Shens Last Gift,
                            # "WOTC": War of the Chosen
    normal_item: str | None = None


next_location_id = 240223152003  # X2WOTC

def get_new_location_id() -> int:
    global next_location_id
    new_location_id = next_location_id
    next_location_id += 1
    return new_location_id

tech_location_prefix = "Research "
shadow_tech_location_prefix = "Research "
enemy_kill_location_prefix = "Kill "
enemy_destroy_location_prefix = "Destroy "
item_use_location_prefix = "Use "
covert_action_location_prefix = "Complete "

########################################################################################################################
##                            TECH LOCATIONS (RESEARCH PROJECTS / SHADOW PROJECTS)                                    ##
########################################################################################################################

#=======================================================================================================================
#                                                 BASE GAME
#-----------------------------------------------------------------------------------------------------------------------

vanilla_weapon_techs: dict[str, X2WOTCLocationData] = {
    "ModularWeapons": X2WOTCLocationData(
        display_name = tech_location_prefix + "Modular Weapons",
        id = get_new_location_id(),
        type = "Tech",
        tags = [],
        difficulty = 0.0,
        normal_item = "ModularWeaponsCompleted"
    ),
    "MagnetizedWeapons": X2WOTCLocationData(
        display_name = tech_location_prefix + "Magnetic Weapons",
        id = get_new_location_id(),
        type = "Tech",
        tags = [],
        difficulty = 15.0,
        normal_item = "MagnetizedWeaponsCompleted"
    ),
    "GaussWeapons": X2WOTCLocationData(
        display_name = tech_location_prefix + "Gauss Weapons",
        id = get_new_location_id(),
        type = "Tech",
        tags = [],
        difficulty = 25.0,
        normal_item = "GaussWeaponsCompleted"
    ),
    "PlasmaRifle": X2WOTCLocationData(
        display_name = tech_location_prefix + "Plasma Rifle",
        id = get_new_location_id(),
        type = "Tech",
        tags = [],
        difficulty = 45.0,
        normal_item = "PlasmaRifleCompleted"
    ),
    "HeavyPlasma": X2WOTCLocationData(
        display_name = tech_location_prefix + "Beam Cannon",
        id = get_new_location_id(),
        type = "Tech",
        tags = [],
        difficulty = 55.0,
        normal_item = "HeavyPlasmaCompleted"
    ),
    "PlasmaSniper": X2WOTCLocationData(
        display_name = tech_location_prefix + "Plasma Lance",
        id = get_new_location_id(),
        type = "Tech",
        tags = [],
        difficulty = 55.0,
        normal_item = "PlasmaSniperCompleted"
    ),
    "AlloyCannon": X2WOTCLocationData(
        display_name = tech_location_prefix + "Storm Gun",
        id = get_new_location_id(),
        type = "Tech",
        tags = [],
        difficulty = 55.0,
        normal_item = "AlloyCannonCompleted"
    )
}

vanilla_armor_techs: dict[str, X2WOTCLocationData] = {
    "HybridMaterials": X2WOTCLocationData(
        display_name = tech_location_prefix + "Hybrid Materials",
        id = get_new_location_id(),
        type = "Tech",
        tags = [],
        difficulty = 0.0,
        normal_item = "HybridMaterialsCompleted"
    ),
    "PlatedArmor": X2WOTCLocationData(
        display_name = tech_location_prefix + "Plated Armor",
        id = get_new_location_id(),
        type = "Tech",
        tags = [],
        difficulty = 25.0,
        normal_item = "PlatedArmorCompleted"
    ),
    "PoweredArmor": X2WOTCLocationData(
        display_name = tech_location_prefix + "Powered Armor",
        id = get_new_location_id(),
        type = "Tech",
        tags = [],
        difficulty = 45.0,
        normal_item = "PoweredArmorCompleted"
    )
}

vanilla_autopsy_techs: dict[str, X2WOTCLocationData] = {
    "AutopsySectoid": X2WOTCLocationData(
        display_name = tech_location_prefix + "Sectoid Autopsy",
        id = get_new_location_id(),
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 5.0,
        normal_item = "AutopsySectoidCompleted"
    ),
    "AutopsyViper": X2WOTCLocationData(
        display_name = tech_location_prefix + "Viper Autopsy",
        id = get_new_location_id(),
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 15.0,
        normal_item = "AutopsyViperCompleted"
    ),
    "AutopsyMuton": X2WOTCLocationData(
        display_name = tech_location_prefix + "Muton Autopsy",
        id = get_new_location_id(),
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 25.0,
        normal_item = "AutopsyMutonCompleted"
    ),
    "AutopsyBerserker": X2WOTCLocationData(
        display_name = tech_location_prefix + "Berserker Autopsy",
        id = get_new_location_id(),
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 35.0,
        normal_item = "AutopsyBerserkerCompleted"
    ),
    "AutopsyArchon": X2WOTCLocationData(
        display_name = tech_location_prefix + "Archon Autopsy",
        id = get_new_location_id(),
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 45.0,
        normal_item = "AutopsyArchonCompleted"
    ),
    "AutopsyGatekeeper": X2WOTCLocationData(
        display_name = tech_location_prefix + "Gatekeeper Autopsy",
        id = get_new_location_id(),
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 75.0,
        normal_item = "AutopsyGatekeeperCompleted"
    ),
    "AutopsyAndromedon": X2WOTCLocationData(
        display_name = tech_location_prefix + "Andromedon Autopsy",
        id = get_new_location_id(),
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 65.0,
        normal_item = "AutopsyAndromedonCompleted"
    ),
    "AutopsyFaceless": X2WOTCLocationData(
        display_name = tech_location_prefix + "Faceless Autopsy",
        id = get_new_location_id(),
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 10.0,
        normal_item = "AutopsyFacelessCompleted"
    ),
    "AutopsyChryssalid": X2WOTCLocationData(
        display_name = tech_location_prefix + "Chryssalid Autopsy",
        id = get_new_location_id(),
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 55.0,
        normal_item = "AutopsyChryssalidCompleted"
    ),
    "AutopsyAdventTrooper": X2WOTCLocationData(
        display_name = tech_location_prefix + "ADVENT Trooper Autopsy",
        id = get_new_location_id(),
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 3.0,
        normal_item = "AutopsyAdventTrooperCompleted"
    ),
    "AutopsyAdventStunLancer": X2WOTCLocationData(
        display_name = tech_location_prefix + "ADVENT Stun Lancer Autopsy",
        id = get_new_location_id(),
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 15.0,
        normal_item = "AutopsyAdventStunLancerCompleted"
    ),
    "AutopsyAdventShieldbearer": X2WOTCLocationData(
        display_name = tech_location_prefix + "ADVENT Shieldbearer Autopsy",
        id = get_new_location_id(),
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 15.0,
        normal_item = "AutopsyAdventShieldbearerCompleted"
    ),
    "AutopsyAdventMEC": X2WOTCLocationData(
        display_name = tech_location_prefix + "ADVENT MEC Breakdown",
        id = get_new_location_id(),
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 25.0,
        normal_item = "AutopsyAdventMECCompleted"
    ),
    "AutopsyAdventTurret": X2WOTCLocationData(
        display_name = tech_location_prefix + "ADVENT Turret Breakdown",
        id = get_new_location_id(),
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 85.0,
        normal_item = "AutopsyAdventTurretCompleted"
    ),
    "AutopsySectopod": X2WOTCLocationData(
        display_name = tech_location_prefix + "Sectopod Breakdown",
        id = get_new_location_id(),
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 75.0,
        normal_item = "AutopsySectopodCompleted"
    )
}

vanilla_goldenpath_techs: dict[str, X2WOTCLocationData] = {
    "AlienBiotech": X2WOTCLocationData(
        display_name = tech_location_prefix + "Alien Biotech",
        id = get_new_location_id(),
        type = "Tech",
        tags = ["goldenpath"],
        difficulty = 0.0,
        normal_item = "AlienBiotechCompleted"
    ),
    "ResistanceCommunications": X2WOTCLocationData(
        display_name = tech_location_prefix + "Resistance Communications",
        id = get_new_location_id(),
        type = "Tech",
        tags = ["goldenpath"],
        difficulty = 5.0,
        normal_item = "ResistanceCommunicationsCompleted"
    ),
    "AutopsyAdventOfficer": X2WOTCLocationData(
        display_name = tech_location_prefix + "ADVENT Officer Autopsy",
        id = get_new_location_id(),
        type = "Tech",
        tags = ["goldenpath", "autopsy"],
        difficulty = 2.0,
        normal_item = "AutopsyAdventOfficerCompleted"
    ),
    "AlienEncryption": X2WOTCLocationData(
        display_name = tech_location_prefix + "Alien Encryption",
        id = get_new_location_id(),
        type = "Tech",
        tags = ["goldenpath"],
        difficulty = 20.0,
        normal_item = "AlienEncryptionCompleted"
    ),
    "CodexBrainPt1": X2WOTCLocationData(
        display_name = shadow_tech_location_prefix + "Codex Brain",
        id = get_new_location_id(),
        type = "Tech",
        tags = ["goldenpath", "shadow"],
        difficulty = 40.0,
        normal_item = "CodexBrainPt1Completed"
    ),
    "CodexBrainPt2": X2WOTCLocationData(
        display_name = shadow_tech_location_prefix + "Encrypted Codex Data",
        id = get_new_location_id(),
        type = "Tech",
        tags = ["goldenpath", "shadow"],
        difficulty = 50.0,
        normal_item = "CodexBrainPt2Completed"
    ),
    "BlacksiteData": X2WOTCLocationData(
        display_name = shadow_tech_location_prefix + "Blacksite Vial",
        id = get_new_location_id(),
        type = "Tech",
        tags = ["goldenpath", "shadow"],
        difficulty = 30.0,
        normal_item = "BlacksiteDataCompleted"
    ),
    "ForgeStasisSuit": X2WOTCLocationData(
        display_name = shadow_tech_location_prefix + "Recovered ADVENT Stasis Suit",
        id = get_new_location_id(),
        type = "Tech",
        tags = ["goldenpath", "shadow"],
        difficulty = 50.0,
        normal_item = "ForgeStasisSuitCompleted"
    ),
    "PsiGate": X2WOTCLocationData(
        display_name = shadow_tech_location_prefix + "Psionic Gate",
        id = get_new_location_id(),
        type = "Tech",
        tags = ["goldenpath", "shadow"],
        difficulty = 60.0,
        normal_item = "PsiGateCompleted"
    ),
    "AutopsyAdventPsiWitch": X2WOTCLocationData(
        display_name = shadow_tech_location_prefix + "Avatar Autopsy",
        id = get_new_location_id(),
        type = "Tech",
        tags = ["goldenpath", "shadow"],
        difficulty = 75.0,
        normal_item = "AutopsyAdventPsiWitchCompleted"
    )
}

vanilla_other_techs: dict[str, X2WOTCLocationData] = {
    "ResistanceRadio": X2WOTCLocationData(
        display_name = tech_location_prefix + "Resistance Radio",
        id = get_new_location_id(),
        type = "Tech",
        tags = [],
        difficulty = 15.0,
        normal_item = "ResistanceRadioCompleted"
    ),
    "Tech_Elerium": X2WOTCLocationData(
        display_name = tech_location_prefix + "Elerium",
        id = get_new_location_id(),
        type = "Tech",
        tags = [],
        difficulty = 35.0,
        normal_item = "EleriumCompleted"
    ),
    "Psionics": X2WOTCLocationData(
        display_name = tech_location_prefix + "Psionics",
        id = get_new_location_id(),
        type = "Tech",
        tags = [],
        difficulty = 20.0,
        normal_item = "PsionicsCompleted"
    )
}

#=======================================================================================================================
#                                               ALIEN HUNTERS
#-----------------------------------------------------------------------------------------------------------------------

alien_hunters_techs: dict[str, X2WOTCLocationData] = {
    "ExperimentalWeapons": X2WOTCLocationData(
        display_name = tech_location_prefix + "Experimental Weapons",
        id = get_new_location_id(),
        type = "Tech",
        tags = [],
        difficulty = 5.0,
        dlc = "AH",
        normal_item = "ExperimentalWeaponsCompleted"
    ),
    "AutopsyViperKing": X2WOTCLocationData(
        display_name = tech_location_prefix + "Viper King Autopsy",
        id = get_new_location_id(),
        type = "Tech",
        tags = ["autopsy", "kill_ruler"],
        difficulty = 45.0,
        dlc = "AH",
        normal_item = "AutopsyViperKingCompleted"
    ),
    "AutopsyBerserkerQueen": X2WOTCLocationData(
        display_name = tech_location_prefix + "Berserker Queen Autopsy",
        id = get_new_location_id(),
        type = "Tech",
        tags = ["autopsy", "kill_ruler"],
        difficulty = 60.0,
        dlc = "AH",
        normal_item = "AutopsyBerserkerQueenCompleted"
    ),
    "AutopsyArchonKing": X2WOTCLocationData(
        display_name = tech_location_prefix + "Archon King Autopsy",
        id = get_new_location_id(),
        type = "Tech",
        tags = ["autopsy", "kill_ruler"],
        difficulty = 75.0,
        dlc = "AH",
        normal_item = "AutopsyArchonKingCompleted"
    )
}

#=======================================================================================================================
#                                             WAR OF THE CHOSEN
#-----------------------------------------------------------------------------------------------------------------------

wotc_autopsy_techs: dict[str, X2WOTCLocationData] = {
    "AutopsyAdventPurifier": X2WOTCLocationData(
        display_name = tech_location_prefix + "ADVENT Purifier Autopsy",
        id = get_new_location_id(),
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 20.0,
        dlc = "WOTC",
        normal_item = "AutopsyAdventPurifierCompleted"
    ),
    "AutopsyAdventPriest": X2WOTCLocationData(
        display_name = tech_location_prefix + "ADVENT Priest Autopsy",
        id = get_new_location_id(),
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 20.0,
        dlc = "WOTC",
        normal_item = "AutopsyAdventPriestCompleted"
    ),
    "AutopsyTheLost": X2WOTCLocationData(
        display_name = tech_location_prefix + "The Lost Autopsy",
        id = get_new_location_id(),
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 15.0,
        dlc = "WOTC",
        normal_item = "AutopsyTheLostCompleted"
    ),
    "AutopsySpectre": X2WOTCLocationData(
        display_name = tech_location_prefix + "Spectre Autopsy",
        id = get_new_location_id(),
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 35.0,
        dlc = "WOTC",
        normal_item = "AutopsySpectreCompleted"
    )
}

wotc_chosen_weapon_techs: dict[str, X2WOTCLocationData] = {
    "ChosenAssassinWeapons": X2WOTCLocationData(
        display_name = tech_location_prefix + "Assassin Weapons",
        id = get_new_location_id(),
        type = "Tech",
        tags = ["defeat_assassin"],
        difficulty = 80.0,
        dlc = "WOTC",
        normal_item = "ChosenAssassinWeaponsCompleted"
    ),
    "ChosenHunterWeapons": X2WOTCLocationData(
        display_name = tech_location_prefix + "Hunter Weapons",
        id = get_new_location_id(),
        type = "Tech",
        tags = ["defeat_hunter"],
        difficulty = 80.0,
        dlc = "WOTC",
        normal_item = "ChosenHunterWeaponsCompleted"
    ),
    "ChosenWarlockWeapons": X2WOTCLocationData(
        display_name = tech_location_prefix + "Warlock Weapons",
        id = get_new_location_id(),
        type = "Tech",
        tags = ["defeat_warlock"],
        difficulty = 80.0,
        dlc = "WOTC",
        normal_item = "ChosenWarlockWeaponsCompleted"
    )
}

########################################################################################################################
##                                            ENEMY KILL LOCATIONS                                                    ##
########################################################################################################################

#=======================================================================================================================
#                                                 BASE GAME
#-----------------------------------------------------------------------------------------------------------------------

vanilla_enemy_kills: dict[str, X2WOTCLocationData] = {
    "KillSectoid": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Sectoid",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 5.0
    ),
    "KillViper": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Viper",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 15.0
    ),
    "KillMuton": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Muton",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 25.0
    ),
    "KillBerserker": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Berserker",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 35.0
    ),
    "KillArchon": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Archon",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 45.0
    ),
    "KillGatekeeper": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Gatekeeper",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 75.0
    ),
    "KillAndromedon": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Andromedon",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 65.0
    ),
    "KillAndromedonRobot": X2WOTCLocationData(
        display_name = enemy_destroy_location_prefix + "Andromedon Suit",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 65.0
    ),
    "KillFaceless": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Faceless",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 10.0
    ),
    "KillChryssalid": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Chryssalid",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 55.0
    ),
    "KillAdventTrooper": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "ADVENT Trooper",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 0.0
    ),
    "KillAdventCaptain": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "ADVENT Officer",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 0.0
    ),
    "KillCyberus": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Codex",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 40.0
    ),
    "KillAdventPsiWitch": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Avatar",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 75.0
    ),
    "KillAdventStunLancer": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "ADVENT Stun Lancer",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 15.0
    ),
    "KillAdventShieldBearer": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "ADVENT Shieldbearer",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 15.0
    ),
    "KillAdventMEC": X2WOTCLocationData(
        display_name = enemy_destroy_location_prefix + "ADVENT MEC",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 25.0
    ),
    "KillAdventTurret": X2WOTCLocationData(
        display_name = enemy_destroy_location_prefix + "ADVENT Turret",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 35.0
    ),
    "KillSectopod": X2WOTCLocationData(
        display_name = enemy_destroy_location_prefix + "Sectopod",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 75.0
    )
}

#=======================================================================================================================
#                                               ALIEN HUNTERS
#-----------------------------------------------------------------------------------------------------------------------

alien_hunters_enemy_kills: dict[str, X2WOTCLocationData] = {
    "KillViperKing": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Viper King",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = ["kill_ruler"],
        difficulty = 45.0,
        dlc = "AH"
    ),
    "KillBerserkerQueen": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Berserker Queen",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = ["kill_ruler"],
        difficulty = 60.0,
        dlc = "AH"
    ),
    "KillArchonKing": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Archon King",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = ["kill_ruler"],
        difficulty = 75.0,
        dlc = "AH"
    )
}

#=======================================================================================================================
#                                             WAR OF THE CHOSEN
#-----------------------------------------------------------------------------------------------------------------------

wotc_enemy_kills: dict[str, X2WOTCLocationData] = {
    "KillAdventPurifier": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "ADVENT Purifier",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 20.0,
        dlc = "WOTC"
    ),
    "KillAdventPriest": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "ADVENT Priest",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 20.0,
        dlc = "WOTC"
    ),
    "KillTheLost": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "The Lost",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 15.0,
        dlc = "WOTC"
    ),
    "KillSpectre": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Spectre",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 35.0,
        dlc = "WOTC"
    ),
    "KillChosenAssassin": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Chosen Assassin",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = ["kill_assassin"],
        difficulty = 80.0,
        dlc = "WOTC"
    ),
    "KillChosenSniper": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Chosen Hunter",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = ["kill_hunter"],
        difficulty = 80.0,
        dlc = "WOTC"
    ),
    "KillChosenWarlock": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Chosen Warlock",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = ["kill_warlock"],
        difficulty = 80.0,
        dlc = "WOTC"
    )
}

########################################################################################################################
##                                             ITEM USE LOCATIONS                                                     ##
########################################################################################################################

#=======================================================================================================================
#                                                 BASE GAME
#-----------------------------------------------------------------------------------------------------------------------

vanilla_item_uses: dict[str, X2WOTCLocationData] = {
    "UseMedikit": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Medikit",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["utility"],
        difficulty = 0.0
    ),
    "UseNanoMedikit": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Nanomedikit",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["utility", "proving_ground", "req:AutopsyViperCompleted"],
        difficulty = 25.0
    ),
    "UseSKULLJACK": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Skulljack",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["utility", "proving_ground"],
        difficulty = 10.0
    ),
    "UseFragGrenade": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Frag Grenade",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["grenade"],
        difficulty = 0.0
    ),
    "UseAlienGrenade": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Plasma Grenade",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["grenade", "proving_ground", "req:AutopsyMutonCompleted"],
        difficulty = 15.0
    ),
    "UseProximityMine": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Proximity Mine",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["grenade", "req:AutopsyAndromedonCompleted"],
        difficulty = 5.0
    ),
    "UseFlashbangGrenade": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Flashbang Grenade",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["grenade"],
        difficulty = 0.0
    ),
    "UseEMPGrenade": X2WOTCLocationData(
        display_name = item_use_location_prefix + "EMP Grenade",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["grenade", "proving_ground", "req:AutopsyAdventMECCompleted"],
        difficulty = 15.0
    ),
    "UseEMPGrenadeMk2": X2WOTCLocationData(
        display_name = item_use_location_prefix + "EMP Bomb",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["grenade", "proving_ground", "req:AutopsyAdventMECCompleted", "req:AutopsyMutonCompleted"],
        difficulty = 35.0
    ),
    "UseSmokeGrenade": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Smoke Grenade",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["grenade"],
        difficulty = 0.0
    ),
    "UseSmokeGrenadeMk2": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Smoke Bomb",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["grenade", "proving_ground", "req:AutopsyMutonCompleted"],
        difficulty = 15.0
    ),
    "UseBattleScanner": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Battle Scanner",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["utility", "req:AutopsyAdventTrooperCompleted"],
        difficulty = 0.0
    ),
    "UseMimicBeacon": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Mimic Beacon",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["utility", "req:AutopsyFacelessCompleted"],
        difficulty = 15.0
    ),
    "UseCombatStims": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Overdrive Serum",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["utility", "req:AutopsyBerserkerCompleted"],
        difficulty = 40.0
    ),
    "UseBluescreenRounds": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Bluescreen Rounds",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["ammo", "proving_ground", "req:AutopsyAdventMECCompleted"],
        difficulty = 15.0
    ),
    "UseExperimentalAmmo": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Experimental Ammo",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["ammo", "proving_ground"],
        difficulty = 15.0
    ),
    "UseExperimentalGrenade": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Experimental Grenade",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["grenade", "proving_ground"],
        difficulty = 15.0
    ),
    "UseExperimentalGrenadeMk2": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Experimental Bomb",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["grenade", "proving_ground", "req:AutopsyMutonCompleted"],
        difficulty = 45.0
    ),
    "UseRocketLauncher": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Rocket Launcher",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["weapon", "proving_ground", "req:PlatedArmorCompleted"],
        difficulty = 25.0
    ),
    "UseExperimentalHeavyWeapon": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Experimental Heavy Weapon",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["weapon", "proving_ground", "req:PlatedArmorCompleted"],
        difficulty = 45.0
    ),
    "UseExperimentalPoweredWeapon": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Experimental Powered Weapon",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["weapon", "proving_ground", "req:PoweredArmorCompleted"],
        difficulty = 60.0
    )
}

#=======================================================================================================================
#                                               ALIEN HUNTERS
#-----------------------------------------------------------------------------------------------------------------------

alien_hunters_item_uses: dict[str, X2WOTCLocationData] = {
    "UseFrostbomb": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Frost Bomb",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["grenade", "proving_ground", "req:ExperimentalWeaponsCompleted"],
        difficulty = 50.0,
        dlc = "AH"
    )
}

#=======================================================================================================================
#                                             WAR OF THE CHOSEN
#-----------------------------------------------------------------------------------------------------------------------

wotc_item_uses: dict[str, X2WOTCLocationData] = {
    "UseUltrasonicLure": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Ultrasonic Lure",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["utility", "req:AutopsyTheLostCompleted"],
        difficulty = 0.0,
        dlc = "WOTC"
    ),
    "UseRefractionField": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Refraction Field",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["utility", "req:AutopsySpectreCompleted"],
        difficulty = 40.0,
        dlc = "WOTC"
    )
}

########################################################################################################################
##                                          COVERT ACTION LOCATIONS                                                   ##
########################################################################################################################

#=======================================================================================================================
#                                                 CHOSEN HUNT
#-----------------------------------------------------------------------------------------------------------------------

chosen_hunt_covert_actions: dict[str, X2WOTCLocationData] = {
    "ChosenHuntPt1:1": X2WOTCLocationData(
        display_name = covert_action_location_prefix + "First Chosen Hunt 1/3",
        id = get_new_location_id(),
        type = "CovertAction",
        tags = ["chosen_hunt", "meet_first_chosen", "influence:0"],
        difficulty = 20.0,
        dlc = "WOTC",
        normal_item = "DefaultChosenHuntReward"
    ),
    "ChosenHuntPt1:2": X2WOTCLocationData(
        display_name = covert_action_location_prefix + "Second Chosen Hunt 1/3",
        id = get_new_location_id(),
        type = "CovertAction",
        tags = ["chosen_hunt", "meet_all_chosen", "influence:0"],
        difficulty = 40.0,
        dlc = "WOTC",
        normal_item = "DefaultChosenHuntReward"
    ),
    "ChosenHuntPt1:3": X2WOTCLocationData(
        display_name = covert_action_location_prefix + "Third Chosen Hunt 1/3",
        id = get_new_location_id(),
        type = "CovertAction",
        tags = ["chosen_hunt", "meet_all_chosen", "influence:0"],
        difficulty = 60.0,
        dlc = "WOTC",
        normal_item = "DefaultChosenHuntReward"
    ),
    "ChosenHuntPt2:1": X2WOTCLocationData(
        display_name = covert_action_location_prefix + "First Chosen Hunt 2/3",
        id = get_new_location_id(),
        type = "CovertAction",
        tags = ["chosen_hunt", "meet_first_chosen", "influence:1"],
        difficulty = 40.0,
        dlc = "WOTC",
        normal_item = "DefaultChosenHuntReward"
    ),
    "ChosenHuntPt2:2": X2WOTCLocationData(
        display_name = covert_action_location_prefix + "Second Chosen Hunt 2/3",
        id = get_new_location_id(),
        type = "CovertAction",
        tags = ["chosen_hunt", "meet_all_chosen", "influence:3"],
        difficulty = 55.0,
        dlc = "WOTC",
        normal_item = "DefaultChosenHuntReward"
    ),
    "ChosenHuntPt2:3": X2WOTCLocationData(
        display_name = covert_action_location_prefix + "Third Chosen Hunt 2/3",
        id = get_new_location_id(),
        type = "CovertAction",
        tags = ["chosen_hunt", "meet_all_chosen", "influence:5"],
        difficulty = 70.0,
        dlc = "WOTC",
        normal_item = "DefaultChosenHuntReward"
    ),
    "ChosenHuntPt3:1": X2WOTCLocationData(
        display_name = covert_action_location_prefix + "First Chosen Hunt 3/3",
        id = get_new_location_id(),
        type = "CovertAction",
        tags = ["chosen_hunt", "meet_first_chosen", "influence:2"],
        difficulty = 60.0,
        dlc = "WOTC",
        normal_item = "DefaultChosenHuntReward"
    ),
    "ChosenHuntPt3:2": X2WOTCLocationData(
        display_name = covert_action_location_prefix + "Second Chosen Hunt 3/3",
        id = get_new_location_id(),
        type = "CovertAction",
        tags = ["chosen_hunt", "meet_all_chosen", "influence:4"],
        difficulty = 70.0,
        dlc = "WOTC",
        normal_item = "DefaultChosenHuntReward"
    ),
    "ChosenHuntPt3:3": X2WOTCLocationData(
        display_name = covert_action_location_prefix + "Third Chosen Hunt 3/3",
        id = get_new_location_id(),
        type = "CovertAction",
        tags = ["chosen_hunt", "meet_all_chosen", "influence:6"],
        difficulty = 80.0,
        dlc = "WOTC",
        normal_item = "DefaultChosenHuntReward"
    )
}

########################################################################################################################
##                                              EVENT LOCATIONS                                                       ##
########################################################################################################################

event_locations: dict[str, X2WOTCLocationData] = {
    "Victory": X2WOTCLocationData(
        display_name = "Victory",
        difficulty = 90.0,
        normal_item = "Victory"
    ),
    "Broadcast": X2WOTCLocationData(
        display_name = "Broadcast",
        difficulty = 80.0,
        normal_item = "Broadcast"
    ),
    "Stronghold1": X2WOTCLocationData(
        display_name = "Stronghold 1",
        difficulty = 50.0,
        normal_item = "Stronghold1"
    ),
    "Stronghold2": X2WOTCLocationData(
        display_name = "Stronghold 2",
        difficulty = 60.0,
        normal_item = "Stronghold2"
    ),
    "Stronghold3": X2WOTCLocationData(
        display_name = "Stronghold 3",
        difficulty = 70.0,
        normal_item = "Stronghold3"
    )
}

########################################################################################################################
##                                              TOTAL LOCATIONS                                                       ##
########################################################################################################################

tech_location_table: dict[str, X2WOTCLocationData] = {
    **vanilla_weapon_techs,
    **vanilla_armor_techs,
    **vanilla_autopsy_techs,
    **vanilla_goldenpath_techs,
    **vanilla_other_techs,
    **alien_hunters_techs,
    **wotc_autopsy_techs,
    **wotc_chosen_weapon_techs
}

kill_location_table: dict[str, X2WOTCLocationData] = {
    **vanilla_enemy_kills,
    **alien_hunters_enemy_kills,
    **wotc_enemy_kills
}

item_use_location_table: dict[str, X2WOTCLocationData] = {
    **vanilla_item_uses,
    **alien_hunters_item_uses,
    **wotc_item_uses
}

covert_action_location_table: dict[str, X2WOTCLocationData] = {
    **chosen_hunt_covert_actions
}

location_table: dict[str, X2WOTCLocationData] = {
    **tech_location_table,
    **kill_location_table,
    **item_use_location_table,
    **covert_action_location_table,
    **event_locations
}
