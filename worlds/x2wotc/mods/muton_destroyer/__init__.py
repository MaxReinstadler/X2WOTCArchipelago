from BaseClasses import ItemClassification

from ...ItemData import X2WOTCItemData, get_new_item_id, tech_item_prefix
from ...LocationData import (
    X2WOTCLocationData,
    get_new_location_id,
    tech_location_prefix,
    enemy_kill_location_prefix,
    item_use_location_prefix
)


# Steam workshop: https://steamcommunity.com/sharedfiles/filedetails/?id=2482812108
name = "Muton Destroyer - WotC"

items: dict[str, X2WOTCItemData] = {
    "Autopsy_AshMutonDestroyerCompleted": X2WOTCItemData(
        display_name = tech_item_prefix + "Muton Destroyer Autopsy",
        id = get_new_item_id(),
        classification = ItemClassification.progression,
        layer = "Strategy",
        type = "TechCompleted",
        tags = ["armor", "weapon"],
        power = 35.0,
        normal_location = "Autopsy_AshMutonDestroyer"
    )
}

locations: dict[str, X2WOTCLocationData] = {
    "Autopsy_AshMutonDestroyer": X2WOTCLocationData(
        display_name = tech_location_prefix + "Muton Destroyer Autopsy",
        id = get_new_location_id(),
        layer = "Strategy",
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 30.0,
        normal_item = "Autopsy_AshMutonDestroyerCompleted"
    ),
    "KillAshMutonDestroyer": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Muton Destroyer",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 30.0
    ),
    "UseWeapon_AshConcussionGrenadeXCom": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Concussion Grenade",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["grenade", "proving_ground", "req:Autopsy_AshMutonDestroyerCompleted"],
        difficulty = 20.0,
    )
}
