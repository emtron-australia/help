---
title: "Frictional Loss Tables"
weight: 1019
---

# Frictional Loss Tables

![Image](</img/Untitled279.jpg>)

The engine torque produced by combustion is calculated by the ECU and referred to as “Ideal” Engine Torque.  The moving parts within the engine have mass and are subject to frictional losses and therefore limit the actual torque available. As such, the estimate of torque required to overcome this drag effect is called Frictional Loss. This estimate is found in the Frictional Loss Table in units of Nm.  A default table is provided as a guide to be adjusted (See below)

These internal torque losses are mainly influenced by the cylinder count i.e. the more cylinders you have, the more moving parts and therefore more friction & the more parasitic loss of torque. 

![Image](</img/Torque man 10.jpg>)

## Calibrating Frictional Loss

The engine must be actually mapped and calibrated before editing this table. An easy way to get a close representation of this loss is to adjust the frictional loss value at each RPM point to achieve a normal Engine Torque (uncorrected) value of 0 Nm (i.e. no engine acceleration or deceleration).  Another hint that there is an incorrect setting will be correlation problems between the ECU calculated torque and a known accurate reading. See the Torque tab in the Runtime menu (F3) to view this data     

| **Engine Torque (Uncorrected) =  (Engine Torque Ideal - Torque Frictional Loss) x Engine Torque Correction** |
| ----------------------------------------------------------------------------------------------------------------- |

![Image](</img/Untitled280.jpg>)

# Frictional Loss Offset Tables

There are two (2) tables that allow offsetting of the frictional loss.  One typical example will be adjusting the loss based on oil temperature. 

![Image](</img/Untitled178.png>)

