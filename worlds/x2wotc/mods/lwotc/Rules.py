from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from worlds.x2wotc import X2WOTCWorld
from ...Rules import RuleManager

from BaseClasses import CollectionState


class RuleManager_LW(RuleManager):
    def can_do_blacksite_mission(self, state):
        return self.can_make_more_contact(state)

    def has_proving_ground(self, state):
        return self.has_item_or_impossible(state, "AutopsyAdventTrooperCompleted")

    def has_skulljack(self, state):
        return (self.has_proving_ground(state)
                and self.has_item_or_impossible(state, "AutopsyAdventOfficerCompleted"))

def set_rules(world: "X2WOTCWorld"):
    world.rule_manager = RuleManager_LW(world)
    world.rule_manager.set_rules()
