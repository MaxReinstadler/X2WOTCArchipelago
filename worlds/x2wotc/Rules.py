from BaseClasses import MultiWorld, CollectionState
from worlds.generic.Rules import set_rule, add_rule
from .Items import item_table, get_total_power
from .Locations import location_table, is_enabled
from typing import Callable

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
    return state.has(item_table["ResistanceCommunicationsCompleted"].display_name, player)

def has_resistance_comms(state: CollectionState, player: int) -> bool:
    return state.has(item_table["ResistanceCommunicationsCompleted"].display_name, player)

def can_make_more_contact(state: CollectionState, player: int) -> bool:
    return (can_make_contact(state, player)
            and has_resistance_comms(state, player))

# Facility Assault
def can_do_facility_mission(state: CollectionState, player: int) -> bool:
    return can_make_more_contact(state, player)

# Chosen Hunt
def has_resistance_ring(state: CollectionState, player: int) -> bool:
    return True

def can_find_chosen(state: CollectionState, player: int) -> bool:
    return has_resistance_ring(state, player)

def can_kill_chosen(state: CollectionState, player: int) -> bool:
    return (can_find_chosen(state, player)
            and can_make_more_contact(state, player))

# Shadow Chamber
def has_shadow_chamber(state: CollectionState, player: int) -> bool:
    return state.has(item_table["AlienEncryptionCompleted"].display_name, player)

# Blacksite -> Blacksite Data -> Forge -> Forge Stasis Suit
def can_do_blacksite_mission(state: CollectionState, player: int) -> bool:
    return can_make_contact(state, player)

def has_blacksite_data_objective(state: CollectionState, player: int) -> bool:
    return can_do_blacksite_mission(state, player)

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
    return can_skulljack_officer(state, player)

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
            and finished_psi_gate_objective(state, player))

def can_do_truth_mission(state: CollectionState, player: int) -> bool:
    return (state.has(item_table["AutopsyAdventPsiWitchCompleted"].display_name, player)
            and has_autopsy_avatar_objective(state, player)
            and has_shadow_chamber(state, player))

def can_do_final_mission(state: CollectionState, player: int) -> bool:
    return can_do_truth_mission(state, player)

# Victory
def has_won(state: CollectionState, player: int) -> bool:
    return state.has(item_table["Victory"].display_name, player)

#======================================================================================================================#
#                                                     SET RULES                                                        #
#----------------------------------------------------------------------------------------------------------------------#

def set_rules(world: MultiWorld, player: int):
    #------------------------------------------------ Power rules -----------------------------------------------------#
    #------------------------------------------------------------------------------------------------------------------#
    for loc_name, loc_data in location_table.items():
        if not is_enabled(player, loc_name):
            continue

        location = world.get_location(loc_data.display_name, player)
        power_rule = get_power_rule(player, loc_name)
        set_rule(location, power_rule)
    
    #---------------------------------------------- Completion rule ---------------------------------------------------#
    #------------------------------------------------------------------------------------------------------------------#
    world.completion_condition[player] = lambda state: has_won(state, player)

    #------------------------------------------------ Story rules -----------------------------------------------------#
    #------------------------------------------------------------------------------------------------------------------#
    loc_name_alien_encryption = location_table["AlienEncryption"].display_name
    add_rule(world.get_location(loc_name_alien_encryption, player),
             lambda state: (can_do_blacksite_mission(state, player)
                            or can_skulljack_officer(state, player)))
    
    loc_name_codex_brain_pt1 = location_table["CodexBrainPt1"].display_name
    add_rule(world.get_location(loc_name_codex_brain_pt1, player),
             lambda state: can_skulljack_officer(state, player))
    
    loc_name_codex_brain_pt2 = location_table["CodexBrainPt2"].display_name
    add_rule(world.get_location(loc_name_codex_brain_pt2, player),
             lambda state: world.get_location(loc_name_codex_brain_pt1, player).can_reach(state))
    
    loc_name_blacksite_data = location_table["BlacksiteData"].display_name
    add_rule(world.get_location(loc_name_blacksite_data, player),
             lambda state: can_do_blacksite_mission(state, player))
    
    loc_name_forge_stasis_suit = location_table["ForgeStasisSuit"].display_name
    add_rule(world.get_location(loc_name_forge_stasis_suit, player),
             lambda state: can_do_forge_mission(state, player))
    
    loc_name_psi_gate = location_table["PsiGate"].display_name
    add_rule(world.get_location(loc_name_psi_gate, player),
             lambda state: can_do_psi_gate_mission(state, player))
    
    loc_name_autopsy_advent_psi_witch = location_table["AutopsyAdventPsiWitch"].display_name
    add_rule(world.get_location(loc_name_autopsy_advent_psi_witch, player),
             lambda state: (world.get_location(loc_name_forge_stasis_suit, player).can_reach(state)
                            and world.get_location(loc_name_psi_gate, player).can_reach(state)
                            and can_skulljack_codex(state, player)))
    
    loc_name_victory = location_table["Victory"].display_name
    add_rule(world.get_location(loc_name_victory, player),
             lambda state: can_do_final_mission(state, player))
    
    #------------------------------------------ Alien Ruler autopsy rules ---------------------------------------------#
    #------------------------------------------------------------------------------------------------------------------#
    try:
        loc_name_autopsy_viper_king = location_table["AutopsyViperKing"].display_name
        add_rule(world.get_location(loc_name_autopsy_viper_king, player),
                 lambda state: can_do_facility_mission(state, player))
        
        loc_name_autopsy_berserker_queen = location_table["AutopsyBerserkerQueen"].display_name
        add_rule(world.get_location(loc_name_autopsy_berserker_queen, player),
                 lambda state: can_do_facility_mission(state, player))
        
        loc_name_autopsy_archon_king = location_table["AutopsyArchonKing"].display_name
        add_rule(world.get_location(loc_name_autopsy_archon_king, player),
                 lambda state: can_do_facility_mission(state, player))
        
    except KeyError:
        print("Alien Ruler autopsy locations not found, assuming disabled.")
    
    #------------------------------------------- Chosen weapon tech rules ---------------------------------------------#
    #------------------------------------------------------------------------------------------------------------------#
    loc_name_chosen_assassin_weapons = location_table["ChosenAssassinWeapons"].display_name
    add_rule(world.get_location(loc_name_chosen_assassin_weapons, player),
             lambda state: can_kill_chosen(state, player))
    
    loc_name_chosen_hunter_weapons = location_table["ChosenHunterWeapons"].display_name
    add_rule(world.get_location(loc_name_chosen_hunter_weapons, player),
             lambda state: can_kill_chosen(state, player))
    
    loc_name_chosen_warlock_weapons = location_table["ChosenWarlockWeapons"].display_name
    add_rule(world.get_location(loc_name_chosen_warlock_weapons, player),
             lambda state: can_kill_chosen(state, player))
    
    #------------------------------------------------------------------------------------------------------------------#
    #--------------------------------- See ./Regions.py for entrance access rules -------------------------------------#
