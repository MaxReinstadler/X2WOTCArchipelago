from typing import Callable

from BaseClasses import MultiWorld, CollectionState
from worlds.generic.Rules import set_rule, add_rule

from ...LocationData import X2WOTCLocationData


def example_mod_rule(state: CollectionState, player: int) -> bool:
    return True

def set_rules(world: MultiWorld, player: int,
              location_table: dict[str, X2WOTCLocationData],
              is_enabled: Callable[[int, str], bool]):
    for loc_name, loc_data in location_table.items():

        # Make sure not to edit rules for disabled locations
        if not is_enabled(player, loc_name):
            continue

        location = world.get_location(loc_data.display_name, player)

        # NOTE: set_rule overrides previously applied rules, e.g. the power rule
        if loc_name == "ExampleModLocation":
            set_rule(location, lambda state: example_mod_rule(state, player))

        # You can change rules for existing locations
        if loc_name == "UseMedikit":
            add_rule(location, lambda state: example_mod_rule(state, player))
