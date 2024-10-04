from dataclasses import dataclass
from Options import Toggle, PerGameCommonOptions

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

class EnableProgressiveRifleTechs(Toggle):
    """Forces rifle techs to be collected in order."""
    display_name = "Enable Progressive Rifle Techs"
    default = False

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
    enable_progressive_rifle_techs: EnableProgressiveRifleTechs
    enable_progressive_melee_techs: EnableProgressiveMeleeTechs
    enable_progressive_armor_techs: EnableProgressiveArmorTechs
    enable_progressive_gremlin_techs: EnableProgressiveGREMLINTechs
    enable_progressive_psionics_techs: EnableProgressivePsionicsTechs
