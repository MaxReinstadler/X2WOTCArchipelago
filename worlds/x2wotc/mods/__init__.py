import importlib
import pkgutil
from typing import NamedTuple, Callable

from BaseClasses import MultiWorld
from Options import Option
from worlds.AutoWorld import World

from ..ItemData import X2WOTCItemData
from ..LocationData import X2WOTCLocationData


ModOption = tuple[str, type[Option]]  # (option name, option class)


class X2WOTCModData(NamedTuple):
    name: str
    rule_priority: float = 0.0
    items: dict[str, X2WOTCItemData] = {}
    filler_items: dict[str, X2WOTCItemData] = {}
    locations: dict[str, X2WOTCLocationData] = {}
    set_rules: Callable[[MultiWorld, int], None] | None = None
    options: list[ModOption] = []
    generate_early: Callable[[World], None] | None = None


mods_data: list[X2WOTCModData] = []

mod_names: list[str] = []
mod_items: dict[str, X2WOTCItemData] = {}
mod_filler_items: dict[str, X2WOTCItemData] = {}
mod_locations: dict[str, X2WOTCLocationData] = {}
mod_options: list[ModOption] = []

# Collect mod data from directories
for loader, module_name, ispkg in pkgutil.iter_modules(__path__):
    try:
        module = importlib.import_module(f".{module_name}", __name__)
    except ImportError:
        print(f"X2WOTC: Failed to import module mods/{module_name}")
        continue

    mods_data.append(X2WOTCModData(
        name = module.name if hasattr(module, "name") else module_name,
        rule_priority = module.rule_priority if hasattr(module, "rule_priority") else 0,
        items = module.items if hasattr(module, "items") else {},
        filler_items = module.filler_items if hasattr(module, "filler_items") else {},
        locations = module.locations if hasattr(module, "locations") else {},
        set_rules = module.set_rules if hasattr(module, "set_rules") else None,
        options = module.options if hasattr(module, "options") else [],
        generate_early = module.generate_early if hasattr(module, "generate_early") else None
    ))

# Sort mods by rule priority
mods_data.sort(key=lambda x: x.rule_priority)

# Flatten mod data and check for duplicates
for mod_data in mods_data:
    if mod_data.name not in mod_names:
        mod_names.append(mod_data.name)
    else:
        print(f"X2WOTC: Duplicate mod name {mod_data.name}")

    for item_name, item_data in mod_data.items.items():
        if item_name not in mod_items:
            mod_items[item_name] = item_data
        else:
            print(f"X2WOTC: Duplicate item name {item_name} in mod {mod_data.name}")

    for item_name, item_data in mod_data.filler_items.items():
        if item_name not in mod_filler_items:
            mod_filler_items[item_name] = item_data
        else:
            print(f"X2WOTC: Duplicate filler item name {item_name} in mod {mod_data.name}")

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

# Sort mod names alphabetically
mod_names.sort()
