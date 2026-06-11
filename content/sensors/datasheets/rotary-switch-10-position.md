---
title: "10 Position Rotary Switch Datasheet"
weight: 6
---

## Description

The Emtron Rotary Switch is a high quality 10 position Rotary Switch that produces a stepped output voltage for each change in switch position. The output voltage will swing between ground and the supply. The switch is terminated with the reliable and environmentally sealed Deutsch DTM connector.

**Features**

- High quality single deck Grayhill rotary switch.
- Suitable for medium to high shock environments.
- Rotor contact: Brass, silver over nickel plate.
- Common ring: Brass, gold over silver over nickel plate.
- Max Supply Voltage: 5.00V to 20.00 Volts DC. {{% badge style="note" %}}NOTE{{% /badge %}} The supply **MUST** be regulated to generate a stable and consistent output voltage.
- Current supply: 4.5mA at 5.0V; 7.3mA at 8.0V
- The output voltage has linear stepping as the switch position changes.
- 5V Supply: Approximately 0.450V per position change (see calibration data below)
- 8V Supply: Approximately 0.720V per position change (see calibration data below)

## Calibration Data

| Output Voltage (V), 5.0V Supply | Rotary Position | &nbsp; | Output Voltage (V), 8.0V Supply | Rotary Position |
|:-------------------------------:|:---------------:|:------:|:-------------------------------:|:---------------:|
|             < 0.225             |      Fault      |        |             < 0.365             |      Fault      |
|              0.451              |        1        |        |              0.727              |        1        |
|              0.901              |        2        |        |              1.448              |        2        |
|              1.350              |        3        |        |              2.175              |        3        |
|              1.815              |        4        |        |              2.924              |        4        |
|              2.238              |        5        |        |              3.610              |        5        |
|              2.702              |        6        |        |              4.350              |        6        |
|              3.142              |        7        |        |              5.055              |        7        |
|              3.597              |        8        |        |              5.763              |        8        |
|              4.039              |        9        |        |              6.428              |        9        |
|              4.481              |       10        |        |              7.100              |       10        |
|             > 4.770             |      Fault      |        |             > 7.65              |      Fault      |

## Wiring

**Deutsch 3-Way Connector Pinout**

| Pin | Function  |
|:---:|-----------|
|  1  | 0V        |
|  2  | Signal    |
|  3  | 5V Supply |

Connect the Sensor 0V (Pin 1) to the ECU Sensor 0V Reference pin. **DO NOT** connect the 0V pin directly to the ECU ground or engine block.

## Ordering Information

| Product                                               | Part Number |
|-------------------------------------------------------|-------------|
| Emtron 10 Position Switch DTM (Actuator Type - Small) | 1816-10S    |
| Emtron 10 Position Switch DTM (Actuator Type - Large) | 1816-10L    |
