import os
import importlib
from BaseClasses import MultiWorld
from Options import Option
from worlds.AutoWorld import World
from ..ItemData import X2WOTCItemData
from ..LocationData import X2WOTCLocationData
from typing import Optional, List, Dict, Tuple, NamedTuple, Callable

ModOption = Tuple[str, type[Option]]  # (option name, option class)

class X2WOTCModData(NamedTuple):
    name: str
    rule_priority: float = 0.0
    items: Dict[str, X2WOTCItemData] = {}
    locations: Dict[str, X2WOTCLocationData] = {}
    set_rules: Optional[Callable[[MultiWorld, int], None]] = None
    options: List[ModOption] = []
    generate_early: Optional[Callable[[World], None]] = None

mods_data: List[X2WOTCModData] = []

mod_items: Dict[str, X2WOTCItemData] = {}
mod_locations: Dict[str, X2WOTCLocationData] = {}
mod_options: List[ModOption] = []

base_path = os.path.dirname(__file__)
directories = [name for name in os.listdir(base_path)
               if os.path.isdir(os.path.join(base_path, name)) 
               and not name.startswith("__")]

# Collect mod data from directories
for directory in directories:
    try:
        module = importlib.import_module(f".{directory}", __name__)
    except ImportError:
        print(f"X2WOTC: Failed to import module mods/{directory}")
        continue

    mods_data.append(X2WOTCModData(
        name = module.name if hasattr(module, "name") else directory,
        rule_priority = module.rule_priority if hasattr(module, "rule_priority") else 0,
        items = module.items if hasattr(module, "items") else {},
        locations = module.locations if hasattr(module, "locations") else {},
        set_rules = module.set_rules if hasattr(module, "set_rules") else None,
        options = module.options if hasattr(module, "options") else [],
        generate_early = module.generate_early if hasattr(module, "generate_early") else None
    ))

# Sort mods by rule priority
mods_data.sort(key=lambda x: x.rule_priority)

# Aggregate mod items, locations and options
for mod_data in mods_data:
    for item_name, item_data in mod_data.items.items():
        if item_name not in mod_items:
            mod_items[item_name] = item_data
        else:
            print(f"X2WOTC: Duplicate item name {item_name} in mod {mod_data.name}")

    for loc_name, loc_data in mod_data.locations.items():
        if loc_name not in mod_locations:
            mod_locations[loc_name] = loc_data
        else:
            print(f"X2WOTC: Duplicate location name {loc_name} in mod {mod_data.name}")

    for option in mod_data.options:
        if option[0] not in [mod_option[0] for mod_option in mod_options]:
            mod_options.append(option)
        else:
            print(f"X2WOTC: Duplicate option name {option[0]} in mod {mod_data.name}")
