---
title: "MAP Sensor 1.0 Bar Datasheet"
weight: 1
---

**Rev 1.1**

## 1.0 Description

The Emtron 1.0 Bar MAP Sensor uses a state-of-the-art piezoresistive transducer from NXP Semiconductors. It is highly accurate, providing a high level analog output signal that is proportional to the applied pressure.

### 1.1 Features

- Genuine NXP Sensor
- Pressure Range: 15kPa to 115kPa
- Supply Voltage: 4.75 to 5.25 Volts DC
- Current Supply 6.0mA
- Protective Silicone Gel prevents sensor damage from airborne contaminates like oil, petrol and methanol.
- Fully calibrated and temperature compensated from -40 DegC to +125 DegC
- Response time 1ms
- Compact Design
- Stainless Steel 303 body for durability then coated in black nickel for superior abrasion resistance
- Fully potted for a waterproof seal and resistance to shock and vibration
- 1/8 NPT Thread
- Deutsch 3 Way Connector (mating end also supplied)

### 1.2 Dimensions

{{< figure src="/img/sensors-datasheets/map-sensor-1-bar/dimensions.png" caption="MAP Sensor 1.0 Bar dimensions." >}}

## 2.2 Installation

Fit to a prepared 1/8 NPT tapped port. Screw the MAP sensor finger tight into the port then tighten with a spanner 1.5 to 3.0 turns past finger tight. Do not exceed 16Nm (12 lbs/ft).

An anaerobic thread sealant may be used sparingly. Avoid excessive use to prevent sensor blockage/failure.

{{% badge style="warning" %}}WARNING{{% /badge %}} Do not back off an installed MAP sensor to achieve a desired alignment. Loosening the installed MAP sensor will compromise the seal and lead to potential leakage or failure.

## 2.3 Wiring

**Deutsch 3 Way Connector Pinout**

| Pin | Function      |
|:---:|---------------|
| 1   | Sensor 0V ref |
| 2   | Signal        |
| 3   | 5.0V          |

1. Connect the MAP Sensor 0V (Pin 1) to the ECU Sensor 0V Reference pin (Sensor Ground). **DO NOT** connect the MAP Sensor 0V directly to the ECU ground or engine block.
2. Connect the MAP Sensor Signal to an available Analog Voltage input or Digital input.
3. Connect the MAP Sensor 5.0V to an available 5.0V VRef source which can be referenced in the Emtune software for ratiometric correction.

## 2.4 Calibration

**Transfer Function:** Vout = Sensor-Supply × (0.009 × P − 0.095)

*Sensor-Supply allows for ratiometric correction. Set to 5.000V when not required.*

- P = 115kPa: Vout = 5.00 × (0.009 × 115.0 − 0.095) = 4.700V
- P = 15.0kPa: Vout = 5.00 × (0.009 × 15.0 − 0.095) = 0.200V

| Voltage (V) | Pressure (kPa) |
|-------------|----------------|
| 0.200       | 15.0           |
| 4.700       | 115.0          |

This calibration option is available from Emtune. Select the **"Emtron 1.0 Bar"** option from the Predefined Calibration list on any Analog Channel Input.

**Filter Settings**

- Filter Setting Minimum = 0 (OFF)
- Filter Setting Maximum = 50
- Recommended Filter Range = 15 - 25

{{% badge style="note" %}}NB{{% /badge %}} This setting is heavily dependent on engine setup and the stability of the MAP signal at idle. Engines with large overlapping camshafts, for example, will most likely need a larger filter value to achieve a more stable MAP signal.

## 2.5 Ordering Information

| Product                    | Part Number |
|----------------------------|-------------|
| Emtron MAP Sensor 1.0 Bar  | 1301-10A    |
