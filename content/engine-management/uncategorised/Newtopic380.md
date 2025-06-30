---
title: "Boost PID Setup"
---

**Control Rate**


The rate at which the PID control algorithm calculations are performed.


Typical : 25 Hz

\

**Boosst Deadband +/-**


The output control signal is held constant when the Input Signal (normally MAP) falls within the deadband range of the Setpoint (Boost Target). This helps reduce steady state error and oscillations.


Typical : 2 kPa


**Input Filter**


Filters the Input signal to help smooth out any pulsations


Note: Input Signal usually MAP.


Typical Value: 5 ( 0 = OFF)

\

**Target Filter**


Filters the Target signal to help smooth out any pulsations


Typcial Value: 4 ( 0 = OFF)


