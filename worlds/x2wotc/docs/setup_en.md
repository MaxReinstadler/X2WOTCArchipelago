# XCOM 2 War of the Chosen Archipelago Setup Guide

## Required Software

- [XCOM 2](https://store.steampowered.com/app/268500/XCOM_2/) with the
[War of the Chosen DLC](https://store.steampowered.com/app/593380/XCOM_2_War_of_the_Chosen/) installed through Steam
- [XCOM 2 WotC Archipelago Mod](https://steamcommunity.com/sharedfiles/filedetails/?id=3281191663)
- [Archipelago](https://github.com/ArchipelagoMW/Archipelago/releases)
- [XCOM 2 WotC APWorld](https://github.com/MaxReinstadler/X2WOTCArchipelago/releases)

## Optional Software

- **(Highly recommended)** Any dedicated XCOM 2 WotC Mod Launcher like the
[Alternative Mod Launcher (AML)](https://github.com/X2CommunityCore/xcom2-launcher)
- **(Highly recommended)** [Mod Config Menu for WotC](https://steamcommunity.com/sharedfiles/filedetails/?id=667104300)
- Alien Hunters and Shen's Last Gift DLCs are supported but not required.

## Setup

### XCOM 2 War of the Chosen Mod

1. Install [XCOM 2](https://store.steampowered.com/app/268500/XCOM_2/) and the
[War of the Chosen DLC](https://store.steampowered.com/app/593380/XCOM_2_War_of_the_Chosen/) through Steam.
2. Subscribe to the [XCOM 2 WotC Archipelago Mod](https://steamcommunity.com/sharedfiles/filedetails/?id=3281191663).
3. **(Optional)** Install any dedicated Mod Launcher (e.g. [AML](https://github.com/X2CommunityCore/xcom2-launcher)).
4. Launch XCOM 2 WotC with the AP Mod enabled.

### XCOM 2 WotC AP Client

1. Download and install the latest [Archipelago](https://github.com/ArchipelagoMW/Archipelago/releases) release.
2. Download the latest release of the [XCOM 2 WotC APWorld](https://github.com/MaxReinstadler/X2WOTCArchipelago/releases).
Double-click it to install automatically, or copy it to your Archipelago installation's `custom_worlds` folder manually.
2. Launch the XCOM 2 War of the Chosen AP Client from the Archipelago Launcher.

## Generating a Multiworld

1. Follow the general [Archipelago Guide](https://archipelago.gg/tutorial/Archipelago/setup/en) for generating and
hosting a Multiworld.
    - Multiworld will have to be generated locally but can be hosted on the website.
    - [APWorld](https://github.com/MaxReinstadler/X2WOTCArchipelago/releases) can be found on GitHub.
    - [Options Template](https://github.com/MaxReinstadler/X2WOTCArchipelago/releases) can be generated with the
    'Generate Template Options' button in the Archipelago Launcher, or found on GitHub.

## Joining a Multiworld

0. Upon launching the XCOM 2 WotC AP Client, the proxy server will be hosted locally (at port 24728 by default).
    - If this doesn't work for you for whatever reason, the port can be changed using the `/proxy` command.
    If you do, you will also have to edit the corresponding in-game setting via the
    [Mod Config Menu](https://steamcommunity.com/sharedfiles/filedetails/?id=667104300) or by accessing the
    [user config file](https://www.reddit.com/r/xcom2mods/wiki/wotc_modding/folder_paths/#wiki_user_config) directly.
1. In the client, connect to the address the Multiworld is hosted at.
2. Provide your slot name (the name you entered into your YAML).
3. If asked, provide the room password that was set during generation.
4. The client should tell you that you're connected. Start playing!
