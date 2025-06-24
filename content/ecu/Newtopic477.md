---
title: "RPM Control: Throttle Plate(PID) + (Retard Table)"
---

**RPM Control: Throttle Plate(PID) + Retard (Table):**

With a properly tuned Throttle Area table ([Throttle Mass Flow)](<ThrottleMassFlow.md>), the ECU can calculate the outflow requirement for desired torque requests


In some cases depending onm the hardware, an open loop a timing retard table can be applied to generate "reserve" torque as well in Turbocharged applications.&nbsp;


\*\* EGT, Turbine speed, and boost pressure should be considered



**Static Mode Example Data:**

![Image](</img/NewItem889.png>)

In the above static example, you can see the ECU holding the “Launch Torque Target” (Yellow Arrows) in the second plot. &nbsp;

This is done by adjusting final torque via Engine Torque (TMF) channels


