---
title: "Charge Temperature Estimation"
weight: 21
---
## Charge Temperature Estimate Table - Overview

The Charge Temperature Estimate table is used to calculate the estimated temperature of the air entering the combustion chamber. This estimated charge temperature is derived by blending the Inlet Air Temperature (IAT) sensor reading with the Engine Coolant Temperature (ECT).

Under many operating conditions, the measured intake air temperature does not accurately represent the temperature of the air charge entering the cylinder. Heat transfer from the intake manifold, cylinder head and engine components can significantly warm the intake charge, particularly during idle, low airflow and hot restart conditions.

The Charge Temperature Estimate table allows the ECU to compensate for these effects by blending the Intake Air Temperature with the Engine Coolant Temperature as a function of engine operating conditions.

### Table Values

Table values are expressed as a percentage and determine the contribution of the Engine Coolant Temperature to the calculated charge temperature.

| Value | Estimated Charge Temperature |
|--------:|------------------------------|
| **0%** | Charge Temperature = Intake Air Temperature |
| **50%** | Charge Temperature = Midway between Intake Air Temperature and Engine Coolant Temperature |
| **100%** | Charge Temperature = Engine Coolant Temperature 


> **ℹ️ Important**
>
> The Charge Temperature Estimate function uses only the configured **Inlet Air Temperature (IAT)** sensor and **Engine Coolant Temperature (ECT)** sensor to estimate the Charge Temperature.
>
> No other air temperature source is considered during this calculation. If multiple temperature sensors are configured within the ECU, only the **Inlet Air Temperature (IAT)** sensor is used for the air temperature component of the blend.

### 🔧 Tuning Guidelines

At **low engine speed and light engine load**, airflow through the intake system is relatively low. This allows heat from the engine to warm the intake manifold and incoming air, causing the actual charge temperature to be significantly higher than the measured Intake Air Temperature. Higher blend values are therefore typically required.

As **engine speed and engine load increase**, air mass flow through the intake system also increases. The higher airflow reduces heat transfer from the engine, allowing the Intake Air Temperature sensor to more accurately represent the temperature of the air entering the cylinder. Consequently, lower blend values are generally required.

For turbocharged and supercharged engines operating under boost, the Intake Air Temperature sensor typically provides an accurate measurement of the compressed intake charge. Little or no Engine Coolant Temperature blending is therefore normally required at higher engine loads.

### ℹ️ Notes

- The table axes are **Engine Speed (RPM)** and **Efficiency Calculation/ Manifold Pressure (kPa)**.
- Lower table values place greater reliance on the Intake Air Temperature sensor.
- Higher table values increase the influence of Engine Coolant Temperature to compensate for engine heat soak.
- Correct calibration improves air density estimation, resulting in more accurate fuel delivery and ignition calculations during idle, heat soak, hot restart and transient operating conditions.
<br>

![Image](</img/AAAA118.jpg>)

---

## Charge Temperature Offset Table

The Charge Temperature Offset table applies an absolute temperature correction to the calculated **Charge Temperature Estimate**. This table is used to compensate for the cooling effect of fuel evaporation, which is not directly accounted for by the Charge Temperature Estimate calculation.

Table values are expressed in **degrees Celsius (°C)** and are added to or subtracted from the calculated Charge Temperature Estimate. A **negative value** reduces the calculated Charge Temperature, while a **positive value** increases it.

### Typical Table Axes

- **X-Axis:** Stoichiometric Target (AFR)
- **Y-Axis:** Inlet Air Temperature (IAT)

### Operation

Different fuels absorb different amounts of heat as they evaporate. Fuels with a high latent heat of vaporisation, such as **Ethanol** and **Methanol**, can significantly cool the intake charge during the injection process.  By applying a negative Charge Temperature Offset, the ECU can compensate for this evaporative cooling effect, producing a more accurate estimate of the air charge temperature for fuel and ignition calculations.

For conventional gasoline fuels, little or no offset is typically required.

### 🔧 Tuning Guidelines

- Gasoline applications typically require minimal or no correction.
- Ethanol blends generally require a moderate negative offset.
- Methanol applications often require a larger negative offset due to its high evaporative cooling effect.
- Flex Fuel applications can use this table to progressively increase the cooling correction as ethanol content increases. Refer to the supplied sample calibration for an example implementation.<br>

> **ℹ️ Important**
>
> The Charge Temperature Offset is applied **after** the Charge Temperature Estimate has been calculated. It does not alter the Charge Temperature Estimate blending between the Inlet Air Temperature (IAT) and Engine Coolant Temperature (ECT); it simply adds or subtracts a fixed temperature offset from the final calculated Charge Temperature Estimate.

![Image](</img/AAAA120.jpg>)

---

## Charge Temperature Fuel Table

The Charge Temperature Fuel table applies a **percentage fuel correction** to the **Base Pulse Width**

The ECU uses the Charge Temperature Estimate during the air mass calculation to determine the amount of air entering the engine. The calculated air mass is then used to determine the required fuel delivery.

In some engine combinations, the calculated charge temperature may not perfectly model the actual cylinder charge temperature under all operating conditions. This can result in small fueling errors. The Charge Temperature Fuel table provides a means of applying a fine fuel correction to compensate for these residual errors.

### Table Values

Table values are expressed as a **percentage (%)**.

- **Positive values** increase the Base Pulse Width (richer).
- **Negative values** decrease the Base Pulse Width (leaner).
- **0%** applies no fuel correction.

### 🔧Tuning Notes

- In most applications, this table can be left at **0%** across the entire operating range.
- The **Charge Temperature Estimate** table should be calibrated first to provide the most accurate estimate of the cylinder charge temperature. Then adjust the Charge Temperate Fuel Table if required.
- Large corrections typically indicate that the Charge Temperature Estimate table should be reviewed before using this table for compensation.

> **ℹ️ Important**
>
> This table does **not** modify the calculated Charge Temperature. It applies a percentage correction to the **Base Pulse Width** after the Charge Temperature Estimate has been used during the ECU's air mass calculation.

---

## Charge Temperature Fuel Table Control

Enables or disables the **Charge Temperature  Fuel Table**.

When enabled, the **Charge Temperature Estimate Fuel Table** applies a percentage fuel correction to the **Base Pulse Width**.

When disabled, no fuel correction is applied and the Charge Temperature Fuel Table is ignored.

### Options

| Value | Mode |
|---------|---------|
| 0 | Disabled |
| 1 | Enabled |

> ### ⚠️ Notes
>
> In most applications, the **Charge Temperature Fuel Table** can remain disabled, as little or no additional fuel correction is typically required.