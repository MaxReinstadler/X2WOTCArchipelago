import asyncio

from CommonClient import (
    ClientCommandProcessor,
    server_loop,
    get_base_parser,
    gui_enabled,
    logger
)
try:
    from worlds.tracker.TrackerClient import TrackerGameContext as SuperContext  # type: ignore
except ModuleNotFoundError:
    from CommonClient import CommonContext as SuperContext

from .Proxy import run_proxy
from .Version import client_version, recommended_mod_version


class X2WOTCCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: SuperContext):
        super().__init__(ctx)

    def _cmd_proxy(self, port: str = "") -> bool:
        """Start the proxy server with a specific port number."""
        if port == "":
            self.output(f"Current proxy port: {self.ctx.proxy_port}")
            return False

        try:
            port = int(port)
        except ValueError:
            self.output("Invalid port number (not an integer).")
            return False

        if port < 0 or port > 65535:
            self.output("Port number out of range (0 to 65535).")
            return False

        self.ctx.proxy_port = port
        self.ctx.start_proxy()
        return True

    def _cmd_version(self) -> bool:
        """Print the version of the client."""
        self.output(f"Client version: {client_version}\nRecommended mod version: {recommended_mod_version}")
        return True


class X2WOTCContext(SuperContext):
    command_processor = X2WOTCCommandProcessor
    game = "XCOM 2 War of the Chosen"
    items_handling = 0b111  # full remote
    tags = {"AP"}

    class DualEvent:
        def __init__(self):
            self._set_event = asyncio.Event()
            self._clear_event = asyncio.Event()
            self._clear_event.set()

        def set(self):
            self._set_event.set()
            self._clear_event.clear()

        def clear(self):
            self._set_event.clear()
            self._clear_event.set()

        def is_set(self):
            return self._set_event.is_set()

        def wait(self):
            return self._set_event.wait()

        def wait_clear(self):
            return self._clear_event.wait()

    connected = DualEvent()
    scouted = DualEvent()

    goal_location: str = ""

    proxy_port = 24728
    proxy_task: asyncio.Task | None = None

    def __init__(self, server_address: str | None, password: str | None):
        super().__init__(server_address, password)
        self.locations_checked = set()
        self.locations_scouted = set()

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super().server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    async def disconnect(self, allow_autoreconnect: bool = False):
        await super().disconnect(allow_autoreconnect)
        self.locations_scouted = set()
        self.connected.clear()
        self.scouted.clear()

    def on_package(self, cmd: str, args: dict):
        super().on_package(cmd, args)
        if cmd == "Connected":
            slot_data = args["slot_data"]
            if "goal_location" not in slot_data:
                logger.warning("X2WOTCClient: slot_data missing goal_location, falling back on Victory")
                self.goal_location = "Victory"
            else:
                self.goal_location = slot_data["goal_location"]
            self.connected.set()

    def make_gui(self):
        ui = super().make_gui()
        ui.base_title = "Archipelago XCOM 2 War of the Chosen Client"
        return ui

    def start_proxy(self):
        if self.proxy_task:
            self.proxy_task.cancel()
        self.proxy_task = asyncio.create_task(run_proxy(self), name="proxy")


def launch():
    async def main(args):
        ctx = X2WOTCContext(args.connect, args.password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server_loop")
        ctx.start_proxy()

        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        await ctx.exit_event.wait()
        await ctx.proxy_task
        await ctx.shutdown()

    import colorama

    parser = get_base_parser()
    args = parser.parse_args()

    colorama.init()
    asyncio.run(main(args))
    colorama.deinit()
