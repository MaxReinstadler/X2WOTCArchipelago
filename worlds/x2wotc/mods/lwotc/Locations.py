from ...LocationData import (
    X2WOTCLocationData,
    get_new_location_id,
    tech_location_prefix,
    enemy_kill_location_prefix,
    enemy_destroy_location_prefix,
    item_use_location_prefix
)

# For the full definition of X2WOTCLocationData, see worlds/x2wotc/LocationData.py
lwotc_techs: dict[str, X2WOTCLocationData] = {
    "AutopsyDrone": X2WOTCLocationData(
        display_name = tech_location_prefix + "ADVENT Robotics",
        id = get_new_location_id(),
        layer = "Strategy",
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 40.0,
        normal_item = "AutopsyDroneCompleted"
    ),
    "AutopsyMutonElite": X2WOTCLocationData(
        display_name = tech_location_prefix + "Muton Elite Autopsy",
        id = get_new_location_id(),
        layer = "Strategy",
        type = "Tech",
        tags = ["autopsy"],
        difficulty = 75.0,
        normal_item = "AutopsyMutonEliteCompleted"
    ),
    "LaserWeapons": X2WOTCLocationData(
        display_name = tech_location_prefix + "Laser Weapons",
        id = get_new_location_id(),
        layer = "Strategy",
        type = "Tech",
        tags = [],
        difficulty = 5.0,
        normal_item = "LaserWeaponsCompleted"
    ),
    "AdvancedLasers": X2WOTCLocationData(
        display_name = tech_location_prefix + "Advanced Laser Weapons",
        id = get_new_location_id(),
        layer = "Strategy",
        type = "Tech",
        tags = [],
        difficulty = 10.0,
        normal_item = "AdvancedLasersCompleted"
    ),
    "Coilguns": X2WOTCLocationData(
        display_name = tech_location_prefix + "Coilguns",
        id = get_new_location_id(),
        layer = "Strategy",
        type = "Tech",
        tags = [],
        difficulty = 35.0,
        normal_item = "CoilgunsCompleted"
    ),
    "AdvancedCoilguns": X2WOTCLocationData(
        display_name = tech_location_prefix + "Advanced Coilguns",
        id = get_new_location_id(),
        layer = "Strategy",
        type = "Tech",
        tags = [],
        difficulty = 40.0,
        normal_item = "AdvancedCoilgunsCompleted"
    ),
    "EXOSuit": X2WOTCLocationData(
        display_name = tech_location_prefix + "Battle Armor",
        id = get_new_location_id(),
        layer = "Strategy",
        type = "Tech",
        tags = [],
        difficulty = 35.0,
        normal_item = "EXOSuitCompleted"
    ),
    "WARSuit": X2WOTCLocationData(
        display_name = tech_location_prefix + "Battlesuits",
        id = get_new_location_id(),
        layer = "Strategy",
        type = "Tech",
        tags = [],
        difficulty = 55.0,
        normal_item = "WARSuitCompleted"
    ),
    "SpiderSuit": X2WOTCLocationData(
        display_name = tech_location_prefix + "Mobile Armor",
        id = get_new_location_id(),
        layer = "Strategy",
        type = "Tech",
        tags = [],
        difficulty = 35.0,
        normal_item = "SpiderSuitCompleted"
    ),
    "WraithSuit": X2WOTCLocationData(
        display_name = tech_location_prefix + "Shadow Armor",
        id = get_new_location_id(),
        layer = "Strategy",
        type = "Tech",
        tags = [],
        difficulty = 55.0,
        normal_item = "WraithSuitCompleted"
    ),
}

lwotc_item_uses: dict[str, X2WOTCLocationData] = {
    "UseShapedCharge": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Shaped Charge",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["grenade"],
        difficulty = 0.0,
    ),
    "UseGasGrenade": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Gas Grenade",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["grenade", "proving_ground", "req:HybridMaterialsCompleted", "req:AutopsyViperCompleted"],
        difficulty = 35.0,
    ),
    "UseGasBomb": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Gas Bomb",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["grenade", "proving_ground", "req:HybridMaterialsCompleted", "req:AutopsyViperCompleted", "req:AutopsyMutonCompleted", "req:AutopsyAndromedonCompleted"],
        difficulty = 65.0,
    ),
    "UseIncendiaryGrenade": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Incendiary Grenade",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["grenade", "proving_ground", "req:AutopsyPurifierCompleted"],
        difficulty = 35.0,
    ),
    "UseIncendiaryBomb": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Incendiary Bomb",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        difficulty = 65.0,
        tags = ["grenade", "proving_ground", "req:AutopsyPurifierCompleted", "req:AutopsyMutonCompleted", "req:AutopsyAndromedonCompleted"],
    ),
    "UseAcidGrenade": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Acid Grenade",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["grenade", "proving_ground", "req:AutopsySpectreCompleted"],
        difficulty = 35.0,
    ),
    "UseAcidBomb": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Acid Bomb",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["grenade", "proving_ground", "req:AutopsySpectreCompleted", "req:AutopsyMutonCompleted", "req:AutopsyAndromedonCompleted"],
        difficulty = 65.0,
    ),
    "UsePrototypePlasmaBlaster": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Prototype Plasma Blaster",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["weapon", "req:EXOSuitCompleted"],
        difficulty = 40.0,
    ),
    "UsePlasmaBlaster": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Plasma Blaster",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["weapon", "proving_ground", "req:PlasmaRifleCompleted", "req:EXOSuitCompleted"],
        difficulty = 75.0,
    ),
    "UseShredderGun": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Shredder Gun",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["weapon", "req:EXOSuitCompleted"],
        difficulty = 40.0,
    ),
    "UseShredstormCannon": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Shredstorm Cannon",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["weapon", "proving_ground", "req:AdvancedCoilgunsCompleted", "req:WARSuitCompleted"],
        difficulty = 75.0,
    ),
    "UseAPRounds": X2WOTCLocationData(
        display_name = item_use_location_prefix + "AP Rounds",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["ammo", "req:AlienBiotechCompleted"],
        difficulty = 10.0,
    ),
    "UseTracerRounds": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Tracer Rounds",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["ammo"],
        difficulty = 5.0,
    ),
    "UseTalonRounds": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Talon Rounds",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["ammo", "proving_ground", "req:AutopsyAdventOfficerCompleted"],
        difficulty = 15.0,
    ),
    "UseVenomRounds": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Venom Rounds",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["ammo", "proving_ground", "req:AutopsyViperCompleted"],
        difficulty = 20.0,
    ),
    "UseDragonRounds": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Dragon Rounds",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["ammo", "proving_ground", "req:AutopsyMutonEliteCompleted"],
        difficulty = 80.0,
    ),
    "UseStilettoRounds": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Stiletto Rounds",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["ammo", "proving_ground", "req:AutopsyAdventShieldbearerCompleted"],
        difficulty = 45.0,
    ),
    "UseFlechetteRounds": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Flechette Rounds",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["ammo", "proving_ground", "req:AutopsyChryssalidCompleted"],
        difficulty = 55.0,
    ),
    "UseRedScreenRounds": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Redscreen Rounds",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["ammo", "proving_ground", "req:AutopsyDroneCompleted"],
        difficulty = 45.0,
    ),
    "UseNeedleRounds": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Needle Rounds",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["ammo", "proving_ground", "req:AutopsyFacelessCompleted"],
        difficulty = 35.0,
    ),
    "UseFalconRounds": X2WOTCLocationData(
        display_name = item_use_location_prefix + "Shredder Rounds",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "ItemUse",
        tags = ["ammo", "proving_ground", "req:AutopsyAdventTurretCompleted"],
        difficulty = 35.0,
    ),
}

lwotc_enemy_kills: dict[str, X2WOTCLocationData] = {
    "KillAdvEngineer": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "ADVENT Engineer",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 5.0
    ),
    "KillAdvGunner": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "ADVENT Gunner",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 5.0
    ),
    "KillAdvSentry": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "ADVENT Sentry",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 5.0
    ),
    "KillAdvRocketeer": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "ADVENT Rocketeer",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 20.0
    ),
    "KillAdvScout": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "ADVENT Scout",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 25.0
    ),
    "KillAdvSergeant": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "ADVENT Sergeant",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 30.0
    ),
    "KillAdvGrenadier": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "ADVENT Grenadier",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 35.0
    ),
    "KillAdvGeneral_LW": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "ADVENT General",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 50.0
    ),
    "KillAdvShockTroop": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "ADVENT Shock Trooper",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 70.0
    ),
    "KillAdvVanguard": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "ADVENT Vanguard",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 70.0
    ),
    "KillLWDrone": X2WOTCLocationData(
        display_name = enemy_destroy_location_prefix + "Drone",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 5.0
    ),
    "KillMecArcher": X2WOTCLocationData(
        display_name = enemy_destroy_location_prefix + "MEC Archer",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 5.0
    ),
    "KillSidewinder": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Sidewinder",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 20.0
    ),
    "KillNaja": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Naja",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 25.0
    ),
    "KillMutonM2_LW": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Muton Centurion",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 45.0
    ),
    "KillMutonM3_LW": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Muton Elite",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 65.0
    ),
    "KillChryssalidSoldier": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Chryssalid Soldier",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 70.0
    ),
    "KillHiveQueen": X2WOTCLocationData(
        display_name = enemy_kill_location_prefix + "Hive Queen",
        id = get_new_location_id(),
        layer = "Tactical",
        type = "EnemyKill",
        tags = [],
        difficulty = 85.0
    ),
}

locations: dict[str, X2WOTCLocationData] = {
    **lwotc_techs,
    **lwotc_item_uses,
    **lwotc_enemy_kills
}
