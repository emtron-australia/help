---
title: "Air Mass Compensation Table"
weight: 11
---

## Overview

## Air Mass Compensation Table

The Air Mass Compensation Table applies a percentage adjustment to the final calculated air mass.

This 3D table can be used to compensate for engine operating conditions that are not fully represented by the selected Air Mass Model, improving air mass accuracy across the operating range.

The compensation is applied after the primary air mass calculation has been completed.

- **0.0%** = No compensation applied
- **Positive values** = Increase calculated air mass
- **Negative values** = Decrease calculated air mass

> **ℹ️ Note**
>
> - The Air Mass Compensation Table should not be used to compensate for incorrect VE calibration or sensor scaling errors. These should be corrected at their source wherever possible.
>
> - The X and Y axes of the Air Mass Comp Table are fully configurable and may be assigned to any suitable ECU runtime. This allows the compensation to be tailored to the specific engine and application.