---
title: "Global Fuel Trim"
weight: 5
---

This function applies a global fuel trim to the base calibration.

It provides a percentage-based adjustment to injector pulse width, allowing the overall air-fuel ratio to be shifted richer or leaner without modifying individual fuel tables.

The trim is applied uniformly across all operating conditions and is independent of engine speed (RPM) and load.

## Specifications

- **Units:** %
- **Minimum Value:** -50.0%
- **Maximum Value:** +50.0%

## Function Behaviour

- Positive values increase fuel delivery (richens mixture)
- Negative values decrease fuel delivery (leans mixture)
- Applied globally to all fuel calculations derived from the base calibration

## ⚠️ Notes

This function is intended as a calibration and setup aid only.

It allows for a rapid changes to the overall mixture and works independent of RPM and load.

This trim should be returned to 0% before final tuning to ensure the base fuel model is accurate and consistent.
