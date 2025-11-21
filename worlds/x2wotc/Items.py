from copy import deepcopy
from random import Random

from BaseClasses import Item

from .ItemData import (
    X2WOTCItemData,
    resource_item_table,
    weapon_mod_item_table,
    staff_item_table,
    trap_item_table,
    filler_item_table,
    item_table,
)

from .mods import mod_items


class X2WOTCItem(Item):
    game: str = "XCOM 2 War of the Chosen"

    def __init__(self, player: int, item_data: X2WOTCItemData):
        super(X2WOTCItem, self).__init__(
            item_data.display_name,
            item_data.classification,
            item_data.id,
            player
        )


# Add mod items
for item_name, item_data in mod_items.items():
    if item_name not in item_table:
        item_table[item_name] = item_data
    else:
        print(f"X2WOTC: Duplicate item {item_name} in mods, skipping")

# Lookup tables
item_display_name_to_id = {
    item_data.display_name: item_data.id
    for item_data in item_table.values()
    if item_data.id
}
item_display_name_to_key = {
    item_data.display_name: key
    for key, item_data in item_table.items()
}
item_id_to_key = {
    item_data.id: key
    for key, item_data in item_table.items()
    if item_data.id
}

# Groups
item_types = {
    item_data.type
    for item_data in item_table.values()
    if item_data.id
}
item_groups = {
    item_type: {
        item_data.display_name
        for item_data in item_table.values()
        if item_data.id and item_data.type == item_type
    } for item_type in item_types
}

# Progressive groups
"""
for item_data in item_table.values():
    if item_data.stages is not None:
        item_groups[item_data.display_name] = {item_data.display_name}
        for stage in item_data.stages:
            stage_name = item_table[stage].display_name
            item_groups[item_data.display_name].add(stage_name)

            if stage_name not in item_groups:
                item_groups[stage_name] = {stage_name}
            item_groups[stage_name].add(item_data.display_name)
"""


class ItemManager:
    item_display_name_to_id = item_display_name_to_id
    item_display_name_to_key = item_display_name_to_key
    item_id_to_key = item_id_to_key

    item_types = item_types
    item_groups = item_groups

    def __init__(self):
        self.item_table: dict[str, X2WOTCItemData] = deepcopy(item_table)
        self.locked: bool = False

        self.resource_items = list(resource_item_table.keys())
        self.weapon_mod_items = list(weapon_mod_item_table.keys())
        self.staff_items = list(staff_item_table.keys())
        self.trap_items = list(trap_item_table.keys())

        self.filler_item_names = [
            item_data.display_name
            for item_data in filler_item_table.values()
        ]

        self.item_count: dict[str, int] = {}
        self.num_items: int = 0

        for item_name, item_data in self.item_table.items():
            if item_data.normal_location is None:  # Progressive and filler/trap items (and DefaultChosenHuntReward)
                self.item_count[item_name] = 0
            else:
                self.item_count[item_name] = 1
                self.num_items += 1

    def replace(self, item_name: str, **kwargs):
        if self.locked:
            raise RuntimeError("Cannot replace item data after item manager has been locked.")

        item_data = self.item_table[item_name]
        self.item_table[item_name] = item_data.replace(**kwargs)

    def set_item_count(self, item_name: str, new_count: int):
        if self.locked:
            raise RuntimeError("Cannot set item counts after item manager has been locked.")

        old_count = self.item_count[item_name]
        self.item_count[item_name] = new_count
        self.num_items += new_count - old_count

    def add_item(self, item_name: str, count: int = 1):
        self.set_item_count(item_name, self.item_count[item_name] + count)

    def disable_item(self, item_name: str):
        self.set_item_count(item_name, 0)

    def enable_progressive_item(self, item_name: str) -> bool:
        item_data = self.item_table[item_name]
        stages = item_data.stages
        if stages is None:
            return False

        if self.item_count[item_name] != 0:
            return False
        for stage_name in stages:
            if stage_name is not None and self.item_count[stage_name] != 1:
                return False

        for stage_name in stages:
            if stage_name is not None:
                self.set_item_count(stage_name, 0)

        self.set_item_count(item_name, len(stages))
        return True

    def disable_progressive_item(self, item_name: str):
        item_data = self.item_table[item_name]
        stages = item_data.stages
        if stages is None:
            return False

        if self.item_count[item_name] != len(stages):
            return False
        for stage_name in stages:
            if stage_name is not None and self.item_count[stage_name] != 0:
                return False

        for stage_name in stages:
            if stage_name is not None:
                self.set_item_count(stage_name, 1)

        self.set_item_count(item_name, 0)
        return True

    def enable_chosen_hunt_items(self):
        self.set_item_count("FactionInfluence", 6)
        self.set_item_count("AssassinStronghold", 1)
        self.set_item_count("HunterStronghold", 1)
        self.set_item_count("WarlockStronghold", 1)

    def enable_mod_filler_item(self, item_name: str):
        self.resource_items.append(item_name)
        self.filler_item_names.append(self.item_table[item_name].display_name)

    def add_filler_items(
            self,
            num_filler_items: int,
            weapon_mod_share: float,
            staff_share: float,
            trap_share: float,
            random: Random
        ):
        num_names_pairs = [
            (
                int(num_filler_items * weapon_mod_share),
                list(self.weapon_mod_items)
            ),
            (
                int(num_filler_items * staff_share),
                list(self.staff_items)
            ),
            (
                int(num_filler_items * trap_share),
                list(self.trap_items)
            ),
        ]

        # Add specified number of each type of filler/trap
        num_unfilled = num_filler_items
        for (num, names) in num_names_pairs:
            for _ in range(num):
                item_name = random.choice(names)
                self.add_item(item_name)

                num_unfilled -= 1
                if num_unfilled == 0:
                    return

        # Fill the rest with resource or mod filler items
        possible_names = list(self.resource_items)
        for _ in range(num_unfilled):
            item_name = random.choice(possible_names)
            self.add_item(item_name)
