import ModuleUpdate
import Utils
from worlds.x2wotc.Client import launch

ModuleUpdate.update()

if __name__ == "__main__":
    Utils.init_logging("X2WOTCClient", exception_logger="Client")
    launch()
