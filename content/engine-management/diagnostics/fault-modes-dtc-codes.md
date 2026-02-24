---
title: "Fault Modes & DTC Codes"
weight: 99
---

The ECU monitors the relationship between the Servo Positions 1/2 signals, Pedal Positions 1/2 signals and Target vs Actual Plate Position. When an error occurs the ECU will generate the following DTC's 

* P1574 Throttle Position Sensor Disagreement between Sensors
* P1577 Pedal Position Sensor Disagreement between Sensors
* P1570 DBW Target Tracking Error 
* P1581 DBW Shutdown

The DTC code will be cleared automatically by the ECU when the fault condition is removed. However, an error counter will be incremented so the fault history can be viewed. 

During an active DBW DTC the ECU will limit the engine speed for safety reasons. There are several options available using the DBW Fault Mode setting: 

1. Non adjustable engine limit set at 2000RPM.(Recommended setting)
1. Use Limp Home Table1. This is an adjustable 3D table.
1. Use Limp Home Table2. This is an adjustable 3D table.

## CAUTION. When using the Limp Home Tables make sure these are setup correctly.
