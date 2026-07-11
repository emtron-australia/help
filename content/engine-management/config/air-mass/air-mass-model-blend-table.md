---
title: "Air Mass Model Blend Table"
hide_title: true
weight: 7
---

##  Air Mass Model Blend Table

The Air Mass Blend Table defines the contribution of two air mass calculations used to generate the final engine air mass value.

The table output is expressed as a percentage and determines the weighting applied to each air mass calculation based on the selected Air Mass Model configuration.

A value of:

- **0.0%** uses **100%** of the primary air mass calculation.
- **100.0%** uses **100%** of the secondary air mass calculation.
- **50.0%** uses an equal contribution from both calculations.

This allows the ECU to transition smoothly between two air mass calculation methods as engine operating conditions change, combining the advantages of each model over different areas of the engines operating range.

The Air Mass Blend Table is configured from:

`Tuning → Fuel → Air Mass Model Blend Table`

---

### Air Mass Model 3
**Air Mass Modelled + Throttle Mass Flow (TMF) Blend**

- **0.0%** → 100% Air Mass Modelled
- **100.0%** → 100% Throttle Mass Flow (TMF)

---

### Air Mass Model 4
**Speed Density (MAP) + Throttle Mass Flow (TMF) Blend**

- **0.0%** → 100% Speed Density (MAP)
- **100.0%** → 100% Throttle Mass Flow (TMF)

---

### Air Mass Model 5
**Emtron Air Mass Model**

- **0.0%** → 100% Air Mass Model Calculation 1
- **100.0%** → 100% Air Mass Model Calculation 2

The calculation methods used by Calculation 1 and Calculation 2 are configured from the [Emtron Air Mass Model](air-mass-model-emtron.md) setup page.