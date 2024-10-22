from dataclasses import dataclass
from Options import Toggle, OptionSet, PerGameCommonOptions

class DisableAlienHunters(Toggle):
    """Generation leaves all checks introduced by the Alien Hunters DLC untouched.
    Activate this if you don't own the DLC or wish to play without it."""
    display_name = "Disable Alien Hunters DLC"
    default = False

class DisableIntegratedDLC(Toggle):
    """Generation leaves all checks introduced by the Integrated DLC option untouched.
    Activate this if you wish to play with DLC missions enabled."""
    display_name = "Disable Integrated DLC"
    default = False

class DisableContactTechs(Toggle):
    """Generation leaves Resistance Communications and Resistance Radio untouched.
    **RECOMMENDED** These techs are currently broken and may create near impossible playthroughs."""
    display_name = "Disable Contact Techs"
    default = True

class CampaignCompletionRequirements(OptionSet):
    """Require these objectives to be completed for the final mission to be unlocked.
    Set this if you wish to experience more classical XCOM 2 story progression.
    **IMPORTANT** Must adjust the corresponding in-game settings accordingly (e.g. via MCM).

    PsiGateObjective: Requires completion of the psi gate research.
    StasisSuitObjective: Requires completion of the stasis suit research.
    AvatarCorpseObjective: Requires acquisition of an avatar corpse."""
    display_name = "Campaign Completion Requirements"
    default = {}
    valid_keys = {"PsiGateObjective", "StasisSuitObjective", "AvatarCorpseObjective"}

class EnableProgressiveRifleTechs(Toggle):
    """Forces rifle techs to be collected in order."""
    display_name = "Enable Progressive Rifle Techs"
    default = True

class EnableProgressiveMeleeTechs(Toggle):
    """Forces melee weapon techs to be collected in order."""
    display_name = "Enable Progressive Melee Weapon Techs"
    default = True

class EnableProgressiveArmorTechs(Toggle):
    """Forces armor techs to be collected in order."""
    display_name = "Enable Progressive Armor Techs"
    default = True

class EnableProgressiveGREMLINTechs(Toggle):
    """Forces GREMLIN techs to be collected in order."""
    display_name = "Enable Progressive GREMLIN Techs"
    default = True

class EnableProgressivePsionicsTechs(Toggle):
    """Forces psionics techs to be collected in order."""
    display_name = "Enable Progressive Psionics Techs"
    default = True

@dataclass
class X2WOTCOptions(PerGameCommonOptions):
    disable_alien_hunters: DisableAlienHunters
    disable_integrated_dlc: DisableIntegratedDLC
    disable_contact_techs: DisableContactTechs
    campaign_completion_requirements: CampaignCompletionRequirements
    enable_progressive_rifle_techs: EnableProgressiveRifleTechs
    enable_progressive_melee_techs: EnableProgressiveMeleeTechs
    enable_progressive_armor_techs: EnableProgressiveArmorTechs
    enable_progressive_gremlin_techs: EnableProgressiveGREMLINTechs
    enable_progressive_psionics_techs: EnableProgressivePsionicsTechs
