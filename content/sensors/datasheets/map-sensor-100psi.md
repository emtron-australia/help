---
title: "MAP Sensor 100psi Datasheet"
weight: 3
---

**Rev 1.0**

## 1.0 Description

The Emtron 100psi MAP Sensor uses a state-of-the-art piezoresistive transducer from Bourns Semiconductors. It is highly accurate, providing a high level analog output signal that is proportional to the applied pressure.

### 1.1 Features

- Genuine Bourns BPX130 series sensor
- Pressure Range: 0kPa to 689.5kPa
- Supply Voltage: 4.50 to 5.50 Volts DC
- Current Supply 10.0mA
- Compatible with harsh media – air, water, oil, petrol and methanol.
- Fully calibrated and temperature compensated from -40 DegC to +150 DegC
- Response time 1ms
- Compact Design
- Stainless Steel 303 body for durability then coated in black nickel for superior abrasion resistance
- Fully potted for a waterproof seal and resistance to shock and vibration
- 1/8 NPT Thread
- Deutsch 3 Way Connector (mating end also supplied)

### 1.2 Dimensions

{{< figure src="/img/sensors-datasheets/map-sensor-100psi/dimensions.png" caption="MAP Sensor 100psi dimensions." >}}

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
3. Connect the MAP Sensor 5.0V to an available 5.0V VRef source which will be referenced for ratiometric correction in the Emtune software.

## 2.4 Calibration

*Sensor-Supply allows for ratiometric correction. Set to 5.000V when not required.* The output is linear between the endpoints below.

| Voltage (V) | Pressure (kPa) |
|-------------|----------------|
| 0.500       | 0              |
| 4.500       | 689.5          |

This calibration option is available from Emtune. Select the **"Emtron 100psi"** option from the Predefined Calibration list on any Analog Channel Input.

**Filter Settings**

- Filter Setting Minimum = 0 (OFF)
- Filter Setting Maximum = 50
- Recommended Filter Range = 15 - 25

{{% badge style="note" %}}NB{{% /badge %}} This setting is heavily dependent on engine setup and the stability of the MAP signal at idle. Engines with large overlapping camshafts, for example, will most likely need a larger filter value to achieve a more stable MAP signal.

## 2.5 Ordering Information

| Product                   | Part Number |
|---------------------------|-------------|
| Emtron MAP Sensor 100 Psi | 1606-100A   |
