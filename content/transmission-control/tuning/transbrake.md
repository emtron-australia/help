---
title: "Transbrake"
---

>[!WARNING] Transbrake is a motorsport orientated function can lead to transmission and/or other driveline component damage if not used correctly.

The Transbrake function locks up the transmission so that engine load can be applied against the torque converter for staging and launching. It works by applying additional clutches along with the clutches required for the current forward gear. Typically this is achieved by engaging Reverse and First gear at the same time, effectively binding the transmission.

## Transbrake Mode
There are two modes of operation:
 - **Forward + Reverse**: Engages the clutches for reverse AND the current forward gear (eg: 1st).
  - **Clutch Select Table**: User definable clutch selection to be applied in combination with the current forward gear's clutches.

## Activation
The Tranbrake is activated by the `Transbrake Switch` input. The switch input is configured separately in Input Config.

## Lockouts
Any lockout condition will result in the Transbrake being disabled.

**Output Shaft Speed Max**
If the output shaft speed exceeds this value, the Transbrake is disabled.

**Gear Max**
The transbrake will be disabled above this gear.

**User Enable**
A User Function can be selected to act as a lockout. The selected User Function must be ON or the Transbrake will be disabled.

## Bump
Bump is activated by the `Bump Switch` input. The switch input is configured separately in Input Config.