---
title: "Transmission Brake Control"
weight: 85
---

The Transmission Brake Function allows the ECU to directly control the Trans Brake inside the gearbox. 

## Output

The Function can be switched ON from the Config view -> Functions -> Motorsport Functions tab -> Transmission Brake Control. This menu allows the Output Channel to be selected and configured.

**NOTE**: 

* **When driving the solenoid directly from the ECU, use ONLY Auxiliary Channels 13-16. These solenoids typically require a minimum of 10A to switch**. 
* **Make sure the ECU is grounding the solenoid and sufficient ECU grounds are connected to support the current.  Typically a PDM would be used to supply power to the solenoid.**

## Input

Two Inputs will need to be setup under the Config View -> Inputs -> Motorsport Tab

1) Trans Brake Switch. When the switch is ON, the selected output will be switched ON

2) Trans Brake Bump Switch. When the switch is ON, the Output will be switch OFF for the time set in the "Trans Brake Bump Time". This allows the Trans Brake to be released for a sort period of time allowing the vehicle to move forward.