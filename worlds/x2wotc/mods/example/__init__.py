from worlds.AutoWorld import World
from .Items import items, filler_items
from .Locations import locations
from .Rules import set_rules
from .Options import options

name = "Example Mod"

# For defining the order rules are applied in (in case of set_rule)
# The order is lowest to highest priority
rule_priority = 0.0

# Handle mod options here
# def generate_early(world: World):
#     if world.options.example_mod_option:
#         world.disable_location("ExampleModLocation")
#         world.disable_item("ExampleModItem")
