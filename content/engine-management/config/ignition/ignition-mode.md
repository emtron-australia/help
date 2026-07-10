---
title: "Ignition Mode"
weight: 1
---

## Overview

![Image](</img/Ignition2.jpg>)

Selects the ignition output strategy used by the engine. The selected ignition mode determines how ignition events are distributed across the available ignition output channels.

> **⚠️ Warning**
>
> The ECU Ignition Output provides a TTL-level trigger signal intended to control an external ignitor or a coil with an integrated ignitor module. 
> 
> **Do not connect the ECU Ignition Output directly to a coil negative terminal.** Incorrect connection will result in damage to the ECU and/or ignition system.

## Options

| Value | Mode |
|--------:|------|
| **0** | Off |
| **1** | Direct Fire |
| **2** | Wasted Spark |
| **3** | Distributor |
| **4** | Twin Distributor |
| **5** | Direct Fire + Direct Trailing Spark |
| **6** | Wasted Spark + Direct Trailing Spark |
| **7** | CDI 8 |


# Mode Descriptions

### Off

Disables all ignition outputs.

### Direct Fire

Each cylinder is assigned its own dedicated ignition output channel.

### Wasted Spark

Each ignition output fires two cylinders simultaneously, with one spark occurring on the compression stroke and the other on the exhaust stroke.

### Distributor

Uses a single ignition output to drive a conventional distributor ignition system.

### Twin Distributor

Uses two ignition outputs to drive a twin distributor ignition system.

### Direct Fire + Direct Trailing Spark

Provides individual ignition outputs for both leading and trailing spark plugs. Commonly used on rotary engines requiring independent control of leading and trailing ignition events.

### Wasted Spark + Direct Trailing Spark

Uses wasted spark ignition for the leading plugs while maintaining individual control of the trailing spark plugs.

### CDI 8

Configures the ECU for operation with an external 8-channel Capacitive Discharge Ignition (CDI) system.

---

> **ℹ️ Note**
>
> - **Ignition Channel 1** is the only ignition output available in **Distributor** mode.
> - **Ignition Channels 1 and 2** are the only ignition outputs available in **Twin Distributor** mode.
> - For **Direct Fire + Direct Trailing Spark** and **Wasted Spark + Direct Trailing Spark** modes, a maximum of **6 trailing ignition channels** are available.
> - All other ignition modes provide fully configurable ignition channel assignments.

See [*Ignition Channel Setup*](<ignition-channel-setup.md>) for channel setup help.
