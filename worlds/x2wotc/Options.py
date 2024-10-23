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
    Set this if you wish to experience a more classical XCOM 2 story progression.
    **IMPORTANT** Must adjust the corresponding in-game settings accordingly (e.g. via MCM).

    'PsiGateObjective': Require completion of the psi gate research.
    'StasisSuitObjective': Require completion of the stasis suit research.
    'AvatarCorpseObjective': Require acquisition of an avatar corpse."""
    display_name = "Campaign Completion Requirements"
    completion_requirements = frozenset([
        "PsiGateObjective",
        "StasisSuitObjective",
        "AvatarCorpseObjective"
    ])
    default = frozenset()
    valid_keys = completion_requirements

class ProgressiveItems(OptionSet):
    """Force these items to be collected in order.
    Values: 'RifleTech', 'MeleeWeaponTech', 'ArmorTech', 'GREMLINTech', 'PsionicsTech'"""
    display_name = "Progressive Items"
    progressive_items = frozenset([
        "RifleTech",
        "MeleeWeaponTech",
        "ArmorTech",
        "GREMLINTech",
        "PsionicsTech"
    ])
    default = progressive_items
    valid_keys = progressive_items

@dataclass
class X2WOTCOptions(PerGameCommonOptions):
    disable_alien_hunters: DisableAlienHunters
    disable_integrated_dlc: DisableIntegratedDLC
    disable_contact_techs: DisableContactTechs
    campaign_completion_requirements: CampaignCompletionRequirements
    progressive_items: ProgressiveItems
