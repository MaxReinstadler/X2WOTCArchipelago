# Troubleshooting

### LINUX USERS NOTE

**The native Linux port of XCOM 2 WotC does not play nice with my mod. Use the Windows distribution through Proton instead.**

## Nothing is happening

Check if the mod is actually loaded by looking for the version text in the bottom left corner of the main menu. If it's not there, try restarting the game and consider using [AML](https://github.com/X2CommunityCore/xcom2-launcher) if the problem persists.

## I'm getting networking errors in-game

### Request Timed Out

1. Check if the XCOM 2 WotC AP Client (which is included in the [APWorld](https://github.com/MaxReinstadler/X2WOTCArchipelago/releases)) is running. Refer to the [Setup Guide](https://github.com/MaxReinstadler/X2WOTCArchipelago/blob/main/worlds/x2wotc/docs/setup_en.md) for further instructions.
2. It may be that the proxy port settings in the client and in-game are mismatched or something else is wrong with the default port. Check the settings in-game via [MCM](https://steamcommunity.com/sharedfiles/filedetails/?id=667104300) and in the client via the `/proxy` command, and change them if necessary.

### Client Disconnected

Make sure the XCOM 2 WotC AP Client is connected to your slot in the multiworld server before checking locations.

## The game isn't behaving how I expected

### I have a skulljack but can't use it

To build the skulljack, all you need is `[Tech] ADVENT Officer Autopsy` which unlocks the proving ground. To use it, the corresponding objective will need to be active as well, which only happens once you've also received `[Tech] Alien Biotech`.

## My problem isn't listed here

Let me know in the [Discord Thread](https://discord.com/channels/731205301247803413/1037751568700805141)! If the issue is in-game, there might be some useful info in the log file (`Documents/My Games/XCOM2 War of the Chosen/XComGame/Logs/Launch.log` by default on Windows).
