---
title: "Overview"
---

The ECU offers **two** Ground Speed Limit Tables which can operate either independently and together to produce a single speed limit value.&nbsp; Each Limit Table also has two Offsets Tables.


The Function is enabled from the Config View -\> Functions Tab.


Table selection is controlled using the "Speed Limit Table Control" setting.&nbsp;


&#48;: Speed Limit Table 1 is the only table active

&#49;: Speed Limit Table 2 is the only table active

&#51;: Both Table 1 and Table 2 active,&nbsp; allowing two independent speed limits

&#53;: The Cal Slot Table selects the active Speed Limit Table (1 or 2).

&#54;: Z-Axis control calculates a single Speed Limit value by interpolating between Speed Limit Table 1 and 2.&nbsp;

NOTE: In Z-Axis mode only Speed Limit Table 1" single zone settings are used. Table 2 settings are not used



**Speed Limit EN Switch:**

When the 'Speed Limit EN Switch' has an Input Source assigned, the Speed Limit is only active when the switch is ON. Can be used for pit lane limiting.

This applies to all Table Control modes.


Use the Runtime menu to view the current Limit values. 0 = OFF



![Image](</lib/Untitled26.jpg>)
