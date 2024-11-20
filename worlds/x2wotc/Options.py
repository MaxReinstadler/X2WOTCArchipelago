from dataclasses import dataclass
from Options import Choice, Toggle, OptionSet, PerGameCommonOptions

class AlienHuntersDLC(Choice):
    """Set which locations and items from the Alien Hunters DLC are enabled.
    
    all:                All Alien Hunters DLC locations and items are enabled.
    no_integrated_dlc:  Experimental Weapons location is disabled; for playing without the Integrated DLC option.
    no_alien_rulers:    Alien Ruler locations are disabled; for avoiding tedious encounters.
    none:               All Alien Hunters DLC locations and items are disabled; for playing without the Alien Hunters DLC."""
    display_name = "Alien Hunters DLC"
    option_all = 0
    option_no_integrated_dlc = 1
    option_no_alien_rulers = 2
    option_none = 3
    default = 0

class DisableContactTechs(Toggle):
    """Disable Resistance Communications and Resistance Radio locations.
    **RECOMMENDED** These techs are currently broken and may create near impossible playthroughs."""
    display_name = "Disable Contact Techs"
    default = True

class CampaignCompletionRequirements(OptionSet):
    """Require these objectives to be completed for the final mission to be unlocked.
    Set this if you wish to experience a more classical XCOM 2 story progression.
    **IMPORTANT** Must adjust the corresponding in-game settings accordingly (e.g. via MCM).

    'PsiGateObjective':         Require completion of the psi gate research.
    'StasisSuitObjective':      Require completion of the stasis suit research.
    'AvatarCorpseObjective':    Require acquisition of an avatar corpse."""
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
    Valid values: 'RifleTech', 'MeleeWeaponTech', 'ArmorTech', 'GREMLINTech', 'PsionicsTech'"""
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

class ChosenHuntSanity(Toggle):
    """Shuffle Chosen Hunt covert actions and their rewards, i.e. Resistance Faction influence and Chosen Stronghold missions."""
    display_name = "Chosen Hunt-Sanity"
    default = True

@dataclass
class X2WOTCOptions(PerGameCommonOptions):
    alien_hunters_dlc: AlienHuntersDLC
    disable_contact_techs: DisableContactTechs
    campaign_completion_requirements: CampaignCompletionRequirements
    progressive_items: ProgressiveItems
    chosen_hunt_sanity: ChosenHuntSanity
