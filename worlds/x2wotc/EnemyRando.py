from random import Random
from typing import NamedTuple

from Options import OptionError

from .Options import EnemyPlando


class StatChange(NamedTuple):
    type: str
    delta: float
    min: float = 0.0
    max: float = 1000.0


class EnemyData(NamedTuple):
    bucket: int
    difficulty: float = 0.0
    base_enemies: list[str] = []
    stat_changes: dict[int, list[StatChange]] = {}


# Enemies are divided into buckets 0-5 by approximate defensive and offensive capabilities.
# Some examples of enemies, stat ranges (on commander difficulty) and notes for each bucket:
#   0: AdvTrooperM1
#     - First follower; 4 HP, 3 damage
#   1: Most ADVENT M1 units, Sectoid, Viper
#     - Early leaders; 7-8 HP, 3-5 damage
#   2: Most ADVENT M2 units, AdvMEC_M1, Muton, Chryssalid
#     - 8-12 HP, 0-2 armor, 5-7 damage, 3-5 damage AOE
#   3: Most ADVENT M3 units
#     - Stats vary widely, here are some examples:
#       - AdvStunLancerM3:    12 HP,  1 armor,  8-10  damage
#       - AdvShieldBearerM3:  11 HP,  3 armor,  6-7   damage
#       - AdvPriestM3:        18 HP,  0 armor,  5-6   damage
#   4: AdvMEC_M2, Berserker, Archon
#     - Considerably more tanky without sacrificing lethality:
#       - AdvMEC_M2:          15 HP,  3 armor,  8-9   damage
#       - Berserker:          24 HP,  0 armor,  5-8   damage
#       - Archon:             20 HP,  0 armor,  6-9   damage
#   5: Andromedon, Gatekeeper, Sectopod
#     - Late-game/boss units:
#       - Andromedon:         18 HP,  4 armor,  9-11  damage,  5-7 damage AOE
#         - Spawns 18 HP AndromedonRobot (bucket 4) on death
#       - Gatekeeper:         25 HP,  6 armor,  9-12  damage,  5-7 damage AOE
#       - Sectopod:           32 HP,  5 armor,  10-11 damage,  7-9 damage AOE
#
# When an enemy is shuffled into a foreign bucket, its stats are adjusted for balance. Most changes will focus on
# HP, armor, and defense, though other defensive stats (like dodge) and even offensive stats may also be adjusted.
# Difficulties for finding, killing, and performing autopsies on shuffled enemies are also derived from this table.
enemy_table: dict[str, EnemyData] = {

    #===============#
    #  A D V E N T  #
    #---------------#

    # ADVENT Troopers are pod filler and consistently behind other ADVENT units in power level.
    # Stat changes will primarily come in the form of HP buffs/nerfs;
    # secondarily weaker variants will focus on defense, stronger variants on armor.
    "AdvTrooperM1": EnemyData(
        bucket = 0,
        difficulty = 0.0,  # Gatecrasher
        stat_changes = {
            # Constant: 3 damage
            # Default: 4 HP
            1: [
                StatChange("eStat_HP", 6),  # 10 HP
            ],
            2: [
                StatChange("eStat_HP", 11),  # 15 HP
                StatChange("eStat_Defense", 10),  # 10 defense
                StatChange("eStat_CritChance", 0, 100),  # +1 crit
            ],
            3: [
                StatChange("eStat_HP", 18),  # 22 HP
                StatChange("eStat_Defense", 20),  # 20 defense
                StatChange("eStat_CritChance", 0, 100),  # +1 crit
            ],
            4: [
                StatChange("eStat_HP", 26),  # 30 HP
                StatChange("eStat_Defense", 40),  # 40 defense
                StatChange("eStat_CritChance", 0, 100),  # +1 crit
            ],
            5: [
                StatChange("eStat_HP", 36),  # 40 HP
                StatChange("eStat_Defense", 60),  # 60 defense
                StatChange("eStat_CritChance", 0, 100),  # +1 crit
            ],
        }
    ),
    "AdvTrooperM2": EnemyData(
        bucket = 1,
        difficulty = 29.0,  # FL 7
        stat_changes = {
            # Constant: 5 damage, 2-3 damage AOE
            # Default: 8 HP
            0: [
                StatChange("eStat_HP", -5, 1),  # 3 HP
            ],
            2: [
                StatChange("eStat_HP", 3),  # 11 HP
                StatChange("eStat_Defense", 10),  # 10 defense
            ],
            3: [
                StatChange("eStat_HP", 8),  # 16 HP
                StatChange("eStat_ArmorMitigation", 1),  # 1 armor
                StatChange("eStat_Defense", 10),  # 10 defense
            ],
            4: [
                StatChange("eStat_HP", 12),  # 20 HP
                StatChange("eStat_ArmorMitigation", 1),  # 1 armor
                StatChange("eStat_Defense", 20),  # 20 defense
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
            5: [
                StatChange("eStat_HP", 27),  # 35 HP
                StatChange("eStat_ArmorMitigation", 3),  # 3 armor
                StatChange("eStat_Defense", 30),  # 30 defense
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
        }
    ),
    "AdvTrooperM3": EnemyData(
        bucket = 2,
        difficulty = 53.0,  # FL 13
        stat_changes = {
            # Constant: 5-6 damage, 3-4 damage AOE
            # Default: 10 HP, 10 defense
            0: [
                StatChange("eStat_HP", -8, 1),  # 2 HP
                StatChange("eStat_Defense", -10),  # 0 defense
            ],
            1: [
                StatChange("eStat_HP", -3, 1),  # 7 HP
                StatChange("eStat_Defense", -10),  # 0 defense
            ],
            3: [
                StatChange("eStat_HP", 4),  # 14 HP
                StatChange("eStat_ArmorMitigation", 2),  # 2 armor
            ],
            4: [
                StatChange("eStat_HP", 8),  # 18 HP
                StatChange("eStat_ArmorMitigation", 2),  # 2 armor
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
            5: [
                StatChange("eStat_HP", 20),  # 30 HP
                StatChange("eStat_ArmorMitigation", 6),  # 6 armor
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
        }
    ),

    # ADVENT Stun Lancers are extremely reckless melee units whose offense far outpaces their defense.
    # Stat changes will primarily come in the form of HP buffs/nerfs;
    # secondarily weaker variants will focus on dodge, stronger variants on armor.
    "AdvStunLancerM1": EnemyData(
        bucket = 1,
        difficulty = 13.0,  # FL 3
        stat_changes = {
            # Constant: 2-4 damage
            # Default: 7 HP
            0: [
                StatChange("eStat_HP", -3, 1),  # 4 HP
            ],
            2: [
                StatChange("eStat_HP", 4),  # 11 HP
                StatChange("eStat_Dodge", 25),  # 25 dodge
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
            3: [
                StatChange("eStat_HP", 9),  # 16 HP
                StatChange("eStat_Dodge", 45),  # 45 dodge
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
            4: [
                StatChange("eStat_HP", 14),  # 21 HP
                StatChange("eStat_Dodge", 65),  # 65 dodge
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
            5: [
                StatChange("eStat_HP", 18),  # 25 HP
                StatChange("eStat_Dodge", 90),  # 90 dodge
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
        }
    ),
    "AdvStunLancerM2": EnemyData(
        bucket = 2,
        difficulty = 41.0,  # FL 10
        stat_changes = {
            # Constant: 5-7 damage
            # Default: 8 HP, 1 armor, 10 defense, 25 dodge
            0: [
                StatChange("eStat_HP", -5, 1),  # 3 HP
                StatChange("eStat_ArmorMitigation", -1),  # 0 armor
                StatChange("eStat_Defense", -10),  # 0 defense
                StatChange("eStat_Dodge", -25),  # 0 dodge
            ],
            1: [
                StatChange("eStat_HP", -3, 1),  # 6 HP
                StatChange("eStat_ArmorMitigation", -1),  # 0 armor
                StatChange("eStat_Defense", -10),  # 0 defense
                StatChange("eStat_Dodge", -10),  # 15 dodge
            ],
            3: [
                StatChange("eStat_HP", 5),  # 13 HP
                StatChange("eStat_Dodge", 10),  # 35 dodge
            ],
            4: [
                StatChange("eStat_HP", 10),  # 18 HP
                StatChange("eStat_ArmorMitigation", 1),  # 2 armor
                StatChange("eStat_Dodge", 10),  # 35 dodge
            ],
            5: [
                StatChange("eStat_HP", 17),  # 25 HP
                StatChange("eStat_ArmorMitigation", 2),  # 3 armor
                StatChange("eStat_Dodge", 20),  # 45 dodge
                StatChange("eStat_CritChance", 0, 100),  # +3 crit
            ],
        }
    ),
    "AdvStunLancerM3": EnemyData(
        bucket = 3,
        difficulty = 65.0,  # FL 16
        stat_changes = {
            # Constant: 8-10 damage
            # Default: 12 HP, 1 armor, 10 defense, 25 dodge
            0: [
                StatChange("eStat_HP", -10, 1),  # 2 HP
                StatChange("eStat_ArmorMitigation", -1),  # 0 armor
                StatChange("eStat_Defense", -10),  # 0 defense
                StatChange("eStat_Dodge", -25),  # 0 dodge
            ],
            1: [
                StatChange("eStat_HP", -8, 1),  # 4 HP
                StatChange("eStat_ArmorMitigation", -1),  # 0 armor
                StatChange("eStat_Defense", -10),  # 0 defense
                StatChange("eStat_Dodge", -15),  # 10 dodge
            ],
            2: [
                StatChange("eStat_HP", -6, 1),  # 6 HP
            ],
            4: [
                StatChange("eStat_HP", 4),  # 16 HP
                StatChange("eStat_ArmorMitigation", 1),  # 2 armor
            ],
            5: [
                StatChange("eStat_HP", 14),  # 28 HP
                StatChange("eStat_ArmorMitigation", 4),  # 5 armor
            ],
        }
    ),

    # ADVENT Shieldbearers are fairly tanky support units.
    # Stat changes will primarily come in the form of HP and armor buffs/nerfs.
    "AdvShieldBearerM2": EnemyData(
        bucket = 2,
        difficulty = 33.0,  # FL 8
        stat_changes = {
            # Constant: 5-6 damage
            # Default: 8 HP, 2 armor, 10 defense
            0: [
                StatChange("eStat_HP", -5, 1),  # 3 HP
                StatChange("eStat_ArmorMitigation", -2),  # 0 armor
                StatChange("eStat_Defense", -10),  # 0 defense
            ],
            1: [
                StatChange("eStat_HP", -3, 1),  # 5 HP
                StatChange("eStat_ArmorMitigation", -1),  # 1 armor
                StatChange("eStat_Defense", -10),  # 0 defense
            ],
            3: [
                StatChange("eStat_HP", 7),  # 15 HP
            ],
            4: [
                StatChange("eStat_HP", 9),  # 17 HP
                StatChange("eStat_ArmorMitigation", 1),  # 3 armor
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
            5: [
                StatChange("eStat_HP", 20),  # 28 HP
                StatChange("eStat_ArmorMitigation", 4),  # 6 armor
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
        }
    ),
    "AdvShieldBearerM3": EnemyData(
        bucket = 3,
        difficulty = 57.0,  # FL 14
        stat_changes = {
            # Constant: 6-7 damage
            # Default: 11 HP, 3 armor, 10 defense
            0: [
                StatChange("eStat_HP", -8, 1),  # 3 HP
                StatChange("eStat_ArmorMitigation", -3),  # 0 armor
                StatChange("eStat_Defense", -10),  # 0 defense
            ],
            1: [
                StatChange("eStat_HP", -7, 1),  # 4 HP
                StatChange("eStat_ArmorMitigation", -2),  # 1 armor
                StatChange("eStat_Defense", -10),  # 0 defense
            ],
            2: [
                StatChange("eStat_HP", -4, 1),  # 7 HP
                StatChange("eStat_ArmorMitigation", -1),  # 2 armor
            ],
            4: [
                StatChange("eStat_HP", 5),  # 16 HP
                StatChange("eStat_ArmorMitigation", 1),  # 4 armor
            ],
            5: [
                StatChange("eStat_HP", 14),  # 25 HP
                StatChange("eStat_ArmorMitigation", 4),  # 7 armor
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
        }
    ),

    # ADVENT MECs are heavily armored units with high damage output.
    # Stat changes will primarily come in the form of HP and armor buffs/nerfs.
    "AdvMEC_M1": EnemyData(
        bucket = 2,
        difficulty = 21.0,  # FL 5
        stat_changes = {
            # Constant: 4-6 damage, 3 damage AOE
            # Default: 8 HP, 2 armor
            0: [
                StatChange("eStat_HP", -5, 1),  # 3 HP
                StatChange("eStat_ArmorMitigation", -2),  # 0 armor
                StatChange("eStat_Defense", -10),  # 0 defense
            ],
            1: [
                StatChange("eStat_HP", -1, 1),  # 7 HP
                StatChange("eStat_ArmorMitigation", -2),  # 0 armor
                StatChange("eStat_Defense", -10),  # 0 defense
            ],
            3: [
                StatChange("eStat_HP", 5),  # 13 HP
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
            4: [
                StatChange("eStat_HP", 9),  # 17 HP
                StatChange("eStat_ArmorMitigation", 1),  # 3 armor
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
            5: [
                StatChange("eStat_HP", 20),  # 28 HP
                StatChange("eStat_ArmorMitigation", 4),  # 6 armor
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
        }
    ),
    "AdvMEC_M2": EnemyData(
        bucket = 4,
        difficulty = 49.0,  # FL 12
        stat_changes = {
            # Constant: 8-9 damage, 3-5 damage AOE
            # Default: 15 HP, 3 armor, 10 defense
            0: [
                StatChange("eStat_HP", -13, 1),  # 2 HP
                StatChange("eStat_ArmorMitigation", -3),  # 0 armor
                StatChange("eStat_Defense", -10),  # 0 defense
            ],
            1: [
                StatChange("eStat_HP", -11, 1),  # 4 HP
                StatChange("eStat_ArmorMitigation", -3),  # 0 armor
                StatChange("eStat_Defense", -10),  # 0 defense
            ],
            2: [
                StatChange("eStat_HP", -8, 1),  # 7 HP
                StatChange("eStat_ArmorMitigation", -2),  # 1 armor
            ],
            3: [
                StatChange("eStat_HP", -5, 1),  # 10 HP
                StatChange("eStat_ArmorMitigation", -1),  # 2 armor
            ],
            5: [
                StatChange("eStat_HP", 15),  # 30 HP
                StatChange("eStat_ArmorMitigation", 2),  # 5 armor
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
        }
    ),

    # ADVENT Purifiers do very little damage but can make the environment more hazardous and serve as soft CC.
    # Stat changes will primarily come in the form of HP and armor buffs/nerfs.
    # These enemies are way too weak, so they will be considerably buffed even within their own buckets.
    "AdvPurifierM1": EnemyData(
        bucket = 1,
        difficulty = 17.0,  # FL 4
        stat_changes = {
            # Constant: 2+ damage, 2 damage AOE
            # Default: 6 HP
            0: [
                StatChange("eStat_HP", -2, 1),  # 4 HP
            ],
            1: [
                StatChange("eStat_HP", 3),  # 9 HP
            ],
            2: [
                StatChange("eStat_HP", 9),  # 15 HP
            ],
            3: [
                StatChange("eStat_HP", 15),  # 21 HP
                StatChange("eStat_ArmorMitigation", 1),  # 1 armor
            ],
            4: [
                StatChange("eStat_HP", 20),  # 26 HP
                StatChange("eStat_ArmorMitigation", 2),  # 2 armor
            ],
            5: [
                StatChange("eStat_HP", 30),  # 36 HP
                StatChange("eStat_ArmorMitigation", 3),  # 3 armor
            ],
        }
    ),
    "AdvPurifierM2": EnemyData(
        bucket = 2,
        difficulty = 37.0,  # FL 9
        stat_changes = {
            # Constant: 2+ damage, 2 damage AOE
            # Default: 9 HP, 1 armor
            0: [
                StatChange("eStat_HP", -6, 1),  # 3 HP
            ],
            1: [
                StatChange("eStat_HP", -2, 1),  # 7 HP
            ],
            2: [
                StatChange("eStat_HP", 4),  # 13 HP
            ],
            3: [
                StatChange("eStat_HP", 9),  # 18 HP
                StatChange("eStat_ArmorMitigation", 1),  # 2 armor
            ],
            4: [
                StatChange("eStat_HP", 14),  # 23 HP
                StatChange("eStat_ArmorMitigation", 2),  # 3 armor
            ],
            5: [
                StatChange("eStat_HP", 24),  # 33 HP
                StatChange("eStat_ArmorMitigation", 3),  # 4 armor
            ],
        }
    ),
    "AdvPurifierM3": EnemyData(
        bucket = 3,
        difficulty = 61.0,  # FL 15
        stat_changes = {
            # Constant: 2+ damage, 5 damage AOE
            # Default: 12 HP, 2 armor
            0: [
                StatChange("eStat_HP", -9, 1),  # 3 HP
                StatChange("eStat_ArmorMitigation", -2),  # 0 armor
            ],
            1: [
                StatChange("eStat_HP", -6, 1),  # 6 HP
                StatChange("eStat_ArmorMitigation", -1),  # 1 armor
            ],
            2: [
                StatChange("eStat_HP", -2, 1),  # 10 HP
            ],
            3: [
                StatChange("eStat_HP", 2),  # 14 HP
                StatChange("eStat_ArmorMitigation", 1),  # 3 armor
            ],
            4: [
                StatChange("eStat_HP", 6),  # 18 HP
                StatChange("eStat_ArmorMitigation", 2),  # 4 armor
            ],
            5: [
                StatChange("eStat_HP", 16),  # 28 HP
                StatChange("eStat_ArmorMitigation", 3),  # 5 armor
            ],
        }
    ),

    # ADVENT Priests are essentially tankier Troopers with psionic abilities.
    # Stat changes will primarily come in the form of HP and armor buffs/nerfs.
    "AdvPriestM1": EnemyData(
        bucket = 1,
        difficulty = 13.0,  # FL 3
        stat_changes = {
            # Constant: 3 damage
            # Default: 8 HP
            0: [
                StatChange("eStat_HP", -4, 1),  # 4 HP
            ],
            2: [
                StatChange("eStat_HP", 4),  # 12 HP
                StatChange("eStat_ArmorMitigation", 1),  # 1 armor
                StatChange("eStat_CritChance", 0, 100),  # +1 crit
            ],
            3: [
                StatChange("eStat_HP", 8),  # 16 HP
                StatChange("eStat_ArmorMitigation", 2),  # 2 armor
                StatChange("eStat_CritChance", 0, 100),  # +1 crit
            ],
            4: [
                StatChange("eStat_HP", 17),  # 25 HP
                StatChange("eStat_ArmorMitigation", 2),  # 2 armor
                StatChange("eStat_CritChance", 0, 100),  # +1 crit
            ],
            5: [
                StatChange("eStat_HP", 27),  # 35 HP
                StatChange("eStat_ArmorMitigation", 6),  # 6 armor
                StatChange("eStat_CritChance", 0, 100),  # +1 crit
            ],
        }
    ),
    "AdvPriestM2": EnemyData(
        bucket = 2,
        difficulty = 33.0,  # FL 8
        stat_changes = {
            # Constant: 5 damage
            # Default: 12 HP
            0: [
                StatChange("eStat_HP", -9, 1),  # 3 HP
            ],
            1: [
                StatChange("eStat_HP", -5, 1),  # 7 HP
            ],
            3: [
                StatChange("eStat_HP", 4),  # 16 HP
                StatChange("eStat_ArmorMitigation", 1),  # 1 armor
            ],
            4: [
                StatChange("eStat_HP", 10),  # 22 HP
                StatChange("eStat_ArmorMitigation", 1),  # 1 armor
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
            5: [
                StatChange("eStat_HP", 21),  # 33 HP
                StatChange("eStat_ArmorMitigation", 4),  # 4 armor
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
        }
    ),
    "AdvPriestM3": EnemyData(
        bucket = 3,
        difficulty = 57.0,  # FL 14
        stat_changes = {
            # Constant: 5-6 damage, 20 dodge
            # Default: 18 HP, 15 defense
            0: [
                StatChange("eStat_HP", -16, 1),  # 2 HP
                StatChange("eStat_Defense", -15),  # 0 defense
            ],
            1: [
                StatChange("eStat_HP", -12, 1),  # 6 HP
                StatChange("eStat_Defense", -15),  # 0 defense
            ],
            2: [
                StatChange("eStat_HP", -6, 1),  # 12 HP
            ],
            4: [
                StatChange("eStat_HP", 5),  # 23 HP
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
            5: [
                StatChange("eStat_HP", 17),  # 35 HP
                StatChange("eStat_ArmorMitigation", 3),  # 3 armor
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
        }
    ),

    #===============#
    #  A L I E N S  #
    #---------------#

    "Sectoid": EnemyData(
        bucket = 1,
        difficulty = 5.0,  # FL 1
        stat_changes = {
            # Constant: 3-4 damage
            # Default: 8 HP
            0: [
                StatChange("eStat_HP", -4, 1),  # 4 HP
            ],
            2: [
                StatChange("eStat_HP", 4),  # 12 HP
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
            3: [
                StatChange("eStat_HP", 10),  # 18 HP
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
            4: [
                StatChange("eStat_HP", 18),  # 26 HP
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
            5: [
                StatChange("eStat_HP", 37),  # 45 HP
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
        }
    ),
    "Viper": EnemyData(
        bucket = 1,
        difficulty = 17.0,  # FL 4
        stat_changes = {
            # Constant: 3-5 damage
            # Default: 8 HP, 33 dodge
            0: [
                StatChange("eStat_HP", -5, 1),  # 3 HP
            ],
            2: [
                StatChange("eStat_HP", 3),  # 11 HP
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
            3: [
                StatChange("eStat_HP", 7),  # 15 HP
                StatChange("eStat_Dodge", 17),  # 50 dodge
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
            4: [
                StatChange("eStat_HP", 12),  # 20 HP
                StatChange("eStat_Dodge", 33),  # 66 dodge
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
            5: [
                StatChange("eStat_HP", 17),  # 25 HP
                StatChange("eStat_Dodge", 57),  # 90 dodge
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
        }
    ),
    "Muton": EnemyData(
        bucket = 2,
        difficulty = 25.0,  # FL 6
        stat_changes = {
            # Constant: 4-6 damage, 4-5 damage AOE
            # Default: 9 HP, 2 armor, 10 defense
            0: [
                StatChange("eStat_HP", -7, 1),  # 2 HP
                StatChange("eStat_ArmorMitigation", -2),  # 0 armor
                StatChange("eStat_Defense", -10),  # 0 defense
            ],
            1: [
                StatChange("eStat_HP", -4, 1),  # 5 HP
                StatChange("eStat_ArmorMitigation", -1),  # 1 armor
                StatChange("eStat_Defense", -10),  # 0 defense
            ],
            3: [
                StatChange("eStat_HP", 1),  # 10 HP
                StatChange("eStat_ArmorMitigation", 1),  # 3 armor
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
            4: [
                StatChange("eStat_HP", 7),  # 16 HP
                StatChange("eStat_ArmorMitigation", 2),  # 4 armor
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
            5: [
                StatChange("eStat_HP", 19),  # 28 HP
                StatChange("eStat_ArmorMitigation", 4),  # 6 armor
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
        }
    ),
    "Faceless": EnemyData(
        bucket = 1,
        difficulty = 10.0,  # FacelessCivilian on terror mission
        stat_changes = {
            # Constant: 3-4 damage
            # Default: 10 HP
            0: [
                StatChange("eStat_HP", -6, 1),  # 4 HP
            ],
            2: [
                StatChange("eStat_HP", 4),  # 14 HP
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
            3: [
                StatChange("eStat_HP", 10),  # 20 HP
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
            4: [
                StatChange("eStat_HP", 18),  # 28 HP
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
            5: [
                StatChange("eStat_HP", 37),  # 47 HP
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
        }
    ),
    "Berserker": EnemyData(
        bucket = 4,
        difficulty = 29.0,  # FL 7
        stat_changes = {
            # Constant: 5-8 damage
            # Default: 24 HP
            0: [
                StatChange("eStat_HP", -22, 1),  # 2 HP
            ],
            1: [
                StatChange("eStat_HP", -19, 1),  # 5 HP
            ],
            2: [
                StatChange("eStat_HP", -12, 1),  # 12 HP
            ],
            3: [
                StatChange("eStat_HP", -6, 1),  # 18 HP
            ],
            5: [
                StatChange("eStat_HP", 12),  # 36 HP
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
        }
    ),
    "Archon": EnemyData(
        bucket = 4,
        difficulty = 45.0,  # FL 11
        stat_changes = {
            # Constant: 6-9 damage
            # Default: 20 HP, 25 defense, 25 dodge
            0: [
                StatChange("eStat_HP", -18, 1),  # 2 HP
                StatChange("eStat_Defense", -25),  # 0 defense
            ],
            1: [
                StatChange("eStat_HP", -15, 1),  # 5 HP
                StatChange("eStat_Defense", -25),  # 0 defense
            ],
            2: [
                StatChange("eStat_HP", -12, 1),  # 8 HP
                StatChange("eStat_Defense", -15),  # 10 defense
            ],
            3: [
                StatChange("eStat_HP", -7, 1),  # 13 HP
            ],
            5: [
                StatChange("eStat_HP", 5),  # 25 HP
                StatChange("eStat_ArmorMitigation", 3),  # 3 armor
                StatChange("eStat_Dodge", 25),  # 50 dodge
                StatChange("eStat_CritChance", 0, 100),  # +3 crit
            ],
        }
    ),
    "Chryssalid": EnemyData(
        bucket = 2,
        difficulty = 49.0,  # FL 12
        stat_changes = {
            # Constant: 5-6 damage, 1-3 damage poison, 20 dodge
            # Default: 10 HP, 1 armor, 10 defense
            0: [
                StatChange("eStat_HP", -8, 1),  # 2 HP
                StatChange("eStat_ArmorMitigation", -1),  # 0 armor
                StatChange("eStat_Defense", -10),  # 0 defense
            ],
            1: [
                StatChange("eStat_HP", -6, 1),  # 4 HP
                StatChange("eStat_Defense", -10),  # 0 defense
            ],
            3: [
                StatChange("eStat_HP", 4),  # 14 HP
                StatChange("eStat_ArmorMitigation", 1),  # 2 armor
            ],
            4: [
                StatChange("eStat_HP", 9),  # 19 HP
                StatChange("eStat_ArmorMitigation", 1),  # 2 armor
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
            5: [
                StatChange("eStat_HP", 19),  # 29 HP
                StatChange("eStat_ArmorMitigation", 2),  # 5 armor
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
        }
    ),
    "Andromedon": EnemyData(
        bucket = 5,
        difficulty = 57.0,  # FL 14
        stat_changes = {
            # Constant: 9-11 damage, 5-7 damage AOE, spawns AndromedonRobot on death
            # Default: 18 HP, 4 armor, 10 defense
            0: [
                StatChange("eStat_HP", -17, 1),  # 1 HP
                StatChange("eStat_ArmorMitigation", -4),  # 0 armor
                StatChange("eStat_Defense", -10),  # 0 defense
            ],
            1: [
                StatChange("eStat_HP", -14, 1),  # 3 HP
                StatChange("eStat_ArmorMitigation", -4),  # 0 armor
                StatChange("eStat_Defense", -10),  # 0 defense
            ],
            2: [
                StatChange("eStat_HP", -13, 1),  # 5 HP
                StatChange("eStat_ArmorMitigation", -4),  # 0 armor
            ],
            3: [
                StatChange("eStat_HP", -10, 1),  # 8 HP
                StatChange("eStat_ArmorMitigation", -3),  # 1 armor
            ],
            4: [
                StatChange("eStat_HP", -6, 1),  # 12 HP
                StatChange("eStat_ArmorMitigation", -2),  # 2 armor
            ],
        }
    ),
    "AndromedonRobot": EnemyData(
        bucket = 4,
        base_enemies = ["Andromedon"],  # Spawns from Andromedon
        stat_changes = {
            # Constant: 7-10 damage
            # Default: 18 HP
            0: [
                StatChange("eStat_HP", -16, 1),  # 2 HP
            ],
            1: [
                StatChange("eStat_HP", -13, 1),  # 5 HP
            ],
            2: [
                StatChange("eStat_HP", -10, 1),  # 8 HP
            ],
            3: [
                StatChange("eStat_HP", -5, 1),  # 13 HP
            ],
            5: [
                StatChange("eStat_HP", 12),  # 30 HP
                StatChange("eStat_ArmorMitigation", 4),  # 4 armor
            ],
        }
    ),
    "Sectopod": EnemyData(
        bucket = 5,
        difficulty = 65.0,  # FL 16
        stat_changes = {
            # Constant: 10-11 damage, 7-9 damage AOE
            # Default: 32 HP, 5 armor
            0: [
                StatChange("eStat_HP", -31, 1, 1),  # 1 HP
            ],
            1: [
                StatChange("eStat_HP", -29, 1, 5),  # 3 HP
                StatChange("eStat_ArmorMitigation", -5),  # 0 armor
            ],
            2: [
                StatChange("eStat_HP", -26, 1),  # 6 HP
                StatChange("eStat_ArmorMitigation", -5),  # 0 armor
            ],
            3: [
                StatChange("eStat_HP", -22, 1),  # 10 HP
                StatChange("eStat_ArmorMitigation", -3),  # 2 armor
            ],
            4: [
                StatChange("eStat_HP", -17, 1),  # 15 HP
                StatChange("eStat_ArmorMitigation", -2),  # 3 armor
            ],
        }
    ),
    "Gatekeeper": EnemyData(
        bucket = 5,
        difficulty = 73.0,  # FL 18
        stat_changes = {
            # Constant: 9-12 damage, 5-7 damage AOE, +25 defense and +3 armor closed
            # Default: 25 HP, 3 armor, 15 defense
            0: [
                StatChange("eStat_HP", -24, 1, 1),  # 1 HP
                StatChange("eStat_Defense", -15),  # 0 defense
            ],
            1: [
                StatChange("eStat_HP", -23, 1, 3),  # 2 HP
                StatChange("eStat_ArmorMitigation", -3),  # 0 armor
                StatChange("eStat_Defense", -15),  # 0 defense
            ],
            2: [
                StatChange("eStat_HP", -21, 1),  # 4 HP
                StatChange("eStat_ArmorMitigation", -3),  # 0 armor
                StatChange("eStat_Defense", -15),  # 0 defense
            ],
            3: [
                StatChange("eStat_HP", -16, 1),  # 9 HP
                StatChange("eStat_ArmorMitigation", -3),  # 0 armor
            ],
            4: [
                StatChange("eStat_HP", -12, 1),  # 13 HP
                StatChange("eStat_ArmorMitigation", -2),  # 1 armor
            ],
        }
    ),
    "SpectreM1": EnemyData(
        bucket = 2,
        difficulty = 33.0,  # FL 8
        stat_changes = {
            # Constant: 4-5 damage
            # Default: 14 HP, 20 dodge
            0: [
                StatChange("eStat_HP", -11, 1),  # 3 HP
                StatChange("eStat_Dodge", -20),  # 0 dodge
            ],
            1: [
                StatChange("eStat_HP", -7, 1),  # 7 HP
                StatChange("eStat_Dodge", -10),  # 10 dodge
            ],
            3: [
                StatChange("eStat_Dodge", 10),  # 30 dodge
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
            4: [
                StatChange("eStat_HP", 4),  # 18 HP
                StatChange("eStat_Dodge", 25),  # 45 dodge
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
            5: [
                StatChange("eStat_HP", 13),  # 27 HP
                StatChange("eStat_Dodge", 45),  # 65 dodge
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
        }
    ),
    "SpectreM2": EnemyData(
        bucket = 4,
        difficulty = 61.0,  # FL 15
        stat_changes = {
            # Constant: 6-7 damage
            # Default: 22 HP, 25 dodge
            0: [
                StatChange("eStat_HP", -19, 1),  # 3 HP
                StatChange("eStat_Dodge", -25),  # 0 dodge
            ],
            1: [
                StatChange("eStat_HP", -16, 1),  # 6 HP
                StatChange("eStat_Dodge", -10),  # 15 dodge
            ],
            2: [
                StatChange("eStat_HP", -10, 1),  # 12 HP
            ],
            3: [
                StatChange("eStat_HP", -7, 1),  # 15 HP
            ],
            5: [
                StatChange("eStat_HP", 8),  # 30 HP
                StatChange("eStat_ArmorMitigation", 5),  # 5 armor
                StatChange("eStat_CritChance", 0, 100),  # +2 crit
            ],
        }
    ),
}

enemy_names: list[str] = sorted(enemy_table.keys())


class EnemyRandoManager:
    enemy_table = enemy_table
    enemy_names = enemy_names

    def __init__(self):
        self.enemy_shuffle: list[int] = list(range(len(self.enemy_names)))
        self.is_shuffled: bool = False

        # If this triggers, something is wrong with the above data table
        if self.has_base_enemies_loop():
            raise Exception("EnemyRando: base_enemies loop detected in unshuffled enemy table")

    def shuffle_enemies(self, enemy_plando: EnemyPlando, random: Random):
        if self.is_shuffled:
            return
        self.is_shuffled = True

        shuffle_groups = self.interpret_enemy_plando(enemy_plando)
        for _ in range(100):

            # Shuffle enemies within each group
            for group in shuffle_groups:
                placement_indices = list(group[0])
                placed_indices = list(group[1])
                random.shuffle(placed_indices)
                for placement_index, placed_index in zip(placement_indices, placed_indices):
                    self.enemy_shuffle[placement_index] = placed_index

            # As long as the shuffle is invalid, simply shuffle again
            if not self.has_base_enemies_loop():
                break

        # Failure is virtually always due to impossible enemy plando
        else:
            raise OptionError(
                "X2WOTC: Unable to create enemy shuffle without base_enemies loop. "
                "Check your Enemy Plando for impossible constraints."
            )

    def set_enemy_shuffle(self, enemy_shuffle: list[int]):
        self.enemy_shuffle = enemy_shuffle
        self.is_shuffled = True

    # Translate EnemyPlando into shuffle groups of placement and placed enemy indices
    def interpret_enemy_plando(self, enemy_plando: EnemyPlando) -> set[tuple[frozenset[int], frozenset[int]]]:
        shuffle_groups = set()
        used_placement_indices: set[int] = set()
        used_placed_indices: set[int] = set()

        # Evaluate fixed placements
        filter: str
        for filter in enemy_plando["fixed"]:
            for enemy_index, enemy_name in enumerate(self.enemy_names):
                if self.evaluate_enemy_filter(filter, enemy_name):
                    shuffle_groups.add((frozenset({enemy_index}), frozenset({enemy_index})))
                    used_placement_indices.add(enemy_index)
                    used_placed_indices.add(enemy_index)

        # Evaluate forced groups
        group: list[list[str]]  # len(group) == 2
        for group_index, group in enumerate(enemy_plando["forced"]):

            # Collect placement enemies
            placement_indices: set[int] = set()
            for filter in group[0]:
                for enemy_index, enemy_name in enumerate(self.enemy_names):
                    if self.evaluate_enemy_filter(filter, enemy_name):
                        placement_indices.add(enemy_index)

            # Collect placed enemies
            placed_indices: set[int] = set()
            for filter in group[1]:
                for enemy_index, enemy_name in enumerate(self.enemy_names):
                    if self.evaluate_enemy_filter(filter, enemy_name):
                        placed_indices.add(enemy_index)

            # Validate group
            if len(placement_indices) != len(placed_indices):
                raise OptionError(
                    f"X2WOTC: Mismatched enemy counts in Enemy Plando forced group {group_index}: "
                    f"cannot place {len(placed_indices)} enemies into {len(placement_indices)} slots."
                )
            if used_placement_indices & placement_indices or used_placed_indices & placed_indices:
                raise OptionError(
                    "X2WOTC: Conflict in Enemy Plando forced groups or fixed placements. "
                    "Make sure no enemy matches multiple placement or placed filters."
                )

            shuffle_groups.add((frozenset(placement_indices), frozenset(placed_indices)))
            used_placement_indices.update(placement_indices)
            used_placed_indices.update(placed_indices)

        # Place remaining enemies into one group
        shuffle_groups.add((
            frozenset(set(range(len(self.enemy_names))) - used_placement_indices),
            frozenset(set(range(len(self.enemy_names))) - used_placed_indices),
        ))

        return shuffle_groups

    # Check for exact match or fall back to substring match
    def evaluate_enemy_filter(self, filter: str, enemy_name: str) -> bool:
        if filter in self.enemy_names:
            return filter == enemy_name
        return filter in enemy_name

    # Check for loops in base enemy dependencies due to the shuffle
    def has_base_enemies_loop(self) -> bool:
        for index, name in enumerate(self.enemy_names):

            # DFS to accumulate dependencies
            visited = set()
            stack = self.enemy_table[name].base_enemies.copy()
            while stack:
                current = stack.pop()
                if current not in visited:
                    visited.add(current)
                    stack.extend(self.enemy_table[current].base_enemies)

            # Placement enemy may not depend on placed enemy
            if self.enemy_names[self.enemy_shuffle[index]] in visited:
                return True

        return False

    # Determine placement enemy for a placed enemy from the enemy shuffle
    def get_placement_enemy(self, placed_enemy: str) -> str:
        placed_index = self.enemy_names.index(placed_enemy)
        placement_index = self.enemy_shuffle.index(placed_index)
        placement_enemy = self.enemy_names[placement_index]
        return placement_enemy

    # Determine difficulty of a placed enemy from the (relative and base) difficulty of its placement
    def get_difficulty(self, placed_enemy: str | list[str]) -> float:
        if isinstance(placed_enemy, list):
            return min([self.get_difficulty(enemy) for enemy in placed_enemy], default=0.0)
        placement_enemy = self.get_placement_enemy(placed_enemy)
        placement_base_difficulty = self.get_difficulty(self.enemy_table[placement_enemy].base_enemies)
        placement_relative_difficulty = self.enemy_table[placement_enemy].difficulty
        return placement_base_difficulty + placement_relative_difficulty

    # Determine relative bucket of an enemy from the default buckets of it and its dependencies
    def get_relative_bucket(self, enemy: str) -> int:
        default_bucket = self.enemy_table[enemy].bucket
        default_base_buckets = [self.enemy_table[base_enemy].bucket for base_enemy in self.enemy_table[enemy].base_enemies]
        return default_bucket - min(default_base_buckets, default=0)

    # Determine bucket of a placed enemy from the (relative and base) bucket of its placement
    def get_bucket(self, placed_enemy: str | list[str]) -> int:
        if isinstance(placed_enemy, list):
            return min([self.get_bucket(enemy) for enemy in placed_enemy], default=0)
        placement_enemy = self.get_placement_enemy(placed_enemy)
        placement_base_bucket = self.get_bucket(self.enemy_table[placement_enemy].base_enemies)
        placement_relative_bucket = self.get_relative_bucket(placement_enemy)
        return max(placement_base_bucket + placement_relative_bucket, 0)

    # Determine stat changes for a placed enemy from its placement bucket
    def get_stat_changes(self, placed_enemy: str) -> list[StatChange]:
        placement_bucket = self.get_bucket(placed_enemy)
        return self.enemy_table[placed_enemy].stat_changes.get(placement_bucket, [])
