---
title: "Boost Control Setup"
weight: 37
---

## Boost Control Setup

![Image](</img/Boost Control 1.jpg>)

![Image](</img/Boost Control 2.jpg>)

## Boost Control Mode

Used to select either Open or Closed Loop.

Open Loop mode is generally used to setup initial settings before using Closed Loop mode.

0: Open Loop

1: Closed Loop – Absolute Target

2: Closed Loop – Gauge Target

** Note, Mode 2 works with “0” Manifold Pressure Input only

    The ECU generates a channel Manifold Gauge Pressure

    Manifold Gauge Pressure is derived from the Barometric Pressure Channel

    ** Barometric Pressure Channel must be configured 

Example.

**Absolute Mode**. Target = 250kPa. The ECU will Target an Absolute pressure of 250kPa. Boost Pressure inside the engine will increase as Barometric pressure reduces. 

Barometric Pressure of 100kPa. Boost pressure inside the engine will be 150kPa.

Barometric Pressure of 80kPa. Boost pressure inside the engine will be 170kPa. (250kPa - 80kPa)

**Gauge Mode**. Target = 150kPa. The ECU will Target a boost pressure of 150kPa above Barometric pressure.

Barometric Pressure of 100kPa. ECU Boost Target will be 250kPa, boost pressure inside the engine will be 150kPa.

Barometric Pressure of 80kPa. ECU Boost Target will be 230kPa, boost pressure inside the engine will be 150kPa

Boost Target Tables are used in Closed Loop mode

** Note – Push/Pull Solenoid Mode

Open Loop mode is not available as Closed Loop functionality is required to continuously regulate the target pressure.\

## Boost Control 1/2 Pressure Input

Allows the Boost Control PID Input/Setpoint to be controlled.

** The input for the boost target is using in closed loop. 

0: Manifold Pressure

1: Manifold Pressure - Bank 1

2: Manifold Pressure - Bank 2

3: Manifold Pressure Bank 1/2 Avg

4: Boost Pressure - Bank 1

5: Boost Pressure - Bank 2

6: Boost Pressure Bank 1/2 Avg

7: Wastegate Top Port Pressure 1

8: Wastegate Top Port Pressure 2

9: Boost Pressure

