---
title: "Idle PID Setup"
---

**Control Rate**

\

The rate at which the PID control algorithm calculations are performed.

\

Typical : 10 Hz

\

**Idle Deadband +/-**

\

The output control signal is held constant when the Input Signal (RPM) falls within the deadband range of the Setpoint (Idle Target). This helps reduce steady state error and oscillations.

\

Typical : 20 RPM

\

**RPM Filter**

\

Filters the RPM signal to allow better PID control

\

Typical : 5

\

**Integral Positive/Negative Clamp**

\

Allows the user to set the minimum and maximum I gain compensation used by the closed loop system.  

\

**Re-entry Delay**

\

Delay once all lockouts are cleared before Closed Loop Idle Control becomes active.

\

\*\* Will immediately become active if engine speed falls below the Target RPM
