from worlds.AutoWorld import World

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from worlds.x2wotc import X2WOTCWorld

from .Items import items, filler_items
from .Locations import locations
from .Options import options
from .Rules import set_rules


name = "Long War of the Chosen"

# For defining the order rules are applied in (in case of set_rule)
# The order is lowest to highest priority
rule_priority = 0.0


# Handle mod options here
def generate_early(world: "X2WOTCWorld"):

    # Weapons have 5 tiers in LWOTC
    world.item_manager.disable_progressive_item("ProgressiveRifleTechCompleted")
    world.item_manager.disable_progressive_item("ProgressiveRifleTechCompleted+")
    if "RifleTech+" in world.options.progressive_items:
        if not world.item_manager.enable_progressive_item("ProgressiveRifleTechLwotcCompleted+"):
            print(f"X2WOTC: Failed to enable progressive LWOTC rifle tech+ for player {world.player_name}")
    elif "RifleTech" in world.options.progressive_items:
        if not world.item_manager.enable_progressive_item("ProgressiveRifleTechLwotcCompleted"):
            print(f"X2WOTC: Failed to enable progressive LWOTC rifle tech for player {world.player_name}")

    # GREMLINs are upgraded from ADVENT Robotics
    world.item_manager.disable_progressive_item("ProgressiveGREMLINTechCompleted")

    # Force early proving ground
    if world.options.early_proving_ground:
        del world.multiworld.early_items[world.player][
            world.item_manager.item_table["AutopsyAdventOfficerCompleted"].display_name
        ]
        world.multiworld.early_items[world.player][
            world.item_manager.item_table["AutopsyAdventTrooperCompleted"].display_name
        ] = 1

    # Rocket Launcher is on Gauntlet in LWOTC
    world.loc_manager.disable_location("UseRocketLauncher")

    # You can't obtain Lost corpses in LWOTC
    world.loc_manager.disable_location("AutopsyTheLost")
    world.loc_manager.disable_location("UseUltrasonicLure")

    # Experimental ammo, heavy weapon and grenade projects are disabled in LWOTC
    world.loc_manager.disable_location("UseExperimentalAmmo")
    world.loc_manager.disable_location("UseExperimentalGrenade")
    world.loc_manager.disable_location("UseExperimentalGrenadeMk2")
    world.loc_manager.disable_location("UseExperimentalHeavyWeapon")
    world.loc_manager.disable_location("UseExperimentalPoweredWeapon")
