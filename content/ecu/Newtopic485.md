---
title: "RPM Control: Retard (PID) >Cutting (PID)"
---

**RPM Control: Retard (PID) \>Cutting (PID):**

Balancing “Torque Reduction – Retard” vs “Torque Reduction – Cut” is important when using both static and moving target modes for PID Launch Targeting. &nbsp;


Generally, timing retard is good for control of torque and can also help spool turbines in those applications. &nbsp;

However, during launch, as engine load/boost increases the potential engine torque, ignition timing can/will continue to retard to overcome engine speed from increasing. &nbsp;


\*\* EGT, Turbine speed, and boost pressure must be considered, to determine the **Static/Moving Ignition Retard Clamp** points in their respective tables. &nbsp;


At these points of ignition trim/retard, the Launch system will switch to Launch Torque Reduction – Cut functions. &nbsp;


See:&nbsp;

![Image](</lib/NewItem728.jpg>)


**Torque Reduction Ignition Retard Table:**

Engine Functions -\> Torque Management -\> Torque Reduction Ignition Retard Table

The runtime %Torque Reduction – Retard is used. &nbsp;

The channel correlates to how much retard will be applied vs the amount of Torque Reduction requested. &nbsp;

This is a global function of the ECU, which is why it is under the Torque Management section.&nbsp; &nbsp;


![Image](</lib/NewItem727.png>)

\*\* Warning - The maximum value in this table (at 100% %Torque Reduction – Retard), must be at a higher value than the Static/Moving Ignition Retard Clamp



**Static Mode Example Data:**

![Image](</lib/NewItem726.png>)

In the above static example, you can see the ECU holding the “Launch Torque Target” (Yellow Arrows) in the second plot. &nbsp;

This is done by Torque Reduction – Retard (Blue Arrow), until the load is increased by throttle and boost (Green Arrow). &nbsp;

The Launch Control system automatically controls the Launch Control Target with the required additional Torque Reduction Cut under the higher loads to control the Launch Torque Target (Orange Arrow).&nbsp;

Cuts are introduced once the Static Ignition Retard Clamp is reached. &nbsp;


**Moving Mode Example Data:**

![Image](</lib/NewItem725.png>)

In this moving target example, the ECU is holding “Launch Torque Target” (Yellow Arrows) in the second plot by Torque Reduction – Retard alone.
