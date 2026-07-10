---
title: "Dwell Tables"
weight: 30
---

## Overview

![Image](</img/Ignition12.jpg>)

![Image](</img/Ignition11.jpg>)

The Dwell Table 1 is where the coil charge time factor is set before discharging to the spark to the plug.

In general, a longer charge time will increase both the spark voltage and the heat produced by the coil.

Excessive charge times will cause the coil to fail

## Dwell Offset Table 1

![Image](</img/Ignition13.jpg>)

The Dwell Offset Table 1 is a user-defined offset table that allows ignition coil charge time (**dwell**) to be adjusted based on operating conditions or factors not directly accounted for by Dwell Table 1.

**Final Dwell = Dwell Table 1 + Dwell Offset Table 1**

> **ℹ️ Note**
>
> Dwell Table 1 supports a user-defined Dwell Offset Table. Dwell Table 2 does not have an associated offset table and uses the base dwell values defined within the table only.