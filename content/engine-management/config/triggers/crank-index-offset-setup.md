---
title: "Crank Index Offset Setup"
weight: 20
---

## Overview

The Crank Index Offset Setup is one of the most critical configuration steps within the ECU.

The ECU determines engine position by detecting a known trigger event, commonly referred to as the **Index Tooth**. Since the Index Tooth position does not normally coincide with **Top Dead Centre (TDC) Cylinder #1 Compression**, the **Crank Index Offset** defines the angular relationship between these two events. This allows the ECU to accurately determine crankshaft position and maintain synchronisation with the engine.

---

![Image](</img/AAA.jpg>)

## Tuning Tip

**1)** For **Wasted Spark** applications, always set the **Ignition Lock Angle** to **0.0° BTDC** when verifying the Crank Index Offset.

*Many timing lights calculate ignition advance using the measured ignition pulse frequency. Since wasted spark systems generate two ignition events per engine cycle, some timing lights may calculate an incorrect engine speed and display an incorrect ignition advance value. Using a lock angle of **0.0° BTDC** allows the crankshaft TDC mark to be verified directly and eliminates this source of error.*

**2)** For **Direct Fire** ignition systems, the Ignition Lock Angle may be set to any convenient crankshaft timing mark available on the engine pulley.

**3)** The fuel injectors can be disabled to validate the initial Crank Index Offset value.prior to starting the engine. See Config -> Fuel -> Fuel Main -> Injection Mode -> Off. 

Direct fire engines may be 360deg out of cycle which can be corrected numerically.

---

## Ignition Timing Synchronisation

Before calibrating the ignition system, the ECU ignition timing must be synchronised with the actual engine crankshaft position.

### Crank Index Offset Calibration

1. Enable **Ignition Lock** and configure a fixed ignition timing value using the **Ignition Lock Angle**. <br>
**NOTE: When Ignition Lock Enable is ON, Ignition Lock Angle value overrides all other timing values in ECU  .**
2. Start the engine and use a timing light to measure the actual ignition timing.
3. Compare the measured ignition timing with the configured Ignition Lock Angle.
4. Adjust the **Crank Index Offset** until the timing light reading matches the configured Ignition Lock Angle.

This procedure should be performed with the engine operating at idle speed.

### Ignition Delay Time Calibration

Once the Crank Index Offset has been calibrated at idle, ignition timing should be verified over the engine operating range.

As engine speed increases, ignition coil turn-on delays, ignition module propagation delays and ECU output delays can introduce small timing errors.

The **Ignition Delay Time** parameter compensates for these delays to ensure the commanded ignition timing accurately matches the actual crankshaft position across the complete engine speed range.

Adjustment guidelines:

- If the measured ignition timing **retards as engine speed increases**, increase the **Ignition Delay Time** value.
- If the measured ignition timing **advances as engine speed increases**, decrease the **Ignition Delay Time** value.

Once correctly calibrated, the timing light should indicate a constant ignition timing value regardless of engine speed when Ignition Lock is enabled.

---

> **⚠️ Important**
>
> The **Crank Index Offset** and **Ignition Delay Time** should always be verified regardless of trigger presets or predefined trigger configurations.
>
> Incorrect calibration will result in the ECU commanding ignition timing that does not match the actual crankshaft position, potentially causing poor engine performance or engine damage.