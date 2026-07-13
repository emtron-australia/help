---
title: "Emtron Air Mass Model"
weight: 7
---

## Overview

The **Emtron Air Mass Model** allows the ECU air mass calculation to be customised using one or two independent air mass calculation methods.

Most applications can be accurately modelled using the predefined Air Mass Models (**0 to 4**) and no further customisation is required. The **Emtron Air Mass Model** is intended for advanced applications requiring custom air mass calculations or blending between multiple air mass calculation methods.

Two independent air mass calculations are available:

- **Air Mass Model Calculation 1**
- **Air Mass Model Calculation 2**

Each calculation can be configured to use one of the following air mass calculation methods:

| Value | Calculation Method |
|-------:|--------------------|
| **0** | Off |
| **1** | Speed Density |
| **2** | Mass Air Flow Sensor (MAF) |
| **3** | Throttle Mass Flow (TMF) |
| **4** | Air Mass Modelled |

## Single Calculation Mode

If only a single air mass model is required, configure **Calculation 1** as required and set **Calculation 2** to **Off**.

In this configuration, the ECU uses the output of **Calculation 1** as the final engine air mass value.

## Dual Calculation Blend Mode

For applications requiring the advantages of multiple air mass calculation methods, both Calculation 1 and Calculation 2 may be enabled simultaneously.

When both calculations are enabled, the ECU uses the **Air Mass Model Blend Table** to determine the contribution of each calculation to the final air mass value.

- **0.0% Blend** = 100% Calculation 1
- **100.0% Blend** = 100% Calculation 2
- **50.0% Blend** = Equal contribution from Calculation 1 and Calculation 2

This allows the ECU to transition smoothly between two air mass calculation methods as engine operating conditions change, combining the advantages of each model over different areas of the operating range.

## Application Examnple: Speed Density + Throttle Mass Flow (TMF) 

A common application of the Emtron Air Mass Model is blending **Speed Density** and **Throttle Mass Flow (TMF)** calculations to take advantage of the strengths of each method.

At low **Pressure Ratios (PR)** across the throttle body, such as idle, cruise and part-throttle operation, **Throttle Mass Flow (TMF)** provides superior airflow estimation due to the strong relationship between throttle pressure drop and mass flow.

As the throttle opens and the pressure ratio across the throttle approaches **1.0**, the pressure drop across the throttle body becomes very small and the accuracy and sensitivity of TMF reduces. Under these conditions, **Speed Density** generally provides a more accurate estimation of cylinder air mass.

The **Air Mass Model Blend Table** can therefore be configured to:

- Use predominantly **TMF** at low pressure ratios.
- Progressively transition towards **Speed Density** as the pressure ratio approaches **1.0**.
- Operate using predominantly **Speed Density** during high load and wide open throttle operation.

This approach combines the excellent transient response characteristics of TMF with the steady-state accuracy of Speed Density.

 See here for more information[Air Mass Blend Table](air-mass-model-blend-table.md) 

---

### ⚠️ Important Notes on TMF Blending

- At throttle pressure ratios above approximately **0.9** (Post-Throttle Pressure / Pre-Throttle Pressure), the pressure differential across the throttle body becomes very small, reducing the resolution of the **Throttle Mass Flow (TMF)** calculation. This is why **TMF** must always be blended with an alternative air mass calculation method and cannot be used as the sole air mass model for engine operation.

- The **Air Mass Blend Table** should therefore progressively transition from **TMF** to an alternative air mass calculation method as the throttle pressure ratio approaches **1.0**.

- The **Air Mass Blend Table** forms part of the engine air mass model and must be finalised before tuning starts. 

- TMF tuning is accomplished by validating the [Throttle Body Area Table](<Newtopic77.md>)

- The **TMF Correction Table** can be used to make small adjustments to the TMF calculation if required. In most applications, little or no correction should be necessary.

 --- 

 ## Air Mass Bank Control

Air Mass Bank Control allows the ECU to independently calculate the engine air mass for each cylinder bank. This option is **only** available using the Emtron Air Mass Model.

When enabled, each bank operates as an independent air mass model and requires the appropriate sensors and inputs to support bank-specific airflow calculations.

Typical examples include:

- Independent inlet manifolds.
- Dual throttle body systems.
- Dual plenum engines.
- Engines equipped with bank specific pressure, temperature or airflow sensors.

> **ℹ️ Bank Control Notes**
>
> **1)** Engines with inlet manifolds connected by a balance tube or crossover passage may not exhibit true banked airflow behaviour. Any pressure differential between the manifolds will result in airflow transfer through the balance passage, reducing the effectiveness and accuracy of independent bank air mass calculations.
>
> **2)** Air Mass Bank Control is available for all Air Mass Model types.
>
> **2)** Ensure the **Bank Cylinder Setup** table is configured correctly before enabling Bank Mode.
>
> For more information refer to [Bank Cylinder Setup](../fuel/bank-cylinder-setup.md)

> **⚠️ Important**
>
> Air Mass Bank Control is **not** compatible with Staged Injection operation.