---
title: "Ignition Firing Edge"
weight: 2
---

## Overview

![Image](</img/Ignition3.jpg>)

Selects the ignition output edge used by the ECU to trigger the ignition firing event.

The selected edge defines the polarity of the ignition control signal. One edge initiates coil charging (**Dwell Edge**) while the opposite edge commands the ignition coil to discharge and generate the spark (**Firing Edge**)


> **⚠️ Warning 1**
>
> Ensure the correct ignition edge is selected before connecting the ECU to the ignition system.
> Selecting the incorrect edge may result in damage to the ECU, ignition module, ignition coil(s), or associated wiring.

> **⚠️ Warning 2**
>
> The ECU Ignition Output provides a TTL-level trigger signal intended to control an external ignitor or a coil with an integrated ignitor module. 
> 
> **Do not connect the ECU Ignition Output directly to a coil negative terminal.** Incorrect connection will result in damage to the ECU and/or ignition system.

## Options

| Value | Mode | Description |
|--------:|------|-------------|
| **0** | Falling | Coil charging begins on the **Rising Edge** and the spark is fired on the **Falling Edge**. |
| **1** | Rising | Coil charging begins on the **Falling Edge** and the spark is fired on the **Rising Edge**. |

> **ℹ️ Typical Configuration**
>
> Most modern ignition coils and ignition modules incorporate an internal ignitor and require a **Falling Edge** spark output.
