---
title: "Transient Setup"
weight: 34
---

## Transient Setup

![Image](</img/Z Axis31.jpg>)

![Image](</img/Z Axis32.jpg>)

**Accel Enable:** Enable or Disable Transient Acceleration fuel mode, 

**Decel Enable:** Enable or Disable Transient Deceleration fuel mode, 

**Accel/Decel Mode:** Configures runtime input for transient function initiation. 

0: TPS 1 - Throttle position sensor 1 or Drive By Wire Servo Position Sensor 1

1: MAP - Manifold Absolute Pressure Sensor

2: PP 1 - Pedal Position Sensor 1

**Accel/Decel Threshold (+/-):** The rate of change threshold or lockout of the Accel/Decel mode runtime.

This value is set as a percentage of change over a second over it's previous state.

Lower numbers increase the sensitivity in initiating the transient fuel function.

A typical value is 1.0 %/sec.

