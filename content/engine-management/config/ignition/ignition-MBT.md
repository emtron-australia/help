---
title: "Ignition MBT Reference"
weight: 3
---
 
## Overview

Selects the ignition table that represents **MBT (Minimum Spark Advance for Best Torque)**.

MBT is defined as the ignition timing that produces the maximum engine torque for a given engine speed and load operating point. Additional ignition advance beyond MBT will typically provide little or no increase in torque, while ignition timing retarded from MBT will result in a reduction in engine torque output.

The selected MBT reference table is used by the ECU Engine Torque Model as the reference for maximum available engine torque.

> ***ℹ️ Why is MBT Required?***
>
> The ECU Engine Torque Model requires a reference for the ignition timing that produces maximum engine torque at each engine speed and load point.
>
> By comparing the active ignition timing against the MBT reference table, the ECU can determine when the engine is operating below peak torque due to ignition retard and apply the appropriate correction to the calculated engine torque.


The ECU continuously calculates the difference between the active ignition timing and the configured MBT reference table:

```text
Ignition MBT Offset = Active Ignition Timing - MBT Reference Timing
```

Where:

- **0° Offset** = Engine operating at MBT torque.
- **Negative Offset** = Ignition timing is retarded from MBT and engine torque is reduced.
- **Positive Offset** = Ignition timing is advanced beyond MBT and will typically result in little or no additional engine torque.

**When the MBT Offset becomes negative, the active ignition timing is retarded relative to the MBT reference timing. As a result, the ECU determines that the engine is operating below its maximum torque potential and applies a corresponding reduction to the Engine Torque Model.**

## Options

| Value | Mode |
|--------:|------|
| **0** | Off |
| **1** | Table 1 |
| **2** | Table 2 |

### Off

Disables MBT referencing. The Engine Torque Model assumes no torque reduction due to ignition retard.

### Table 1

Uses **Ignition Table 1** as the MBT reference table.

### Table 2

Uses **Ignition Table 2** as the MBT reference table.

> **ℹ️ Note**
>
> The MBT reference table should represent the ignition timing required to achieve maximum engine torque.
>
> If dual ignition tables are used for different fuel types, such as Petrol and E85, the ignition table representing the highest achievable engine torque should generally be selected as the MBT reference table.
>
> Since E85 typically requires greater ignition advance to achieve MBT than an equivalent Petrol calibration, the E85 ignition table will often be the preferred MBT reference.