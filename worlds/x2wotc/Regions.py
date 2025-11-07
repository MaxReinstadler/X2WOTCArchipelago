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

            # Default to Avenger
            region_name = "Avenger"

            # For tech locations, check tree tags for location dependencies...
            if loc_data.type == "Tech":
                tree_tag_techs = [
                    tag[5:]
                    for tag in loc_data.tags
                    if tag.startswith("tree:")
                ]
                tree_display_names = [
                    self.loc_manager.location_table[tech].display_name
                    for tech in tree_tag_techs
                ]
                region_name = " & ".join(sorted(tree_display_names))

                # ...then fall back to Research Lab (or Shadow Chamber for shadow projects)
                if region_name == "":
                    if "shadow" in loc_data.tags:
                        region_name = "Shadow Chamber"
                    else:
                        region_name = "Research Lab"

            # For covert action locations, assign to Resistance Ring
            elif loc_data.type == "CovertAction":
                region_name = "Resistance Ring"

            if region_name not in self.region_table:
                self.region_table[region_name] = {}
            self.region_table[region_name][loc_data.display_name] = loc_data.id

        # Create regions
        for region_name in self.region_table.keys():
            self.multiworld.regions.append(self.create_region(region_name))

        # Connect regions
        for region_name in self.region_table.keys():
            region = self.multiworld.get_region(region_name, self.player)
            origin_region = self.multiworld.get_region("Menu", self.player)
            access_rule = None
            indirect_region_names = []

            if region_name == "Menu":
                continue

            elif region_name == "Avenger":
                pass

            elif region_name == "Research Lab":
                origin_region = self.multiworld.get_region("Avenger", self.player)

            elif region_name == "Shadow Chamber":
                origin_region = self.multiworld.get_region("Avenger", self.player)
                access_rule = lambda state: self.rule_manager.has_shadow_chamber(state)

            elif region_name == "Resistance Ring":
                origin_region = self.multiworld.get_region("Avenger", self.player)
                access_rule = lambda state: self.rule_manager.has_resistance_ring(state)

            # Connect tag-created research regions
            else:
                loc_display_names = region_name.split(" & ")
                loc_keys = [
                    self.loc_manager.loc_display_name_to_key[display_name]
                    for display_name in loc_display_names
                ]

                origin_region = (
                    self.multiworld.get_region("Shadow Chamber", self.player)
                    if "shadow" in self.loc_manager.location_table[loc_keys[0]].tags
                    else self.multiworld.get_region("Research Lab", self.player)
                )

                access_rule = self.rule_manager.get_reachability_rule(loc_keys)

                # Collect indirect conditions
                for display_name in loc_display_names:
                    for indirect_region_name, locations in self.region_table.items():
                        if display_name in locations:
                            indirect_region_names.append(indirect_region_name)
                            break

            entrance = origin_region.connect(region, rule=access_rule)

            # Register indirect conditions
            for indirect_region_name in indirect_region_names:
                indirect_region = self.multiworld.get_region(indirect_region_name, self.player)
                self.multiworld.register_indirect_condition(indirect_region, entrance)

    def create_region(self, region_name: str) -> Region:
        region = Region(region_name, self.player, self.multiworld)
        region.add_locations(self.region_table[region_name], X2WOTCLocation)
        return region
