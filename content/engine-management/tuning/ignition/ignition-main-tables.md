---
title: "Ignition Main Tables"
weight: 1
---

The Ignition Table defines the base ignition timing commanded by the ECU based on engine operating conditions.

The table value represents the desired ignition timing in **degrees Before Top Dead Center (BTDC)**. The ECU uses engine speed (RPM) and load as the lookup axes to determine the base ignition advance value.

## Specifications

- **Units:** Degrees BTDC
- **Minimum Value:** -100.0 Deg
- **Maximum Value:** 100.0 Deg

## Function Behaviour

- Higher values command more ignition advance.
- Lower values command less ignition advance.
- A value of **0.0 Deg** represents no ignition advance before TDC.
- Negative ignition timing values represent ignition  after TDC (ATDC)

The final ignition timing delivered by the ECU may be modified by additional ignition corrections and compensations, including:

- Global Ignition Trim
- Coolant Temperature Compensation
- Intake Air Temperature Compensation
- Knock Control
- Idle Ignition Control
- Other configured ignition corrections


## ⚠️ Important - Ignition Timing Synchronisation

Before calibrating the Ignition Table, the ECU ignition timing must be synchronised with the actual engine crankshaft position.

To verify synchronisation:

1. Enable **Ignition Lock** and set a fixed ignition timing value (Ignition Lock Angle).
2. Use a timing light to measure the actual ignition timing at the engine.
3. Compare the timing light reading with the configured **Ignition Lock Angle**.
4. Adjust the **Crank Index Offset** until the timing light reading matches the Ignition Lock Angle. This test should be completed at idle.
5. Next, verify the ignition timing as engine speed is increased while adjusting the **Ignition Delay Time**. Correct **Ignition Delay Time** calibration ensures the commanded ignition timing accurately matches the actual crankshaft position across the complete engine speed range.

Adjustment guidelines:
 - If the measured ignition timing **retards as engine speed increases**, increase the **Ignition Delay Time** value.
- If the measured ignition timing **advances as engine speed increases**, decrease the **Ignition Delay Time** value.


Once synchronised, disable **Ignition Lock** and the ECU will accurately command the ignition timing values defined by the Ignition Table and associated ignition corrections.

---

## ⚠️ Warning
Incorrect ignition synchronisation will result in the ECU commanding ignition timing that does not match the actual engine timing, which can lead to poor engine performance or engine damage.