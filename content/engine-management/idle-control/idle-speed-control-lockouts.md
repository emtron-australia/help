---
title: "Idle Speed Control Lockouts"
weight: 55
---

## Idle Speed Lockouts

## TP1/PP1 Lockout

% below in which Idle Speed Control system becomes active.  

- Throttle Position 1 used on Solenoid and Stepper systems

- Pedal Position 1 used on DBW systems

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

12: Rear  Axle Speed

13: Vehicle Speed

** Speed inputs must be defined and properly calibrated under “Input Setup”

## Speed Lockout

Locks out Idle Speed Control when the speed is greater than or equal to this value (KPH).

Typical : 5.0

** Speed Channel must be defined.  

## Idle Range Lockout

The engine speed must fall below the Idle Target + Idle Range Lockout before Idle Speed Control becomes active.

Example:

Idle Target = 800 (set from Idle Speed Control menu)

Idle Range Lockout = 400.

Idle Speed Control will become active when the engine speed falls below 1200 RPM.

Typical: 400 RPM
