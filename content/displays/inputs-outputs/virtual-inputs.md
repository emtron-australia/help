---
title: "Virtual Inputs"
description: "Process and calibrate channel values with filtering."
weight: 5
---

**Inputs/Outputs → Virtual Inputs**

Virtual inputs take an existing channel value, optionally filter and calibrate it, and write the result to a new output channel. They do not read from physical hardware directly.

## Configuration

For each virtual input:

| Setting | Description |
|---------|-------------|
| Input Channel | Source channel to read |
| Output Channel | Destination channel to write |
| Filter | Optional moving-average filter |
| Calibration Table | Optional lookup table to scale or convert the input |

## Use Cases

- Smooth a noisy sensor reading before displaying it on a gauge
- Apply a custom calibration curve to a CAN-received value
- Create a derived channel from an existing one without using the full [Math](../functions/maths) function

> **Note:** Only one function should write to a given output channel. Do not assign the same output channel to multiple virtual inputs or other output functions.