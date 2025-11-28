from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from worlds.x2wotc import X2WOTCWorld
from ...Rules import RuleManager

from BaseClasses import CollectionState


class RuleManager_LW(RuleManager):
    # Facility Assault: Balancing omitted from first draft
    # def can_do_facility_mission(self, state):

    # Chosen hunt: Balancing omitted from first draft
    # def has_resistance_ring(self, state):
    # def can_meet_first_chosen(self, state):
    # def can_meet_all_chosen(self, state):
    # def can_hunt_all_chosen(self, state):
    # def can_defeat_assassin(self, state):
    # def can_defeat_hunter(self, state):
    # def can_defeat_warlock(self, state):
    # def can_defeat_one_chosen(self, state):
    # def can_defeat_two_chosen(self, state):
    # def can_defeat_all_chosen(self, state):
    # def can_kill_assassin(self, state):
    # def can_kill_hunter(self, state):
    # def can_kill_warlock(self, state):

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
