---
title: "Idle Ignition Lockouts"
weight: 49
---

## Idle Ignition Lockouts

![Image](</img/Idle Ignition 3.jpg>)

## TP1/PP1 Lockout

Throttle position below which Idle Ignition Control can become active

When "Pedal Position 1" input is active this channel will be used. Otherwise 'Throttle Position 1"input is used.

Typical : 2%

## Speed Channel

Used to define how the “Speed Lockout” is used.  

0: OFF

1: Drive Speed

2: Ground Speed

3: Drive Speed Front L

4: Drive Speed Front R

5: Drive Speed Rear L

6: Drive Speed Rear R

7: Undriven Speed Front L

8: Undriven Speed Front R

9: Undriven Speed Rear L

10: Undriven Speed Rear R

11: Front Axle Speed

12: Rear  Axle Speed

13: Vehicle Speed

*** Speed inputs must be defined and properly calibrated under “Input Setup”**

## Speed Lockout

Locks out Idle Ignition Control when the speed is greater than or equal to this value (KPH).

Typical : 5.0

** Speed Channel must be defined.  

## Idle Range Lockout

The engine speed must fall below the Idle Target + Idle Range Lockout before Idle Ignition Control becomes active. 

Example:

Idle Target = 800 (set from Idle Speed Control menu)

Idle Range Lockout = 400.

Idle Speed Control will become active when the engine speed falls below 1200 RPM.

Typical: 400 RPM

## Post Start Delay

Delay after the engine speed has exceeded the crank exit RPM before Idle Ignition Control becomes active. 

Typical : 2 sec

## Re-entry Delay

Delay once all lockouts are cleared before Idle Ignition Control becomes active.