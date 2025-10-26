from worlds.AutoWorld import World

from .Items import items, filler_items
from .Locations import locations
from .Options import options
from .Rules import set_rules


name = "Long War of the Chosen"

# For defining the order rules are applied in (in case of set_rule)
# The order is lowest to highest priority
rule_priority = 0.0


# Handle mod options here
def generate_early(world: World):
    # if world.options.example_mod_option:
    #     world.disable_location("ExampleModLocation")
    #     world.disable_item("ExampleModItem")

    # This is Technical's Squaddie skill in LWOTC
    world.disable_location("UseRocketLauncher")

    # You can't obtain Lost corpses in LWOTC
    world.disable_location("AutopsyTheLost")
    world.disable_location("UseUltrasonicLure")

    # Experimental ammo, heavy weapon and grenade projects are disabled in LWOTC
    world.disable_location("UseExperimentalAmmo")
    world.disable_location("UseExperimentalGrenade")
    world.disable_location("UseExperimentalGrenadeMk2")
    world.disable_location("UseExperimentalHeavyWeapon")
    world.disable_location("UseExperimentalPoweredWeapon")
