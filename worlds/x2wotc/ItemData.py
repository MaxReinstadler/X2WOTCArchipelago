from typing import NamedTuple

from BaseClasses import ItemClassification as IC


class X2WOTCItemData(NamedTuple):
    display_name: str
    id: int | None = None
    classification: IC = IC.filler
    layer: str = "Strategy"  # "Strategy" or "Tactical"
    type: str = "Event"
    tags: set[str] = set()
    power: float = 0.0  # Relative to other values
                        # (For reference: Magnetic Weapons = 100.0)
    dlc: str | None = None  # None: Base Game,
                            # "AH": Alien Hunters,
                            # "SLG": Shens Last Gift,
                            # "WOTC": War of the Chosen
    normal_location: str | None = None
    stages: list[str | None] | None = None  # For progressive items

    mutable_fields = {"classification", "tags", "power"}

    def replace(self, **kwargs) -> "X2WOTCItemData":
        immutable_fields = set(self._fields) & set(kwargs.keys()) - self.mutable_fields
        if immutable_fields:
            raise ValueError(f"Cannot replace immutable fields {immutable_fields}.")
        return self._replace(**kwargs)


next_item_id = 240223152003  # X2WOTC

def get_new_item_id() -> int:
    global next_item_id
    new_item_id = next_item_id
    next_item_id += 1
    return new_item_id

tech_item_prefix = "[Tech] "
shadow_tech_item_prefix = "[Tech] "
chosen_hunt_item_prefix = "[Chosen Hunt] "
resource_item_prefix = "[Resource] "
weapon_mod_item_prefix = "[Upgrade] "
staff_item_prefix = "[Staff] "
trap_item_prefix = "[Trap] "

########################################################################################################################
##                        TECH COMPLETION ITEMS (RESEARCH PROJECTS / SHADOW PROJECTS)                                 ##
########################################################################################################################

#=======================================================================================================================
#                                                 BASE GAME
#-----------------------------------------------------------------------------------------------------------------------

vanilla_weapon_tech_items: dict[str, X2WOTCItemData] = {
    "ModularWeaponsCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Modular Weapons",
        id = get_new_item_id(),
        classification = IC.progression,
        type = "TechCompleted",
        tags = {"weapon"},
        power = 40.0,
        normal_location = "ModularWeapons"
    ),
    "MagnetizedWeaponsCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Magnetic Weapons",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"weapon"},
        power = 100.0,
        normal_location = "MagnetizedWeapons"
    ),
    "GaussWeaponsCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Gauss Weapons",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"weapon"},
        power = 100.0,
        normal_location = "GaussWeapons"
    ),
    "PlasmaRifleCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Plasma Rifle",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"weapon"},
        power = 160.0,
        normal_location = "PlasmaRifle"
    ),
    "HeavyPlasmaCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Beam Cannon",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"weapon"},
        power = 160.0,
        normal_location = "HeavyPlasma"
    ),
    "PlasmaSniperCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Plasma Lance",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"weapon"},
        power = 160.0,
        normal_location = "PlasmaSniper"
    ),
    "AlloyCannonCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Storm Gun",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"weapon"},
        power = 160.0,
        normal_location = "AlloyCannon"
    ),
}

vanilla_armor_tech_items: dict[str, X2WOTCItemData] = {
    "HybridMaterialsCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Hybrid Materials",
        id = get_new_item_id(),
        classification = IC.progression_deprioritized_skip_balancing,
        type = "TechCompleted",
        tags = {"armor"},
        power = 0.0,
        normal_location = "HybridMaterials"
    ),
    "PlatedArmorCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Plated Armor",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"armor"},
        power = 100.0,
        normal_location = "PlatedArmor"
    ),
    "PoweredArmorCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Powered Armor",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"armor"},
        power = 180.0,
        normal_location = "PoweredArmor"
    ),
}

vanilla_autopsy_tech_items: dict[str, X2WOTCItemData] = {
    "AutopsySectoidCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Sectoid Autopsy",
        id = get_new_item_id(),
        classification = IC.progression,
        type = "TechCompleted",
        tags = {"utility"},
        power = 20.0,
        normal_location = "AutopsySectoid"
    ),
    "AutopsyViperCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Viper Autopsy",
        id = get_new_item_id(),
        classification = IC.progression,
        type = "TechCompleted",
        tags = {"utility"},
        power = 20.0,
        normal_location = "AutopsyViper"
    ),
    "AutopsyMutonCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Muton Autopsy",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"weapon"},
        power = 80.0,
        normal_location = "AutopsyMuton"
    ),
    "AutopsyBerserkerCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Berserker Autopsy",
        id = get_new_item_id(),
        classification = IC.progression,
        type = "TechCompleted",
        tags = {"utility"},
        power = 20.0,
        normal_location = "AutopsyBerserker"
    ),
    "AutopsyArchonCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Archon Autopsy",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"weapon"},
        power = 120.0,
        normal_location = "AutopsyArchon"
    ),
    "AutopsyGatekeeperCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Gatekeeper Autopsy",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"weapon"},
        power = 60.0,
        normal_location = "AutopsyGatekeeper"
    ),
    "AutopsyAndromedonCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Andromedon Autopsy",
        id = get_new_item_id(),
        classification = IC.progression,
        type = "TechCompleted",
        tags = {"weapon"},
        power = 40.0,
        normal_location = "AutopsyAndromedon"
    ),
    "AutopsyFacelessCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Faceless Autopsy",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"utility"},
        power = 100.0,
        normal_location = "AutopsyFaceless"
    ),
    "AutopsyChryssalidCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Chryssalid Autopsy",
        id = get_new_item_id(),
        classification = IC.progression,
        type = "TechCompleted",
        tags = {"armor"},
        power = 20.0,
        normal_location = "AutopsyChryssalid"
    ),
    "AutopsyAdventTrooperCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "ADVENT Trooper Autopsy",
        id = get_new_item_id(),
        classification = IC.progression,
        type = "TechCompleted",
        tags = {"utility"},
        power = 20.0,
        normal_location = "AutopsyAdventTrooper"
    ),
    "AutopsyAdventStunLancerCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "ADVENT Stun Lancer Autopsy",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"weapon"},
        power = 80.0,
        normal_location = "AutopsyAdventStunLancer"
    ),
    "AutopsyAdventShieldbearerCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "ADVENT Shieldbearer Autopsy",
        id = get_new_item_id(),
        classification = IC.progression,
        type = "TechCompleted",
        tags = {"armor"},
        power = 20.0,
        normal_location = "AutopsyAdventShieldbearer"
    ),
    "AutopsyAdventMECCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "ADVENT MEC Breakdown",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"weapon", "utility"},
        power = 120.0,
        normal_location = "AutopsyAdventMEC"
    ),
    "AutopsyAdventTurretCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "ADVENT Turret Breakdown",
        id = get_new_item_id(),
        classification = IC.progression_deprioritized_skip_balancing,
        type = "TechCompleted",
        tags = {"facility"},
        power = 0.0,
        normal_location = "AutopsyAdventTurret"
    ),
    "AutopsySectopodCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Sectopod Breakdown",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"weapon", "utility"},
        power = 60.0,
        normal_location = "AutopsySectopod"
    ),
}

vanilla_goldenpath_tech_items: dict[str, X2WOTCItemData] = {
    "AlienBiotechCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Alien Biotech",
        id = get_new_item_id(),
        classification = IC.progression,
        type = "TechCompleted",
        tags = {"facility"},
        power = 20.0,
        normal_location = "AlienBiotech"
    ),
    "ResistanceCommunicationsCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Resistance Communications",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"facility"},
        power = 0.0,
        normal_location = "ResistanceCommunications"
    ),
    "AutopsyAdventOfficerCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "ADVENT Officer Autopsy",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"facility"},
        power = 160.0,
        normal_location = "AutopsyAdventOfficer"
    ),
    "AlienEncryptionCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Alien Encryption",
        id = get_new_item_id(),
        classification = IC.progression,
        type = "TechCompleted",
        tags = {"facility"},
        power = 20.0,
        normal_location = "AlienEncryption"
    ),
    "CodexBrainPt1Completed": X2WOTCItemData(
        display_name = shadow_tech_item_prefix + "Codex Brain",
        id = get_new_item_id(),
        classification = IC.progression_skip_balancing,
        type = "TechCompleted",
        tags = {"mission"},
        power = 0.0,
        normal_location = "CodexBrainPt1"
    ),
    "CodexBrainPt2Completed": X2WOTCItemData(
        display_name = shadow_tech_item_prefix + "Encrypted Codex Data",
        id = get_new_item_id(),
        classification = IC.progression_skip_balancing,
        type = "TechCompleted",
        power = 0.0,
        normal_location = "CodexBrainPt2"
    ),
    "BlacksiteDataCompleted": X2WOTCItemData(
        display_name = shadow_tech_item_prefix + "Blacksite Vial",
        id = get_new_item_id(),
        classification = IC.progression_skip_balancing,
        type = "TechCompleted",
        tags = {"mission"},
        power = 0.0,
        normal_location = "BlacksiteData"
    ),
    "ForgeStasisSuitCompleted": X2WOTCItemData(
        display_name = shadow_tech_item_prefix + "Recovered ADVENT Stasis Suit",
        id = get_new_item_id(),
        classification = IC.progression_skip_balancing,
        type = "TechCompleted",
        power = 0.0,
        normal_location = "ForgeStasisSuit"
    ),
    "PsiGateCompleted": X2WOTCItemData(
        display_name = shadow_tech_item_prefix + "Psionic Gate",
        id = get_new_item_id(),
        classification = IC.progression_skip_balancing,
        type = "TechCompleted",
        power = 0.0,
        normal_location = "PsiGate"
    ),
    "AutopsyAdventPsiWitchCompleted": X2WOTCItemData(
        display_name = shadow_tech_item_prefix + "Avatar Autopsy",
        id = get_new_item_id(),
        classification = IC.progression_skip_balancing,
        type = "TechCompleted",
        tags = {"mission"},
        power = 0.0,
        normal_location = "AutopsyAdventPsiWitch"
    ),
}

vanilla_other_tech_items: dict[str, X2WOTCItemData] = {
    "ResistanceRadioCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Resistance Radio",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"facility"},
        power = 0.0,
        normal_location = "ResistanceRadio"
    ),
    "EleriumCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Elerium",
        id = get_new_item_id(),
        classification = IC.progression,
        type = "TechCompleted",
        tags = {"facility"},
        power = 20.0,
        normal_location = "Tech_Elerium"
    ),
    "PsionicsCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Psionics",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"facility", "weapon"},
        power = 160.0,
        normal_location = "Psionics"
    ),
}

#=======================================================================================================================
#                                               ALIEN HUNTERS
#-----------------------------------------------------------------------------------------------------------------------

alien_hunters_tech_items: dict[str, X2WOTCItemData] = {
    "ExperimentalWeaponsCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Experimental Weapons",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"weapon", "utility"},
        power = 140.0,
        dlc = "AH",
        normal_location = "ExperimentalWeapons"
    ),
    "AutopsyViperKingCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Viper King Autopsy",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"armor"},
        power = 120.0,
        dlc = "AH",
        normal_location = "AutopsyViperKing"
    ),
    "AutopsyBerserkerQueenCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Berserker Queen Autopsy",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"armor"},
        power = 140.0,
        dlc = "AH",
        normal_location = "AutopsyBerserkerQueen"
    ),
    "AutopsyArchonKingCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Archon King Autopsy",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"armor"},
        power = 160.0,
        dlc = "AH",
        normal_location = "AutopsyArchonKing"
    ),
}

#=======================================================================================================================
#                                             WAR OF THE CHOSEN
#-----------------------------------------------------------------------------------------------------------------------

wotc_autopsy_tech_items: dict[str, X2WOTCItemData] = {
    "AutopsyAdventPurifierCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "ADVENT Purifier Autopsy",
        id = get_new_item_id(),
        classification = IC.progression,
        type = "TechCompleted",
        tags = {"armor"},
        power = 20.0,
        dlc = "WOTC",
        normal_location = "AutopsyAdventPurifier"
    ),
    "AutopsyAdventPriestCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "ADVENT Priest Autopsy",
        id = get_new_item_id(),
        classification = IC.progression_deprioritized_skip_balancing,
        type = "TechCompleted",
        tags = {"utility"},
        power = 0.0,
        dlc = "WOTC",
        normal_location = "AutopsyAdventPriest"
    ),
    "AutopsyTheLostCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "The Lost Autopsy",
        id = get_new_item_id(),
        classification = IC.progression_deprioritized_skip_balancing,
        type = "TechCompleted",
        tags = {"utility"},
        power = 0.0,
        dlc = "WOTC",
        normal_location = "AutopsyTheLost"
    ),
    "AutopsySpectreCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Spectre Autopsy",
        id = get_new_item_id(),
        classification = IC.progression,
        type = "TechCompleted",
        tags = {"utility"},
        power = 20.0,
        dlc = "WOTC",
        normal_location = "AutopsySpectre"
    ),
}

wotc_chosen_weapon_tech_items: dict[str, X2WOTCItemData] = {
    "ChosenAssassinWeaponsCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Assassin Weapons",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"weapon"},
        power = 200.0,
        dlc = "WOTC",
        normal_location = "ChosenAssassinWeapons"
    ),
    "ChosenHunterWeaponsCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Hunter Weapons",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"weapon"},
        power = 200.0,
        dlc = "WOTC",
        normal_location = "ChosenHunterWeapons"
    ),
    "ChosenWarlockWeaponsCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Warlock Weapons",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"weapon"},
        power = 200.0,
        dlc = "WOTC",
        normal_location = "ChosenWarlockWeapons"
    ),
}

#=======================================================================================================================
#                                            PROGRESSIVE TECH ITEMS
#-----------------------------------------------------------------------------------------------------------------------

progressive_tech_items: dict[str, X2WOTCItemData] = {
    "ProgressiveRifleTechCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Progressive Rifle",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"weapon", "progressive"},
        stages = [
            "MagnetizedWeaponsCompleted",
            "PlasmaRifleCompleted",
        ]
    ),
    "ProgressiveRifleTechCompleted+": X2WOTCItemData(
        display_name = tech_item_prefix + "Progressive Rifle+",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"weapon", "progressive"},
        stages = [
            "ModularWeaponsCompleted",
            "MagnetizedWeaponsCompleted",
            "PlasmaRifleCompleted",
        ]
    ),
    "ProgressiveArmorTechCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Progressive Armor",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"armor", "progressive"},
        stages = [
            "PlatedArmorCompleted",
            "PoweredArmorCompleted",
        ]
    ),
    "ProgressiveArmorTechCompleted+": X2WOTCItemData(
        display_name = tech_item_prefix + "Progressive Armor+",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"armor", "progressive"},
        stages = [
            "HybridMaterialsCompleted",
            "PlatedArmorCompleted",
            "PoweredArmorCompleted",
        ]
    ),
    "ProgressiveMeleeTechCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Progressive Melee Weapon",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"weapon", "progressive"},
        stages = [
            "AutopsyAdventStunLancerCompleted",
            "AutopsyArchonCompleted",
        ]
    ),
    "ProgressiveGREMLINTechCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Progressive GREMLIN",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"utility", "weapon", "progressive"},
        stages = [
            "AutopsyAdventMECCompleted",
            "AutopsySectopodCompleted",
        ]
    ),
    "ProgressivePsionicsTechCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Progressive Psionics",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "TechCompleted",
        tags = {"facility", "weapon", "progressive"},
        stages = [
            "PsionicsCompleted",
            "AutopsyGatekeeperCompleted",
        ]
    ),
}

#=======================================================================================================================
#                                             TECH FRAGMENT ITEMS
#-----------------------------------------------------------------------------------------------------------------------

tech_fragment_items: dict[str, X2WOTCItemData] = {
    "ChosenAssassinWeaponsFragment2": X2WOTCItemData(
        display_name = tech_item_prefix + "Assassin Weapons Fragment (1/2)",
        id = get_new_item_id(),
        classification = IC.progression_skip_balancing,
        type = "TechCompleted",
        tags = {"weapon", "fragment"},
        dlc = "WOTC",
        stages = [
            None,
            "ChosenAssassinWeaponsCompleted",
        ]
    ),
    "ChosenHunterWeaponsFragment2": X2WOTCItemData(
        display_name = tech_item_prefix + "Hunter Weapons Fragment (1/2)",
        id = get_new_item_id(),
        classification = IC.progression_skip_balancing,
        type = "TechCompleted",
        tags = {"weapon", "fragment"},
        dlc = "WOTC",
        stages = [
            None,
            "ChosenHunterWeaponsCompleted",
        ]
    ),
    "ChosenWarlockWeaponsFragment2": X2WOTCItemData(
        display_name = tech_item_prefix + "Warlock Weapons Fragment (1/2)",
        id = get_new_item_id(),
        classification = IC.progression_skip_balancing,
        type = "TechCompleted",
        tags = {"weapon", "fragment"},
        dlc = "WOTC",
        stages = [
            None,
            "ChosenWarlockWeaponsCompleted",
        ]
    ),
    "ChosenAssassinWeaponsFragment3": X2WOTCItemData(
        display_name = tech_item_prefix + "Assassin Weapons Fragment (1/3)",
        id = get_new_item_id(),
        classification = IC.progression_skip_balancing,
        type = "TechCompleted",
        tags = {"weapon", "fragment"},
        dlc = "WOTC",
        stages = [
            None,
            None,
            "ChosenAssassinWeaponsCompleted",
        ]
    ),
    "ChosenHunterWeaponsFragment3": X2WOTCItemData(
        display_name = tech_item_prefix + "Hunter Weapons Fragment (1/3)",
        id = get_new_item_id(),
        classification = IC.progression_skip_balancing,
        type = "TechCompleted",
        tags = {"weapon", "fragment"},
        dlc = "WOTC",
        stages = [
            None,
            None,
            "ChosenHunterWeaponsCompleted",
        ]
    ),
    "ChosenWarlockWeaponsFragment3": X2WOTCItemData(
        display_name = tech_item_prefix + "Warlock Weapons Fragment (1/3)",
        id = get_new_item_id(),
        classification = IC.progression_skip_balancing,
        type = "TechCompleted",
        tags = {"weapon", "fragment"},
        dlc = "WOTC",
        stages = [
            None,
            None,
            "ChosenWarlockWeaponsCompleted",
        ]
    ),
}

########################################################################################################################
##                                         COVERT ACTION REWARD ITEMS                                                 ##
########################################################################################################################

#=======================================================================================================================
#                                              CHOSEN HUNT ITEMS
#-----------------------------------------------------------------------------------------------------------------------

chosen_hunt_items: dict[str, X2WOTCItemData] = {
    "FactionInfluence": X2WOTCItemData(
        display_name = chosen_hunt_item_prefix + "Faction Influence",
        id = get_new_item_id(),
        classification = IC.progression,
        type = "CovertActionReward",
        tags = {"chosen_hunt"},
        power = 40.0,
        dlc = "WOTC"
    ),
    "AssassinStronghold": X2WOTCItemData(
        display_name = chosen_hunt_item_prefix + "Assassin Stronghold",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "CovertActionReward",
        tags = {"chosen_hunt"},
        power = 80.0,
        dlc = "WOTC"
    ),
    "HunterStronghold": X2WOTCItemData(
        display_name = chosen_hunt_item_prefix + "Hunter Stronghold",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "CovertActionReward",
        tags = {"chosen_hunt"},
        power = 80.0,
        dlc = "WOTC"
    ),
    "WarlockStronghold": X2WOTCItemData(
        display_name = chosen_hunt_item_prefix + "Warlock Stronghold",
        id = get_new_item_id(),
        classification = IC.progression | IC.useful,
        type = "CovertActionReward",
        tags = {"chosen_hunt"},
        power = 80.0,
        dlc = "WOTC"
    ),
    # Default reward for disabled chosen hunt locations (never add to itempool)
    "DefaultChosenHuntReward": X2WOTCItemData(
        display_name = "Regular Covert Action Reward",
        type = "CovertActionReward"
    ),
}

########################################################################################################################
##                                                FILLER ITEMS                                                        ##
########################################################################################################################

#=======================================================================================================================
#                                                RESOURCE ITEMS
#-----------------------------------------------------------------------------------------------------------------------

supplies_items: dict[str, X2WOTCItemData] = {
    "Supplies:20": X2WOTCItemData(
        display_name = resource_item_prefix + "20 Supplies",
        id = get_new_item_id(),
        type = "Resource",
        tags = {"filler", "supplies"}
    ),
    "Supplies:35": X2WOTCItemData(
        display_name = resource_item_prefix + "35 Supplies",
        id = get_new_item_id(),
        type = "Resource",
        tags = {"filler", "supplies"}
    ),
    "Supplies:50": X2WOTCItemData(
        display_name = resource_item_prefix + "50 Supplies",
        id = get_new_item_id(),
        classification = IC.useful,
        type = "Resource",
        tags = {"filler", "supplies"}
    ),
}

intel_items: dict[str, X2WOTCItemData] = {
    "Intel:10": X2WOTCItemData(
        display_name = resource_item_prefix + "10 Intel",
        id = get_new_item_id(),
        type = "Resource",
        tags = {"filler", "intel"}
    ),
    "Intel:15": X2WOTCItemData(
        display_name = resource_item_prefix + "15 Intel",
        id = get_new_item_id(),
        type = "Resource",
        tags = {"filler", "intel"}
    ),
    "Intel:20": X2WOTCItemData(
        display_name = resource_item_prefix + "20 Intel",
        id = get_new_item_id(),
        classification = IC.useful,
        type = "Resource",
        tags = {"filler", "intel"}
    ),
}

alien_alloy_items: dict[str, X2WOTCItemData] = {
    "AlienAlloy:5": X2WOTCItemData(
        display_name = resource_item_prefix + "5 Alien Alloys",
        id = get_new_item_id(),
        type = "Resource",
        tags = {"filler", "alien_alloy"}
    ),
    "AlienAlloy:10": X2WOTCItemData(
        display_name = resource_item_prefix + "10 Alien Alloys",
        id = get_new_item_id(),
        type = "Resource",
        tags = {"filler", "alien_alloy"}
    ),
    "AlienAlloy:15": X2WOTCItemData(
        display_name = resource_item_prefix + "15 Alien Alloys",
        id = get_new_item_id(),
        classification = IC.useful,
        type = "Resource",
        tags = {"filler", "alien_alloy"}
    ),
}

elerium_dust_items: dict[str, X2WOTCItemData] = {
    "EleriumDust:5": X2WOTCItemData(
        display_name = resource_item_prefix + "5 Elerium Crystals",
        id = get_new_item_id(),
        type = "Resource",
        tags = {"filler", "elerium_dust"}
    ),
    "EleriumDust:10": X2WOTCItemData(
        display_name = resource_item_prefix + "10 Elerium Crystals",
        id = get_new_item_id(),
        type = "Resource",
        tags = {"filler", "elerium_dust"}
    ),
    "EleriumDust:15": X2WOTCItemData(
        display_name = resource_item_prefix + "15 Elerium Crystals",
        id = get_new_item_id(),
        classification = IC.useful,
        type = "Resource",
        tags = {"filler", "elerium_dust"}
    ),
}

elerium_core_items: dict[str, X2WOTCItemData] = {
    "EleriumCore:1": X2WOTCItemData(
        display_name = resource_item_prefix + "1 Elerium Core",
        id = get_new_item_id(),
        classification = IC.useful,
        type = "Resource",
        tags = {"filler", "elerium_core"}
    ),
}

ability_point_items: dict[str, X2WOTCItemData] = {
    "AbilityPoint:3": X2WOTCItemData(
        display_name = resource_item_prefix + "3 Ability Points",
        id = get_new_item_id(),
        type = "Resource",
        tags = {"filler", "ability_point"},
        dlc = "WOTC"
    ),
    "AbilityPoint:5": X2WOTCItemData(
        display_name = resource_item_prefix + "5 Ability Points",
        id = get_new_item_id(),
        type = "Resource",
        tags = {"filler", "ability_point"},
        dlc = "WOTC"
    ),
    "AbilityPoint:7": X2WOTCItemData(
        display_name = resource_item_prefix + "7 Ability Points",
        id = get_new_item_id(),
        classification = IC.useful,
        type = "Resource",
        tags = {"filler", "ability_point"},
        dlc = "WOTC"
    ),
}

#=======================================================================================================================
#                                               WEAPON MOD ITEMS
#-----------------------------------------------------------------------------------------------------------------------

advanced_weapon_mod_items: dict[str, X2WOTCItemData] = {
    "AimUpgrade_Adv": X2WOTCItemData(
        display_name = weapon_mod_item_prefix + "Advanced Scope",
        id = get_new_item_id(),
        type = "WeaponMod",
        tags = {"filler", "scope", "advanced"}
    ),
    "CritUpgrade_Adv": X2WOTCItemData(
        display_name = weapon_mod_item_prefix + "Advanced Laser Sight",
        id = get_new_item_id(),
        type = "WeaponMod",
        tags = {"filler", "laser_sight", "advanced"}
    ),
    "ReloadUpgrade_Adv": X2WOTCItemData(
        display_name = weapon_mod_item_prefix + "Advanced Auto-Loader",
        id = get_new_item_id(),
        type = "WeaponMod",
        tags = {"filler", "auto_loader", "advanced"}
    ),
    "FreeKillUpgrade_Adv": X2WOTCItemData(
        display_name = weapon_mod_item_prefix + "Advanced Repeater",
        id = get_new_item_id(),
        type = "WeaponMod",
        tags = {"filler", "repeater", "advanced"}
    ),
    "MissDamageUpgrade_Adv": X2WOTCItemData(
        display_name = weapon_mod_item_prefix + "Advanced Stock",
        id = get_new_item_id(),
        type = "WeaponMod",
        tags = {"filler", "stock", "advanced"}
    ),
    "FreeFireUpgrade_Adv": X2WOTCItemData(
        display_name = weapon_mod_item_prefix + "Advanced Hair Trigger",
        id = get_new_item_id(),
        type = "WeaponMod",
        tags = {"filler", "hair_trigger", "advanced"}
    ),
    "ClipSizeUpgrade_Adv": X2WOTCItemData(
        display_name = weapon_mod_item_prefix + "Advanced Expanded Magazine",
        id = get_new_item_id(),
        type = "WeaponMod",
        tags = {"filler", "expanded_magazine", "advanced"}
    ),
}

superior_weapon_mod_items: dict[str, X2WOTCItemData] = {
    "AimUpgrade_Sup": X2WOTCItemData(
        display_name = weapon_mod_item_prefix + "Superior Scope",
        id = get_new_item_id(),
        classification = IC.useful,
        type = "WeaponMod",
        tags = {"filler", "scope", "superior"}
    ),
    "CritUpgrade_Sup": X2WOTCItemData(
        display_name = weapon_mod_item_prefix + "Superior Laser Sight",
        id = get_new_item_id(),
        classification = IC.useful,
        type = "WeaponMod",
        tags = {"filler", "laser_sight", "superior"}
    ),
    "ReloadUpgrade_Sup": X2WOTCItemData(
        display_name = weapon_mod_item_prefix + "Superior Auto-Loader",
        id = get_new_item_id(),
        classification = IC.useful,
        type = "WeaponMod",
        tags = {"filler", "auto_loader", "superior"}
    ),
    "FreeKillUpgrade_Sup": X2WOTCItemData(
        display_name = weapon_mod_item_prefix + "Superior Repeater",
        id = get_new_item_id(),
        classification = IC.useful,
        type = "WeaponMod",
        tags = {"filler", "repeater", "superior"}
    ),
    "MissDamageUpgrade_Sup": X2WOTCItemData(
        display_name = weapon_mod_item_prefix + "Superior Stock",
        id = get_new_item_id(),
        classification = IC.useful,
        type = "WeaponMod",
        tags = {"filler", "stock", "superior"}
    ),
    "FreeFireUpgrade_Sup": X2WOTCItemData(
        display_name = weapon_mod_item_prefix + "Superior Hair Trigger",
        id = get_new_item_id(),
        classification = IC.useful,
        type = "WeaponMod",
        tags = {"filler", "hair_trigger", "superior"}
    ),
    "ClipSizeUpgrade_Sup": X2WOTCItemData(
        display_name = weapon_mod_item_prefix + "Superior Expanded Magazine",
        id = get_new_item_id(),
        classification = IC.useful,
        type = "WeaponMod",
        tags = {"filler", "expanded_magazine", "superior"}
    ),
}

#=======================================================================================================================
#                                                 STAFF ITEMS
#-----------------------------------------------------------------------------------------------------------------------

scientist_items: dict[str, X2WOTCItemData] = {
    "Scientist:1": X2WOTCItemData(
        display_name = staff_item_prefix + "1 Scientist",
        id = get_new_item_id(),
        classification = IC.useful,
        type = "Staff",
        tags = {"filler", "scientist"}
    ),
}

engineer_items: dict[str, X2WOTCItemData] = {
    "Engineer:1": X2WOTCItemData(
        display_name = staff_item_prefix + "1 Engineer",
        id = get_new_item_id(),
        classification = IC.useful,
        type = "Staff",
        tags = {"filler", "engineer"}
    ),
}

########################################################################################################################
##                                                TRAP ITEMS                                                          ##
########################################################################################################################

doom_items: dict[str, X2WOTCItemData] = {
    "Doom:1": X2WOTCItemData(
        display_name = trap_item_prefix + "Avatar Project +1",
        id = get_new_item_id(),
        classification = IC.trap,
        type = "Trap",
        tags = {"doom"}
    ),
}

force_level_items: dict[str, X2WOTCItemData] = {
    "ForceLevel:1": X2WOTCItemData(
        display_name = trap_item_prefix + "Force Level +1",
        id = get_new_item_id(),
        classification = IC.trap,
        type = "Trap",
        tags = {"force_level"}
    ),
}

########################################################################################################################
##                                                EVENT ITEMS                                                         ##
########################################################################################################################

event_items: dict[str, X2WOTCItemData] = {
    "Victory": X2WOTCItemData(
        display_name = "Victory",
        classification = IC.progression,
        normal_location = "Victory"
    ),
    "Broadcast": X2WOTCItemData(
        display_name = "Broadcast",
        classification = IC.progression,
        normal_location = "Broadcast"
    ),
    "Stronghold1": X2WOTCItemData(
        display_name = "Stronghold1",
        classification = IC.progression,
        normal_location = "Stronghold1"
    ),
    "Stronghold2": X2WOTCItemData(
        display_name = "Stronghold2",
        classification = IC.progression,
        normal_location = "Stronghold2"
    ),
    "Stronghold3": X2WOTCItemData(
        display_name = "Stronghold3",
        classification = IC.progression,
        normal_location = "Stronghold3"
    ),
}

########################################################################################################################
##                                                TOTAL ITEMS                                                         ##
########################################################################################################################

tech_item_table: dict[str, X2WOTCItemData] = {
    **vanilla_weapon_tech_items,
    **vanilla_armor_tech_items,
    **vanilla_autopsy_tech_items,
    **vanilla_goldenpath_tech_items,
    **vanilla_other_tech_items,
    **alien_hunters_tech_items,
    **wotc_autopsy_tech_items,
    **wotc_chosen_weapon_tech_items,
    **progressive_tech_items,
    **tech_fragment_items,
}

covert_action_item_table: dict[str, X2WOTCItemData] = {
    **chosen_hunt_items,
}

resource_item_table: dict[str, X2WOTCItemData] = {
    **supplies_items,
    **intel_items,
    **alien_alloy_items,
    **elerium_dust_items,
    **elerium_core_items,
    **ability_point_items,
}

weapon_mod_item_table: dict[str, X2WOTCItemData] = {
    **advanced_weapon_mod_items,
    **superior_weapon_mod_items,
}

staff_item_table: dict[str, X2WOTCItemData] = {
    **scientist_items,
    **engineer_items,
}

filler_item_table: dict[str, X2WOTCItemData] = {
    **resource_item_table,
    **weapon_mod_item_table,
    **staff_item_table,
}

trap_item_table: dict[str, X2WOTCItemData] = {
    **doom_items,
    **force_level_items,
}

item_table: dict[str, X2WOTCItemData] = {
    **tech_item_table,
    **covert_action_item_table,
    **filler_item_table,
    **trap_item_table,
    **event_items,
}
