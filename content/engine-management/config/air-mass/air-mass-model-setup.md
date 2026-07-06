---
title: "Air Mass Model Setup"
---

#  Overview

The **Air Mass Model** defines how the ECU calculates the mass of air entering the engine. The calculated air mass is then used to determine the required fuel mass to achieve the commanded **Lambda Target**, before being converted into an injector pulse width using the configured injector characteristics.

Different engine combinations may benefit from different air mass calculation strategies. Emtron provides several Air Mass Models to suit a wide range of applications.

## Options

| Value | Air Mass Model |
|--------:|----------------|
| **0** | Speed Density (MAP) |
| **1** | Speed Density (BAP) |
| **2** | Mass Air Flow (MAF) |
| **3** | Air Mass Modelled + Throttle Mass Flow (TMF) Blend |
| **4** | Speed Density (MAP) + Throttle Mass Flow (TMF) Blend |
| **5** | Emtron Air Mass Model (Custom) |

## Air Mass Model Descriptions

### Speed Density (MAP)

Calculates engine air mass using the Ideal Gas Law based on **Manifold Absolute Pressure (MAP)**, **Charge Temperature**, **Engine Displacement**, and **Volumetric Efficiency (VE)**.
See here for more information: [MAP air mass](speed-density-map.md)

### Speed Density (BAP)

Calculates engine air mass using **Barometric Absolute Pressure (BAP)** instead of manifold pressure. This mode is typically used on naturally aspirated engines operating with individual throttle bodies (ITBs), where manifold pressure is not a reliable indicator of engine load.
See here for more information: [BAP air mass](speed-density-bap.md)

### Mass Air Flow (MAF)

Calculates engine air mass directly from the measured airflow provided by the configured Mass Air Flow sensor.
See here for more information: [MAF air mass](mass-air-flow-sensor-maf.md)

### Air Mass Modelled + Throttle Mass Flow (TMF) Blend

Blends the calculated **Air Mass Modelled** value with the **Throttle Mass Flow (TMF)** calculation using the **Air Mass Blend** table.

- **0% Blend** = 100% Air Mass Modelled
- **100% Blend** = 100% Throttle Mass Flow

The **TMF Correction Table** can be used to make small adjustments to the TMF calculation if required. In most applications, little or no correction should be necessary.
See here for more information: [TMF air mass](tmf-airmass-modelled-blend.md)

### Speed Density (MAP) + Throttle Mass Flow (TMF) Blend

Blends the **Speed Density (MAP)** calculation with **Throttle Mass Flow (TMF)** using the **Air Mass Blend** table.

- **0% Blend** = 100% Speed Density
- **100% Blend** = 100% Throttle Mass Flow

The **TMF Correction Table** can be used to make small adjustments to the TMF calculation if required. In most applications, little or no correction should be necessary.

### Emtron Air Mass Model (Custom)

Uses the Emtron custom air mass model.

--- 

## Air Mass Blend Table

When **Air Mass Model 3, 4 or 5** is selected, the **Air Mass Blend** table is enabled.

This table determines the contribution of each air mass model used to calculate the final engine air mass.

Intermediate values proportionally blend between the selected air mass models.

See here for more information on Air Mass Blend Table : [Air Mass Blend Table](../../tuning/fuel/air-mass-blend-table.md)