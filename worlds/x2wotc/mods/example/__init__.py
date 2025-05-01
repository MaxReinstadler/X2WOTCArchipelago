from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from worlds.x2wotc import X2WOTCWorld

from .Items import items, filler_items
from .Locations import locations
from .Options import options
from .Rules import set_rules


name = "Example Mod"

# For defining the order rules are applied in (in case of set_rule)
# The order is lowest to highest priority
rule_priority = 0.0

# Handle mod options here
def generate_early(world: "X2WOTCWorld"):
    # if world.options.example_mod_option:
    #     world.loc_manager.disable_location("ExampleModLocation")
    #     world.item_manager.disable_item("ExampleModItem")
    pass

# Insert config data here to define in-game behavior
# See Config/XComWOTCArchipelago.ini in the game mod directory
# for more information on the structure of the config file
config: dict[str, str] = {
    "X2Item_ResearchCompleted": "+CheckCompleteTechs=(TechName=ExampleTech)",
    "X2EventListener_WOTCArchipelago": "+CheckKillDefaultCharacterGroups=ExampleCharacterGroup",
    "X2Effect_ItemUseCheck": "+CheckUseItems=ExampleItem",
}
