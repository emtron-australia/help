---
title: "Overview"
weight: 113
---

The ECU offers **two** Ground Speed Limit Tables which can operate either independently and together to produce a single speed limit value.  Each Limit Table also has two Offsets Tables.

The Function is enabled from the Config View -> Functions Tab.

Table selection is controlled using the "Speed Limit Table Control" setting. 

0: Speed Limit Table 1 is the only table active

1: Speed Limit Table 2 is the only table active

3: Both Table 1 and Table 2 active,  allowing two independent speed limits

5: The Cal Slot Table selects the active Speed Limit Table (1 or 2).

6: Z-Axis control calculates a single Speed Limit value by interpolating between Speed Limit Table 1 and 2. 

NOTE: In Z-Axis mode only Speed Limit Table 1" single zone settings are used. Table 2 settings are not used

## Speed Limit EN Switch:

When the 'Speed Limit EN Switch' has an Input Source assigned, the Speed Limit is only active when the switch is ON. Can be used for pit lane limiting.

This applies to all Table Control modes.

Use the Runtime menu to view the current Limit values. 0 = OFF

![Image](</img/Untitled26.jpg>)
