---
title: "CAN Torque Reported Modifier"
---

**CAN Torque Reported Modifier**&nbsp;


Torque Information over the CAN bus can be modified.&nbsp;

This can change the behavior of the Gearshift along with clutch pressure in gear.&nbsp;

If there is excessive slip typically the Torque reported should be increased.&nbsp;

If the gearshift feel is too sharp and aggressive the Torque reported should be reduced.&nbsp;


The table applies an offset.&nbsp;


This effects:&nbsp;

&#49;) Engine Torque Demand&nbsp;

&#50;) Engine Torque&nbsp;

Table range is +/- 500Nm&nbsp;


![Image](</img/AAAA68.jpg>)


The above example shows a typical setting.&nbsp;

The increase in Torque reported over the CAN bus will have the effect of sharpening the transmission shifting and clutch lockup.&nbsp;

It is important to note that directly programming the TCM through a third party flashing tool is advised over using the ECU to offset the torque reported.