---
title: "Global Trim"
weight: 2
---

This function applies a global ignition timing trim across all ignition channels.

The configured trim value is added to the final calculated ignition timing after all other ignition corrections and compensations have been applied. The trim is applied uniformly across all operating conditions and is independent of engine speed (RPM) and load.

## Specifications

- **Units:** Deg
- **Minimum Value:** -100.0 Deg
- **Maximum Value:** +100.0 Deg

## Function Behaviour

- Positive values advance ignition timing.
- Negative values retard ignition timing.
- A value of **0.0 Deg** applies no global ignition correction.

## ⚠️ Notes

This function is intended as a quick global adjustment to the overall ignition timing.

For permanent calibration changes, adjust the appropriate ignition tables or compensation maps rather than relying on the global ignition trim.
