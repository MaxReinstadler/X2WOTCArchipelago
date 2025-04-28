from BaseClasses import ItemClassification

from worlds.x2wotc.ItemData import X2WOTCItemData, get_new_item_id, tech_item_prefix
from worlds.x2wotc.LocationData import (
    X2WOTCLocationData,
    get_new_location_id,
    tech_location_prefix,
    enemy_kill_location_prefix
)


# Steam workshop: https://steamcommunity.com/sharedfiles/filedetails/?id=1160638944
name = "Flame Viper - WotC"

items: dict[str, X2WOTCItemData] = {
    "Autopsy_AshFlameViperCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Flame Viper Autopsy",
        id = get_new_item_id(),
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["armor", "weapon"],
        power = 25.0,
        normal_location = "Autopsy_AshFlameViper"
    )
}

# Electing not to add ammo checks because they require specific experimental ammo to build which involves RNG
locations: dict[str, X2WOTCLocationData] = {
    "Autopsy_AshFlameViper": X2WOTCLocationData(
        display_name = tech_location_prefix + "Flame Viper Autopsy",
        id = get_new_location_id(),
        layer = "Strategy",
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 25.0,
        normal_item = "Autops_AshFlameViperCompleted"
    ),
    "KillAshFlameViper": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Flame Viper",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 25.0
    )
}
