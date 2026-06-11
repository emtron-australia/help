---
title: "Mitsubishi EVO 9"
weight: 0
---

**Mitsubishi EVO 9 Plug-in ECU User Manual**

## 1.0 Introduction

The Mitsubishi EVO 9 ECU is designed to be plugged into the OEM harness to allow for a true "Plug and Play" install. The system is based on the KV Series Motorsport ECU, so all the same features are available with the limitation based around the OEM connector system. An Expansion loom is included giving access to unused Input channels. CAN Bus 2 is also available providing additional I/O expandability.

## 2.0 Plugin Features

**General**

- KV8 ECU based platform — Dual 100MHz processors, 32MB ECU logging memory, over 1000 logging channels, 1Hz to 500Hz logging rate
- Aluminium 6061 Grade CNC billet enclosure
- Compatible with all Emtron proven motorsport features (Launch Control, Rolling Launch, Anti-Lag, Traction Control)
- Upgradeable to run the Emtron fuel model through installation of a flex meter, fuel temperature and fuel pressure sensor
- Idle speed closed loop control using DBW with advanced Throttle Mass Flow (TMF) airflow calculations
- Knock control with high speed digital filtering for each cylinder using the OEM sensor with selectable centre frequency and bandwidth
- Pre-configured calibration file loaded providing a comprehensive tuning platform
- Input Expansion Capabilities through DTM connector: 3× User Analog Volt Inputs (Fuel Temperature, Fuel Pressure, Inlet Temperature), 3× User Digital Input (Flex Meter Input and switch inputs)
- Emtune software for tuning and data analysis

**Communications:** CAN 2.0B Bus 2 (User CAN Bus for I/O expansion — Lambda, EGT); High Speed Ethernet 100Mbps for tuning software connection.

**Operating Temperature:** -30 to 85°C (-22 to 185°F)

**Physical:** Enclosure Size 160 × 162 × 38 mm, 890g

## 3.0 Installation

### 3.1 Expansion Port

The ECU's input capabilities can be expanded using the expansion connection, which is a male DTM 12 Way. These additional inputs can be connected to any sensor, but the recommended sensors are indicated in brackets.

{{< figure src="/img/mitsubishi-evo-9/expansion-port.jpeg" caption="EVO 9 expansion port connector (DTM 12-way)." >}}

**Table 3.0 — Expansion Port Pinout (DTM06-12SA)**

| Pin | Function                                                            |
|:---:|---------------------------------------------------------------------|
|  1  | Analog Sensor 0V Reference                                          |
|  2  | 5V Vref2 Supply                                                     |
|  3  | AN 8 (e.g. Fuel Temp or Inlet Temp)                                 |
|  4  | AN 9 (e.g. Fuel Temp or Inlet Temp)                                 |
|  5  | AN 10 (e.g. Fuel Pressure)                                          |
|  6  | DI 6 (e.g. Ethanol Content Sensor)                                  |
|  7  | 14V Out Protected (e.g. ELC2 Power Supply). Post ECU SN 2700 only.  |
|  8  | ECU Ground (e.g. ELC2 or E85 Sensor Ground). Post ECU SN 2700 only. |
|  9  | DI 13                                                               |
| 10  | DI 14                                                               |
| 11  | CAN 2 Hi                                                            |
| 12  | CAN 2 Lo                                                            |

### 3.2 CAN Bus 2 Wiring

The ECU CAN Bus 2 is reserved for Emtron CAN Bus devices, expanding the IO capability of the ECU. The following devices can be connected: ELC1/2 (Lambda to CAN), ETC4/ETC8M (Thermocouple to CAN), EIC10/EIC16M (Input to CAN). All these CAN devices share a common power, ground and CAN pinout using a 4-way DTM.

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
| CAN 2 Lo |           Pin 12            |        Pin 2         |
| CAN 2 Hi |           Pin 11            |        Pin 3         |
| Power    |            Pin 7            |        Pin 4         |

Standard CAN bus precautions apply — twisted pair (min one twist per 40mm), minimise connectors, 120 ohm 0.25W termination at each END, stub length < 0.3m (ISO 11898). All Emtron CAN devices have no on-board terminating resistor, allowing them to be wired at any position on the Bus.

### 3.3 Sensor Wiring

**5V VRef2 Sensor Supply (Pin 2 of Expansion port)** — A 250mA 5V output designed to supply automotive sensors.

**Sensor 0V Reference (Pin 1 of Expansion port)** — This pin should be connected directly to the 0V (Ground) pin on any low current analog sensor, for example Pressure or Temperature.

- **DO NOT** connect the 0V Reference pin directly to the Engine Block or ECU Ground. This is a dedicated and specialised 0V/ground output for analog sensors.
- **DO NOT** connect frequency-based sensor grounds to the 0V Reference pin; for example, an Ethanol content sensor. Use Pin 8 (Ground) in the Expansion port.

{{< figure src="/img/mitsubishi-evo-9/sensor-0v-correct.jpeg" caption="Figure 3.3 — Correct Pressure Sensor 0V wiring (direct to the Sensor 0V Reference)." >}}
{{< figure src="/img/mitsubishi-evo-9/sensor-0v-incorrect.png" caption="Figure 3.4 — Incorrect Pressure Sensor 0V wiring." >}}

### 3.4 Ethanol Content Sensor Wiring

An Ethanol Content sensor can be wired into the ECU using the Expansion port. The following channel assignment is recommended for the GM sensor:

| GM Sensor Pinout | Expansion Loom        | Description                             |
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

| ECU Channel    | Function               |
|----------------|------------------------|
| Injection 1-4  | Fuel Injector Cyl 1-4  |
| Injection 5    | Rear Lambda Heater     |
| Injection 6    | Front Lambda Heater    |
| Injection 7    | Purge Solenoid 1       |
| Injection 8    | Secondary Air Solenoid |
| Injection 9-12 | Not Used               |

### Ignition

| ECU Channel    | Function                |
|----------------|-------------------------|
| Ignition 1     | Ignition Cylinder 1/4   |
| Ignition 2     | Ignition Cylinder 2/3   |
| Ignition 3     | I/C Spray Lamp          |
| Ignition 4     | Alternator Load Control |
| Ignition 5     | Fuel Pump Relay         |
| Ignition 6     | Fuel Pump Speed Relay   |
| Ignition 7     | A/C Clutch Relay        |
| Ignition 8     | CE Light                |
| Ignition 9     | A/C Fan High            |
| Ignition 10    | A/C Fan Low             |
| Ignition 11-12 | Not Used                |

### Analog Inputs

| ECU Channel                   | Function                       |
|-------------------------------|--------------------------------|
| Analog Voltage 1              | MAP                            |
| Analog Voltage 2              | TPS                            |
| Analog Voltage 3              | O2 Front                       |
| Analog Voltage 4              | O2 Rear                        |
| Analog Voltage 5              | MAF Baro                       |
| Analog Voltage 6              | Fuel Level                     |
| Analog Voltage 7 (Pull-up)    | Engine Temperature             |
| Analog Voltage 8-10 (Pull-up) | IO Expansion port              |
| Analog Voltage 11 (Pull-up)   | Intake Temperature in MAF      |
| Analog Voltage 12 (Pull-up)   | Fuel Tank Pressure (US Models) |
| Analog Voltage 13-14          | Not Used                       |

*Analog Voltage Channels 7-12 have switchable pull-ups suitable for temperature measurement.*

### Digital Inputs

| ECU Channel         | Function                           |
|---------------------|------------------------------------|
| Digital Input 1     | Cam Position - Inlet               |
| Digital Input 2     | Vehicle Speed                      |
| Digital Input 3     | Clutch Switch                      |
| Digital Input 4     | Power Steer Pressure Switch        |
| Digital Input 5     | A/C Switch 2                       |
| Digital Input 6     | IO Expansion Loom (Ethanol Sensor) |
| Digital Input 7     | MAF                                |
| Digital Input 8     | I/C Spray Switch - Auto            |
| Digital Input 9     | I/C Spray Switch - Manual          |
| Digital Input 10    | Fuel Level Low Light               |
| Digital Input 11    | Ignition Start                     |
| Digital Input 12    | A/C Pressure Switch                |
| Digital Input 13-14 | IO Expansion port                  |

### Auxiliary Outputs

| ECU Channel     | Function                  |
|-----------------|---------------------------|
| Auxiliary 1     | VVT Inlet Solenoid        |
| Auxiliary 2     | Wastegate Solenoid        |
| Auxiliary 3     | Tacho                     |
| Auxiliary 4     | Engine Fan Relay          |
| Auxiliary 5     | Stepper Motor B1          |
| Auxiliary 6     | Stepper Motor A1          |
| Auxiliary 7     | Stepper Motor A2          |
| Auxiliary 8     | Stepper Motor B1          |
| Auxiliary 9     | Fuel Pressure Solenoid    |
| Auxiliary 10    | I/C Spray Relay           |
| Auxiliary 11    | EGR Solenoid              |
| Auxiliary 12    | Evap Ventilation Solenoid |
| Auxiliary 13-16 | Not Used                  |

*Auxiliary Channel 9/10 can be reconfigured to run DBW.*

### Crank / Cam

| ECU Channel | Function                |
|-------------|-------------------------|
| Crank Index | Crank Sensor            |
| Sync Sensor | Cam Position - Inlet LH |

## 5.0 Plug-in Specific Information

### 5.1 Fuel Model

The base ECU calibration is supplied in Speed Density mode. It is recommended to install an Emtron 4Bar MAP sensor and wire it to an unused ANV Input in the Emtron expansion port. The ECU may also be configured to run on MAF only, or using a combination of MAF and Speed Density (MAP).

### 5.2 Inlet Air Temperature

ECU Pin 62 is assigned to the Intake Air Temperature (MAF), which is physically located in the Mass Air Flow Meter. This is not ideal for the fuel model — it is recommended to install an inlet air temperature sensor in the inlet manifold, wired directly to pin 3 in the Emtron expansion port connector. ANV8 may then be assigned in the inputs setup page in Emtune. Some models have an inlet air temperature sensor fitted in the plenum, connected to Pin 94 in the ECU and also assigned to ANV8 — if the vehicle is already fitted with a plenum-mounted sensor the input channel simply needs to be assigned.

{{% badge style="note" %}}NOTE{{% /badge %}} If the OEM sensor is fitted, pin 3 on the Emtron expansion port will no longer be available (unless that sensor is disconnected) as the pin is shared.

### 5.3 Drive by Wire (DBW)

Auxiliary Channels 9 and 10 can be reconfigured to run DBW.

| Channel             | OEM Configuration      | Reconfigured |
|---------------------|------------------------|--------------|
| Auxiliary Output 9  | Fuel Pressure Solenoid | DBW Motor +  |
| Auxiliary Output 10 | I/C Spray Relay        | DBW Motor -  |

## 6.0 Diagnostic Trouble Codes (DTCs)

On initial installation it is advised to clear all the DTCs if errors are reported. Connect to Emtune and look at the DTC status in the bottom toolbar (red if errors are present). Open the DTC window via the DTC Status box or **File → Open DTC**, select "Clear ALL DTCs", and confirm all the Error Codes have been removed (status box goes green). If the error codes have not all been removed, select "Update DTC" then use the DTC window to locate the sensor that is on fault.

## 7.0 Ordering Information

| Product                             | Part Number |
|-------------------------------------|-------------|
| Emtron Mitsubishi EVO 9 Plugin      | 1609-5229   |
| Emtron Ethernet Tuning Cable (1.5m) | 553-15      |

## Appendix A – EVO 9 ECU Pinout

| Pin | Function                                      | Channel Assignment       |
|:---:|-----------------------------------------------|--------------------------|
|  1  | Injector 1                                    | INJ 1                    |
|  2  | Injector 4                                    | INJ 2                    |
|  3  | Front O2 Heater                               | INJ 6                    |
|  4  | Secondary Air Solenoid                        | INJ 8                    |
|  6  | EGR Solenoid Relay                            | AUX 11                   |
|  8  | Alternator G Terminal                         | IGN 4                    |
|  9  | Injector 2                                    | INJ 2                    |
| 11  | Ignition Coil 1 & 4                           | IGN 1                    |
| 12  | Ignition Coil 2 & 3                           | IGN 2                    |
| 14  | Stepper Motor Coil A1                         | AUX 6                    |
| 15  | Stepper Motor Coil B1                         | AUX 5                    |
| 16  | Evaporative Purge Solenoid                    | INJ 7                    |
| 18  | Engine Fan (4kHz)                             | AUX 4                    |
| 19  | Volume Airflow Sensor Reset Signal            |                          |
| 20  | A/C Compressor Clutch Relay                   | IGN 7                    |
| 21  | Fuel Pump Relay                               | IGN 5                    |
| 22  | Check Engine Indicator Lamp                   | IGN 8                    |
| 24  | Injector 3                                    | INJ 3                    |
| 26  | Rear O2 Sensor Heater (USDM)                  | INJ 5                    |
| 28  | Stepper Motor Coil A2                         | AUX 7                    |
| 29  | Stepper Motor Coil B2                         | AUX 8                    |
| 30  | A/C Condenser Fan Relay (Low)                 | IGN 9                    |
| 31  | A/C Condenser Fan Relay (High)                | IGN 10                   |
| 32  | MIVEC Oil Control Solenoid                    | AUX 1                    |
| 34  | Sensor Ground (CAS, AFM)                      | ECU GROUND               |
| 35  | Evaporative Ventilation Solenoid (USDM)       | AUX 12                   |
| 41  | Wastegate Solenoid #1                         | AUX 2                    |
| 42  | + 5V Supply                                   | +5V Vref1                |
| 43  | Crank Signal                                  | Crank Index +            |
| 44  | Engine Coolant Temperature                    | ANV 7                    |
| 45  | Tacho                                         | AUX 3                    |
| 46  | Engine Block/Power Ground                     | ECU Ground               |
| 47  | ECU 14V from Main Relay                       | ECU Supply               |
| 48  | Fuel Pressure Solenoid                        | AUX 9                    |
| 49  | Sensor Ground (MAP, TPS)                      | Sensor 0V Reference      |
| 50  | CAM Angle Sensor (Exhaust Cam)                | Sync Sensor              |
| 51  | Barometric Pressure Sensor (MAF)              | ANV 5                    |
| 52  | Alt FR terminal (Field response) - Freq Based |                          |
| 53  | Inlet Cam Position Sensor                     | DI 1                     |
| 54  | Power Steer Pressure Switch                   | DI 4                     |
| 55  | Fuel Pump Speed Relay                         | IGN 6                    |
| 56  | I/C Spray Relay                               | AUX 10                   |
| 57  | Main Relay (Gnd to operate)                   | EFI RELAY                |
| 58  | Engine Block/Power Ground                     | ECU Ground               |
| 59  | ECU 14V from Main Relay                       | ECU Supply               |
| 60  | Battery Backup (+12 Constant)                 | Internal Flywheel Supply |
| 61  | Volume Air Flow Sensor                        | DI 7                     |
| 62  | Intake Air Temp Sensor (MAF)                  | ANV 11                   |
| 63  | Wastegate Solenoid #2                         | AUX 2                    |
| 65  | A/C Switch                                    | DI 5                     |
| 66  | I/C Auto Switch                               | DI 8                     |
| 67  | I/C Manual Switch                             | DI 9                     |
| 68  | Ignition Start Signal                         | DI 11                    |
| 71  | O2 Sensor Signal Front                        | ANV 3                    |
| 73  | O2 Sensor Signal Rear                         | ANV 4                    |
| 75  | (N/C)                                         | ECU Ground               |
| 78  | Throttle Position Sensor                      | ANV 2                    |
| 80  | Vehicle Speed                                 | DI 2                     |
| 83  | A/C Request (Pressure Switch)                 | DI 12                    |
| 85  | Diagnostics K-line (OBD Pin 7)                |                          |
| 88  | Clutch Switch                                 | DI 3                     |
| 90  | I/C Spray Lamp                                | IGN 3                    |
| 91  | Knock Sensor                                  | Knock 1 +                |
| 92  | Manifold Absolute Pressure Sensor             | ANV 1                    |
| 93  | Fuel Tank Differential Pressure Sensor        | ANV 12                   |
| 95  | Fuel Level                                    | ANV 6                    |
| 96  | Inlet Plenum Temperature                      | ANV 8                    |
| 97  | Fuel Level Low (USDM)                         | DI 10                    |
| 98  | Immobiliser                                   |                          |
| 99  | Ignition Switch                               | Ignition Switch          |
| 100 | Diagnostics                                   |                          |
