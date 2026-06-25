---
title: "Lambda Target Table Control"
weight: 7
---

## Table Control Setup

This control determines whether a single target table is used or whether Z-axis blending is enabled between two calibration tables.

## Available Options

| Value | Mode |
|------|----------------------------|
| 0 | OFF |
| 1 | ON - Table 1 |
| 2 | ON - Table 2 |
| 3 | Not Available |
| 4 | Not Available |
| 5 | Cal Slot |
| 6 | ON - Z-Axis |

## Mode Descriptions

### OFF (0)
Disables the Lambda Target table input

---

### ON - Table 1 (1)

Uses **Table 1 only** for Lambda Target calculation.

Typically represents the base calibration (e.g. Petrol Lambda Target strategy).

---

### ON - Table 2 (2)
Uses **Table 2 only** for Lambda Target calculation.

Typically represents an alternative calibration strategy (e.g. Methanol or high-load enrichment strategy).

---

### Not Available (3–4)
Reserved for future functionality and should not be selected.

---

## Cal Slot (5)
Enables **real-time switching of the active Lambda Target table via calibration slot selection**.

This allows the ECU to switch between pre-defined calibration sets without modifying the Table Control setting. See Tuning view -> Cal Control menu

Example application:
- **Table 1 = Petrol Lambda Target calibration**
- **Table 2 = Methanol Lambda Target calibration**

The active table can be switched in real time depending on:
- Fuel type
- Engine mode
- Test or development configuration

This mode is commonly used for:
- Rapid calibration comparison
- Track-side strategy changes
- Different Fuel system 


---

### ON - Z-Axis (6)
Enables **Z-axis blending between Table 1 and Table 2**.

The ECU interpolates between both tables based on the configured Z-axis input (typically Ethanol Content %), producing a blended fuel value.

- 0% Z-axis → 100% Table 1
- 100% Z-axis → 100% Table 2
- Intermediate values → linear interpolation between both tables


## Z-Axis Blended (Dual Table Interpolation)

The ECU supports a Z-axis blending strategy that allows lambda targets to be interpolated between two tables based on a third operating axis.

## Concept Overview

Two base Lambda Target tables are defined:

- **Table 1 (Reference Fuel – Petrol)**  
  Defines Lambda Targets for standard petrol operation.

- **Table 2 (Alternative Fuel – High Oxygen Content Fuel)**  
  Defines Lambda Targets for high ethanol or methanol operation.

A Z-axis input (typically fuel composition such as ethanol content) is used to interpolate between the two tables.


This example shows the blend between Table 1 and Table 1 spanned on the Z-axis using Ethanol content

![Image](</img/Z Axis29.jpg>)

