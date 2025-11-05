from typing import TYPE_CHECKING

from BaseClasses import MultiWorld, Region

if TYPE_CHECKING:
    from worlds.x2wotc import X2WOTCWorld

from .Locations import X2WOTCLocation, LocationManager
from .Rules import RuleManager


class RegionManager:
    def __init__(self, world: "X2WOTCWorld"):
        self.region_table: dict[str, dict[str, int | None]] = {
            "Menu": {},
            "Avenger": {},
            "Research Lab": {},
            "Shadow Chamber": {},
            "Resistance Ring": {},
        }

        self.loc_manager: LocationManager = world.loc_manager
        self.rule_manager: RuleManager = world.rule_manager
        self.multiworld: MultiWorld = world.multiworld
        self.player: int = world.player

    def create_regions(self):
        # Add locations
        for loc_name, loc_data in self.loc_manager.location_table.items():
            if not self.loc_manager.enabled[loc_name]:
                continue

            region_name = "Avenger"

            if loc_data.type == "Tech":
                if "shadow" in loc_data.tags:
                    region_name = "Shadow Chamber"
                else:
                    region_name = "Research Lab"

            if loc_data.type == "CovertAction":
                region_name = "Resistance Ring"

            self.region_table[region_name][loc_data.display_name] = loc_data.id

        # Create regions
        for region_name in self.region_table.keys():
            self.multiworld.regions.append(self.create_region(region_name))

        # Connect regions
        self.multiworld.get_region("Menu", self.player).connect(
            self.multiworld.get_region("Avenger", self.player)
        )
        self.multiworld.get_region("Avenger", self.player).connect(
            self.multiworld.get_region("Research Lab", self.player)
        )
        self.multiworld.get_region("Avenger", self.player).connect(
            self.multiworld.get_region("Shadow Chamber", self.player),
            rule = lambda state: self.rule_manager.has_shadow_chamber(state)
        )
        self.multiworld.get_region("Avenger", self.player).connect(
            self.multiworld.get_region("Resistance Ring", self.player),
            rule = lambda state: self.rule_manager.has_resistance_ring(state)
        )

    def create_region(self, region_name: str) -> Region:
        region = Region(region_name, self.player, self.multiworld)
        region.add_locations(self.region_table[region_name], X2WOTCLocation)
        return region
