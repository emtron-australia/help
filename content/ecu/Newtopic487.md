---
title: "PID Based Launch Control"
---

**PID Based Launch Control:**

The Emtron PID based Launch Control will apply gains in the static mode function only, as the PID target is the Launch RPM. &nbsp;

\*\* RPM Control is the only PID base

This means in "Moving" mode, the ECU will follow Engine reduction calculates via the Torque Reduction Ignition, Torque Reduction Cut, and Throttle Area Demand



**Launch PID Setup**



**Launch System Delay**


This setting delays&nbsp; the routine to allow the closed loop system to function, as the torque is *calculated*.&nbsp;



&#48; = 10ms

&#49; = 20ms

&#50; = 50ms

&#51; = 100ms


&nbsp; &nbsp; Typical setting for Ignition Based PID - "2"&nbsp;

&nbsp; &nbsp; Typical setting for Throttle Based PID - "1"



**Launch Control Proportional Gain**


A value of 1.00 will output +/- 10Nm for every 100 RPM of Target error.


&nbsp; &nbsp; Typical setting for Ignition Based PID - "3"&nbsp;

&nbsp; &nbsp; Typical setting for Throttle Based PID - "0.5"


\*\* Throttle Based PID - the least amount of error in the throttle area/TMF calculation feeds forward this PID


**Launch Control Integral Gain**


A value of 1.00 will output +/- 10Nm for every 100 RPM of Target error, but increment/count up to the integral gain limit


&nbsp; &nbsp; Typical setting for Ignition Based PID - "0.150"&nbsp;

&nbsp; &nbsp; Typical setting for Throttle Based PID - "0.050"


\*\* Throttle Based PID - the least amount of error in the throttle area/TMF calculation feeds forward this PID


**Launch Control Derivative Gain**


The derivative change of the engine torque vs the target will be affected by this gain value


&nbsp; &nbsp; Typical setting for Ignition Based PID - "3"&nbsp;

&nbsp; &nbsp; Typical setting for Throttle Based PID - "1"


\*\* Throttle Based PID - the least amount of error in the throttle area/TMF calculation feeds forward this PID


