---
title: "Nissan GTR R35 Build"
weight: 1
---

## Nissan GT-R R35

Nissan GTR R35 dedicated menu shown with GTR R35 build enabled

The Nissan R35 GT-R's turbo control system and monitoring is different than many turbocharged cars. 

Commonly turbocharged engines have a common plenum that feeds all the engines cylinders. 

Each cylinder draws air from a common plenum. 

On the Nissan R35 GT-R one bank feeds one set of three cylinders(1-3) and the other turbo feeds the other three cylinders (4-6) via separated plenum's. There is also a cross over balance pipe between the plenum's. 

To correctly calculate the fueling requirements for each bank the ECU uses MAF Meter 1 (Bank 1) to control the fueling on Cylinders 1-3 and MAF Meter 2 (Bank 2) to control the fueling on Cylinders 4-6. There are also boost pressure sensors on each bank along with a single manifold pressure sensor on one bank. These pressure sensors allow for various calculations to be made by the ECU, offering a number methods to use for fuel calculations. 

The Emtron R35 GT-R Plug-in ECU is a replacement engine management system designed to be installed and integrate seamlessly with the vehicle, whilst also allowing extreme flexibility and control from the KV12 based ECU platform. 

The Nissan GTR R35 tab allows access to dedicated R35 features:

**▪ Nissan Vehicle Dynamic Control (VDC)** – This system employs an extremely complex system of vehicle sensors including wheel speed, steering angle, g-force and yaw which are used to generate various torque requests which the ECU must abide by accurately. This will not only achieve maximum vehicle performance, it is also a safety feature. 

**▪ Nissan Transmission Control Module Integration (TCM)** - The ECU must accurately calculate and perform torque requests assigned by the TCM for the drive-train to function correctly and smoothly for all driving conditions. Limitations on the transmission torque capacity must also be considered and hence another reason why the torque supplied by the engine must be accurately metered.

**▪ Launch Control** – The TCM provides the ECU torque requests during a launch OFF mode and is able to place the ECU into launch mode where the Torque Limit is not requested, allowing the ECU to increase the launch limit through a raised engine speed limit and an ECU determined torque limit.

**▪ Downshift Rev Matching** – The ECU must accurately calculate and increase torque to smoothly match the engine RPM in the next gear on downshift, by increasing the throttle mass flow (TMF) during the downshift event until the TCM is satisfied with the engine speed and torque levels.

{{% badge style="note" %}}NOTE{{% /badge %}} This page covers the plug-in install reference. For the detailed dedicated R35 tuning menus see [Nissan GTR R35 VDC](nissan-gtr-r35-vdc/), [Nissan GTR R35 TCM](nissan-gtr-r35-tcm/) and [TCM Torque Limit Engine Cut Setup](tcm-torque-limit-engine-cut-setup/).

## Plugin Features

- **KV12 ECU based platform** — Dual 100MHz processors, 32MB ECU logging memory, over 1000 channels, 1Hz to 500Hz logging rate, Emtune software, Dual Knock Control using Bosch digital filtering
- 6061 Grade Aluminium CNC Billet Enclosure
- Fully compatible with all OEM systems and user programmable, including Vehicle Dynamic Control (VDC) via throttle torque reduction, Transmission (TCM) Torque and Shift Management, and Torque Management Launch Control
- Compatible with all Emtron proven motorsport features
- Sequential Staged injection option available through the OEM header
- Upgradeable to run the Emtron Fuel model through installation of a Flex Meter, Fuel Temperature and Fuel Pressure Sensor
- Input Expansion through DTM connector: 2× User Analog Volt Inputs (Fuel Temperature and Pressure), 1× User Digital Input (Flex Meter Input)

**Communications:** CAN 2.0B Node 1 — User CAN Bus for I/O expansion (Lambda, EGT); CAN 2.0B Node 2 — 500k Baud Full CAN Bus OEM Integration; High Speed Ethernet 100Mbps.

**Operating Temperature:** -30 to 125°C (-22 to 257°F). **Physical:** 160 × 162 × 38 mm, 890g.

## Kit Contents

When purchasing a Nissan R35 plug-in the following items are included:

- GTR R35 Plug-in ECU
- Ethernet Communications Cable
- 12 way DTM to ELC Adapter Loom (120 Ohm CAN Termination resistors preinstalled)
- ELC2 Dual Channel Lambda to CAN controller – LSU4.9 version
- 2 × LSU4.9 Lambda Sensors + 2 × LSU4.9 Sensor Extension Looms
- ECU Mounting Kit

### Expansion Loom

The ECU's Input capabilities can be expanded using the expansion connection, which is a male DTM 12 Way. These additional inputs can be connected to any sensor, but the recommended sensors are indicated in brackets.

{{< figure src="/img/nissan-gtr-r35/expansion-port.jpeg" caption="DTM 12 Way expansion loom connector (ECU side)." >}}

| Pin | Function                                  |
|:---:|-------------------------------------------|
| 1   | Analog Sensor 0V Reference                |
| 2   | 5V Aux Supply                             |
| 3   | AN 10 (e.g. Fuel Temp or Inlet Temp)     |
| 4   | Not Used                                  |
| 5   | AN 6 (e.g. Fuel Pressure)                |
| 6   | DI 6 (e.g. Ethanol Content Sensor)       |
| 7   | 14V Out Protected (ELC2 Power Supply)     |
| 8   | Ground (ELC2 Ground)                      |
| 9   | 14V Out Protected (ELC2 Power Supply)     |
| 10  | Ground (ELC2 Ground)                      |
| 11  | CAN 1 Hi                                  |
| 12  | CAN 1 Lo                                  |

## ECU Channel Assignment

### Injection

| ECU Channel    | Function                  |
|----------------|---------------------------|
| Injection 1-12 | Fuel Injector Cylinder 1-12 |

### Ignition

| ECU Channel  | Function              |
|--------------|-----------------------|
| Ignition 1-6 | Ignition Cylinder 1-6 |
| Ignition 7   | DBW Relay             |
| Ignition 8   | Spare                 |
| Ignition 9-12| Not Used              |

### Analog Inputs

| ECU Channel                  | Function                          |
|------------------------------|-----------------------------------|
| Analog Voltage 1             | MAP                               |
| Analog Voltage 2             | DBW Servo Position Main Bank 1    |
| Analog Voltage 3             | DBW Servo Position Sub Bank 1     |
| Analog Voltage 4             | DBW Servo Position Main Bank 2    |
| Analog Voltage 5             | DBW Servo Position Sub Bank 2     |
| Analog Voltage 6             | Fuel Pressure                     |
| Analog Voltage 7 (Pull-up)   | Engine Temperature                |
| Analog Voltage 8 (Pull-up)   | Airbox Temperature                |
| Analog Voltage 9 (Pull-up)   | Engine Oil Temperature            |
| Analog Voltage 10 (Pull-up)  | IO Expansion loom (Emtron Fuel Temp/IAT) |
| Analog Voltage 11 (Pull-up)  | Pedal Position Sensor (PPS) Main  |
| Analog Voltage 12 (Pull-up)  | Pedal Position Sensor (PPS) Sub   |
| Analog Voltage 13            | MAF Bank 1                        |
| Analog Voltage 14            | MAF Bank 2                        |

### Digital Inputs

| ECU Channel      | Function                            |
|------------------|-------------------------------------|
| Digital Input 1  | Cam Position - Inlet RH             |
| Digital Input 2  | Brake Switch                        |
| Digital Input 3  | Neutral Switch                      |
| Digital Input 4  | Fuel Level                          |
| Digital Input 5  | Steering Wheel Button               |
| Digital Input 6  | IO Expansion Loom (Ethanol Sensor)  |
| Digital Input 7  | FP Feedback Sec Pump                |
| Digital Input 8  | FP Feedback Prim Pump               |
| Digital Input 9  | Power Steering Pressure             |
| Digital Input 10 | Evap System Pressure                |
| Digital Input 11 | Secondary Air MAF Sensor            |
| Digital Input 12 | Boost Pressure Bank 1               |
| Digital Input 13 | Boost Pressure Bank 2               |
| Digital Input 14 | AC System Pressure                  |

### Auxiliary Outputs

| ECU Channel  | Function                              |
|--------------|---------------------------------------|
| Auxiliary 1  | VVT Solenoid Bank 1                   |
| Auxiliary 2  | VVT Solenoid Bank 2                   |
| Auxiliary 3  | Purge                                 |
| Auxiliary 4  | Wastegate Solenoid                   |
| Auxiliary 5  | Sub Fuel Pump                         |
| Auxiliary 6  | Purge Vent                           |
| Auxiliary 7  | Fuel Pump Speed Control              |
| Auxiliary 8  | Tacho                                |
| Auxiliary 9  | DBW + Bank 1                         |
| Auxiliary 10 | DBW – Bank 1                         |
| Auxiliary 11 | DBW + Bank 2                         |
| Auxiliary 12 | DBW – Bank 2                         |
| Auxiliary 13 | Air Pump Relay                       |
| Auxiliary 14 | Air Cut Solenoid Relay Control (Bank 1 & 2) |
| Auxiliary 15 | Narrow Band Sensor Heater            |
| Auxiliary 16 | Not Used                             |

### Crank / Cam

| ECU Channel | Function                       |
|-------------|--------------------------------|
| Crank Index | Crank Sensor                   |
| Sync Sensor | Cam Position - Inlet Bank 1 (LH)|

## Plug-in Specific Information

### Staged Injection

Injector channels 7-12 are available in the OEM header and can be used for additional outputs or for Sequential Staged Injection: Injector Ch 7 = A11, Ch 8 = A12, Ch 9 = A16, Ch 10 = A35, Ch 11 = A39, Ch 12 = A43.

### Fuel Model

The base calibration is supplied with a **Blend** method of MAP Modelled (MAP Sensor and MAP Estimate) and Mass Air Flow (MAF Sensor). A fully adjustable combination of Throttle Pressure Ratio and Air Mass balances the priority of the two inputs. Many other fuel modelling methods are possible, including removing the MAF Sensors completely — a common implementation when the OEM sensors don't allow enough flow, or when engine modifications (cams, air bypass valves, larger turbos, modified intake piping) generate unstable Mass Flow readings. When MAF is selected, the Secondary Load table can be used to scale the MAF (switch ON via **Fuel Menu → Fuel Table Control → Secondary Load Table**, set to 12).

### Inlet Air Temperature

A factory-fitted Inlet Temperature Sensor is available on Analog Input 8 and should already be configured in the base calibration.

### Check Engine Light / Air-Con Switch

Both are handled through the CAN bus; the base calibration has the CE Light output and Air-Con Switch input source already configured and selected to "CAN Bus OEM".

## User CAN Bus 1

The ECU CAN Bus 1 is available for I/O expansion (ELC1/2, ETC4/ETC8M, EIC10/EIC16M). The ELC Power, Ground and CAN wires connect directly into the ECU IO Expansion Loom using the supplied 12 way DTM to ELC Adapter Loom (120 Ohm termination resistors pre-installed — completely plug and play). If other devices are added to the CAN bus, ensure no additional resistors are introduced.

| Name   | ELC 4-Way DTM | ECU IO Expansion 12-Way DTM |
|--------|:-------------:|:---------------------------:|
| Ground | Pin 1         | Pin 8                       |
| CAN Lo | Pin 2         | Pin 12                      |
| CAN Hi | Pin 3         | Pin 11                      |
| Power  | Pin 4         | Pin 7                       |

## OEM CAN Bus 2

The ECU communicates on CAN Bus 2, reserved for the R35 GT-R, maintaining full compatibility with all other CAN devices in the vehicle. Emtune has a dedicated R35 GT-R runtime tab; these runtimes are available throughout the ECU's functions and viewable in the Emtune logger.

## Emtron Torque Management

The ECU performs accurate torque calculations provided the engine model configuration is accurate. The Torque Management section allows the user to calibrate errors in the torque model whilst influencing torque delivery: **Torque Reduction Ign Retard Clamp**, **Torque Nitrous Gain**, **BSFC**, **Engine Torque Correction Table**, **Torque Demand Correction Table**, **Frictional Loss Table** (+ Offset 1 Table, commonly spanned against Engine Oil Temperature), **Torque Reduction Ignition Retard Gain Table** (% per degree) and **Torque Reduction Gain Table** (% per %cut).

## Launch Control

Launch Control is enabled in the base calibration. The TCM controls how it is armed — the ECU arms based on enabling R Mode of the transmission. The feature allows the user to target a torque level; the base calibration leverages **Engine Speed Limit 2** (RPM Limit 2 Table) to control engine speed during launch. The correct torque target achieves good acceleration and traction without requiring engine speed limiting once the vehicle is moving.

## Communications Torque

Torque information over the CAN bus can be modified (a ±500Nm offset table), changing gearshift behaviour and in-gear clutch pressure. If there is excessive slip, increase the reported Torque; if the gearshift feel is too sharp/aggressive, reduce it. This affects Engine Torque Demand and Engine Torque. *Note: directly programming the TCM through a third-party flashing tool is advised over using the ECU to offset the torque reported.*

## Ordering Information

| Product           | Part Number |
|-------------------|-------------|
| Emtron R35 Plugin | 1609-1835   |

## Appendix A – ECU Pinout

### Connector A

| OEM Pin | Function                                         | Channel Assignment       |
|---------|--------------------------------------------------|--------------------------|
| A1      | Throttle Control Motor Supply (paired with pin 49) | AUX 9-12 Supply (option 2) |
| A2      | Throttle Servo Bank 2 Motor +                    | AUX11                    |
| A3      | AF Sensor 2 Heater (denso narrowband)            | AUX15                    |
| A4      | AF Sensor 1 Heater (denso narrowband)            | AUX15                    |
| A5      | Throttle Servo Bank 2 Motor -                    | AUX12                    |
| A6      | Power Ground                                     | GROUND                   |
| A7      | Evaporative Purge Canister Vent Control Valve     | AUX6                     |
| A8      | Evaporative Purge Canister Volume Control Solenoid| AUX3                     |
| A9      | Ignition Cylinder 2                              | Ignition Channel 2       |
| A10     | Ignition Cylinder 1                              | Ignition Channel 1       |
| A11     | Secondary Injector 1                             | Injector Channel 7       |
| A12     | Secondary Injector 2                             | Injector Channel 8       |
| A13     | Ignition Cylinder 3                              | Ignition Channel 3       |
| A15     | TPS Bank 2 Ground                                | Sensor Ground 1          |
| A16     | Secondary Injector 3                             | Injector Channel 9       |
| A17     | Fuel Injector Cylinder 3                         | INJ 3                    |
| A19     | MAF Sensor Bank 2 Ground                         | Sensor Ground 1          |
| A20     | TPS Bank 1 Ground                                | Sensor Ground 1          |
| A21     | Fuel Injector Cylinder 2                         | INJ 2                    |
| A22     | MAF Sensor Bank 1 Ground                         | Sensor Ground 1          |
| A23     | SAMAF and TAM Ground                             | Sensor Ground 1          |
| A24     | Secondary Air Injection MAF Sensor (SAMAF)       | DI 11                    |
| A25     | Fuel Injector Cylinder 1                         | INJ 1                    |
| A26     | Engine Oil Temp / Engine Temp Ground             | Sensor Ground 1          |
| A27     | Engine Oil Temperature                           | ANV9                     |
| A28     | Throttle Servo Bank 2 Position Main              | ANV4                     |
| A29     | Fuel Pump Control Signal                         | AUX7                     |
| A30     | Fuel Pump Control Diag Input                     | DI 8                     |
| A31     | Mass Flow Sensor Bank 1                          | ANV13                    |
| A32     | Throttle Servo Bank 2 Position Tracking          | AV5                      |
| A33     | Ignition Cylinder 4                              | Ignition Channel 4       |
| A34     | Ignition Cylinder 5                              | Ignition Channel 5       |
| A35     | Secondary Injector 4                             | Injector Channel 10      |
| A36     | Throttle Servo Bank 1 Position Tracking          | ANV3                     |
| A37     | Fuel Injector Cylinder 4                         | INJ 4                    |
| A38     | Ignition Cylinder 6                              | Ignition Channel 6       |
| A39     | Secondary Injector 5                             | Injector Channel 11      |
| A40     | Throttle Servo Bank 1 Position Main              | ANV 1                    |
| A41     | Fuel Injector Cylinder 5                         | INJ 5                    |
| A42     | Fuel Level Sensor                                | ANV 10                   |
| A43     | Secondary Injector 6                             | Injector Channel 12      |
| A44     | Airbox Temperature                               | ANV8                     |
| A45     | Fuel Injector Cylinder 6                         | INJ 6                    |
| A46     | Coolant Temperature                              | ANV7                     |
| A47     | Inlet Mass Flow Bank 2                           | ANV14                    |
| A48     | Inlet Manifold Pressure Bank 2                   | ANV1                     |

### Connector B

| OEM Pin | Function                                         | Channel Assignment       |
|---------|--------------------------------------------------|--------------------------|
| B49     | Throttle Control Motor Supply (paired with pin 1)| Aux 9-12 Supply (option 1)|
| B50     | Throttle Servo Bank 1 Motor +                    | AUX 9                    |
| B51     | Inlet Camshaft Bank 2 Solenoid                   | AUX 2                    |
| B52     | Inlet Camshaft Bank 1 Solenoid                   | AUX 1                    |
| B53     | Throttle Servo Bank 1 Motor -                    | AUX 10                   |
| B54     | Power Ground                                     | GROUND                   |
| B55     | O2HR1 - Wideband bank 1 Heater                   | Not Connected            |
| B56     | O2HR2 - Wideband bank 2 Heater                   | Not Connected            |
| B61     | Boost Control Solenoid                           | AUX 4                    |
| B62     | Ground - Camshaft Position Bank 1                | Sync Sensor -            |
| B63     | Camshaft Bank 1 Position Sensor (inlet)          | Sync Sensor +            |
| B64     | Crankshaft Position Sensor                       | Crank Index +            |
| B66     | Ground - Camshaft Position Bank 2                | Sync Sensor -            |
| B67     | Camshaft Bank 2 Position Sensor (Inlet)          | DI 1                     |
| B68     | Ground - Crankshaft Position Sensor              | Crank Index -            |
| B70     | Ground - WB Sensor 1 and 2 (joined in loom)      | GROUND                   |
| B71     | Knock Sensor Ground for Bank 1 and 2 (joined)    | ECU Ground               |
| B72     | Knock Sensor Bank 1                              | Knock 1 +                |
| B73     | O2SR1 - Wideband bank 1 sensor                   | Not Connected            |
| B74     | Ground (Power Steer Pres, MAP, Refrigerant Pres) | Sensor Ground 1          |
| B75     | Ground (Evap sensor, Boost sensor Bank 1 and 2)  | Sensor Ground 1          |
| B76     | Knock Sensor Bank 2                              | Knock 2 +                |
| B77     | O2SR2 - Wideband bank 2 sensor                   | Not Connected            |
| B78     | Evap Control System Pressure Sensor              | DI 10                    |
| B79     | Boost Pressure Bank 2                            | DI12                     |
| B80     | Boost Pressure Bank 1                            | DI13                     |
| B81     | Denso Sensor AF+ (Bank 1 Narrowband)             | Not Connected            |
| B82     | Denso Sensor AF- (Bank 1 Narrowband)             | Sensor Ground 1          |
| B83     | Power Steering Pressure                          | DI 9                     |
| B84     | 5V Supply - TPS Bank 2                           | 5V Engine Supply         |
| B85     | Denso Sensor AF+ (Bank 2)                        | Not Connected            |
| B86     | Denso Sensor AF- (Bank 2)                        | Sensor Ground 1          |
| B87     | 5V Supply - Crankshaft                           | 5V Trigger Supply        |
| B88     | 5V Supply - Camshaft Position Bank 1             | 5V Trigger Supply        |
| B89     | Air Conditioner Refrigerant Pressure             | DI 14                    |
| B91     | 5V Supply - Camshaft Position Bank 2             | 5V Trigger Supply        |
| B92     | 5V Supply - Evap sensor, Boost sensor Bank 1/2   | 5V Aux Supply            |
| B93     | Sub Fuel Pump + (feedback)                       | DI 7                     |
| B94     | Sub Fuel Pump - (feedback)                       | Not Connected            |
| B95     | 5V Supply - Power Steer Pres, MAP, Refrig Pres   | 5V Engine Supply         |
| B96     | 5V Supply - TPS Bank 1                           | 5V Engine Supply         |

### Connector C

| OEM Pin | Function                                         | Channel Assignment       |
|---------|--------------------------------------------------|--------------------------|
| C97     | 500k vehicle CAN bus to ABS                      | CAN 2 LO (500kbps)       |
| C99     | 5V Supply - Pedal Position Sensor 2              | 5V Engine Supply         |
| C100    | 5V Supply - Pedal Position Sensor 1              | 5V Engine Supply         |
| C101    | 500k vehicle CAN bus to ABS                      | CAN 2 HI                 |
| C102    | Steering Wheel Button                            | DI 5                     |
| C103    | Ground - Pedal Position Sensor 1                 | Sensor Ground 1          |
| C104    | Pedal Position Main                              | ANV11                    |
| C105    | ECM relay                                        | EFI Relay                |
| C106    | Ignition Switch                                  | Ignition Switch          |
| C107    | Ground - Pedal Position Sensor 2                 | Sensor Ground 1          |
| C108    | Pedal Position Tracking                          | ANV12                    |
| C109    | Air Cut Solenoids Relay Control (Banks 1 & 2 joined)| AUX14                 |
| C110    | Brake Switch (Stop Lamp Switch)                  | DI 4                     |
| C111    | Neutral Switch (from TCM)                        | DI 3                     |
| C113    | Tacho out (To Power Steer control unit)          | AUX 8                    |
| C114    | K-Line                                           |                          |
| C117    | Cruise Control Brake Switch                      | DI 2                     |
| C118    | Keep Alive Memory power                          | Hot Supply               |
| C120    | Air Pump Relay                                   | AUX 13                   |
| C121    | VBR - Power from ECM Relay (Sec Air Inj Pump, MAF)| ECU Supply              |
| C122    | VBR - Power from ECM Relay                       | ECU Supply               |
| C124    | Power Ground                                     | GROUND                   |
| C126    | Sub Fuel Pump Relay                              | AUX 5                    |
| C127    | DBW on/off relay (coil power from ECM Relay)     | IGN 7                    |
| C128    | Power Ground                                     | GROUND                   |

