---
title: "Mitsubishi EVO 4-8"
weight: 0
---

**Mitsubishi EVO 4-8 Plug-in ECU User Manual**

## 1.0 Introduction

The Mitsubishi EVO 4-8 ECU is designed to be plugged into the OEM harness to allow for a true "Plug and Play" install. The system is based on the KV Series Motorsport ECU, so all the same features are available excluding any limitations based around the OEM connector system. An Expansion port is included giving access to unused Input channels. CAN Bus 1 is also available providing additional I/O expandability.

## 2.0 Plugin Features

**General**

- KV8 ECU based platform — Dual 100MHz processors, 32MB ECU logging memory, over 1000 logging channels, 1Hz to 500Hz logging rate
- Aluminium 6061 Grade CNC billet enclosure
- Compatible with all Emtron proven motorsport features (Launch Control, Rolling Launch, Anti-Lag, Traction Control)
- Upgradeable to run the Emtron fuel model through installation of a flex meter, fuel temperature and fuel pressure sensor
- Idle speed closed loop control using DBW with advanced Throttle Mass Flow (TMF) airflow calculations
- Knock control with high speed digital filtering for each cylinder using the OEM sensor with selectable centre frequency and bandwidth
- Pre-configured calibration file loaded providing a comprehensive tuning platform
- Input Expansion Capabilities through DTM connector: 3× User Analog Volt Inputs (Fuel Temperature, Fuel Pressure, Inlet Temperature), 1× User Digital Input (Flex Meter Input and switch inputs), 2× User Analog Inputs
- Emtune software for tuning and data analysis

**Communications:** CAN 2.0B Bus 1 (User CAN Bus for I/O expansion — Lambda, EGT); High Speed Ethernet 100Mbps for tuning software connection.

**Operating Temperature:** -30 to 85°C (-22 to 185°F)

**Physical:** Enclosure Size 160 × 162 × 38 mm, 890g

## 3.0 Installation

### 3.1 Expansion Port

The ECU's input capabilities can be expanded using the expansion connection, which is a male DTM 12 Way. These additional inputs can be connected to any sensor, but the recommended sensors are indicated in brackets.

{{< figure src="/img/mitsubishi-evo-4-8/expansion-port.jpeg" caption="EVO 4-8 expansion port connector (DTM 12-way)." >}}

**Table 3.0 — Expansion Port Pinout (DTM06-12SA)**

| Pin | Function                                                            |
|:---:|---------------------------------------------------------------------|
|  1  | Analog Sensor 0V Reference                                          |
|  2  | 5V Vref2 Supply                                                     |
|  3  | AN 8 (e.g. Fuel Temp or Inlet Temp)                                 |
|  4  | AN 11 (e.g. Fuel Temp or Inlet Temp)                                |
|  5  | AN 12 (e.g. Fuel Pressure)                                          |
|  6  | DI 6 (e.g. Ethanol Content Sensor)                                  |
|  7  | DI 13                                                               |
|  8  | DI 14                                                               |
|  9  | 14V Out Protected (e.g. ELC2 Power Supply). Post ECU SN 2700 only.  |
| 10  | ECU Ground (e.g. ELC2 or E85 Sensor Ground). Post ECU SN 2700 only. |
| 11  | CAN 1 Hi                                                            |
| 12  | CAN 1 Lo                                                            |

### 3.2 CAN Bus 1 Wiring

The ECU CAN Bus 1 is reserved for Emtron CAN Bus devices, expanding the IO capability of the ECU. The following devices can be connected: ELC1/2 (Lambda to CAN), ETC4/ETC8M (Thermocouple to CAN), EIC10/EIC16M (Input to CAN). All these CAN devices share a common power, ground and CAN pinout using a 4-way DTM.

**Table 3.1 — CAN Device Power and CAN Deutsch Connector Pinout**

| Pin | Function   | Wire Colour |
|:---:|------------|-------------|
|  1  | Ground     | BLACK       |
|  2  | CAN Lo     | GREEN       |
|  3  | CAN Hi     | YELLOW      |
|  4  | 12V Supply | RED         |

To help with installation time, each CAN Device pin can be directly connected into the ECU IO Expansion port:

**Table 3.2 — IO Expansion to CAN Device wiring**

| Name     | ECU IO Expansion 12-Way DTM | CAN Device 4-Way DTM |
|----------|:---------------------------:|:--------------------:|
| Ground   |            Pin 8            |        Pin 1         |
| CAN 1 Lo |           Pin 12            |        Pin 2         |
| CAN 1 Hi |           Pin 11            |        Pin 3         |
| Power    |            Pin 7            |        Pin 4         |

Standard CAN bus precautions apply — twisted pair (min one twist per 40mm), minimise connectors, 120 ohm 0.25W termination at each END, stub length < 0.3m (ISO 11898). All Emtron CAN devices have no on-board terminating resistor, allowing them to be wired at any position on the Bus.

### 3.3 Sensor Wiring

**5V VRef2 Sensor Supply (Pin 2 of Expansion port)** — A 250mA 5V output designed to supply automotive sensors.

**Sensor 0V Reference (Pin 1 of Expansion port)** — This pin should be connected directly to the 0V (Ground) pin on any low current analog sensor, for example Pressure or Temperature.

- **DO NOT** connect the 0V Reference pin directly to the Engine Block or ECU Ground. This is a dedicated and specialised 0V/ground output for analog sensors.
- **DO NOT** connect frequency-based sensor grounds to the 0V Reference pin; for example, an Ethanol content sensor. Use Pin 8 (Ground) in the Expansion port.

{{< figure src="/img/mitsubishi-evo-4-8/sensor-0v-correct.jpeg" caption="Figure 3.3 — Correct Pressure Sensor 0V wiring (direct to the Sensor 0V Reference)." >}}
{{< figure src="/img/mitsubishi-evo-4-8/sensor-0v-incorrect.png" caption="Figure 3.4 — Incorrect Pressure Sensor 0V wiring." >}}

### 3.4 Ethanol Content Sensor Wiring

An Ethanol Content sensor can be wired into the ECU using the Expansion port. The following channel assignment is recommended for the GM sensor:

| GM Sensor Pinout | Expansion Port        | Description                             |
|:----------------:|-----------------------|-----------------------------------------|
|      Pin 1       | Pin 9 — 14V Protected | Supply, 8V or 14V                       |
|      Pin 2       | Pin 10 — ECU Ground   | Ground                                  |
|      Pin 3       | Pin 6 — DI 6          | Output. Temperature and Ethanol Content |

{{% badge style="note" %}}NOTE{{% /badge %}} **DO NOT** connect the Ethanol Content sensor ground to the "Analog Sensor 0V Reference" — use the ECU Ground from Pin 10. The Ethanol sensor produces a frequency-based output; suitable ECU channels are DI 1-8.

| Description         | Calibration                             |
|---------------------|-----------------------------------------|
| Ethanol Content (%) | 50Hz = 0% Ethanol, 150Hz = 100% Ethanol |
| Fuel Temperature    | 1ms = -40°C, 5ms = 125°C                |

To configure the ECU for this sensor, select the Ethanol Sensor Input Source to DI6. The ECU will automatically decode the Ethanol Content and Fuel Temperature. Once assigned, more settings become available in the **Tuning View → Engine Functions** menu.

## 4.0 ECU Channel Assignment

### Injection

| ECU Channel    | Function              |
|----------------|-----------------------|
| Injection 1-4  | Fuel Injector Cyl 1-4 |
| Injection 5    | Rear Lambda Heater    |
| Injection 6    | Front Lambda Heater   |
| Injection 7    | A/C Fan Relay (High)  |
| Injection 8    | CE Light              |
| Injection 9-12 | Not Used              |

### Ignition

| ECU Channel   | Function                |
|---------------|-------------------------|
| Ignition 1    | Ignition Cylinder 1/4   |
| Ignition 2    | Ignition Cylinder 2/3   |
| Ignition 3    | A/C Fan Relay (Low)     |
| Ignition 4    | IC Spray Lamp           |
| Ignition 5    | Alternator Load Control |
| Ignition 6    | Fuel Pump Relay         |
| Ignition 7    | Fuel Pump Speed Relay   |
| Ignition 8    | A/C Clutch Relay        |
| Ignition 9-12 | Not Used                |

### Analog Inputs

| ECU Channel                    | Function                     |
|--------------------------------|------------------------------|
| Analog Voltage 1               | MAP                          |
| Analog Voltage 2               | TPS                          |
| Analog Voltage 3               | O2 Front                     |
| Analog Voltage 4               | O2 Rear                      |
| Analog Voltage 5-6             | Not Used                     |
| Analog Voltage 7 (Pull-up)     | Engine Temperature           |
| Analog Voltage 8 (Pull-up)     | (IO Expansion port)          |
| Analog Voltage 9 (Pull-up)     | Intake Temperature (IAT MAF) |
| Analog Voltage 10 (Pull-up)    | Fuel Tank Temp (USDM)        |
| Analog Voltage 11-12 (Pull-up) | (IO Expansion port)          |
| Analog Voltage 13-14           | Not Used                     |

*Analog Voltage Channels 7-12 have switchable pull-ups suitable for temperature measurement.*

### Digital Inputs

| ECU Channel         | Function                           |
|---------------------|------------------------------------|
| Digital Input 1     | MAF Reset                          |
| Digital Input 2     | Vehicle Speed                      |
| Digital Input 3     | Clutch Switch                      |
| Digital Input 4     | Power Steer Pressure Switch        |
| Digital Input 5     | Alternator FR Signal               |
| Digital Input 6     | IO Expansion port (Ethanol Sensor) |
| Digital Input 7     | MAF                                |
| Digital Input 8     | I/C Spray Switch - Auto            |
| Digital Input 9     | I/C Spray Switch - Manual          |
| Digital Input 10    | ACD Input                          |
| Digital Input 11    | Ignition Start                     |
| Digital Input 12    | A/C Pressure Switch                |
| Digital Input 13-14 | IO Expansion port                  |

### Auxiliary Outputs

| ECU Channel     | Function                           |
|-----------------|------------------------------------|
| Auxiliary 1     | Purge Solenoid                     |
| Auxiliary 2     | Wastegate Solenoid                 |
| Auxiliary 3     | Tacho                              |
| Auxiliary 4     | Engine Fan Relay (EVO 7-8) - PWM   |
| Auxiliary 5     | Stepper Motor A1                   |
| Auxiliary 6     | Stepper Motor A2                   |
| Auxiliary 7     | Stepper Motor B1                   |
| Auxiliary 8     | Stepper Motor B2                   |
| Auxiliary 9     | Fuel Pressure Solenoid             |
| Auxiliary 10    | I/C Spray Relay                    |
| Auxiliary 11    | Engine Fan Relay                   |
| Auxiliary 12    | Sec Air/EGR Solenoid               |
| Auxiliary 13    | EVO8 Crank ground / EVO7 Cat Light |
| Auxiliary 14-16 | Not Used                           |

### Crank / Cam

| ECU Channel | Function                |
|-------------|-------------------------|
| Crank Index | Crank Sensor            |
| Sync Sensor | Cam Position - Inlet LH |

## 5.0 Plug-in Specific Information

### 5.1 Fuel Model

The base ECU calibration is supplied in Speed Density mode. It is recommended to install an Emtron 4Bar MAP sensor and wire it to a spare ANV Input in the Emtron expansion port. The ECU may also be configured to run on MAF only, or using a combination of MAF and Speed Density (MAP).

### 5.2 Inlet Air Temperature

ANV9 (ECU Pin 72) is assigned to the Inlet Air Temperature Sensor, which is physically located in the Mass Air Flow Meter. This is not ideal for the fuel model — it is recommended to install an inlet air temperature sensor in the inlet manifold. The Mass Air Flow Meter wiring can be reassigned, or the Air Temp sensor can be wired directly to pin 3 or 4 in the Emtron expansion port connector. ANV8, 11 or 12 may then be assigned in the inputs setup page in Emtune. Some EVO models have an inlet air temperature sensor fitted; however, this is not accounted for in the Emtron Plugin ECU — it is recommended to wire to the expansion port connector.

### 5.3 ECU Pin 40 Configuration

ECU Pin 40 configuration depends on the model. A low current, low side driver is connected to this pin, controlled by Auxiliary Output 13.

- **EVO 8 — Crank/Cam Sensor Ground:** A ground pin for the Crank and Cam sensors that acts as an immobiliser function. Aux 13 needs to be switched ON to provide a ground and allow the engine to start.
- **EVO 4-7 — CAT Light:** The CAT light requires a ground to switch the light on. Aux 13 can be used to control this light.

## 6.0 Diagnostic Trouble Codes (DTCs)

On initial installation it is advised to clear all the DTCs if errors are reported. Connect to Emtune and look at the DTC status in the bottom toolbar. If there are errors the status box will be red. To open the DTC window, click on the DTC Status box in the bottom toolbar OR use **File → Open DTC**. Select "Clear ALL DTCs" and confirm all the Error Codes have been removed — the DTC Status box should go green. If the error codes have not all been removed, select "Update DTC" then use the DTC window to locate the sensor that is on fault.

## 7.0 Ordering Information

| Product                             | Part Number |
|-------------------------------------|-------------|
| Emtron Mitsubishi EVO 4-8 Plugin    | 1609-52248  |
| Emtron Ethernet Tuning Cable (1.5m) | 553-15      |

## Appendix A – EVO 4-8 ECU Pinout

| Pin | Function                                       | Channel Assignment       |
|:---:|------------------------------------------------|--------------------------|
|  1  | Injector 1                                     | INJ 1                    |
|  2  | Injector 3                                     | INJ 3                    |
|  3  | Fuel Pressure Solenoid                         | AUX 9                    |
|  4  | Stepper Motor Coil A1                          | AUX 5                    |
|  5  | Stepper Motor Coil B1                          | AUX 6                    |
|  6  | EGR Solenoid Relay                             | AUX 12                   |
|  8  | Fuel Pump Relay                                | IGN 6                    |
|  9  | Purge Solenoid                                 | AUX 1                    |
| 10  | Ignition Coil 1 & 4                            | IGN 1                    |
| 11  | Wastegate Solenoid                             | AUX 2                    |
| 12  | ECU 14V from Main Relay                        | ECU SUPPLY               |
| 13  | Engine Block/Power Ground                      | ECU GROUND               |
| 14  | Injector 2                                     | INJ 2                    |
| 15  | Injector 4                                     | INJ 4                    |
| 16  | Evaporative Purge Solenoid                     | AUX 1                    |
| 17  | Stepper Motor Coil A2                          | AUX 6                    |
| 18  | Stepper Motor Coil B3                          | AUX 8                    |
| 19  | Volume Airflow Sensor Reset Signal             | DI 1                     |
| 20  | Engine Fan Speed low (EVO 4-6)                 | AUX 11                   |
| 21  | Engine Fan PWM Control (EVO 7-8)               | AUX 4                    |
| 22  | A/C Clutch Relay                               | IGN 8                    |
| 23  | Ignition Coil 2 & 3                            | IGN 2                    |
| 25  | ECU 14V from Main Relay                        | ECU SUPPLY               |
| 26  | Engine Block/Power Ground                      | ECU GROUND               |
| 32  | A/C Fan Relay High                             | INJ 7                    |
| 33  | Alternator G Terminal                          | IGN 5                    |
| 34  | A/C Fan Relay Low                              | IGN 3                    |
| 35  | I/C Spray Lamp                                 | IGN 4                    |
| 36  | CE Light                                       | INJ 8                    |
| 37  | Power Steer Pressure Switch                    | DI 4                     |
| 38  | ECU Main Relay Control                         | MAIN EFI RELAY           |
| 39  | Fuel Pump Speed                                | IGN 7                    |
| 40  | Crank/Cam sensor ground (EVO8) / CAT (EVO 4-7) | AUX 13                   |
| 41  | Alt FR terminal (Field response) - Freq Based  | DI 5                     |
| 43  | Clutch Switch                                  | DI 3                     |
| 44  | I/C Spray Switch - Auto                        | DI 8                     |
| 45  | AC Pressure Switch                             | DI 12                    |
| 51  | Immobiliser                                    |                          |
| 53  | Sec Air Solenoid (EVO7)                        | AUX 12                   |
| 54  | O2 Heater Rear                                 | INJ 5                    |
| 55  | I/C Spray Relay (EVO7)                         | AUX 10                   |
| 56  | Diagnostics – OBD II Pin 1                     |                          |
| 57  | I/C Spray Relay (EVO8)                         | AUX 10                   |
| 58  | Tacho                                          | AUX 3                    |
| 60  | O2 Heater Front                                | INJ 6                    |
| 62  | Diagnostics – OBD II Pin 7                     |                          |
| 71  | Start Switch                                   | DI 11                    |
| 72  | Intake Air Temperature                         | ANV 8                    |
| 73  | Manifold Absolute Pressure Sensor              | ANV 1                    |
| 75  | O2 Sensor Signal Rear                          | ANV 4                    |
| 76  | O2 Sensor Signal Front                         | ANV 3                    |
| 77  | Fuel Tank Temperature (USDM)                   | ANV 10                   |
| 78  | Knock Sensor                                   | KNOCK 1+                 |
| 80  | Battery Backup (+12 Constant)                  | Internal Flywheel Supply |
| 81  | + 5V Supply                                    | +5V Vref1                |
| 82  | Ignition Switch                                | Ignition Switch          |
| 83  | Engine Coolant Temperature                     | ANV 7                    |
| 84  | Throttle Position Sensor                       | ANV 2                    |
| 85  | External Barometric Pressure                   |                          |
| 86  | Vehicle Speed                                  | DI 2                     |
| 87  | ACD Signal/Idle Switch                         | DI 10                    |
| 88  | Cam Signal                                     | Sync Sensor              |
| 89  | Crank Signal                                   | Crank Index              |
| 90  | Volume Air Flow Sensor                         | DI 7                     |
| 91  | I/C Spray Switch – Manual (EVO 7-8)            | DI 9                     |
| 92  | Sensor Ground (MAP, TPS)                       | Sensor 0V Reference      |
