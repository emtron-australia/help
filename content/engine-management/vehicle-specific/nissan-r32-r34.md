---
title: "Nissan R32-R34"
weight: 0
---

**Nissan R32-R34 Plug-in ECU User Manual**

## 1.0 Introduction

The Nissan R32-R34 ECU is designed to be plugged into the OEM harness to allow for a true "Plug and Play" install. The system is based on the KV Series Motorsport ECU, so all the same features are available excluding any limitations based around the OEM connector system. An Expansion port is included giving access to unused Input channels. CAN Bus 1 is also available providing additional I/O expandability.

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

{{< figure src="/img/nissan-r32-r34/expansion-port.jpeg" caption="Nissan R32-R34 expansion port connector (DTM 12-way)." >}}

**Table 3.0 — Expansion Port Pinout (DTM06-12SA)**

| Pin | Function                                    |
|:---:|---------------------------------------------|
|  1  | Analog Sensor 0V Reference                  |
|  2  | 5V Vref2 Supply                             |
|  3  | AN 8 (e.g. Fuel Temp or Inlet Temp)         |
|  4  | AN 9 (e.g. Fuel Temp or Inlet Temp)         |
|  5  | AN 10 (e.g. Fuel Pressure)                  |
|  6  | DI 6 (e.g. Ethanol Content Sensor)          |
|  7  | ANV 13                                      |
|  8  | ANV 14                                      |
|  9  | 14V Out Protected (e.g. ELC2 Power Supply)  |
| 10  | ECU Ground (e.g. ELC2 or E85 Sensor Ground) |
| 11  | CAN 1 Hi                                    |
| 12  | CAN 1 Lo                                    |

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

### 3.3 Analog Sensor Wiring

**5V VRef2 Sensor Supply (Pin 2 of Expansion port)** — A 250mA 5V output designed to supply automotive sensors.

**Sensor 0V Reference (Pin 1 of Expansion port)** — This pin should be connected directly to the 0V (Ground) pin on any low current analog sensor, for example Pressure or Temperature.

- **DO NOT** connect the 0V Reference pin directly to the Engine Block or ECU Ground. This is a dedicated and specialised 0V/ground output for analog sensors.
- **DO NOT** connect frequency-based sensor grounds to the 0V Reference pin; for example, an Ethanol content sensor. Use Pin 8 (Ground) in the Expansion port.

{{< figure src="/img/nissan-r32-r34/sensor-0v-correct.jpeg" caption="Figure 3.3 — Correct Pressure Sensor 0V wiring (direct to the Sensor 0V Reference)." >}}
{{< figure src="/img/nissan-r32-r34/sensor-0v-incorrect.png" caption="Figure 3.4 — Incorrect Pressure Sensor 0V wiring." >}}

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
| Injection 1-6  | Fuel Injector Cyl 1-6 |
| Injection 7    | O2 Heater             |
| Injection 8-12 | Not Used              |

### Ignition

| ECU Channel    | Function                     |
|----------------|------------------------------|
| Ignition 1-6   | Ignition Cylinder 1-6        |
| Ignition 7     | FPCM1                        |
| Ignition 8     | FPCM1                        |
| Ignition 9     | Trigger Sensor 120/1 Control |
| Ignition 10-12 | Not Used                     |

### Analog Inputs

| ECU Channel                    | Function           |
|--------------------------------|--------------------|
| Analog Voltage 1               | TPS                |
| Analog Voltage 2               | O2 Front           |
| Analog Voltage 3               | O2 Rear            |
| Analog Voltage 4               | MAF (Rear R32)     |
| Analog Voltage 5               | MAF Front R32      |
| Analog Voltage 6               | Not Used           |
| Analog Voltage 7 (Pull-up)     | Engine Temperature |
| Analog Voltage 8-10 (Pull-up)  | IO Expansion port  |
| Analog Voltage 11-12 (Pull-up) | Not Used           |
| Analog Voltage 13-14           | Not Used           |

*Analog Voltage Channels 7-12 have switchable pull-ups suitable for temperature measurement.*

### Digital Inputs

| ECU Channel        | Function                           |
|--------------------|------------------------------------|
| Digital Input 1    | Vehicle Speed                      |
| Digital Input 2    | Neutral Switch                     |
| Digital Input 3    | Start Switch                       |
| Digital Input 4    | AC Request Switch                  |
| Digital Input 5    | Alternator FR Signal               |
| Digital Input 6    | IO Expansion port (Ethanol Sensor) |
| Digital Input 7    | Power Steer Pressure Switch        |
| Digital Input 8-14 | Not Used                           |

### Auxiliary Outputs

| ECU Channel     | Function                                |
|-----------------|-----------------------------------------|
| Auxiliary 1     | VTC Solenoid                            |
| Auxiliary 2     | Wastegate Solenoid                      |
| Auxiliary 3     | Tacho                                   |
| Auxiliary 4     | ISC Solenoid                            |
| Auxiliary 5     | Fuel Pump Relay                         |
| Auxiliary 6     | A/C Clutch Relay                        |
| Auxiliary 7     | CE Light                                |
| Auxiliary 8     | Fan Relay (R32)                         |
| Auxiliary 9     | EGT Light (R33)                         |
| Auxiliary 10    | Injector %DC Display                    |
| Auxiliary 11    | Connected to pin 111 (user output – 5A) |
| Auxiliary 12    | Connected to pin 112 (user output – 5A) |
| Auxiliary 13-16 | Not Used                                |

### Crank / Cam

| ECU Channel | Function                        |
|-------------|---------------------------------|
| Crank Index | Crank Position Sensor (120 Deg) |
| Sync Sensor | Crank Position Sensor (1 Deg)   |

## 5.0 Plug-in Specific Information

### 5.1 Fuel Model

The ECU has the ability of using any Emtron-based Fuel Model; however, the base calibration provided implements a simple version of Speed Density. The Main VE Table has the Efficiency Calculation configured to span against TPS, which simplifies the mapping process. The fuel calculation will still account for Inlet Manifold Pressure. The Lambda Target is modified by a combination of Engine Speed and Manifold Pressure in the base calibration and allows for increasing enrichment based on an increase in engine load.

### 5.2 Inlet Air Temperature

Factory Inlet Air Temperature using ECU input ANV 8 is available on most models. If the input shows 4.85V or higher, this sensor is not connected and will need to be fitted and wired in using the Expansion port (refer to section 3.1).

### 5.3 ECU User Pins 111, 102

ECU pins 111 and 102 are unused OEM pins which connect directly to Aux 11 and 12 respectively. These are Half Bridge drivers rated at 5A continuous and 8A limit, and can be used as Low Side, High Side or together for DC motor control.

### 5.3 EGT Light

The R33 models have an EGT Light on Auxiliary 9. This can be configured and controlled from a User Channel.

### 5.4 Crank (120) and Crank (1) Signal Selection

For correct engine decoding, the ECU Crank Index input should be connected to the Nissan 120 degree signal and the Sync input connected to the Nissan 1 degree signal. The R32 and R33 should not require the signal swap enabled. The **R34 will require the enabling of the Crank (120) and Crank (1) signal swap**, which will otherwise prevent the engine from starting (cranking RPM will read extremely high if the pin swap is not enabled). These signals can be swapped using internal circuitry controlled by Ignition 9 — it doesn't require any physical pins to be swapped. A User channel can be configured to control this.

**Table 5.0 — Ignition 9 Crank Signal Configuration**

| ECU Pin   | Ignition 9 OFF          | Ignition 9 ON           |
|-----------|-------------------------|-------------------------|
| Pin 41/51 | Crank Signal 120 degree | Crank Signal 1 Degree   |
| Pin 42/52 | Crank Signal 1 Degree   | Crank Signal 120 degree |

## 6.0 Diagnostic Trouble Codes (DTCs)

On initial installation it is advised to clear all the DTCs if errors are reported. Connect to Emtune and look at the DTC status in the bottom toolbar (red if errors are present). Open the DTC window via the DTC Status box or **File → Open DTC**, select "Clear ALL DTCs", and confirm all the Error Codes have been removed (status box goes green). If the error codes have not all been removed, select "Update DTC" then use the DTC window to locate the sensor that is on fault.

## 7.0 Ordering Information

| Product                             | Part Number |
|-------------------------------------|-------------|
| Emtron Nissan R32-R34 Plugin        | 1609-1834   |
| Emtron Ethernet Tuning Cable (1.5m) | 553-15      |

## Appendix A – Nissan R32-R34 ECU Pinout

| Pin | Function                                 | Channel Assignment       |
|:---:|------------------------------------------|--------------------------|
|  1  | Ignition 1                               | IGN 1                    |
|  2  | Ignition 5                               | IGN 5                    |
|  3  | Ignition 3                               | IGN 3                    |
|  4  | Idle Speed Control Solenoid              | AUX 4                    |
|  5  | AT Shift Request                         | DI 5                     |
|  6  | Engine Fan Relay (R32)                   | AUX 8                    |
|  7  | Tacho                                    | AUX 3                    |
|  8  | Ignition Switch (some models only)       | Ignition Switch          |
|  9  | A/C Clutch Relay                         | AUX 6                    |
| 10  | Ignition Ground                          | ECU GROUND               |
| 11  | Ignition 6                               | IGN 6                    |
| 12  | Ignition 2                               | IGN 2                    |
| 13  | Ignition 4                               | IGN 4                    |
| 16  | ECCS Relay                               | EFI RELAY                |
| 17  | Injector %DC Display (or E85)            | AUX 10                   |
| 18  | Fuel Pump Relay                          | AUX 5                    |
| 19  | Power Steer Pressure Switch              | DI 7                     |
| 20  | Ignition Ground                          | ECU GROUND               |
| 23  | Knock Sensor 1                           | Knock 1+                 |
| 24  | Knock Sensor 2                           | Knock 2+                 |
| 25  | Wastegate Solenoid                       | AUX 2                    |
| 26  | MAF Ground                               | ECU GROUND               |
| 27  | Mass Air Flow Sensor (Rear)              | ANV 4                    |
| 28  | Engine Coolant Temperature               | ANV 7                    |
| 29  | O2 Sensor Front                          | ANV 2                    |
| 30  | Sensor Ground (Coolant, O2)              | Sensor 0V Reference      |
| 31  | Clock (Sync Signal)                      |                          |
| 32  | CE Light                                 | AUX 7                    |
| 33  | EGT Light (R33)                          | AUX 9                    |
| 34  | MAF Ground                               | ECU GROUND               |
| 35  | Mass Air Flow Sensor (Front)             | ANV 5                    |
| 36  | Inlet Air Temperature (some models only) | ANV 8                    |
| 38  | Throttle Closed Switch                   | ANV 1                    |
| 40  | Sensor Ground (MAP, TPS)                 | Sensor 0V Reference      |
| 41  | Crank Position Sensor (120)              | Crank Index              |
| 42  | Crank Position Sensor (1)                | Sync Sensor              |
| 43  | Start Switch                             | DI 3                     |
| 44  | Neutral Switch                           | DI 2                     |
| 45  | Ignition Switch                          | Ignition Switch          |
| 46  | A/C Request Switch                       | DI 4                     |
| 48  | TPS +5V Supply                           | + 5V Supply              |
| 49  | Control Unit Power Supply                | ECU SUPPLY               |
| 50  | Control Unit Ground                      | ECU GROUND               |
| 51  | Crank Position Sensor (120)              | Crank Index              |
| 52  | Crank Position Sensor (1)                | Sync Sensor              |
| 53  | Vehicle Speed Sensor                     | DI 1                     |
| 55  | O2 Sensor Rear                           | ANV 3                    |
| 56  | Throttle Position Out                    | AV OUT 1                 |
| 58  | Battery Backup (+12 Constant)            | Internal Flywheel Supply |
| 59  | Control Unit Power Supply                | ECU SUPPLY               |
| 60  | Control Unit Ground                      | ECU GROUND               |
| 101 | Injector 1                               | INJ 1                    |
| 102 | (N/C — user output)                      | AUX 12                   |
| 103 | Injector 3                               | INJ 3                    |
| 104 | Fuel Pump Control #1                     | IGN 7                    |
| 105 | Injector 2                               | INJ 2                    |
| 106 | Fuel Pump Control #2                     | IGN 8                    |
| 107 | Injector Ground                          | ECU GROUND               |
| 108 | Injector Ground                          | ECU GROUND               |
| 110 | Injector 5                               | INJ 5                    |
| 111 | (N/C — user output)                      | AUX 11                   |
| 112 | Injector 6                               | INJ 6                    |
| 113 | VTC Solenoid (R33)                       | AUX 1                    |
| 114 | Injector 4                               | INJ 4                    |
| 115 | O2 Heater Rear (R33/R34)                 | INJ 7                    |
| 116 | Injector Ground                          | ECU GROUND               |
