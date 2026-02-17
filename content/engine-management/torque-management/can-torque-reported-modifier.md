---
title: "CAN Torque Reported Modifier"
weight: 61
---

## CAN Torque Reported Modifier

Torque Information over the CAN bus can be modified. 

This can change the behavior of the Gearshift along with clutch pressure in gear. 

If there is excessive slip typically the Torque reported should be increased. 

If the gearshift feel is too sharp and aggressive the Torque reported should be reduced. 

The table applies an offset. 

This effects: 

1) Engine Torque Demand 

2) Engine Torque 

Table range is +/- 500Nm 

![Image](</img/AAAA68.jpg>)

The above example shows a typical setting. 

The increase in Torque reported over the CAN bus will have the effect of sharpening the transmission shifting and clutch lockup. 

It is important to note that directly programming the TCM through a third party flashing tool is advised over using the ECU to offset the torque reported.