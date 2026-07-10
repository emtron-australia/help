---
title: "Dwell Tables"
weight: 13
---

## Overview

![Image](</img/Ignition11.jpg>)

The Dwell Table defines the ignition coil charge time (**dwell**) as a function typically of **ECU Supply Voltage** and **Engine Speed**.

Dwell time is the amount of time the ignition coil primary winding is energised prior to the spark event and is expressed in units of **milliseconds (ms)**.

During the dwell period, energy is stored within the ignition coil magnetic field and is subsequently released when the ignition event occurs. Insufficient dwell time may result in a weak spark and ignition misfire, while excessive dwell time can overheat the ignition coil and ignition driver circuitry.

Two independent Dwell Tables are available and can be assigned to individual cylinders using the **Dwell Setup** configuration page. See [*Dwell Setup*](<dwell_setup.md>) for more infomration.


> **ℹ️ Note**
>
> Excessive dwell time does not generally increase spark energy once the ignition coil has reached magnetic saturation and may result in unnecessary heating and/or failure of the ignition coil and ignition drivers.

--- 

## Dwell Offset Table 1

![Image](</img/Ignition13.jpg>)

The Dwell Offset Table 1 is a user-defined offset table that allows ignition coil charge time (**dwell**) to be adjusted based on operating conditions or factors not directly accounted for by Dwell Table 1.

**Final Dwell = Dwell Table 1 + Dwell Offset Table 1**

> **ℹ️ Note**
>
> Dwell Table 1 supports a user-defined Dwell Offset Table. Dwell Table 2 does not have an associated offset table and uses the base dwell values defined within the table only.