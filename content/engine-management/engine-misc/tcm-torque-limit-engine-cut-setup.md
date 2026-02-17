---
title: "TCM Torque Limit Engine Cut Setup"
weight: 113
---

## TCM Torque Limit Engine Cut Setup

In some motorsport environments and extremely high-end applications the OEM Torque Reductions may not deliver maximum performance. This has been addressed by allowing the user the ability to leverage the factory torque requests and applying a cut for more instantaneous torque reduction. 

This is particularly useful on gear shifts where sharper than factory shift response is required. 

![Image](</img/AAAA71.jpg>)

## TCM Torque Limiting Engine Cut Mode

![Image](</img/AAAA56.jpg>)

0: OFF 

1: TCM Torque Limit Ref: Throttle 

2: TCM Torque Limit Ref: Retard 

This mode is used to assist  the TCM and ECU in reducing the engines torque for improved gearshift control. 

The primary source of Torque Reduction is throttle plate control and retard, but in situations of a large torque reduction, the addition of engine cutting can be used to help this process. 

The TCM Sends torque limit requests using either Throttle or Retard.  

Either torque value can be selected as the reference for the engine cutting calculation.

* ONLY gets applied on the Up-shift

* A minimum Engine Torque lockout is used to prevent the cut operating under light loads

## TCM Torque Limiting Engine Cut Type

![Image](</img/AAAA58.jpg>)

0: Ignition Cut

1: Fuel Cut

2: Ignition + Fuel Cut

## TCM Torque Limit Engine Cut Threshold

![Image](</img/AAAA59.jpg>)

This mode is used to assist  the TCM and ECU in reducing the engines torque for improved gearshift control.  

The ECU converts the Torque Limit (Nm) sent by the TCM into a calibrated Engine Cut Percentage.

This setting controls the Torque Threshold above which Engine Cutting can be used to reduce torque 

Example.: 

Cut Threshold 10%

TCM Requesting Torque Limit of 300Nm. 

Engine Torque 600Nm

10% of 300Nm = 330Nm

The ECU will calculate the required cut % from 600Nm down to 330Nm.

## TCM Torque Limit Engine Cut - Max Clamp

![Image](</img/AAAA60.jpg>) 

This mode is used to assist  the TCM and ECU in reducing the engines torque for improved gearshift control. 

The primary source of Torque Reduction is the closing of the throttle plate, but in situations of a large torque reduction, 

Ignition cutting can be used to help this process. 

The ECU converts the Torque Limit (Nm) into a calibrated Engine Cut Percentage.

This setting controls the Maximum amount of Cut the ECU can apply for a given Torque Limit request. 

Example.: 50%

This means the Maximum Cut applied to the Engine will be clamped to 50%.

## TCM Torque Limit Engine Cut Gain

![Image](</img/AAAA61.jpg>)

During a TCM Torque Reduction request the ECU can cut the engine to reduce Torque. 

This setting indicates to the ECU the percentage of Torque reduced for every 1% of Engine Cut.

Example.  

- Engine Torque at 600Nm.

- 200Nm Torque Reduction is requested.

- This is a 33% Reduction in Torque

1.0 %/ %Cut. ECU will cut engine at 33%

0.8 %/ %Cut. ECU will cut engine at 41%

1.2 %/ %Cut. ECU will cut engine at 27%

## TCM Torque Limit Min Torque

![Image](</img/AAAA62.jpg>)

The Uncorrected Engine Torque must be greater than the entered value for the Engine Cut to be enabled

