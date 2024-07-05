from aiohttp import web
from typing import Optional, List, Dict, Tuple
from CommonClient import CommonContext, NetworkItem, NetworkSlot, logger
from NetUtils import ClientStatus

# Note: item and location tables include disabled item/location pairs
from .Items import item_table, item_id_to_key
from .Locations import location_table, loc_id_to_key

ctx: CommonContext

LocationsInfo = Dict[
    str,  # Location name (key)
    Tuple[
        str,  # Item name (key)
        Optional[NetworkItem],
        Optional[NetworkSlot]
    ]
]

ItemsInfo = Dict[
    str,  # Item name (key)
    Tuple[
        NetworkItem,
        Optional[NetworkSlot]
    ]
]

#======================================================================================================================#
#                                                  HELPER FUNCTIONS                                                    #
#----------------------------------------------------------------------------------------------------------------------#

def get_slot_info(slot: int) -> Optional[NetworkSlot]:
    try:
        return ctx.slot_info[slot]
    except KeyError:
        logger.debug(f"Proxy: No slot {slot}")
        return None

# ----------------------------------------------------- SCOUT -------------------------------------------------------- #

async def scout_locations():
    await ctx.connected.wait()

    for loc_id in ctx.server_locations:  # If the server knows the location
        if loc_id in loc_id_to_key.keys():  # If it's ours
            ctx.locations_scouted.add(loc_id)  # Scout it

    if ctx.locations_scouted:
        await ctx.send_msgs([{
            "cmd": "LocationScouts",
            "locations": list(ctx.locations_scouted)
        }])

    logger.debug("Proxy: Locations scouted")

def get_locations_info(checks: List[str]) -> LocationsInfo:
    locations_info = {}
    for loc_name in checks:

        try:
            loc_data = location_table[loc_name]
            loc_id = loc_data.id
        except KeyError:
            logger.warn(f"Proxy: Location {loc_name} not found")
            continue

        if loc_id not in ctx.locations_scouted:
            logger.debug(f"Proxy: Location {loc_name} not scouted, will be treated as disabled")
            item_name = loc_data.normal_item
            locations_info[loc_name] = (item_name, None, None)
            continue
        
        network_item = ctx.locations_info[loc_id]
        item_name = item_id_to_key[network_item.item]
        slot_info = get_slot_info(network_item.player)
        locations_info[loc_name] = (item_name, network_item, slot_info)

    return locations_info

# ----------------------------------------------------- CHECK -------------------------------------------------------- #

async def send_checks(checks: List[str]):
    for loc_name in checks:

        if loc_name == "Victory":
            await ctx.send_msgs([{
                "cmd": "StatusUpdate",
                "status": ClientStatus.CLIENT_GOAL
            }])
            continue

        try:
            loc_id = location_table[loc_name].id
        except KeyError:
            logger.warn(f"Proxy: Location {loc_name} not found")
            continue

        if loc_id == None:
            logger.warn(f"Proxy: Location {loc_name} is event, can't be checked")
            continue
        
        if loc_id not in ctx.server_locations:
            logger.debug(f"Proxy: Location {loc_name} is disabled")
            continue

        ctx.locations_checked.add(loc_id)

    if ctx.locations_checked:
        await ctx.send_msgs([{
            "cmd": "LocationChecks",
            "locations": list(ctx.locations_checked)
        }])

    logger.debug("Proxy: Location checks sent")

# ---------------------------------------------------- RECEIVE ------------------------------------------------------- #

def get_received_items() -> ItemsInfo:
    items_info = {}
    for item in ctx.items_received:
        item_name = item_id_to_key[item.item]
        slot_info = get_slot_info(item.player)
        items_info[item_name] = (item, slot_info)
    return items_info

#======================================================================================================================#
#                                                  REQUEST HANDLERS                                                    #
#----------------------------------------------------------------------------------------------------------------------#

# ----------------------------------------------------- CHECK -------------------------------------------------------- #

async def handle_check(request: web.Request):
    checks = [check for check in request.match_info["tail"].split("/") if check != ""]
    await send_checks(checks)
    
    response_body = ""
    for loc_name, (item_name, item, slot_info) in get_locations_info(checks).items():
        item_data = item_table[item_name]
        
        if response_body != "":
            response_body += "\n\n"

        if item == None:
            logger.debug(f"Proxy: No item at location {loc_name}, will be treated as disabled")
            response_body += f"[{item_data.type}]{item_name}\n"
            response_body += f"Regular Item Found\n"
            response_body += f"Found your {item_data.display_name}!"
        elif item.player == ctx.slot:
            response_body += "None\n"
            response_body += "None"
        elif slot_info:
            response_body += "Archipelago Item Sent\n"
            response_body += f"Sent {item_data.display_name} to {slot_info.name} ({slot_info.game})!"
        else:
            response_body += "Archipelago Item Sent\n"
            response_body += f"Sent {item_data.display_name} to no one..."

    return web.Response(text=response_body)

# ----------------------------------------------------- TICK --------------------------------------------------------- #

def handle_tick(layer: str) -> str:
    response_body = ""

    for item_name, (item, slot_info) in get_received_items().items():
        item_data = item_table[item_name]

        if item_data.layer == layer:
            if response_body != "":
                response_body += "\n\n"

            # Info for the game to process
            response_body += f"[{item_data.type}]{item_name}\n"

            if item.player == ctx.slot:
                response_body += "Archipelago Item Found\n"
                response_body += f"Found your {item_data.display_name}!"
            elif slot_info:
                response_body += "Archipelago Item Received\n"
                response_body += f"Received {item_data.display_name} from {slot_info.name} ({slot_info.game})!"
            else:
                response_body += "Archipelago Item Received\n"
                response_body += f"Received {item_data.display_name} from the server."

    return response_body

async def handle_tick_strategy(request: web.Request):
    response_body = handle_tick("Strategy")
    return web.Response(text=response_body)

async def handle_tick_tactical(request: web.Request):
    response_body = handle_tick("Tactical")
    return web.Response(text=response_body)

#======================================================================================================================#
#                                                     RUN PROXY                                                        #
#----------------------------------------------------------------------------------------------------------------------#

async def run_proxy(local_ctx: CommonContext):
    global ctx
    ctx = local_ctx

    address = ("localhost", ctx.proxy_port)
    
    app = web.Application()
    app.router.add_get("/Tick/Strategy", handle_tick_strategy)
    app.router.add_get("/Tick/Tactical", handle_tick_tactical)
    app.router.add_get("/Check/{tail:.*}", handle_check)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, address[0], address[1])
    await site.start()

    logger.info(f"Proxy: Server started at {address[0]}:{address[1]}")

    await scout_locations()

    try:
        await ctx.exit_event.wait()
    finally:
        await runner.cleanup()
        logger.info("Proxy: Server stopped")
