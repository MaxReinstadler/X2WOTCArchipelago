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

@dataclass
class X2WOTCOptions(PerGameCommonOptions):
    disable_alien_hunters: DisableAlienHunters
    disable_integrated_dlc: DisableIntegratedDLC
