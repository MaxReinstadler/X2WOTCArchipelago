from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from worlds.x2wotc import X2WOTCWorld

from BaseClasses import CollectionState
from worlds.generic.Rules import set_rule, add_rule


def example_mod_rule(state: CollectionState, player: int) -> bool:
    return True

def set_rules(world: "X2WOTCWorld"):
    for loc_name, loc_data in world.loc_manager.location_table.items():

        # Make sure not to edit rules for disabled locations
        if not world.loc_manager.enabled[loc_name]:
            continue

        location = world.multiworld.get_location(loc_data.display_name, world.player)

        # NOTE: set_rule overrides previously applied rules, e.g. the power rule
        if loc_name == "ExampleModLocation":
            set_rule(location, lambda state: example_mod_rule(state, world.player))

        # You can change rules for existing locations
        if loc_name == "UseMedikit":
            add_rule(location, lambda state: example_mod_rule(state, world.player))
