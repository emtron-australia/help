---
title: "Frictional Loss Tables"
---

# Frictional Loss Tables



![Image](</lib/Untitled279.jpg>)


The engine torque produced by combustion is calculated by the ECU and referred to as “Ideal” Engine Torque.  The moving parts within the engine have mass and are subject to frictional losses and therefore limit the actual torque available. As such, the estimate of torque required to overcome this drag effect is called Frictional Loss. This estimate is found in the Frictional Loss Table in units of Nm.  A default table is provided as a guide to be adjusted (See below)

These internal torque losses are mainly influenced by the cylinder count i.e. the more cylinders you have, the more moving parts and therefore more friction \& the more parasitic loss of torque.&nbsp;


![Image](</lib/Torque man 10.jpg>)


**Calibrating Frictional Loss**&nbsp;


The engine must be actually mapped and calibrated before editing this table. An easy way to get a close representation of this loss is to adjust the frictional loss value at each RPM point to achieve a normal Engine Torque (uncorrected) value of 0 Nm (i.e. no engine acceleration or deceleration).&nbsp; Another hint that there is an incorrect setting will be correlation problems between the ECU calculated torque and a known accurate reading. See the Torque tab in the Runtime menu (F3) to view this data&nbsp; &nbsp; &nbsp;



| **Engine Torque (Uncorrected) =&nbsp; (Engine Torque Ideal - Torque Frictional Loss) x Engine Torque Correction** |
| ----------------------------------------------------------------------------------------------------------------- |




![Image](</lib/Untitled280.jpg>)


# Frictional Loss Offset Tables


There are two (2) tables that allow offsetting of the frictional loss.&nbsp; One typical example will be adjusting the loss based on oil temperature.&nbsp;


![Image](</lib/Untitled178.png>)


