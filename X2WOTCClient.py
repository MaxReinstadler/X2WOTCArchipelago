import asyncio
from CommonClient import CommonContext, ClientCommandProcessor
from CommonClient import server_loop, get_base_parser
from CommonClient import gui_enabled
from worlds.x2wotc.Proxy import run_proxy
from typing import Optional

class X2WOTCCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: CommonContext):
        super().__init__(ctx)

class X2WOTCContext(CommonContext):
    command_processor = X2WOTCCommandProcessor
    game = "XCOM 2 War of the Chosen"
    items_handling = 0b111  # full remote

    proxy_task: Optional[asyncio.Task] = None
    connected = asyncio.Event()

    def __init__(self, server_address: Optional[str], password: Optional[str]):
        super(X2WOTCContext, self).__init__(server_address, password)

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(X2WOTCContext, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def on_package(self, cmd: str, args: dict):
        if cmd == "Connected":
            self.connected.set()

    def run_gui(self):
        from kvui import GameManager

        class X2WOTCGameManager(GameManager):
            logging_pairs = [("Client", "Archipelago")]
            base_title = "Archipelago XCOM 2 War of the Chosen Client"

        self.ui = X2WOTCGameManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="ui")

if __name__ == "__main__":
    async def main(args):
        ctx = X2WOTCContext(args.connect, args.password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server_loop")
        ctx.proxy_task = asyncio.create_task(run_proxy(ctx), name="proxy")

        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        await ctx.exit_event.wait()
        await ctx.shutdown()

    import colorama

    parser = get_base_parser()
    args = parser.parse_args()

    colorama.init()
    asyncio.run(main(args))
    colorama.deinit()
