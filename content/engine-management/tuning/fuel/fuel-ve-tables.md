---
title: "VE Tables"
weight: 1
---

## Overview

The fueling calculations used by Emtron are based on an **Air Mass** per cycle which is then converted to a Fuel Mass based on the requested lambda target. This is true whether the system is using directly measuring airflow from the air mass meter, or calculated air mass from speed density or throttle mass flow (TMF)

The Volumetric Efficiency (VE) table is used when the **Air Mass Model** is configured for **Speed Density**.

In Speed Density mode, the ECU does not directly measure the engine airflow. Instead, it calculates the air mass entering each cylinder using the **Ideal Gas Law** based on:

- Engine Displacement
- Manifold Absolute Pressure (MAP)
- Charge Temperature
- Volumetric Efficiency (VE)

The calculated **Air Mass per Engine Cycle** is then used to determine the required **Fuel Mass** based on the commanded **Lambda Target**. The ECU then converts the required fuel mass into an injector pulse width using the configured injector characteristics.

>**ℹ️ Note**
>
> The ECU supports one or two **Volumetric Efficiency (VE)** tables. The active table configuration is selected using the **VE Table Control** setting, which determines whether a single VE table is used or whether blending between two VE tables is enabled (Z- Axis). 

--- 
## Volumetric Efficiency (VE) Table

![Image](</img/AAAA72.jpg>)

The Volumetric Efficiency (VE) table represents the engine's ability to fill its cylinders with air under varying engine speeds and loads.  Volumetric Efficiency (VE) is expressed as a percentage and describes the ratio of the actual **air mass** trapped within the cylinder to the theoretical **air mass** that would occupy the engine's swept cylinder volume under standard atmospheric conditions.

A higher VE indicates the engine is filling its cylinders more efficiently, requiring more fuel to maintain the commanded air-fuel ratio.

Most engines typically operate below **100% VE**.

> **ℹ️ Note**
>
> Due to intake and exhaust tuning, pressure wave dynamics and scavenging effects, a well-designed naturally aspirated engine can exceed **100% VE** over parts of its operating range.

--- 

## Tuning

Before calibrating the **VE** table(s), the **Lambda Target** table(s) should first be configured with the desired lambda or air-fuel ratio for each operating condition.

Once the Lambda Target table(s) have been calibrated, the **VE** table is adjusted until the measured lambda matches the commanded Lambda Target. The two tables are intrinsically linked, the **Lambda Target** defines the desired result, while the **VE** table determines the amount of fuel required to achieve it.

For more information, refer to the [Lambda Target Tables](<lambda-target-tables.md>).

--- 
## Typical Values

Typical VE values vary depending on engine design and operating conditions.

- Idle: **35–40%**
- Engines at full load: **80–100%**
- High-performance naturally aspirated engines: **90–110%** (typical peak)

![Image](</img/VE Table.jpg>)
The above Mitsubishi EVO IX VE table example shows the typical range of values         

### 🔧Tuning Notes
- The **VE** table is calibrated by adjusting its values until the measured lambda matches the commanded **Lambda Target** across the engine's operating range.
- This process is most efficient when the ECU is configured with a **Wideband Lambda** input, allowing the measured lambda to be compared directly with the commanded target.
- Once the VE table has been correctly calibrated, the engine's volumetric efficiency model has been established, providing an accurate basis for fuel delivery calculations.
- The objective is to minimise the error between the **measured lambda** and the **Lambda Target** under all operating conditions.
- A simple method of validating the VE calibration is to change the **Lambda Target** at a specific operating point. If the VE table and injector characterization have been calibrated correctly, the measured lambda should follow the new Lambda Target without requiring further VE adjustments.
- If changes to the VE table are required to achieve the new Lambda Target, this may indicate an error in the VE calibration or the configured injector characterization (injector flow, deadtime, or non-linearity).
- When **Closed Loop Lambda Control** is enabled, the VE table provides the feed-forward fuel calculation, while the closed loop controller applies only the corrections necessary to eliminate any remaining fueling error.

---

##  VE Table Control 

This control determines whether a single target table is used or whether Z-axis blending is enabled between two calibration tables.

## Available Options

| Value | Mode |
|------|----------------------------|
| 0 | OFF |
| 1 | ON - Table 1 |
| 2 | ON - Table 2 |
| 3 | Not Available |
| 4 | Not Available |
| 5 | Cal Slot |
| 6 | ON - Z-Axis |

## Mode Descriptions

### OFF (0)
Disables the Lambda Target table input


### ON - Table 1 (1)

Uses **VE Table 1 only** for air masss speed density model

### ON - Table 2 (2)
Uses **VE Table 2 only** for air masss speed density model

### Not Available (3–4)
Reserved for future functionality and should not be selected.

### Cal Slot (5)
Enables **real-time switching of the Fuel VE tables via calibration slot selection**.

This allows the ECU to switch between pre-defined calibration sets without modifying the Table Control setting. See Tuning view -> Cal Control menu

 Dual VE tables are particularly useful for engines with significantly different airflow characteristics between operating modes. For example, on a **Honda VTEC** engine, one VE table can be calibrated for the low-lift cam profile and the second VE table calibrated for the high-lift cam profile. Once both tables have been tuned across the full operating range, the VTEC changeover point can be adjusted to determine the optimum switching RPM without requiring the VE calibration to be retuned.> 

Example application:
- **Table 1 = VTEC Low-lift  Cam**
- **Table 1 = VTEC high-lift  Cam**

The active table can be switched in real time based on RPM or a user defined switch condition

### ON - Z-Axis (6)
The Z-Axis enables a user-defined third axis used to swap or blend between **VE Table 1** and **VE Table 2**.

The ECU performs real-time linear interpolation between both VE tables based on the configured Z-Axis input. This allows fuel delivery to be dynamically adjusted across a third operating dimension, which can be spanned using any available runtime parameter within the ECU.

- 0% Z-axis → 100% Table 1
- 100% Z-axis → 100% Table 2
- Intermediate values → linear interpolation between both tables

## Example.

With an engine operating at 85% VE and has a known Charge Temperature and Manifold Pressure, the ECUs calculates an **Air Mass** per Induction of 0.789 grams.  To achieve at Lambda target of 0.85 (12.50 AFR petrol) the corresponding fuel mass needs to be 0.06312 grams. With a known Injector Size in cc/min and Fuel Density (g/ml) the injector mass flow can be determined. Lets use 10.73 grams/sec. 

> **ℹ️ Note** Other factors also affect the injector mass flow. When enabled the ECU monitors the differential pressure across the injector and corrects if it moves away from the nominal static pressure. It does this using "Bernoulli's equation"  which is a square root law.

Knowing that our fuel injector has a static flow rate of 10.73 grams per second, we divide that into our fuel mass and arrive at a injector pulsewidth value of  5.704 ms. However, the injector cannot just be opened for this time to achieve the calculated Fuel Mass. The **Dynamic Characteristics** of the fuel injector must be used. This includes injector deadtime and low pulse width non-linearities. 

The Graph below of Theoretical vs Actual flow explains this better. The Blue line is the Raw/Theoretical Flow and the Red line is the actual Injector Flow .. note the large error. At 5.7ms the actual fuel mass produced by the injector is 0.0587g instead of the calculated 0.06312 g.  This is only 93% of the fuel requested.

![Image](</img/Inj Deadime Pic13.jpg>)

The flow error is caused by an offset that exists between the actual injector flow (Red line) and the theoretical flow (Blue line). This offset exists on all injectors and must be included for the fuel calculation to be accurate.  As the offset is constant across the "majority" of the injector operating range, we can correct for it by adding it to our final injector pulsewidth. This offset error/flow error is known as **Injector Deadtime.** The ECUs uses a 3D deadtime table spanned on Battery Voltage and Differential Fuel Pressure. See section [Injector Deadtime Table](<injector-deadtime-table1.md>) for more information.

Once the offset is corrected the Theoretical vs Actual flow graph looks like:

![Image](</img/Inj Deadime Pic2.jpg>)

The correction across "most" of the operating range is complete and we can expect the ECU calculated pulsewidth to deliver the requested mass flow. However the range at low pulsewidth still has errors i.e there is a difference between the theoretical and actual pulse with. This is known as the "non linear operating range" of the injector and the graph below has this area zoomed in.

![Image](</img/Inj Deadime Pic3.jpg>)

Below 2 ms we have a situation similar to our initial conditions where there was an offset between the actual flow, and theoretical flow of the injector. Unlike the offset within the linear operating range of the injector, this is not constant, and cannot be corrected for with a single value.

The solution is the low pulse adder table which uses offset values that vary with pulsewidth, correcting the lower non linear operating range of the injector. More information can be found [Injector Low Pulsewidth Linearisation](<injector-low-pulsewidth-linearisati.md>)

With the addition of these values the ECU can achieve nearly perfect fueling down to practically zero flow, and the ECU can do its job of calculating and commanding the correct air fuel ratio under all operating conditions.