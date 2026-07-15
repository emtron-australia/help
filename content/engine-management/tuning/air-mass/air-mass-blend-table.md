---
title: "Air Mass Model Blend Table"
weight: 10
---

## Background

The **Air Mass Model** defines how the ECU calculates the mass of air entering the engine. The calculated air mass is then used to determine the required fuel mass to achieve the commanded **Lambda Target**, before being converted into an injector pulse width using the configured injector characteristics.

Different engine combinations may benefit from different air mass calculation strategies. Emtron provides several Air Mass Models to suit a wide range of applications.

### Options

| Value | Air Mass Model |
|--------:|----------------|
| **0** | Speed Density (MAP) |
| **1** | Speed Density (BAP) |
| **2** | Mass Air Flow (MAF) |
| **3** | Air Mass Modelled + Throttle Mass Flow (TMF) Blend |
| **4** | Speed Density (MAP) + Throttle Mass Flow (TMF) Blend |
| **5** | Emtron Air Mass Model (Custom) |


When **Air Mass Model 3, 4 or 5** is selected, the **Air Mass Blend Table** becomes active. The **Air Mass Blend Table** is a three-dimensional calibration table that determines the contribution of each selected Air Mass Model to the final calculated engine air mass.

The table output is expressed as a percentage, where:

- **0%** = 100% Primary Air Mass Model
- **100%** = 100% Secondary Air Mass Model
- **Intermediate values** proportionally blend the two Air Mass Models.

This allows the ECU to transition smoothly between two air mass calculation methods as engine operating conditions change, combining the advantages of each model over different areas of the operating range.

### Air Mass Modelled + Throttle Mass Flow (TMF) Blend (Option 3)

- **0.0%** → 100% Air Mass Modelled
- **50.0%** → Equal blend of both models
- **100.0%** → 100% Throttle Mass Flow (TMF)

### Speed Density (MAP) + Throttle Mass Flow (TMF) Blend (Option 4)

- **0.0%** → 100% Speed Density (MAP)
- **50.0%** → Equal blend of both models
- **100.0%** → 100% Throttle Mass Flow (TMF)

### Emtron Air Mass Model (Option 5)

- **0.0%** → 100% **Calculation 1
- **50.0%** → Equal blend of both models
- **100.0%** → 100% **Calculation 2


> **ℹ️ Note**
>
> The X and Y axes of the Air Mass Blend Table are fully configurable and may be assigned to any suitable ECU runtime. This allows the blend ratio to be tailored to the specific engine and application.