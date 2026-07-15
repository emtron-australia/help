---
title: "Air Mass Model Blend Table"
weight: 7
---

##  Overview

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

### Air Mass Model 3: Air Mass Modelled + Throttle Mass Flow (TMF) Blend**

- **0.0%** → 100% Air Mass Modelled
- **100.0%** → 100% Throttle Mass Flow (TMF)

---

### Air Mass Model 4: Speed Density (MAP) + Throttle Mass Flow (TMF) Blend**

- **0.0%** → 100% Speed Density (MAP)
- **100.0%** → 100% Throttle Mass Flow (TMF)

---

### Air Mass Model 5: Emtron Air Mass Model

- **0.0%** → 100% Air Mass Model Calculation 1
- **100.0%** → 100% Air Mass Model Calculation 2

The calculation methods used by Calculation 1 and Calculation 2 are configured from the [Emtron Air Mass Model](air-mass-model-emtron.md) setup page.

*ℹ️ Important Note: Air Mass Validation**
>
> When an Air Mass Blend mode is enabled, both air mass calculations continue to operate simultaneously regardless of the blend ratio currently being applied.
>
> This allows the individual air mass calculations to be logged and compared directly against one another.
>
> If both air mass models have been calibrated correctly, the calculated air mass values should closely overlay one another when operating under the same engine conditions.
>
> For example, when using **Speed Density + TMF Blend**, the calculated **Speed Density Air Mass** and **TMF Air Mass** should produce similar air mass values for a given engine speed and load condition.
>
> Significant differences between the two calculations typically indicate calibration errors within one of the air mass models, such as:
>
> - Volumetric Efficiency (VE) calibration errors
> - TMF model calibration errors
> - Throttle Body Area table errors
> - Charge Temperature model errors
> - Sensor scaling or sensor placement issues
>
> Comparing multiple air mass models in this manner provides a powerful method for validating the engine air mass calibration and improving overall model accuracy.
>
>Below is an example datalog illustrating the correlation between the calculated Speed Density and TMF air mass values under the same operating conditions.