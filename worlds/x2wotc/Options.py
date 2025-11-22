from dataclasses import dataclass, make_dataclass
from schema import And, Schema

from Options import Choice, Toggle, OptionDict, OptionSet, Range, PerGameCommonOptions

from .mods import mod_names, mod_options


class AlienHuntersDLC(Choice):
    """Set which locations and items from the Alien Hunters DLC are enabled.

    all:                  All Alien Hunters DLC locations and items are enabled.
    no_integrated_dlc:    Experimental Weapons location is disabled; for playing without the Integrated DLC option.
    no_alien_rulers:      Alien Ruler locations are disabled; for avoiding tedious encounters.
    none:                 All Alien Hunters DLC locations and items are disabled; for playing without the Alien Hunters DLC."""
    display_name = "Alien Hunters DLC"
    option_all = 0
    option_no_integrated_dlc = 1
    option_no_alien_rulers = 2
    option_none = 3
    default = 3


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

    value_to_location: dict[int, str] = {
        0: "Victory",
        1: "Broadcast",
        2: "Stronghold1",
        3: "Stronghold2",
        4: "Stronghold3",
    }


class CampaignCompletionRequirements(OptionSet):
    """Require these objectives to be completed for the final mission to be unlocked.
    Set all if you wish to experience a more vanilla XCOM 2 story progression.

    'PsiGateObjective':         Require completion of the psi gate research.
    'StasisSuitObjective':      Require completion of the stasis suit research.
    'AvatarCorpseObjective':    Require acquisition of an avatar corpse."""
    display_name = "Campaign Completion Requirements"
    completion_requirements = frozenset([
        "PsiGateObjective",
        "StasisSuitObjective",
        "AvatarCorpseObjective",
    ])
    valid_keys = completion_requirements
    default = frozenset()


class EnemySanity(Toggle):
    """Enable locations for the first kill of each enemy type."""
    display_name = "Enemysanity"
    default = True


class ItemSanity(Toggle):
    """Enable locations for the first use of each item type."""
    display_name = "Itemsanity"
    default = False


class ChosenHuntSanity(Toggle):
    """Shuffle Chosen Hunt covert actions and their rewards, i.e. Resistance Faction influence and Chosen Stronghold missions."""
    display_name = "Chosen Huntsanity"
    default = False


class ProgressiveItems(OptionSet):
    """Force these items to be collected in order.
    Valid values: 'RifleTech', 'RifleTech+' (includes [Tech] Modular Weapons),
                  'ArmorTech', 'ArmorTech+' (includes [Tech] Hybrid Materials),
                  'MeleeWeaponTech', 'GREMLINTech', 'PsionicsTech'"""
    display_name = "Progressive Items"
    valid_keys = frozenset([
        "RifleTech",
        "RifleTech+",
        "ArmorTech",
        "ArmorTech+",
        "MeleeWeaponTech",
        "GREMLINTech",
        "PsionicsTech",
    ])
    default = frozenset([
        "RifleTech",
        "ArmorTech",
        "MeleeWeaponTech",
        "GREMLINTech",
        "PsionicsTech",
    ])


class ChosenWeaponFragments(Choice):
    """Split Chosen weapons into two or three fragments each. Collect all fragments to unlock the corresponding tech.
    This should decrease the likelihood of receiving Chosen weapons too early and trivializing the game.
    NOTE: This option requires enabling additional vacant locations, e.g. through Enemysanity or Itemsanity."""
    display_name = "Chosen Weapon Fragments"
    option_off = 0
    option_two = 1
    option_three = 2
    default = 0


class EarlyProvingGround(Toggle):
    """Force the Proving Ground to be unlockable very early (sphere 1).
    This ensures access to many powerful items but may significantly increase the amount of reachable locations."""
    display_name = "Early Proving Ground"
    default = False


class ResourceShare(Range):
    """Set the share of filler items to be resources."""
    display_name = "Resource Share"
    range_start = 0
    range_end = 100
    default = 65


class WeaponModShare(Range):
    """Set the share of filler items to be weapon upgrades."""
    display_name = "Weapon Mod Share"
    range_start = 0
    range_end = 100
    default = 15


class PCSShare(Range):
    """Set the share of filler items to be PCSs."""
    display_name = "PCS Share"
    range_start = 0
    range_end = 100
    default = 10


class StaffShare(Range):
    """Set the share of filler items to be staff."""
    display_name = "Staff Share"
    range_start = 0
    range_end = 100
    default = 10


class TrapShare(Range):
    """Set the share of filler items to be traps."""
    display_name = "Trap Share"
    range_start = 0
    range_end = 100
    default = 0


class EnemyRando(Toggle):
    """Enable enemy shuffle, randomizing both scripted and procedural encounters."""
    display_name = "Enemy Rando"
    default = False


class EnemyPlando(OptionDict):
    """If enemy rando is enabled, constrain enemy placements.
    Define explicit shuffle groups with the 'forced' key.
    Exempt enemies from shuffling with the 'fixed' key.
    
    Example: {
        'forced': [
            [['Sectoid', 'Muton'], ['Viper', 'Archon']],
            [['Adv'], ['Adv']]
        ],
        'fixed': ['Gatekeeper', 'Sectopod']
    }
    Sectoids and Mutons will be replaced by Vipers and Archons randomly.
    All ADVENT enemies will be replaced by random ADVENT enemies.
    Gatekeepers and Sectopods will not be shuffled.
    All other enemies will be shuffled among each other."""
    display_name = "Enemy Plando"
    schema = Schema({
        "forced": [And([[str]], lambda l: len(l) == 2)],
        "fixed": [str],
    })
    default = {"forced": [], "fixed": []}


class HintResearchProjects(Choice):
    """Enable research project hints in the Avenger laboratory and shadow chamber.
    Can be changed in-game via Mod Config Menu.
    
    off:       Reveal no item info and don't create server hints.
    partial:   Reveal item categories but don't create server hints.
    full:      Reveal all item info and create server hints."""
    display_name = "Hint Research Projects"
    option_off = 0
    option_partial = 1
    option_full = 2
    default = 0


class SkipMissionTypes(OptionSet):
    """Automatically skip these mission types when they are spawned from a regular calendar event.
    Can be changed in-game via Mod Config Menu.
    Valid values: 'SupplyRaid', 'CouncilMission', 'ResistanceOp'"""
    display_name = "Skip Tedious Missions"
    mission_types = frozenset([
        "SupplyRaid",
        "CouncilMission",
        "ResistanceOp",
    ])
    valid_keys = mission_types
    default = mission_types


class DisableCovertActionRisks(OptionSet):
    """Disable these covert action risks.
    Can be changed in-game via Mod Config Menu.
    Valid values: 'Ambush', 'Capture'"""
    display_name = "Disarm Covert Action Risks"
    covert_action_risks = frozenset([
        "Ambush",
        "Capture",
    ])
    valid_keys = covert_action_risks
    default = covert_action_risks


class SupplyRaidRewardBase(Range):
    """Set the amount of resources that are rewarded for skipped supply raids.
    The base represents a percentage of set maximum values for supplies (200), alien alloys (80), elerium crystals (40) and elerium cores (3).
    The error determines the range of possible values, e.g. 35-65% for default settings.
    Can be changed in-game via Mod Config Menu."""
    display_name = "Supply Raid Reward Base"
    range_start = 0
    range_end = 100
    default = 50


class SupplyRaidRewardError(Range):
    """Set the amount of resources that are rewarded for skipped supply raids.
    The base represents a percentage of set maximum values for supplies (200), alien alloys (80), elerium crystals (40) and elerium cores (3).
    The error determines the range of possible values, e.g. 35-65% for default settings.
    Can be changed in-game via Mod Config Menu."""
    display_name = "Supply Raid Reward Error"
    range_start = 0
    range_end = 100
    default = 15


class ExtraXPGain(Range):
    """Set the amount of extra XP that soldiers gain passively.
    Each time an enemy dies, each soldier has the given fraction of a kill attributed to them, speeding up promotions.
    Because this system is agnostic to who got the final hit, soldiers with low kill counts will benefit more from the increase.
    In general, the effect will be much stronger than it seems; the default setting for example will work out to a 35% increase in XP from kills,
    but something like a 140% increase in XP from assists, meaning the actual bonus lies somewhere in between.
    Can be changed in-game via Mod Config Menu."""
    display_name = "Extra XP Gain"
    range_start = 0
    range_end = 200
    default = 35


class ExtraCorpseGain(Range):
    """Set the amount of extra corpses that each enemy drops.
    Can be changed in-game via Mod Config Menu."""
    display_name = "Extra Corpse Gain"
    range_start = 0
    range_end = 5
    default = 1


class DisableDayOneTraps(Toggle):
    """Disable traps when they are received during the first day of a campaign.
    One use for this is if you wish to retire traps received during previous runs after a restart.
    Can be changed in-game via Mod Config Menu."""
    display_name = "Disable Day One Traps"
    default = False


class ActiveMods(OptionSet):
    """Activate these mods from the x2wotc/mods directory.
    This is only relevant when modding *the APWorld* (NOT the game), leave empty if you're unsure what that means.
    List all available mods with the /mods client command."""
    display_name = "Active Mods"
    valid_keys = frozenset(mod_names)
    default = frozenset()


@dataclass
class X2WOTCOptions(PerGameCommonOptions):
    # DLC options
    alien_hunters_dlc: AlienHuntersDLC

    # Goal options
    goal: Goal
    campaign_completion_requirements: CampaignCompletionRequirements

    # Location options
    enemy_sanity: EnemySanity
    item_sanity: ItemSanity
    chosen_hunt_sanity: ChosenHuntSanity

    # Item options
    progressive_items: ProgressiveItems
    chosen_weapon_fragments: ChosenWeaponFragments
    early_proving_ground: EarlyProvingGround

    # Filler options
    resource_share: ResourceShare
    weapon_mod_share: WeaponModShare
    pcs_share: PCSShare
    staff_share: StaffShare
    trap_share: TrapShare

    # More randomization options
    enemy_rando: EnemyRando
    enemy_plando: EnemyPlando

    # Config options
    hint_research_projects: HintResearchProjects
    skip_mission_types: SkipMissionTypes
    disable_covert_action_risks: DisableCovertActionRisks
    supply_raid_reward_base: SupplyRaidRewardBase
    supply_raid_reward_error: SupplyRaidRewardError
    extra_xp_gain: ExtraXPGain
    extra_corpse_gain: ExtraCorpseGain
    disable_day_one_traps: DisableDayOneTraps

    # Mod options
    active_mods: ActiveMods


# Add mod options
X2WOTCOptions = make_dataclass("X2WOTCOptions", mod_options, bases=(X2WOTCOptions,))
