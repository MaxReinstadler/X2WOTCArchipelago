from typing import Callable

from BaseClasses import MultiWorld, CollectionState
from worlds.generic.Rules import set_rule, add_rule

from .Items import item_table, get_total_power, get_item_count as get_max_item_count
from .Locations import location_table, is_enabled
from .Options import X2WOTCOptions, Goal


options: dict[int, X2WOTCOptions] = {}

#======================================================================================================================#
#                                                   GENERAL HELPERS                                                    #
#----------------------------------------------------------------------------------------------------------------------#

def get_item_count(state: CollectionState, player: int, item: str) -> int:
    count = 0
    for item_name, item_data in item_table.items():
        delta_count = state.count(item_data.display_name, player)
        if item_name == item:
            count += delta_count
        elif item_data.stages is not None:
            count += item_data.stages[:delta_count].count(item)
    return count

def get_item_count_rule(player: int, item: str, count: int, if_impossible: bool = True) -> Callable[[CollectionState], bool]:
    return lambda state: (get_item_count(state, player, item) >= count
                          or (if_impossible and get_max_item_count(player, item) < count))

def can_reach_or_disabled(world: MultiWorld, state: CollectionState, player: int, loc_name: str) -> bool:
    if not is_enabled(player, loc_name):
        return True

    loc_display_name = location_table[loc_name].display_name
    location = world.get_location(loc_display_name, player)
    return location.can_reach(state)

#======================================================================================================================#
#                                                 POWER RULE HELPERS                                                   #
#----------------------------------------------------------------------------------------------------------------------#

def get_current_power(state: CollectionState, player: int) -> float:
    power = 0.0
    for item_data in item_table.values():
        count = state.count(item_data.display_name, player)
        if item_data.stages is None:
            power += item_data.power * count
        else:
            power += sum([item_table[item_data.stages[i]].power for i in range(count)])
    return power

def has_power(state: CollectionState, player: int, power: float) -> bool:
    return get_current_power(state, player) >= power

def can_reasonably_reach(state: CollectionState, player: int, location: str) -> bool:
    difficulty = location_table[location].difficulty
    total_power = get_total_power(player)
    req_power = difficulty * total_power / 100.0
    return has_power(state, player, req_power)

def get_power_rule(player: int, location: str) -> Callable[[CollectionState], bool]:
    return lambda state: can_reasonably_reach(state, player, location)

#======================================================================================================================#
#                                                 STORY RULE HELPERS                                                   #
#----------------------------------------------------------------------------------------------------------------------#

# Contact
def can_make_contact(state: CollectionState, player: int) -> bool:
    return (state.has(item_table["ResistanceCommunicationsCompleted"].display_name, player)
            or True)  # Contact techs are always disabled

def has_radio_relays(state: CollectionState, player: int) -> bool:
    return (state.has(item_table["ResistanceRadioCompleted"].display_name, player)
            or True)  # Contact techs are always disabled

def can_make_more_contact(state: CollectionState, player: int) -> bool:
    return (can_make_contact(state, player)
            and has_radio_relays(state, player))

# Facility Assault
def can_do_facility_mission(state: CollectionState, player: int) -> bool:
    return can_make_more_contact(state, player)

# Chosen Hunt
def has_resistance_ring(state: CollectionState, player: int) -> bool:
    return True

def can_meet_first_chosen(state: CollectionState, player: int) -> bool:
    return True

def can_meet_all_chosen(state: CollectionState, player: int) -> bool:
    return can_make_more_contact(state, player)

def can_hunt_all_chosen(state: CollectionState, player: int) -> bool:
    return (can_meet_all_chosen(state, player)
            and has_resistance_ring(state, player))

def can_defeat_assassin(state: CollectionState, player: int) -> bool:
    return (state.has(item_table["AssassinStronghold"].display_name, player)
            and can_meet_all_chosen(state, player)
            or (not options[player].chosen_hunt_sanity
                and can_hunt_all_chosen(state, player)))

def can_defeat_hunter(state: CollectionState, player: int) -> bool:
    return (state.has(item_table["HunterStronghold"].display_name, player)
            and can_meet_all_chosen(state, player)
            or (not options[player].chosen_hunt_sanity
                and can_hunt_all_chosen(state, player)))

def can_defeat_warlock(state: CollectionState, player: int) -> bool:
    return (state.has(item_table["WarlockStronghold"].display_name, player)
            and can_meet_all_chosen(state, player)
            or (not options[player].chosen_hunt_sanity
                and can_hunt_all_chosen(state, player)))

def can_defeat_one_chosen(state: CollectionState, player: int) -> bool:
    return (can_defeat_assassin(state, player)
            or can_defeat_hunter(state, player)
            or can_defeat_warlock(state, player))

def can_defeat_two_chosen(state: CollectionState, player: int) -> bool:
    return ((can_defeat_assassin(state, player) and can_defeat_hunter(state, player))
            or (can_defeat_assassin(state, player) and can_defeat_warlock(state, player))
            or (can_defeat_hunter(state, player) and can_defeat_warlock(state, player)))

def can_defeat_all_chosen(state: CollectionState, player: int) -> bool:
    return (can_defeat_assassin(state, player)
            and can_defeat_hunter(state, player)
            and can_defeat_warlock(state, player))

def can_kill_assassin(state: CollectionState, player: int) -> bool:
    return (can_meet_all_chosen(state, player)
            or can_defeat_assassin(state, player))

def can_kill_hunter(state: CollectionState, player: int) -> bool:
    return (can_meet_all_chosen(state, player)
            or can_defeat_hunter(state, player))

def can_kill_warlock(state: CollectionState, player: int) -> bool:
    return (can_meet_all_chosen(state, player)
            or can_defeat_warlock(state, player))

# Shadow Chamber
def has_shadow_chamber(state: CollectionState, player: int) -> bool:
    return state.has(item_table["AlienEncryptionCompleted"].display_name, player)

# Blacksite -> Blacksite Data -> Forge -> Forge Stasis Suit
def can_do_blacksite_mission(state: CollectionState, player: int) -> bool:
    return can_make_contact(state, player)

def has_blacksite_data_objective(state: CollectionState, player: int) -> bool:
    return (can_do_blacksite_mission(state, player)
            and has_shadow_chamber(state, player))

def can_do_forge_mission(state: CollectionState, player: int) -> bool:
    return (state.has(item_table["BlacksiteDataCompleted"].display_name, player)
            and has_blacksite_data_objective(state, player)
            and can_make_more_contact(state, player))

def has_forge_stasis_suit_objective(state: CollectionState, player: int) -> bool:
    return can_do_forge_mission(state, player)

def finished_forge_stasis_suit_objective(state: CollectionState, player: int) -> bool:
    return (state.has(item_table["ForgeStasisSuitCompleted"].display_name, player)
            and has_forge_stasis_suit_objective(state, player))

# Skulljack
def has_proving_ground(state: CollectionState, player: int) -> bool:
    return state.has(item_table["AutopsyAdventOfficerCompleted"].display_name, player)

def has_skulljack(state: CollectionState, player: int) -> bool:
    return has_proving_ground(state, player)

# Skulljack Officer -> Codex Brain -> Psi Gate
def has_autopsy_officer_objective(state: CollectionState, player: int) -> bool:
    return state.has(item_table["AlienBiotechCompleted"].display_name, player)

def has_skulljack_officer_objective(state: CollectionState, player: int) -> bool:
    return (state.has(item_table["AutopsyAdventOfficerCompleted"].display_name, player)
            and has_autopsy_officer_objective(state, player))

def can_skulljack_officer(state: CollectionState, player: int) -> bool:
    return (has_skulljack_officer_objective(state, player)
            and has_skulljack(state, player))

def has_codex_brain_pt1_objective(state: CollectionState, player: int) -> bool:
    return (can_skulljack_officer(state, player)
            and has_shadow_chamber(state, player))

def can_do_psi_gate_mission(state: CollectionState, player: int) -> bool:
    return (state.has(item_table["CodexBrainPt1Completed"].display_name, player)
            and has_codex_brain_pt1_objective(state, player)
            and can_make_more_contact(state, player))

def has_psi_gate_objective(state: CollectionState, player: int) -> bool:
    return can_do_psi_gate_mission(state, player)

def finished_psi_gate_objective(state: CollectionState, player: int) -> bool:
    return (state.has(item_table["PsiGateCompleted"].display_name, player)
            and has_psi_gate_objective(state, player))

# Skulljack Codex -> Avatar Corpse
def has_codex_brain_pt2_objective(state: CollectionState, player: int) -> bool:
    return (state.has(item_table["CodexBrainPt1Completed"].display_name, player)
            and has_codex_brain_pt1_objective(state, player))

def has_skulljack_codex_objective(state: CollectionState, player: int) -> bool:
    return (state.has(item_table["CodexBrainPt2Completed"].display_name, player)
            and has_codex_brain_pt2_objective(state, player))

def can_skulljack_codex(state: CollectionState, player: int) -> bool:
    return (has_skulljack_codex_objective(state, player)
            and has_skulljack(state, player))

# Final Mission
def has_autopsy_avatar_objective(state: CollectionState, player: int) -> bool:
    return (finished_forge_stasis_suit_objective(state, player)
            or finished_psi_gate_objective(state, player)
            or can_skulljack_codex(state, player))

def can_finish_autopsy_avatar_objective(state: CollectionState, player: int) -> bool:
    req_psi_gate_obj = "PsiGateObjective" in options[player].campaign_completion_requirements
    req_stasis_suit_obj = "StasisSuitObjective" in options[player].campaign_completion_requirements
    req_avatar_corpse_obj = "AvatarCorpseObjective" in options[player].campaign_completion_requirements

    psi_gate_condition = finished_psi_gate_objective(state, player) or not req_psi_gate_obj
    stasis_suit_condition = finished_forge_stasis_suit_objective(state, player) or not req_stasis_suit_obj
    avatar_corpse_condition = can_skulljack_codex(state, player) or not req_avatar_corpse_obj

    return (psi_gate_condition and stasis_suit_condition and avatar_corpse_condition)

def can_do_truth_mission(state: CollectionState, player: int) -> bool:
    return (state.has(item_table["AutopsyAdventPsiWitchCompleted"].display_name, player)
            and has_autopsy_avatar_objective(state, player)
            and can_finish_autopsy_avatar_objective(state, player)
            and has_shadow_chamber(state, player))

def can_do_final_mission(state: CollectionState, player: int) -> bool:
    return can_do_truth_mission(state, player)

# Victory
def has_won(state: CollectionState, player: int) -> bool:
    return ((options[player].goal == Goal.option_alien_fortress and state.has(item_table["Victory"].display_name, player))
            or (options[player].goal == Goal.option_network_tower and state.has(item_table["Broadcast"].display_name, player))
            or (options[player].goal == Goal.option_chosen_stronghold_1 and state.has(item_table["Stronghold1"].display_name, player))
            or (options[player].goal == Goal.option_chosen_stronghold_2 and state.has(item_table["Stronghold2"].display_name, player))
            or (options[player].goal == Goal.option_chosen_stronghold_3 and state.has(item_table["Stronghold3"].display_name, player)))

#======================================================================================================================#
#                                                     SET RULES                                                        #
#----------------------------------------------------------------------------------------------------------------------#

def set_rules(world: MultiWorld, player: int):
    global options
    options[player] = world.worlds[player].options

    world.completion_condition[player] = lambda state: has_won(state, player)

    for loc_name, loc_data in location_table.items():
        if not is_enabled(player, loc_name):
            continue

        location = world.get_location(loc_data.display_name, player)

        #-------------------------------------------- Power rules -----------------------------------------------------#
        #--------------------------------------------------------------------------------------------------------------#
        power_rule = get_power_rule(player, loc_name)
        set_rule(location, power_rule)

        #-------------------------------------------- Story rules -----------------------------------------------------#
        #--------------------------------------------------------------------------------------------------------------#
        if loc_name == "AlienEncryption":
            add_rule(location, lambda state: (can_do_blacksite_mission(state, player)
                                              or can_skulljack_officer(state, player)))

        if loc_name == "CodexBrainPt1":
            add_rule(location, lambda state: can_skulljack_officer(state, player))

        if loc_name == "CodexBrainPt2":
            add_rule(location, lambda state: can_reach_or_disabled(world, state, player, "CodexBrainPt1"))

        if loc_name == "BlacksiteData":
            add_rule(location, lambda state: can_do_blacksite_mission(state, player))

        if loc_name == "ForgeStasisSuit":
            add_rule(location, lambda state: can_do_forge_mission(state, player))

        if loc_name == "PsiGate":
            add_rule(location, lambda state: can_do_psi_gate_mission(state, player))

        if loc_name == "AutopsyAdventPsiWitch":
            add_rule(location, lambda state: (can_reach_or_disabled(world, state, player, "ForgeStasisSuit")
                                              and can_reach_or_disabled(world, state, player, "PsiGate")
                                              and can_skulljack_codex(state, player)))

        if loc_name == "Broadcast":
            add_rule(location, lambda state: can_do_truth_mission(state, player))

        if loc_name == "Victory":
            add_rule(location, lambda state: can_do_final_mission(state, player))

        #------------------------------------------ Alien Ruler rules -------------------------------------------------#
        #--------------------------------------------------------------------------------------------------------------#
        if "kill_ruler" in loc_data.tags:
            add_rule(location, lambda state: can_do_facility_mission(state, player))

        #--------------------------------------------- Chosen rules ---------------------------------------------------#
        #--------------------------------------------------------------------------------------------------------------#
        if "meet_first_chosen" in loc_data.tags:
            add_rule(location, lambda state: can_meet_first_chosen(state, player))
        if "meet_all_chosen" in loc_data.tags:
            add_rule(location, lambda state: can_meet_all_chosen(state, player))

        if "kill_assassin" in loc_data.tags:
            add_rule(location, lambda state: can_kill_assassin(state, player))
        if "kill_hunter" in loc_data.tags:
            add_rule(location, lambda state: can_kill_hunter(state, player))
        if "kill_warlock" in loc_data.tags:
            add_rule(location, lambda state: can_kill_warlock(state, player))

        if "defeat_assassin" in loc_data.tags:
            add_rule(location, lambda state: can_defeat_assassin(state, player))
        if "defeat_hunter" in loc_data.tags:
            add_rule(location, lambda state: can_defeat_hunter(state, player))
        if "defeat_warlock" in loc_data.tags:
            add_rule(location, lambda state: can_defeat_warlock(state, player))

        for tag, value in [(f"influence:{i}", i) for i in range(7)]:
            if tag in loc_data.tags:
                influence_rule = get_item_count_rule(player, "FactionInfluence", value)
                add_rule(location, influence_rule)

        if loc_name == "Stronghold1":
            add_rule(location, lambda state: can_defeat_one_chosen(state, player))

        if loc_name == "Stronghold2":
            add_rule(location, lambda state: can_defeat_two_chosen(state, player))

        if loc_name == "Stronghold3":
            add_rule(location, lambda state: can_defeat_all_chosen(state, player))

        #-------------------------------------- Skulljack enemy kill rules --------------------------------------------#
        #--------------------------------------------------------------------------------------------------------------#
        if loc_name == "KillCyberus":
            add_rule(location, lambda state: can_skulljack_officer(state, player))

        if loc_name == "KillAdventPsiWitch":
            add_rule(location, lambda state: can_skulljack_codex(state, player))

        #---------------------------------------- Item requirement rules ----------------------------------------------#
        #--------------------------------------------------------------------------------------------------------------#
        if "proving_ground" in loc_data.tags:
            add_rule(location, lambda state: has_proving_ground(state, player))

        for tag in loc_data.tags:
            if tag.startswith("req:"):
                requirement_rule = get_item_count_rule(player, tag[4:], 1)
                add_rule(location, requirement_rule)

        # UseSKULLJACK depends on objectives
        if loc_name == "UseSKULLJACK":
            add_rule(location, lambda state: can_skulljack_officer(state, player))

    #------------------------------------------------------------------------------------------------------------------#
    #--------------------------------- See ./Regions.py for entrance access rules -------------------------------------#
