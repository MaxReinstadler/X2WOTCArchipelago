# Config Settings Guide

Config settings enable users to adjust certain behaviors and parameters of the game mod. It is strongly recommended you use [Mod Config Menu](https://steamcommunity.com/sharedfiles/filedetails/?id=667104300) to edit them. This guide aims to explain the purpose and functionality of each setting in more depth.

## General

### Debug Logging

- Default: On
Enables logging to `Launch.log`, which can be very useful for debugging purposes. Leave this enabled if you can.

### Proxy Port

- Default: 24728
Sets the port the game mod tries to contact the proxy at. This has to match the port the proxy is actually hosted at by the client, which can be changed with the `/proxy` command. Don't change this unless you run into an issue with the default.

## Reduced Campaign Duration

### Skip Supply Raids / Council Missions / Resistance Ops

- Default: On
If set, the specified mission type will be automatically skipped and its rewards will be collected when it is spawned from a regular calender event.

### Disarm Ambush Risk / Capture Risk

- Default: On
If set, the specified risk type will have no effect when it is rolled during a covert op.

### Supply Raid Reward Base / Error

- Default: 0.5 / 0.15
Sets the amount of resources that are rewarded for skipped supply raids. A random value is multiplied with the maximum amounts for supplies (200), alien alloys (80), elerium crystals (40) and elerium cores (3) and rounded down to the nearest integer. The error determines the range of possible values from which each multiplier can be rolled, e.g. 0.35 to 0.65 for default settings.

### Increase XP Gain

- Default: 0.35
Each time an enemy dies, each soldier has the given fraction of a kill attributed to them, speeding up promotions. Because this system is agnostic to who got the final hit, soldiers with low kill counts will benefit more from the increase. In general, the effect will be much stronger than it seems; the default setting for example will work out to a 35% increase in XP from kills, but something like a 140% increase in XP from assists, meaning the actual bonus lies somewhere in between.

### Increase Corpse Gain

- Default: 1
Each time an enemy dies, the given number of additional corpses are added to the mission rewards. This means that the default setting is effectively a 2x corpse multiplier.

## Campaign Completion Requirements

### Require Psi Gate Objective / Stasis Suit Objective / Avatar Corpse Objective

- Default: Off
If set, the final set of missions can only become available after the specified lines of objectives is completed. This has to match what you set for `Campaign Completion Requirements` in your yaml.

## Miscellaneous

### Disable Day One Traps

- Default: Off
If set, traps have no effect when received during the first day of a campaign. One use for this is if you wish to retire traps received during previous runs after a restart.
