---
title: "Idle Ignition PID Setup"
---

**Idle Ignition PID Setup**


![Image](</img/Idle Ignition 5.jpg>)


**Control Rate**


The frequency or rate at which the PID control algorithm calculations are performed.


Typical : 10 Hz


**Idle Ignition Deadband +/-**


The output control signal is held constant when the Input Signal (RPM) falls within the deadband range of the Setpoint (RPM Target). This helps reduce steady state error and oscillations.


Typical : 25 RPM


**RPM Filter**


Filters the RPM signal to allow better PID control


Typical : 5


**Integral Positive/Negative Clamp**&nbsp;


Allows the user to set the minimum and maximum Integral gain compensation used by the closed loop system.