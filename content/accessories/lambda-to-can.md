---
title: "Emtron Lambda to CAN"
---

![](/img/elc/image1.jpeg)

ELC1/ ELC2/ ELC2M

Kit Contents

When purchasing an ELC1/ELC2 the following items are included:

* ELC1/2 Device with Flying Harness
* Deustch DTM 4-way mating connector with female pins (DTM06-4S)

![](/img/elc/image4.jpeg)

ELC2 kit pictured.

When purchasing an ELC2M the loom side mating Autosport connector is not included but can be purchased separately.

Contents

# 1.0 Description

The Emtron Lambda to CAN devices are available in both Standard and Mil Spec versions.

![](/img/elc/image5.jpeg)

**ELC2M**

The ELC2M is a Mil Spec Dual Channel Lambda to CAN device using the Motorsport proven Deutsch Autosport connector system(Green). The enclosure is made from billet 6061 aluminium and is waterproof, allowing for use in extreme environments.

![](/img/elc/image6.jpeg)

**ELC1**

The ELC1 is a Single Lambda to CAN device with a concentric twisted flying loom system, terminated with the reliable and environmentally sealed Deutsch DTM connector. The water proof enclosure is extremely compact and made from billet 6061 aluminium.

![](/img/elc/image7.jpeg)

**ELC2**

The ELC2 is a Dual Channel Lambda to CAN device with a concentric twisted flying loom system, terminated with the reliable and environmentally sealed Deutsch DTM connector. The waterproof enclosure is extremely compact and made from billet 6061 aluminium.

All devices control the Bosch LSU4.9 Lambda Sensor and are compatible with all Emtron ECUs. Bosch proven integrated circuit technology is used for sensor control, Nernst Cell temperature measurement with advanced PID algorithms for precise heater control. Exhaust Pressure compensation is available when enabled. The device is connected to the ECU via CAN bus and will be automatically detected, significantly minimising configuration time.

# 2.0 Specification

**Power Supply**

* Operating Voltage: 7.0 to 22.0 Volts DC
* Operating Current Standby: 38mA at 14.0V
* Operating Current Average: 3A at 14.0V (Peak 8A Warmup)
* Reverse Battery Protection: 0mA current draw
* Battery Transient/Over Current Protection

**Internal**

* 64MHz 16-bit Automotive Processor

**Inputs**

* Bosch LSU4.9. Supports Single or Dual Channel
* Resolution: 0.001 Lambda
* Range: 0.580 Lambda to open air.
* Lambda Signal sampling rate: 100 Hz
* Exhaust Pressure Pump Current Compensation

**Communications**

* CAN 2.0B Baud Rate: 250kBaud, 500kBaud or 1Mbaud Auto Detect
* CAN Transmit Rate 100Hz

**Operating Temperature**

* Operating Temperature Range: -30 to 85°C (-22 to 185°F)

**Physical**

**ELC2M**

* Enclosure Size 52 mm x 74 mm x 18 mm
* 125g (Excludes loom)

**ELC1/ ELC2**

* Enclosure Size 63mm x 54 mm x 20mm
* ELC1 165g, ELC2 200g (includes flying loom)

# 3.0 Installation

Each device has a M4 x 1.5 thread tapped into the base of the enclosure and can be used for mounting. In high vibration applications rubber mounting is recommended.

{{% icon style="warning" %}} *CAUTION* When mounting the device inside the engine compartment, it should be positioned in cooler areas and away from heat sources such as exhaust manifolds. Any unnecessary radiated heat may affect device performance.

## 3.1 ELC1/2 Wiring

The pinouts are shown below in Table 3.0 and Table 3.1.

![](/img/elc/image8.jpeg)
**Power and CAN Flying Loom Connector: DTM 4 pin (M).**

| Pin | Function   | Wire Colour                                          |
|:---:|------------|------------------------------------------------------|
|  1  | Ground     | {{% icon icon="circle-dot" style="black" %}} Black   |
|  2  | CAN Lo     | {{% icon icon="circle-dot" style="green" %}} Green   |
|  3  | CAN Hi     | {{% icon icon="circle-dot" style="yellow" %}} Yellow |
|  4  | 12V Supply | {{% icon icon="circle-dot" style="red" %}} Red       |

Table 3.0. ELC Power and CAN Deustch Connector Pinout

**Lambda Flying Loom Connector: Bosch LSU 4.9 (F)**

| Pin | Function            | Wire Colour                                          |
|:---:|---------------------|------------------------------------------------------|
|  1  | Pump Current        | {{% icon icon="circle-dot" style="red" %}} Red       |
|  2  | Virtual Ground      | {{% icon icon="circle-dot" style="yellow" %}} Yellow |
|  3  | Heater Ground       | {{% icon icon="circle-dot" style="white" %}} White   |
|  4  | Heater 12 Supply    | {{% icon icon="circle-dot" style="grey" %}} Grey     |
|  5  | Cal Resistor        | {{% icon icon="circle-dot" style="orange" %}} Orange |
|  6  | Nernst Cell Voltage | {{% icon icon="circle-dot" style="black" %}} Black   |

Table 3.1 ELC1/2 LSU 4.9 Connector Pinout

## 3.2 ELC2M Wiring

![](/img/elc/image9.jpeg)


| Mating Connector Loom Side (Deutsch Autosport AS Series) |
|----------------------------------------------------------|
| AS612-35PD (Green)                                       |


| Pin | Function                               | Bosch Datasheet Reference |
|:---:|----------------------------------------|---------------------------|
|  1  | 14 V Supply                            |                           |
|  2  | Ground                                 |                           |
|  3  | CAN Hi                                 |                           |
|  4  | CAN Lo                                 |                           |
|  5  | Lambda 1 Pump Current                  | APE                       |
|  6  | Lambda 1 Nernst Cell Voltage           | RE                        |
|  7  | Lambda 1 Cal Resistor                  |                           |
|  8  | Lambda 1 Virtual Ground                | IPN                       |
|  9  | Lambda 2 Pump Current                  | APE                       |
| 10  | Lambda 2 Nernst Cell Voltage           | RE                        |
| 11  | Lambda 2 Cal Resistor                  |                           |
| 12  | Lambda 2 Virtual Ground                | IPN                       |
| 13  | Lambda 1 Heater Ground                 |                           |
| 14  | Lambda 2 Heater Ground                 |                           |
| 15  | Lambda 1 Heater 14V Supply (Protected) |                           |
| 16  | Lambda 2 Heater 14V Supply (Protected) |                           |
| 17  | *(Not used)*                           |                           |
| 18  | *(Not used)*                           |                           |
| 19  | *(Not used)*                           |                           |
| 20  | *(Not used)*                           |                           |
| 21  | *(Not used)*                           |                           |
| 22  | *(Not used)*                           |                           |

Table 3.2. ELC2M Pinout

## 3.3 Bosch LSU4.9 Sensor Wiring

**Lambda Connector: Bosch LSU 4.9 (F)**

| Pin | Function            | Wire Colour                                          |
|:---:|---------------------|------------------------------------------------------|
|  1  | Pump Current        | {{% icon icon="circle-dot" style="red" %}} Red       |
|  2  | Virtual Ground      | {{% icon icon="circle-dot" style="yellow" %}} Yellow |
|  3  | Heater Ground       | {{% icon icon="circle-dot" style="white" %}} White   |
|  4  | Heater 12 Supply    | {{% icon icon="circle-dot" style="grey" %}} Grey     |
|  5  | Cal Resistor        | {{% icon icon="circle-dot" style="orange" %}} Orange |
|  6  | Nernst Cell Voltage | {{% icon icon="circle-dot" style="black" %}} Black   |

Table 3.3. Bosch LSU 4.9 Sensor Pinout

![](/img/elc/image11.png)

![](/img/elc/image10.png)

Figure 3.0. LSU4.9 Connector Pinout

{{% badge style="note" %}}To avoid signal errors and loss of accuracy, a cable of a maximum length of 1.5 m between sensor and ELC is recommended.{{% /badge %}}

## 3.4 CAN Bus Wiring

* CAN Bus High and Low are differential signals, so twisted pair **MUST** be used. Failing to do so will compromise the entire CAN Bus System.
* In some extreme environments, shielded twisted pair may be required to help with reliability and data integrity.
* The less connectors in any transmission system the better. Unnecessary connectors are almost guaranteed to present an impedance discontinuity and hence may cause reflections and data loss.
* CAN Bus termination must be done correctly by using a 120 ohm 0.25W resistor at each END of the bus system.
* Maximum Stub length to a device from the main Bus is recommended at 0.3m, in accordance with High-Speed ISO 11898 Standard specification. See Figure 3.3.

The ELC devices do **not** include an on-board CAN termination resistor, allowing the device to be wired at any position on the Bus. CAN Bus termination must be done correctly by using a 120 ohm 0.25W resistor at each end of the bus system as mentioned above. Figures 3.1 and 3.2 show possible CAN Bus Implementation examples

![](/img/elc/image12.jpg)

Figure 3.1. CAN Bus Wiring Example. ECU and Dash at each end with 120 Ohm Termination

![](/img/elc/image13.jpg)

Figure 3.2. CAN Bus Wiring Example. ECU and ELC2 at each end with 120 Ohm Termination

![](/img/elc/image14.png)

Figure 3.3. CAN Bus Wiring Example. Stub Length less than 0.3m

##

## 3.5 ELC CAN Bus

The ELC devices can be connected to the ECUs CAN Bus 1 or 2.

All devices on the CAN Bus must be configured to use the same baud rate. For this reason, all Emtron CAN devices will Auto-scan the CAN bus until a successful baud rate has been detected. Once detected this rate will be stored and used at the next power up.

The device will scan 3 different Baud rates at 500ms intervals moving from 1Mbaud -> 500kBaud -> 250k Baud -> 1Mbaud and so on.

**NOTE:** For this process to function effectively, when **new** devices are introduced to the CAN bus, they should initially be connected **one at a time.** This allows each device to sync up to the CAN Bus baud rate and store that setting. This typically takes 3-5 seconds.

The ELC devices leave the factory programmed with individual serial numbers, but all have the same Base CAN Address ID used to transmit data over the Bus. The CAN Base address can be adjusted from the factory setting using the ID Reprogramming Tool. This is required when 2 or more of the same devices are connected to the CAN Bus (See section 4.2).

* Factory CAN Base Address of 671. Transmits data sequentially on the next ID. Total CAN ID Range is therefore 671 – 672.
* Up to 6x ELC devices (ELC or ELCM) can be used on the CAN Bus giving a total of 12 available Lambda Channels.

## 3.6 Noise Immunity

To minimise signal contamination and maximise noise immunity, the wire pairs shown in Table 3.2 must be twisted. It is recommended to twist the wire pairs at a minimum one twist per 40mm of cable. This is very important and should always be implemented on both CAN Bus and LSU Sensor wiring.

|                     |           |                |
|---------------------|-----------|----------------|
| Pair 1              |           | Pair 2         |
| CAN High            | <-------> | CAN Low        |
| Pump Current        | <-------> | Cal Resistor   |
| Nernst Cell Voltage | <-------> | Virtual Ground |

Table 3.4. Wire pairing for twisting

# 4.0 Lambda Sensor Installation

Installation angle must be inclined at least 10° towards horizontal, (electrical connection upwards) up to a maximum of 75°. This prevents the collection of liquids between sensor housing and sensor element during the cold start phase.

The angle against the exhaust gas stream should be aimed as 90°. Maximum inclination should be 90°+15° (protection tube towards gas stream) or 90°-30°.

**NOTE: NEVER** mount the sensor directly on the horizontal or within 10 degrees of the horizontal. Doing so will result in intermittent sensor shutdown.

![](/img/elc/image15.png)

Also route the sensor cable to avoid high moisture locations – just a small amount of moisture is enough to provide a conductive path within the connector that will upset measurement from the sensor.

Winter and salted roads compound this issue. Always check for a cracked or broken connector when strange results occur.

# 5.0 Heater Control and Sensor Calibration

## 5.1 Heater Control

During engine start-up, condensation forms in the exhaust which may damage the sensor. It is recommended to only start heating the LSU sensor after the engine is running and the moisture content in the exhaust has evaporated. ELC settings allow the ECU to control heater setup if enabled.

For maximum sensor life the ECU should control heater start-up. It does this by communicating with the ELC over CAN Bus. For setup options see Config View -> Communications Tab -> Emtron CAN Device -> Emtron Lambda to CAN (ELC/ELCM) Setup. See Figure 5.0.

![](/img/elc/image16.png)

Figure 5.0. Emtune ELC Setup menu - Heater Control

Once changed, the settings are automatically stored by the ELC and therefore used on the next power cycle. If the CAN bus is not used to control the heater (Enable Heater Override = OFF), then by default the heater remains OFF for 15 seconds after the device is powered up.

## 5.2 Sensor Calibration

The sensor is calibrated by the ELC on power up. During the Calibration process two important pieces of data are read:

* The optimal **Nernst Cell Temperature** which is used for sensor heater control. The ELC applies duty cycle and a PID routine to maintain a constant and accurate heater temperature which results in a very stable and accurate Lambda value.
* The **Pump Current** that corresponds to a Lambda reading of 1.000 Lambda.

**NOTE:** A Free-Air Calibration is NOT required on the LSU4.9. The sensor uses a reference pump current instead of reference air. The big advantage with this is that the reference is a calibrated electrical signal and remains constant.

# 6.0 Exhaust Back Pressure (EMAP) Compensation

Wideband Lambda sensors primarily count oxygen atom numbers through measuring the oxygen ion current within the sensors pump cell. The exhaust gas pressure affects this oxygen ion current. The more pressure means more atoms per unit volume and a **higher** pump current at the same Lambda i.e. this will cause the sensor to read farther from stoichiometric.

A rich reading will appear richer than it really is.

A lean reading will appear leaner than it really is.

This predominantly becomes an issue in Turbocharged applications. This is the main reason you should position the sensor after the turbo where exhaust back-pressure is lowest.

Excessive Exhaust Back Pressure (EMAP) can also damage the sensor. The following rule should be observed:

|                                 |
|---------------------------------|
| Exhaust Back Pressure < 2.5 Bar |

When measuring Exhaust Back Pressure, an Absolute Pressure Sensor MUST be used. (i.e. **do not** use a Gauge Pressure Sensor). The ECU MUST have the Exhaust Manifold Pressure channel configured so data transmitted from ECU to ELC is valid.

The EMAP setting can be enabled by going to the the Config View -> Communications Tab -> Emtron CAN Device -> Emtron Lambda to CAN (ELC/ELCM) Setup and selecting the “Enable EMAP” setting to ON (Figure 6.0). Once enabled to ECU will transmit the EMAP value over the CAN Bus and the ELC will received this value so the correction can be applied.

![](/img/elc/image17.png)

Figure 6.0. Emtune ELC setup menu - EMAP Enable

**NOTE:** Once changed, the setting is automatically stored by the ELC and therefore used on the next power cycle.

# 7.0 ELC Device Configuration

Once the ELC is powered and connected to the ECU’s CAN bus, the following steps should be taken to complete the setup. All setup and device monitoring is done using Emtune so this software needs to be installed and connected to the ECU.

## 7.1 ELC Single Device Setup

This section outlines the setup procedure for a single device and involves 2 steps:

1. Device Detection by the ECU
2. ECU CAN Bus configuration

### 7.11 ELC Device Detection

To confirm the ELC device has been detected, connect to the ECU using Emtune. Open the ECU Runtime menu (F3) and select the Communications Tab. Within this tab there will be a list of Emtron CAN devices the ECU has detected. It will list:

1. CAN Device Model
2. Device Serial Number
3. Device Firmware Version
4. Device Hardware Version
5. CAN Base Address ID

With a single ELC device connected, the data should look as shown in Figure 7.0/7.1.

**Important**:

* At this stage the ECU has only detected the device. It has not been configured to an ECU CAN Channel so the ELC data is not yet available.
* Note the CAN Base Address ID. This is required in the ECU CAN setup. The factory setting is ID 671 for the ELC and ELC2M.

![](/img/elc/image18.png)

Figure 7.0. Example ELC2M device detected by the ECU.

![](/img/elc/image19.png)

Figure 7.1. Example ELC2 device detected by the ECU

### 7.12 ECU CAN Channel Configuration for Single Device

The next step is to configure an ECU CAN channel, allowing the ECU to decode the ELC CAN packets.

For this example, CAN 1- Channel 1 has been selected.

1. Set "Enable" to (ON)
2. Set "CAN Base Address" to the ID shown in Figure 7.0/7.1 In this example its ID 671.
3. Set "DATA Set" to 50 (ELC/ELC2M 1x Device). See Figure 7.2.

The ECU in now configured and reading the data from the ELC Device.

![](/img/elc/image20.png)

Figure 7.2. ELC CAN Configuration

## 7.2 ELC Multiple Device Setup

As mentioned in section 3.5, the Base CAN Address ID used to transmit Data over the Bus by default is the same for each device type. The ELC has a factory CAN Base Address of 671. When multiple ELC devices are installed on the same CAN Bus, each device **MUST** have a unique CAN Base Address to avoid Bus conflicts. This means the CAN Base Address ID will need to be reprogrammed which is a simple task using the ID Reprogramming Tool as outlined in section 7.22.

**REMEMBER:** For this process to function effectively, when multiple **new** devices are introduced to the CAN bus, they should initially be connected **one at a time.** This allows each device to sync up to the CAN Bus baud rate and store that setting. This usually takes 3-5 seconds.

### 7.21 ELC Multiple Device Detection

To confirm the ELC device has been detected, connect to the ECU using Emtune. Open the ECU Runtime menu (F3) and select the Communications Tab. Within this tab there will be a list of Emtron CAN devices the ECU has detected. It will list:

1. CAN Device Model
2. Device Serial Number
3. Device Firmware Version
4. Device Hardware Version
5. CAN Base Address

With multiple ELC devices connected, the CAN Summary List should look as shown in Figure 7.3. In this example x2 ELC2 devices are connected to the BUS. Device 1 with SN 1241 and Device 2 with SN 1242.

![](/img/elc/image21.png)

Figure 7.3. Example show two ELC2 Devices detected by the ECU

**Note:** ALL devices have the same Base Address of ID 671, which is the factory setting for a single device. To avoid Bus conflicts, the factory base address needs to be changed when multiple devices are used, to ensure each device has its own unique ID. When re-programming the Base Address for each device the IDs MUST be:

1. Sequential in order.
2. Have a gap of 2 numbers between each ELC device.

The Base Address ID can be any number but Emtron recommends the following:

* ELC Device 1: ID Base Address 671. (CAN ID Range 671-672)
* ELC Device 2: ID Base Address 722. (CAN ID Range 673-674)
* ELC Device 3: ID Base Address 722. (CAN ID Range 675-676)
* ELC Device 4: ID Base Address 722. (CAN ID Range 677-678)
* ELC Device 5: ID Base Address 722. (CAN ID Range 679-680)
* ELC Device 6: ID Base Address 722. (CAN ID Range 681-682)

### 7.22 ELC CAN Base Address ID Reprogramming

To ensure each ELC device has a unique ID from the example in Figure 7.3, ELC2 Device 2 (SN 1242) needs a new Base Address of 673.

This is easily done using Emtune from the Config view -> Communications Menu -> Emtron CAN Devices -> Emtron CAN Device Programming menu

In this example, ELC Device 2 will need to have its Base Address re-programmed to 673. This is easily done using Emtune from the Config view -> Communications Menu -> Emtron CAN Devices -> Emtron CAN Device Programming menu. In this example select:

![](/img/elc/image22.png)

Device 2 ID Reprogramming

Enter in Serial Number = 1242

Enter in Custom Address = 673

Make sure the “Program Address” checkbox is ticked.

Select the “Program” button and the new Custom Address ID will be programmed into the device.

To check the device has been correctly programmed with the new CAN Base Address, open the F3 menu -> Communications Tab. CAN device 2 with SN 1242 should have a new Base Address of 673. See Figure 7.5

![](/img/elc/image23.png)

Figure 7.5. 2x ELC Devices detected by the ECU with reprogrammed IDs

### 7.23 ECU CAN Configuration for Multiple Devices

The next step is to configure an ECU CAN channel, allowing the ECU to decode the ELC CAN packets.

Only 1 CAN Channel is required for multiple devices. CAN 1 - Channel 4 has been selected. Config as follows:

1. ![](/img/elc/image24.png)Set “Enable" to 1(ON)”
2. Set "CAN Base Address" to the **Lowest** Base Address ID shown in Figure 7.5. In this example its 671.
3. Set "DATA Set" to 51 -Emtron ELC/ELCM 2x Devices (CAN PID 671/673).

The ECU is now configured and will receive data from all devices on IDs 671-672, 673-674.

**NOTE**: You only need to program in the lowest Base Address . The ECU automatically configures the remaining IDs based on the assumption that the IDs are sequential in order.

# 8.0 ECU Channel Configuration

Once the ECU has been configured to receive the ELC data, the next step is assigning the data to an ECU lambda channel(s). There are several options:

**Option A:** Use the Lambda 1 and Lambda 2 Input Channel(s) as shown in Figure 8.0. With a ELC1 set the Lambda 1 to **CAN ELC #1 Ch-A** and for an ELC2 set Lambda 1 to **CAN ELC #1 Ch-A** and Lambda 2 to **CAN ELC #1 Ch-B**.

![](/img/elc/image25.png)

Figure 8.0.

When this option is used the Runtime menu (F3) -> Lambda tab can be used to view the data from both channels. This includes Lambda data and Diagnostics data to help with fault finding should any issues occur. See Figure 8.1.

![](/img/elc/image26.png)

Figure 8.1

**Options B:** Use the Lambda Cylinder Input Channels. This setup is normally done when multiple ELC devices are used to measure the lambda on individual cylinders. Figure 8.2 shows four ELC devices configured, measuring the individual Lambda on an 8-cylinder engine. Example setup:

* To configure the ELC Device 1:
  + Channel A to Cylinder 1; set the Channel Input Source for Lambda Cyl 1 to **CAN ELC #1 Ch-A**
  + Channel B to Cylinder 2; set the Channel Input Source for Lambda Cyl 2 to **CAN ELC #1 Ch-B**
* To configure the ELC Device 2:
  + Channel A to Cylinder 3; set the Channel Input Source for Lambda Cyl 3 to **CAN ELC #2 Ch-A**
  + Channel B to Cylinder 4; set the Channel Input Source for Lambda Cyl 4 to **CAN ELC #2 Ch-B**

… etc for ELC Device 3 and 4

![](/img/elc/image27.png)

Figure 8.2. Multiple ELC devices channel assignments

# 9.0 ELC Custom Device Settings

The following settings are available to control the ELC. These settings get applied to **ALL** ELC devices connected on the CAN bus.

1. Reset CAN IDs to Default
2. Enable Heater Override (See Section 5.0)
3. Enable EMAP (See Section 6.0)
4. ELC Heater RPM Lockout (See Section 5.0)
5. ELC Heater Post Start Lockout (See Section 5.0)
6. ELC Lambda 1 Test Enable
7. ELC Lambda 2 Test Enable

These settings are available from the Config View -> Communications Tab -> Emtron CAN Device -> Emtron Lambda to CAN (ELC/ELCM) Setup". See Figure 9.0

![](/img/elc/image28.png)

Figure 9.0

The ELC Lambda 1 and 2 Test Enable setting will force the ELC device to send the Test Lambda value over the CAN bus. The ECU will read that value and it’s a simple way of confirming the system is calibrated correctly. Make sure this setting is reset back to zero when finished.

**NOTE:** When any custom ELC setting is changed, the setting is automatically stored by the ELC device and therefore used on the next power cycle.

# 10.0 Ordering Information

| Product      | Part Number |
|--------------|-------------|
| Emtron ELC1  | 5123-1      |
| Emtron ELC2  | 5123-2      |
| Emtron ELC2M | 5123-213    |

# Appendices

## Appendix 1 – CAN Bus Data Packaging

This section outlines the CAN Protocol used to communicate with the ELC device(s). If the device is connected to an Emtron ECU, the CAN Bus packet is automatically decoded when CAN ELC Dataset is selected and no additional setup is required. For more information refer to Section 7.0.

This section provides more detailed information on the CAN ID data structure and requires an understanding of both CAN protocols and data packaging.

Baud Rate

The device will Auto-scan the CAN bus until a successful baud rate has been detected. Once detected this rate will be stored by the device and used at the next power up.

The device will scan 3 different Baud rates at 500ms intervals moving from 1Mbaud -> 500kBaud -> 250k Baud -> 1Mbaud and so on.

ELC CAN Data Format

| ID        | 671 /0x28F (Default)       |
|-----------|----------------------------|
| Data      | Lambda Channel 1           |
| ID Type   | Standard 11-bit identifier |
| Direction | Transmit from Device       |
| Length    | 8 bytes                    |
| Tx Rate   | 100Hz/10ms                 |

| CAN ID    | Name           | Start bit | Length (bits) | Byte Order    | Data Type |
|-----------|----------------|-----------|---------------|---------------|-----------|
| 671/0x28F | Index = 0      | 0         | 8             | Little Endian | Unsigned  |
|           | Lambda 1       | 8         | 16            | Little Endian | Unsigned  |
|           | Pump Current 1 | 24        | 16            | Little Endian | Signed    |
|           | Fault 1        | 40        | 8             | Little Endian | Unsigned  |
|           | Status 1       | 48        | 8             | Little Endian | Unsigned  |
|           | Heater 1 DC    | 56        | 8             | Little Endian | Unsigned  |

Continuation:

| CAN ID    | Name           | Multiplier | Offset | Units | Example        |
|-----------|----------------|------------|--------|-------|----------------|
| 671/0x28F | Index = 0      | 1          | 0      |       |                |
|           | Lambda 1       | 0.001      | 0      | La    | 897 = 0.897 La |
|           | Pump Current 1 | 0.001      | 0      | mA    | 132 = 0.132mA  |
|           | Fault 1        | 1          | 0      |       |                |
|           | Status 1       | 1          | 0      |       |                |
|           | Heater 1 DC    | 1          | 0      | %     | 42 = 42%DC     |

| ID        | 672 /0x290 (Default)       |
|-----------|----------------------------|
| Data      | Lambda Channel 2           |
| ID Type   | Standard 11-bit identifier |
| Direction | Transmit from Device       |
| Length    | 8 bytes                    |
| Tx Rate   | 100Hz/10ms                 |

| CAN ID    | Name           | Start bit | Length (bits) | Byte Order    | Data Type |
|-----------|----------------|-----------|---------------|---------------|-----------|
| 672/0x290 | Index = 0      | 0         | 8             | Little Endian | Unsigned  |
|           | Lambda 2       | 8         | 16            | Little Endian | Unsigned  |
|           | Pump Current 2 | 24        | 16            | Little Endian | Signed    |
|           | Fault 2        | 40        | 8             | Little Endian | Unsigned  |
|           | Status 2       | 48        | 8             | Little Endian | Unsigned  |
|           | Heater 2 DC    | 56        | 8             | Little Endian | Unsigned  |

Continuation:

| CAN ID    | Name           | Multiplier | Offset | Units | Example        |
|-----------|----------------|------------|--------|-------|----------------|
| 672/0x290 | Index = 0      | 1          | 0      |       |                |
|           | Lambda 2       | 0.001      | 0      | La    | 897 = 0.897 La |
|           | Pump Current 2 | 0.001      | 0      | mA    | 132 = 0.132mA  |
|           | Fault 2        | 1          | 0      |       |                |
|           | Status 2       | 1          | 0      |       |                |
|           | Heater 2 DC    | 1          | 0      | %     | 42 = 42%DC     |

| Fault 1/2 – Start BIT 40 Length 8 BITS |                                                                                               |
|----------------------------------------|-----------------------------------------------------------------------------------------------|
| Bit 0/1: Virtual Ground                | 0 = Error: Short to ground  1 = Error: IC Power Supply Low  2 = Error: Short to Vbatt  3 = Ok |
| Bit 2/3: Nernst Cell                   | 0 = Error: Short to ground  1 = Error: IC Power Supply Low  2 = Error: Short to Vbatt  3 = Ok |
| Bit 4/5: Pump Current                  | 0 = Error: Short to ground  1 = Error: IC Power Supply Low  2 = Error: Short to Vbatt  3 = Ok |
| Bit 6/7: Heater                        | 0 = Error: Short to ground  1 = Error: IC Open Load  2 = Error: Short to Vbatt  3 = Ok        |

| Status 1/2 - Start BIT 48 Length 8 BITS               |
|-------------------------------------------------------|
| 0 = OFF                                               |
| 1 = Normal Operation                                  |
| 2 = Sensor Warming up                                 |
| 3 = RPM Lockout (when available)                      |
| 4 = Post Start Lockout (when available)               |
| 5 = Reading Calibration Data                          |
| 14 = Heater Under Temperature (cannot reach 650 DegC) |
| 15 = Heater Over Temperature                          |
| 16 = Sensor Shutdown - Thermal Shock                  |
| 17 = Cannot read Chip ID                              |
| 18 = Set Pump reference command Invalid               |
| 19 = Calibrate Command Invalid                        |
| 20 = Standalone Command Invalid                       |
| 21 = Nernst Cal Data Invalid                          |
| 22 = Pump Cal Data Invalid                            |
| 19 = Lambda Stability Error                           |
| 20 = Error Reading Chip ID                            |
| 22 = System Voltage Low                               |
| 22 = Cannot enter Calibration mode                    |
| 23 = Cannot enter standalone mode                     |
