from dataclasses import dataclass
from Options import Choice, Toggle, OptionSet, Range, PerGameCommonOptions
from typing import Dict

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

class Goal(Choice):
    """Set the goal of the seed.
    
    alien_fortress:         Beat the Alien Fortress Assault mission. (final mission)
    network_tower:          Beat the ADVENT Network Tower Assault mission. (second to last mission)
    chosen_stronghold_1:    Beat any Chosen Stronghold Assault mission.
    chosen_stronghold_2:    Beat any two Chosen Stronghold Assault missions.
    chosen_stronghold_3:    Beat all three Chosen Stronghold Assault missions."""
    display_name = "Goal"
    option_alien_fortress = 0
    option_network_tower = 1
    option_chosen_stronghold_1 = 2
    option_chosen_stronghold_2 = 3
    option_chosen_stronghold_3 = 4
    default = 0

    value_to_location: Dict[int, str] = {
        0: "Victory",
        1: "Broadcast",
        2: "Stronghold1",
        3: "Stronghold2",
        4: "Stronghold3"
    }

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
    valid_keys = completion_requirements
    default = frozenset()

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
    valid_keys = progressive_items
    default = progressive_items

class EarlyProvingGround(Toggle):
    """Force the Proving Ground to be unlockable very early (sphere 1).
    This ensures access to many powerful items but may significantly increase the amount of checks available."""
    display_name = "Early Proving Ground"
    default = False

class EnemySanity(Toggle):
    """Enable locations for the first kill of each enemy type."""
    display_name = "Enemysanity"
    default = True

class ItemSanity(Toggle):
    """Enable locations for the first use of each item type."""
    display_name = "Itemsanity"
    default = True

class ChosenHuntSanity(Toggle):
    """Shuffle Chosen Hunt covert actions and their rewards, i.e. Resistance Faction influence and Chosen Stronghold missions."""
    display_name = "Chosen Hunt-Sanity"
    default = True

class WeaponModShare(Range):
    """Set the share of filler items to be weapon upgrades."""
    display_name = "Weapon Mod Share"
    range_start = 0
    range_end = 100
    default = 15

class StaffShare(Range):
    """Set the share of filler items to be staff."""
    display_name = "Staff Share"
    range_start = 0
    range_end = 100
    default = 20

class TrapShare(Range):
    """Set the share of filler items to be traps."""
    display_name = "Trap Share"
    range_start = 0
    range_end = 100
    default = 20

@dataclass
class X2WOTCOptions(PerGameCommonOptions):
    alien_hunters_dlc: AlienHuntersDLC
    goal: Goal
    campaign_completion_requirements: CampaignCompletionRequirements
    progressive_items: ProgressiveItems
    early_proving_ground: EarlyProvingGround
    enemy_sanity: EnemySanity
    item_sanity: ItemSanity
    chosen_hunt_sanity: ChosenHuntSanity
    weapon_mod_share: WeaponModShare
    staff_share: StaffShare
    trap_share: TrapShare
