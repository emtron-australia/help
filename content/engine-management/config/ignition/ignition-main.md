---
title: "Ignition Main"
---

## Overview 

![Image](</img/Ignition1.jpg>)

Ignition Main allows for configuring the ECU to suit the engine's ignition system.  

The following settings are configured in this menu item :

* Ignition Mode
* Ignition Firing Edge 
* Ignition Current Source 
* Ignition Advance Clamp 
* Ignition Retard Clamp 
* Ignition Spark Duration


> **⚠️ Warning**
>
> The ECU Ignition Output provides a TTL-level trigger signal intended to control an external ignitor or a coil with an integrated ignitor module. 
> 
> **Do not connect the ECU Ignition Output directly to a coil negative terminal.** Incorrect connection will result in damage to the ECU and/or ignition system.

---

## Ignition Mode

See [*Ignition Mode*](<ignition-mode.md>) for help.

---

## Ignition Firing Edge 

See [*Ignition Firing Edge*](<ignition-firing_edge.md>) for help.

---

## Ignition MBT Reference

See [*Ignition MBT Reference*](<ignition-mbt.md>) for help.

## Ignition Current Source

Controls the available current drive capability for all Ignition Channels 

The ECU provides two selectable ignition output current modes:
-	Standard Current Mode 35mA at 5V
-	High Current Mode 70mA at 8.2V

High Current mode provides increased drive capability for ignition systems that require a higher input current  (for example one ignition output driving two ignitors).

---

## Ignition Advance Clamp

Limits the maximum ignition advance that the ECU is permitted to command.

If the final ignition timing calculation exceeds this value, the ignition timing will be clamped to the configured advance limit.

This function can be used to protect the engine from excessive ignition advance due to calibration errors, sensor failures or unexpected operating conditions.

**Example:**

- Calculated Ignition Timing = 49°
- Ignition Advance Clamp = 45°

Final Ignition Timing = **45°**

---

## Ignition Retard Clamp


Limits the maximum ignition retard that the ECU is permitted to command.

If the final ignition timing calculation is retarded beyond this value, the ignition timing will be clamped to the configured retard limit.

This limit is applied to the final ignition timing calculation after all ignition corrections, compensations and modifiers have been applied.

Allowing sufficient ignition retard range is important for functions that intentionally reduce engine torque using ignition timing retard, for example traction control, launch control and anti-lag etc.

A typical value for this setting is **-45° BTDC**.

---

## Ignition Spark Duration

Specifies the minimum off-time after an ignition firing event before the ignition coil is permitted to begin charging again.

This ensures the coil remains de-energised long enough for the energy from the previous spark event to fully dissipate before the next dwell period begins.

This setting only applies when the ignition mode is configured as **Distributor** or **Twin Distributor**.

**Default:** 1.0 ms