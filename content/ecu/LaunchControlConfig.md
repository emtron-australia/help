---
title: "Launch Control"
---

Launch Control Config


![Image](</img/Untitled275.png>)



The following 2 modes are available for Launch Control:


* RPM Limiting
* Torque Limiting


RPM Limiting


This is a conventional RPM limiting mode where where ECU adjusts the engine cutting to achieve a target Launch RPM.


Torque Limiting


The ECU will limit and control the Engine Torque to achieve a Target RPM.&nbsp; The feedforward torque setting is used to achieve stable/constant RPM which&nbsp;

is typically 0 Nm. The ECU then applies a PID over the top to latch the engine speed to the Launch RPM Target.&nbsp;


The methods used by the ECU to control torque are user adjustable with the following options:


1. DBW Plate Control(PID)&nbsp; + Ignition Retard(Table).&nbsp; The ECU will calculate the required DBW Throttle Area for the RPM Target/Torque Request and move the plate to the position. The ECU is able to calculate the plate position using the TMF calculations so this function MUST be calibrated correctly. An Ignition retard table can be used in an open-loop setup to reduce torque and the ECU will automatically correct for this torque loss during the TMF throttle plate calculation.&nbsp;


This mode is most suitable for road applications&nbsp;


2. Engine Cutting(PID) + Retard(Table). The ECU will PID the Torque Target (closed loop) to achieve the correct Launch RPM Target. An Ignition retard table can be used in an open-loop setup (non ECU calculated) to help reduce Torque and spool turbos. The PID closed loop system will account for this Torque loss during the Engine Cut calculation.&nbsp;


This mode is most suitable for track applications&nbsp;


&#51;. &nbsp; Ignition Retard (PID) + Cutting (PID).&nbsp; The is a fully closed loop system with the ECU calculating both the Ignition Retard and %Cut to achieve the Launch RPM/Torque target. The ECU calculates the Retard first until the Retard clamped is reached, then removes any remaining Torque with %Cut.


This mode is most suitable for track applications&nbsp;


For tuning help see [Launch Control (Nm) Setup](<LaunchControlNm.md>)&nbsp; and&nbsp; [Launch Control Tuning Guides](<Newtopic476.md>)

