---
title: "TCM Torque Limit Engine Cut Setup"
---

**TCM Torque Limit Engine Cut Setup**&nbsp;


In some motorsport environments and extremely high-end applications the OEM Torque Reductions may not deliver maximum performance. This has been addressed by allowing the user the ability to leverage the factory torque requests and applying a cut for more instantaneous torque reduction.&nbsp;

This is particularly useful on gear shifts where sharper than factory shift response is required.&nbsp;


![Image](</img/AAAA71.jpg>)


**TCM Torque Limiting Engine Cut Mode**


![Image](</img/AAAA56.jpg>)


&#48;: OFF&nbsp;

&#49;: TCM Torque Limit Ref: Throttle&nbsp;

&#50;: TCM Torque Limit Ref: Retard&nbsp;


This mode is used to assist&nbsp; the TCM and ECU in reducing the engines torque for improved gearshift control.&nbsp;

The primary source of Torque Reduction is throttle plate control and retard, but in situations of a large torque reduction, the addition of engine cutting can be used to help this process.&nbsp;


The TCM Sends torque limit requests using either Throttle or Retard. &nbsp;

Either torque value can be selected as the reference for the engine cutting calculation.


\* ONLY gets applied on the Up-shift

\* A minimum Engine Torque lockout is used to prevent the cut operating under light loads


**TCM Torque Limiting Engine Cut Type**&nbsp;


![Image](</img/AAAA58.jpg>)


&#48;: Ignition Cut

&#49;: Fuel Cut

&#50;: Ignition + Fuel Cut


**TCM Torque Limit Engine Cut Threshold**&nbsp;


![Image](</img/AAAA59.jpg>)


This mode is used to assist&nbsp; the TCM and ECU in reducing the engines torque for improved gearshift control. &nbsp;

The ECU converts the Torque Limit (Nm) sent by the TCM into a calibrated Engine Cut Percentage.


This setting controls the Torque Threshold above which Engine Cutting can be used to reduce torque&nbsp;


Example.:&nbsp;

Cut Threshold 10%

TCM Requesting Torque Limit of 300Nm.&nbsp;

Engine Torque 600Nm


&#49;0% of 300Nm = 330Nm


The ECU will calculate the required cut % from 600Nm down to 330Nm.


**TCM Torque Limit Engine Cut - Max Clamp**&nbsp;


![Image](</img/AAAA60.jpg>)&nbsp;


This mode is used to assist&nbsp; the TCM and ECU in reducing the engines torque for improved gearshift control.&nbsp;

The primary source of Torque Reduction is the closing of the throttle plate, but in situations of a large torque reduction,&nbsp;

Ignition cutting can be used to help this process.&nbsp;


The ECU converts the Torque Limit (Nm) into a calibrated Engine Cut Percentage.


This setting controls the Maximum amount of Cut the ECU can apply for a given Torque Limit request.&nbsp;


Example.: 50%


This means the Maximum Cut applied to the Engine will be clamped to 50%.


**TCM Torque Limit Engine Cut Gain**&nbsp;


![Image](</img/AAAA61.jpg>)


During a TCM Torque Reduction request the ECU can cut the engine to reduce Torque.&nbsp;

This setting indicates to the ECU the percentage of Torque reduced for every 1% of Engine Cut.


Example. &nbsp;

\- Engine Torque at 600Nm.

\- 200Nm Torque Reduction is requested.

\- This is a 33% Reduction in Torque


&#49;.0 %/ %Cut. ECU will cut engine at 33%

&#48;.8 %/ %Cut. ECU will cut engine at 41%

&#49;.2 %/ %Cut. ECU will cut engine at 27%


**TCM Torque Limit Min Torque** &nbsp;


![Image](</img/AAAA62.jpg>)


The Uncorrected Engine Torque must be greater than the entered value for the Engine Cut to be enabled



