from BaseClasses import Item
from .ItemData import resource_item_table, weapon_mod_item_table, staff_item_table
from .ItemData import trap_item_table, filler_item_table, item_table
from .mods import mod_items
from typing import Dict
from random import Random

class X2WOTCItem(Item):
    game: str = "XCOM 2 War of the Chosen"

    def __init__(self, player: int, name: str):
        item_data = item_table[name]
        super(X2WOTCItem, self).__init__(item_data.display_name,
                                         item_data.classification,
                                         item_data.id, player)

# Add mod items
for item_name, item_data in mod_items.items():
    if item_name not in item_table:
        item_table[item_name] = item_data
    else:
        print(f"X2WOTC: Duplicate item {item_name} in mods, skipping")

item_display_name_to_key = {item_data.display_name: key for key, item_data in item_table.items()}
item_id_to_key = {item_data.id: key for key, item_data in item_table.items() if item_data.id}

total_power: Dict[int, float] = {}
item_count: Dict[int, Dict[str, int]] = {}
num_items: Dict[int, int] = {}

def init_item_vars(player: int):
    item_count[player] = {}
    num_items[player] = 0
    for item_name, item_data in item_table.items():
        if item_data.normal_location is None:  # Progressive and filler/trap items (and DefaultChosenHuntReward)
            item_count[player][item_name] = 0
        else:
            item_count[player][item_name] = 1
            num_items[player] += 1

    power_values = [item_data.power * item_count[player][item_name] for item_name, item_data in item_table.items()]
    total_power[player] = sum(power_values)

def get_total_power(player: int) -> float:
    return total_power[player]

def get_item_count(player: int, item_name: str) -> int:
    return item_count[player][item_name]

def get_num_items(player: int) -> int:
    return num_items[player]

def set_item_count(player: int, item_name: str, new_count: int, adjust_total_power: bool = True):
    old_count = item_count[player][item_name]
    item_count[player][item_name] = new_count
    num_items[player] += new_count - old_count

    if adjust_total_power:
        item_data = item_table[item_name]
        total_power[player] += item_data.power * (new_count - old_count)

def disable_item(player: int, item_name: str):
    set_item_count(player, item_name, 0)

def enable_progressive_item(player: int, item_name: str) -> bool:
    item_data = item_table[item_name]
    stages = item_data.stages
    if stages is None:
        return False
    
    for stage_name in stages:
        if item_count[player][stage_name] != 1:
            return False
        
    for stage_name in stages:
        set_item_count(player, stage_name, 0, False)

    set_item_count(player, item_name, len(stages), False)
    return True

def enable_chosen_hunt_items(player: int):
    set_item_count(player, "FactionInfluence", 6)
    set_item_count(player, "AssassinStronghold", 1)
    set_item_count(player, "HunterStronghold", 1)
    set_item_count(player, "WarlockStronghold", 1)

def add_filler_items(player: int, num_filler_items: int, weapon_mod_share: float,
                     staff_share: float, trap_share: float, random: Random):
    num_names_pairs = [
        (int(num_filler_items * weapon_mod_share), list(weapon_mod_item_table.keys())),
        (int(num_filler_items * staff_share), list(staff_item_table.keys())),
        (int(num_filler_items * trap_share), list(trap_item_table.keys()))
    ]

    num_unfilled = num_filler_items
    # Add specified number of each type of filler/trap
    for (num, names) in num_names_pairs:
        for _ in range(num):
            item_name = random.choice(names)
            old_count = item_count[player][item_name]
            set_item_count(player, item_name, old_count + 1)

            num_unfilled -= 1
            if num_unfilled == 0:
                return

    # Fill the rest with resource items
    resource_names = list(resource_item_table.keys())
    for _ in range(num_unfilled):
        item_name = random.choice(resource_names)
        old_count = item_count[player][item_name]
        set_item_count(player, item_name, old_count + 1)
