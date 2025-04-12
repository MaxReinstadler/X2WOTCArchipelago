from typing import Callable

from BaseClasses import MultiWorld, CollectionState
from worlds.generic.Rules import set_rule, add_rule

from ...LocationData import X2WOTCLocationData


def example_mod_rule(state: CollectionState, player: int) -> bool:
    return True

def set_rules(world: MultiWorld, player: int,
              location_table: dict[str, X2WOTCLocationData],
              is_enabled: Callable[[int, str], bool]):
    
    # NOTE: set_rule overrides previously applied rules, e.g. the power rule
    loc_name_example = location_table["ExampleModLocation"].display_name
    set_rule(world.get_location(loc_name_example, player),
             lambda state: example_mod_rule(state, player))
    
    loc_name_use_medikit = location_table["UseMedikit"].display_name
    if is_enabled(player, "UseMedikit"):
        add_rule(world.get_location(loc_name_use_medikit, player),
                 lambda state: example_mod_rule(state, player))
