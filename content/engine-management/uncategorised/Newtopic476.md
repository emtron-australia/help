---
title: "Launch Control Tuning Guides"
---

**Launch Control Tuning Guides**



**Preliminary information:**

For Torque Based Launch Control to work properly, the ECU torque calculations must be correct. &nbsp;

The calibration file must have accurate VE calculations, fuel injector data, etc. &nbsp;


Frictional loss tables of the engine are crucial for the correct torque calculations. &nbsp;

See the [Torque Management Tuning Guide](<TorqueManagementTuningGuide.md>)


**Torque Reduction:**

There are three methods of Torque Reduction that can be used regarding Launch Control. &nbsp;

Retarding ignition timing, cutting, or throttle area vs torque reduction % will reduce torque of the engine. &nbsp;

There are 3 different Launch RPM Torque Modes that can be selected in Launch Control Setup (See Launch Control Setup).&nbsp;


![Image](</img/NewItem888.png>)


Option 0:&nbsp; RPM control using Throttle Mass Flow + Retard.&nbsp;

The ECU will calculate the required throttle area for the RPM target and move the plate to the position. Ignition retard Torque loss will be factored into the calculation to give the correct plate position.


Option 1: RPM control using Cutting(PID) + Retard(Table).

The ECU will PID the Torque Target (closed loop) to achieve the correct Launch RPM Target. An Ignition retard table can be used in an open-loop setup (non ECU calculated) to help reduce Torque and spool turbos. The PID closed loop system will account for an Torque loss due the to retard.


Option 2: RPM control using Retard(PID) \> Cutting(PID)

The is a fully closed loop system with the ECU calculating both the Retard and %Cut to achieve the Torque target. The ECU calculates the Retard first until the Retard clamped is reached, then removes any remaining Torque with %Cut.


**Torque Reduction Ignition Retard Table:**

Engine Functions -\> Torque Management -\> Torque Reduction Ignition Retard Table

The runtime %Torque Reduction – Retard is used. &nbsp;

The channel correlates to how much retard will be applied vs the amount of Torque Reduction requested. &nbsp;

This is a global function of the ECU, which is why it is under the Torque Management section.&nbsp; &nbsp;


![Image](</img/NewItem727.png>)

\*\* Warning - The maximum value in this table (at 100% %Torque Reduction – Retard), must be at a higher value than the Static/Moving Ignition Retard Clamp


**Basic Launch Control Settings:**

See [Launch Control](<LaunchControl.md>)



