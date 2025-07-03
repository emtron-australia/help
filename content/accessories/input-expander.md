---
title: Emtron Input Expansion to CAN
---

![](/img/iec/image2.jpeg)

EIC10 / EIC16M

Kit Contents

When purchasing an EIC10 the following items are included:

* EIC10 Device with Flying Harness
* Deustch DTM 4-way connector and female pins (DTM06-4S)
* Deustch DTM 12-way connector and male pins (DTM04-12PA)

![](/img/iec/image5.jpeg)

EIC10 kit pictured.

When purchasing an EIC16M the loom side mating Autosport connector is not included but can be purchased separately.


# 1.0 Description

![](/img/iec/image6.jpeg)

**EIC16M**

The EIC16M is a Mil Spec device designed to increase the Input channel capability of all Emtron ECUs with 16 high resolution analog and/or 4 frequency based inputs. The device is connected via CAN bus and will be automatically detected which will significantly minimalize configuration time. The enclosure is made from billet 6061 aluminium and is waterproof, allowing for use in extreme environments. Installation is made simple through use of a Motorsport proven Deutsch Autosport connector system.

![](/img/iec/image7.jpeg)

**EIC10**

The EIC10 is designed to increase the Input channel capability of all Emtron ECUs with 10 high resolution analog inputs and/or 4 frequency based inputs. The device is connected via CAN bus and will be automatically detected which will significantly minimalize configuration time. The waterproof enclosure is extremely compact and made from billet 6061 aluminium. The device implements a flying loom system, terminated with the reliable and environmentally sealed Deutsch DTM connectors.

# 2.0 Specification

**Power Supply**

* Operating Voltage: 7.0 to 22.0 Volts DC
* Operating Current: 30mA at 14.0V
* Reverse Battery Protection with zero current draw
* Battery Transient/Over Current Protection

**Internal**

* 64MHz 16-bit Automotive Processor
* Analog Channel Sampling Rate 1000 Hz

**Inputs - General**

* Analog Inputs
  + Range 0.0V to 5.0V, Resolution. 1.22mV 12 Bit
  + 1st order 1600Hz low pass filter
  + Analog sampling rate of 1000Hz
* Frequency Inputs
  + Range 0.5Hz up to 6500.0Hz, Resolution. 0.1Hz
  + Magnetic and Hall effect sensor compatible
  + Rising Edge Threshold = 1.65V, Falling Edge Threshold = 1.0V

**EIC10 – 10 Analog Inputs**

* ANV1-6: Analog Inputs 0.00V - 5.00V Range
  + Input Impedance 100k to ground
  + Switchable 1k pull-up resistor on ANV5-6 to the 5V Sensor Supply for temperature measurement.
* ANV7-10 / Frequency Input 1-4. Analog or Frequency Inputs
  + Analog Inputs 0.0 – 16.0V Range. Resolution. 3.90mV 12 Bit, suitable for analog inputs and switched inputs.
  + Input Impedance 50k to ground
  + Switchable 1k Pullup with blocking diodes to 8V supply
  + Frequency Range 0.5Hz up to 6500.0Hz, Resolution. 0.1Hz

**EIC16M – 16 Analog Inputs**

* ANV1-12: Analog Inputs 0.0V - 5.00V range.
  + Switchable 1k pull-up resistor on ANV9-12 to the 5V Sensor Supply for temperature measurement.
  + Input Impedance 100k to ground
* ANV13-16 / Frequency Input 1-4
  + Analog Inputs 0.0 – 16.0V Range. Resolution. 3.90mV 12 Bit, suitable for analog inputs and switched inputs.
  + Switchable 1k Pullups with blocking diode to 8V Supply
  + Input Impedance 50k to ground
  + Frequency Range 0.5Hz up to 6500.0Hz, Resolution. 0.1Hz

**Outputs**

* 5V Sensor Supply. Output current 250mA. Short circuit to ground protected.

**Communications**

* CAN 2.0B Baud Rate: 250kBaud, 500kBaud or 1Mbaud Auto Detect
* CAN Transmit Rate Adjustable: 50Hz/100Hz/200Hz/500/1000 Hz

**Operating Temperature**

* Operating Temperature Range: -30 to 100°C (-22 to 212°F)

**Physical**

**EIC16M**

* Enclosure Size 52 mm x 74 mm x 18 mm
* 125g

**EIC10**

* Enclosure Size 63mm x 54 mm x 20mm
* 160g

# 3.0 Installation

Each device has a M4 x 1.5 thread tapped into the base of the enclosure and can be used for mounting. In high vibration applications rubber mounting is recommended.

**CAUTION:** When mounting the device inside the engine compartment, it should be positioned in cooler areas and away from heat sources such as exhaust manifolds. Any unnecessary radiated heat may affect device performance.

## 3.1 EIC10 Pinout

The pinouts are shown below in Table 3.0 and Table 3.1.

![](/img/iec/image8.jpeg)

**Power and CAN Flying Loom Connector: DTM 4 pin (M).**

|     |            |             |
|-----|------------|-------------|
| Pin | Function   | Wire Colour |
| 1   | Ground     | BLACK       |
| 2   | CAN Lo     | GREEN       |
| 3   | CAN Hi     | YELLOW      |
| 4   | 12V Supply | RED         |

Table3.0. EIC10 Power and CAN Deustch Connector Pinout

![](/img/iec/image9.jpeg)
**Analog Input Flying Loom Connector: DTM 12 pin (F).**

|     |                            |               |        |             |
|-----|----------------------------|---------------|--------|-------------|
| Pin | Function                   | Voltage Range | Pullup | Wire Colour |
| 1   | Analog Voltage 1           | 0 - 5.0V      | No     | BRN         |
| 2   | Analog Voltage 2           | 0 - 5.0V      | No     | BLUE        |
| 3   | Analog Voltage 3           | 0 - 5.0V      | No     | GREY        |
| 4   | Analog Voltage 4           | 0 - 5.0V      | No     | W/GREY      |
| 5   | Analog Voltage 5           | 0 - 5.0V      | Yes    | W/BLUE      |
| 6   | 5V Sensor Supply           |               |        | W/BRN       |
| 7   | Analog Sensor 0V Reference |               |        | W/RED       |
| 8   | Analog Voltage 6           | 0 - 5.0V      | Yes    | W/BLACK     |
| 9   | Analog Voltage 7/ Freq 1   | 0 - 16.0V     | Yes    | W/OR        |
| 10  | Analog Voltage 8/ Freq 2   | 0 - 16.0V     | Yes    | OR          |
| 11  | Analog Voltage 9/ Freq 3   | 0 - 16.0V     | Yes    | WHITE       |
| 12  | Analog Voltage 10/Freq 4   | 0 - 16.0V     | Yes    | PUR         |

Table3.1. EIC10 Input Deustch Connector Pinout (DTM06-12SA)

## 3.2 EIC16M Pinout

![](/img/iec/image10.jpeg)

|                                                          |
|----------------------------------------------------------|
| Mating Connector Loom Side (Deutsch Autosport AS Series) |
| AS612-35SA (Yellow)                                      |

|     |                               |               |         |
|-----|-------------------------------|---------------|---------|
| Pin | Function                      | Voltage Range | Pull-Up |
| 1   | 14 V Supply                   |               |         |
| 2   | Ground                        |               |         |
| 3   | CAN Hi                        |               |         |
| 4   | CAN Lo                        |               |         |
| 5   | Analog Voltage 1              | 0.0 – 5.0V    | No      |
| 6   | Analog Voltage 2              | 0.0 – 5.0V    | No      |
| 7   | Analog Voltage 3              | 0.0 – 5.0V    | No      |
| 8   | Analog Voltage 4              | 0.0 – 5.0V    | No      |
| 9   | Analog Voltage 5              | 0.0 – 5.0V    | No      |
| 10  | Analog Voltage 6              | 0.0 – 5.0V    | No      |
| 11  | Analog Voltage 7              | 0.0 – 5.0V    | No      |
| 12  | Analog Voltage 8              | 0.0 – 5.0V    | No      |
| 13  | Analog Voltage 9              | 0.0 – 5.0V    | Yes     |
| 14  | Analog Voltage 10             | 0.0 – 5.0V    | Yes     |
| 15  | Analog Voltage 11             | 0.0 – 5.0V    | Yes     |
| 16  | Analog Voltage 12             | 0.0 – 5.0V    | Yes     |
| 17  | Analog Voltage 13/Frequency 1 | 0.0 – 16.0V   | Yes     |
| 18  | Analog Voltage 14/Frequency 2 | 0.0 – 16.0V   | Yes     |
| 19  | Analog Voltage 15/Frequency 3 | 0.0 – 16.0V   | Yes     |
| 20  | Analog Voltage 16/Frequency 4 | 0.0 – 16.0V   | Yes     |
| 21  | 5.0V Sensor Supply            |               |         |
| 22  | 0V Analog Sensor Reference    |               |         |

Table 3.2. EIC16M Pinout

## 3.3 CAN Bus

The EIC10 or EIC16M can be connected to the Emtron’s CAN Bus 1 or 2.

All devices on the CAN Bus must be configured to use the same baud rate. For this reason, all Emtron CAN devices will Auto-scan the CAN bus until a successful baud rate has been detected. Once detected this rate will be stored and used at the next power up.

The device will scan 3 different Baud rates at 500ms intervals moving from 1Mbaud -> 500kBaud -> 250k Baud -> 1Mbaud and so on.

**NOTE:** For this process to function effectively, when **new** devices are introduced to the CAN bus, they should initially be connected **one at a time.** This allows each device to sync up to the CAN Bus baud rate and store that setting. This typically takes 3-5 seconds.

The EIC10 and EIC16M leave the factory programmed with individual serial numbers, but all have the same Base CAN Address ID used to transmit data over the Bus. The CAN Base address can be adjusted from the factory setting using the ID Reprogramming Tool. This is required when 2 or more of the same devices are connected to the CAN Bus.

**EIC10**.

* Factory CAN Base Address of 718. Transmits data sequentially on the next 3 IDs. Total CAN ID Range is therefore 718 – 721.

**EIC16M**.

* Factory CAN Base Address of 705. Transmits data sequentially on the next 5 IDs. Total CAN ID Range is therefore 705 – 710.

## 3.4 Pullup Resistors

### 3.41 EIC10

**Temperature Sensors: 5V 1k Pull-ups**

Analog Voltage Channels 5 -6 have independent software controlled 1k ohm pull-up resistors to the “5V Sensor Supply”. These are suitable for temperature measurement or as ON/OFF inputs by pulling the input to ground through a switch.

*NOTE: An External 1k resistor can be fitted to other inputs if connecting to a temperature sensor. The 5V Sensor Supply pin should be used as the pullup supply.*

**Switched Inputs: 8V 1k Pull-ups**

The EIC10 has x4 software controlled pullup resistors on ANV7 and ANV10 using a 1k ohm resistor and blocking diode to 8V. (NOTE: These 4 inputs can also be used as frequency inputs). These are suitable for switched inputs allowing the device to read between 0.0 and 16.0V. In this configuration with the pull ON, the switch can be wired to pull the input to ground.

Table 3.1 shows the inputs with software controlled 8V 1k Ohm pullup resistors plus blocking diode.

|        |                             |                     |                     |
|--------|-----------------------------|---------------------|---------------------|
| Pin    | Function                    | Voltage Input Range | Pull-Up             |
| Pin 5  | Analog Voltage 5            | 0.0–5.0V            | Yes – 5.0V – 1k Ohm |
| Pin 8  | Analog Voltage 6            | 0.0–5.0V            | Yes – 5.0V – 1k Ohm |
| Pin 9  | Analog Voltage 7 or Freq 1  | 0.0-16.0V           | Yes – 8.0V – 1k Ohm |
| Pin 10 | Analog Voltage 8 or Freq 2  | 0.0-16.0V           | Yes – 8.0V – 1k Ohm |
| Pin 11 | Analog Voltage 9 or Freq 3  | 0.0-16.0V           | Yes – 8.0V – 1k Ohm |
| Pin 12 | Analog Voltage 10 or Freq 4 | 0.0-16.0V           | Yes – 8.0V – 1k Ohm |

Table 3.1. EIC10 Inputs pullup resistor summary

**NOTE:** The blocking diode on the 8V pullup (ANV7 -10) prevents large frequency based signals back-feeding into the supply. If these channels are to be used for temperature measurement this pullup is not suitable. An external 1k resistor will need to be fitted and pulled up to the 5V Sensor Supply.

### 3.42 EIC16M

**Temperature Sensors: 5V 1k Pull-ups**

Analog Voltage Channels 9 -12 have independent software controlled 5V 1k ohm pullup resistors to the “5V Sensor Supply”. These are suitable for temperature measurement or as ON/OFF inputs by pulling the input to ground through a switch.

The EIC16M has x4 software controlled pullup resistors on ANV9 and ANV12 using a 1k ohm resistor pulled high to the 5V Sensor Supply. These are suitable for temperature sensor inputs.

*NOTE: An External 1k resistor can be fitted to other inputs if connecting to a temperature sensor. The 5V Sensor Supply pin should be used as the pullup supply.*

**Switched Inputs: 8V 1k Pull-ups**

The EIC16M has x4 software controlled pullup resistors on ANV13 and ANV16 using a 1k ohm resistor and blocking diode to 8V These are suitable for switched inputs allowing the device to read between 0.0 and 16.0V. In this configuration with the pull ON, the switch can be wired to pull the input to ground.

A summary is shown in Table 3.2.

|     |                               |                     |            |
|-----|-------------------------------|---------------------|------------|
| Pin | Function                      | Voltage Input Range | Pull-Up    |
| 13  | Analog Voltage 9              | 0.0 – 5.0V          | Yes – 5.0V |
| 14  | Analog Voltage 10             | 0.0 – 5.0V          | Yes – 5.0V |
| 15  | Analog Voltage 11             | 0.0 – 5.0V          | Yes – 5.0V |
| 16  | Analog Voltage 12             | 0.0 – 5.0V          | Yes – 5.0V |
| 17  | Analog Voltage 13/Frequency 1 | 0.0 – 16.0V         | Yes – 8.0V |
| 18  | Analog Voltage 14/Frequency 2 | 0.0 – 16.0V         | Yes – 8.0V |
| 19  | Analog Voltage 15/Frequency 3 | 0.0 – 16.0V         | Yes – 8.0V |
| 20  | Analog Voltage 16/Frequency 4 | 0.0 – 16.0V         | Yes – 8.0V |

Table 3.2. EIC16M Inputs pullup resistor summary

**NOTE:** The blocking diode on the 8V pullup prevents large frequency based signals back-feeding into the supply. If these channels are to be used for temperature measurement this pullup is not suitable. An external 1k resistor will need to be fitted and pulled up to the 5V Sensor Supply.

## 3.5 Frequency Inputs

The EIC10 and EIC16M have 4x Frequency Inputs which get shared with Analog Input pins as shown with Tables 3.3 and 3.4.

* Range 0.5Hz up to 6500.0Hz
* Resolution. 0.1Hz
* Rising Edge Threshold = 1.65V
* Falling Edge Threshold = 1.00V
* 8V independent software selectable 1k Ohm pullup resistors
* Both Falling or Rising Edges are software selectable.

**EIC10**

|        |                                        |
|--------|----------------------------------------|
| Pin 9  | Analog Voltage 7 or Frequency Input 1  |
| Pin 10 | Analog Voltage 8 or Frequency Input 2  |
| Pin 11 | Analog Voltage 9 or Frequency Input 3  |
| Pin 12 | Analog Voltage 10 or Frequency Input 4 |

Table 3.3. EIC10 Frequency Input Summary.

**EIC16M**

|     |                               |
|-----|-------------------------------|
| Pin | Function                      |
| 17  | Analog Voltage 13/Frequency 1 |
| 18  | Analog Voltage 14/Frequency 2 |
| 19  | Analog Voltage 15/Frequency 3 |
| 20  | Analog Voltage 16/Frequency 4 |

Table 3.4. EIC16M Frequency Inputs Input Summary.

**NOTE:** Any EIC configuration changes made from Emtune are immediately sent to the EIC10 or EIC16M device over the CAN Bus and stored automatically by the device.

## 3.6 Noise Immunity

To minimise signal contamination and maximise noise immunity, the wire pairs shown in Table 3.2 must be twisted. It is recommended to twist the wire pairs at a minimum one twist per 40mm of cable. This is very important and should always be implemented.

|          |           |         |
|----------|-----------|---------|
| Pair 1   |           | Pair 2  |
| CAN High | <-------> | CAN Low |

Table 3.3. CAN Hi and Lo wire pairing for twisting

##

## 3.7 Sensor Wiring

**5V Sensor Supply Pin**

This is a 250mA 5V output designed to supply automotive sensors.

**Analog Sensor 0V Reference Pin**

This pin should be connected directly to the 0V (Ground) pin on any low current analog sensor, for example Pressure or Temperature.

* **DO NOT** connect the EIC 0V Reference pin directly to the Engine Block or ECU Ground. This is a dedicated and specialised 0V/ground reference for analog sensors.
* **DO NOT** connect a Sensor 0V/ground pin directly to the Engine Block or Device Ground. Instead this pin should be directly connected to the dedicated EIC 0V Reference pin. See Figure 3.1/3.2.
* **DO NOT** connect frequency based sensor grounds to the EIC 0V Reference pin; for example, an Ethanol content sensor. Use the main device ground.

![](/img/iec/image11.png)

Figure 3.1. Correct MAP Sensor 0V Wiring

![](/img/iec/image12.png)

Figure 3.2. Incorrect MAP Sensor 0V Wiring

## 3.8 CAN Bus Wiring

* CAN Bus High and Low are differential signals, so twisted pair **MUST** be used. Failing to do so will compromise the entire CAN Bus System.
* In some extreme environments, shielded twisted pair may be required to help with reliability and data integrity.
* The less connectors in any transmission system the better. Unnecessary connectors are almost guaranteed to present an impedance discontinuity and hence may cause reflections and data loss.
* CAN Bus termination must be done correctly by using a 120 ohm 0.25W resistor at each END of the bus system.
* Maximum Stub length to a device from the main Bus is recommended at 0.3m, in accordance with High-Speed ISO 11898 Standard specification. See Figure 3.3.

The EIC16M and EIC10 devices do **not** include an on-board CAN termination resistor, allowing the device to be wired at any position on the Bus. CAN Bus termination must be done correctly by using a 120 ohm 0.25W resistor at each end of the bus system as mentioned above. Figures 3.1 and 3.2 show possible CAN Bus Implementation examples.

![](/img/iec/image13.jpg)

Figure 3.1. CAN Bus Wiring Example. ECU and Dash at each end with 120 Ohm Termination

![](/img/iec/image14.jpg)

Figure 3.2. CAN Bus Wiring Example. ECU and EIC10 at each end with 120 Ohm Termination

![](/img/iec/image15.png)

Figure 3.3. CAN Bus Wiring Example. Stub Length less than 0.3m

# 4.0 EIC Device Configuration

Once the EIC10 or EIC16M is powered and connected to the ECU’s CAN bus, the following steps should be taken to complete the setup. All setup and device monitoring is done using Emtune, so this software needs to be installed and connected to the ECU.

## 4.1 EIC Single Device Setup

This section outlines the setup procedure for a single device and involves 3 steps:

1. Device Detection by the ECU
2. ECU CAN Bus configuration
3. EIC Live Data Monitoring

### 4.11 EIC Device Detection

To confirm the EIC device has been detected, connect to the ECU using Emtune. Open the ECU Runtime menu (F3) and select the Communications Tab. Within this tab there will be a list of Emtron CAN devices that the ECU has detected. It will list:

1. CAN Device Model
2. Device Serial Number
3. Device Firmware Version
4. Device Hardware Version
5. CAN Base Address ID

With a single EIC10 device connected, the data should look as shown in Figure 4.0. With a single EIC16M device connected, the data should look as shown in Figure 4.1.

**Important**:

* At this stage the ECU has only detected the device. It has not been configured to an ECU CAN Channel so the EIC data is not yet available.
* Note the CAN Base Address ID. This is required in the ECU CAN setup. The factory setting is ID 718 for the EIC10, and ID 705 for the EIC16M

![](/img/iec/image16.png)
Figure 4.0. EIC10 connected to the CAN Bus

![](/img/iec/image17.png)

Figure 4.1. EIC16M connected to the CAN Bus

### 4.12 ECU CAN Configuration for Single Device

Next step is to configure an ECU CAN channel, allowing the ECU to decode the EIC CAN packets.

For this example, CAN 1- Channel 4 has been selected.

1. Set “Enable" to 1(ON)”
2. Set "CAN Base Address" to the Base Address shown in Figure 4.0 / 4.1. In this example select 718 for EIC10 or 705 for EIC16M.
3. **EIC10**. Set "DATA Set" to 73 (EIC10 1x Device). See Figure 4.2

**EIC16M**. Set "DATA Set" to 69 (EIC16M 1x Device). See Figure 4.3

![](/img/iec/image18.png)

Figure 4.2. EIC10 CAN Configuration

![](/img/iec/image19.png)

Figure 4.3. EIC16M CAN Configuration

### 4.13 EIC Data Monitoring for Single Device

To confirm the EIC data is being decoded by the ECU, open the ECU runtime menu (F3) -> Emtron CAN Device Tab. The EIC10/EIC16M live data can be viewed. See Figure 4.4 and 4.5.

![](/img/iec/image20.png)
![](/img/iec/image21.png)

Figure 4.4. EIC10 CAN Live Data – x1 Device

##

Figure 4.5. EIC16M CAN Live Data– x1 Device

## 4.2 EIC CAN Base Address ID Reprogramming

The default CAN Base Address can be changed at any time.

This is easily done using Emtune from the Config view -> Communications Menu -> Emtron CAN Devices -> Emtron CAN Device Programming menu. This example shows the CAN Base address being changed from the default 718 to 722.

![](/img/iec/image22.png)

1. Enter in Serial Number = 1262
2. Enter new Custom Address = 722
3. Make sure the “Program Address” checkbox is ticked.
4. Select the “Program” button and the new Custom Address ID will be programmed into the device.

To check the device(s) have been programmed correctly with the new Base Address, open the ECU Runtime menu (F3)-> Communications Tab. Each device now has a unique Base Address ID. See Figure 4.8 shows before the program and Figure 4.9 after the program.

![](/img/iec/image23.jpg)

Figure 4.8. EIC10 CAN ID Default

![](/img/iec/image24.jpg)

Figure 4.9. EIC10 CAN ID Re-programmed

###

# 5.0 ECU Channel Configuration

Once the ECU has been configured to receive the EIC4/ECIC16M data, the next step is assigning the data to an ECU channel(s). The example shown in Figure 5.0 shows the following channel assignments:

* Compressor Inlet Pressure assigned to EIC16M channel 1
* Compressor Outlet Pressure assigned to EIC16M channel 2
* Compressor Inlet Temperature assigned to EIC16M channel 9
* Compressor Outlet Temperature assigned to EIC16M channel 10

**NOTE:** EIC16M pullup control is done through the Config View-> Communications -> Emtron CAN Devices -> Emtron Input to CAN Expansion menu. See Section 6.2 for more information.

![](/img/iec/image25.png)

Figure 5.0

##

# 6.0 EIC Custom Settings

The EIC10 and EIC16M have custom settings available for:

* Transmit Rates
* Pullup configurations
* Frequency Edge selection

**NOTE:** When any custom EIC setting is changed, the setting is automatically stored by the EIC device and therefore used on the next power cycle.

**CAN Transmit Rates**

The data is separated into 3 categories and can be independently adjusted. There are:

* Analog Voltage Channels 1-10 (EIC10) / Analog Voltage Channels 1-12 (EIC16M)
* Analog Voltage Channels 13-16 (EIC16M
* Frequency 1-4

For these setting see Config view-> Communications -> Emtron CAN Devices -> Emtron Input to CAN Expansion. Inside this menu will be an EIC10 and EIC16M menu. The Default value is 200Hz. It can be adjusted to suit the application and available CAN Bandwidth.

There are 4 options available.

* 200 Hz (Default)
* 50 Hz
* 100Hz
* 500Hz

![](/img/iec/image26.png)

Figure 6.0. EIC10 Transmit Rate setup

![](/img/iec/image27.png)

Figure 6.1. EIC16M Transmit Rate setup

**Pullup Resistor Control**

Section 3.5 previously summarises the Pullup options.

To adjust these setting see Config view-> Communications -> Emtron CAN Devices -> Emtron Input to CAN Expansion

![](/img/iec/image28.png)

Figure 6.2. EIC10 Pullup Settings

![](/img/iec/image29.png)

Figure 6.3. EIC16M Pullup Settings

**Frequency Channel**

Section 3.5 previously summarises the Frequency options. There are 3 frequency modes that can be selected:

* OFF
* Falling Edge
* Rising Edge

The Inputs can accept signals from Magnetic or Hall effect sensors. Magnetic sensors should have the edge selected to Falling. To adjust these setting see Config view-> Communications -> Emtron CAN Devices -> Emtron Input to CAN Expansion menu.

**NOTE:** The Frequency will not read until the Input Channel is selected to ON (i.e. Falling or Rising edge).

![](/img/iec/image30.png)

Figure 6.4. EIC10 Frequency Input Settings

![](/img/iec/image31.png)

Figure 6.5. EIC16M Frequency Input Settings

# 7.0 Ordering Information

| Product       | Part Number |
|---------------|-------------|
| Emtron EIC10  | 593-10      |
| Emtron EIC16M | 593-1613    |
|               |             |

# Appendices

## Appendix 1. CAN Bus Data Packaging

This section outlines the CAN Protocol used to communicate with the EIC device(s). If the device is connected to an Emtron ECU, the CAN Bus packet is automatically decoded when correct CAN Dataset is selected and no additional setup is required. For more information refer to Section 4.0.

This section provides more detailed information on the CAN ID data structure and requires an understanding of both CAN protocols and data packaging.

Baud Rate

The EIC will Auto-scan the CAN bus until a successful baud rate has been detected. Once detected this rate will be stored by the device and used at the next power up.

The device will scan 3 different Baud rates at 500ms intervals moving from 1Mbaud -> 500kBaud -> 250k Baud -> 1Mbaud and so on.

EIC16M CAN Data Format

| ID        | 705 /0x2C1 (Default)           |
|-----------|--------------------------------|
| Data      | Voltage 3dp                    |
| ID Type   | Standard 11-bit identifier     |
| Direction | Transmit from Device           |
| Length    | 8 bytes                        |
| Tx Rate   | Adjustable (50/100/200/500 Hz) |

|           |              |           |               |               |           |
|-----------|--------------|-----------|---------------|---------------|-----------|
| CAN ID    | Name         | Start bit | Length (bits) | Byte Order    | Data Type |
| 705/0x2C1 | AN Voltage 1 | 0         | 16            | Little Endian | Unsigned  |
|           | AN Voltage 2 | 16        | 16            | Little Endian | Unsigned  |
|           | AN Voltage 3 | 32        | 16            | Little Endian | Unsigned  |
|           | AN Voltage 4 | 48        | 16            | Little Endian | Unsigned  |
| 705/0x2C1 | AN Voltage 1 | 0.001      | 0      | V     | 0.0 V | 5.0V | CAN 3046 = 3.046V |
|           | AN Voltage 2 | 0.001      | 0      | V     | 0.0 V | 5.0V |                   |
|           | AN Voltage 3 | 0.001      | 0      | V     | 0.0 V | 5.0V |                   |
|           | AN Voltage 4 | 0.001      | 0      | V     | 0.0 V | 5.0V |                   |

|           |                                |
|-----------|--------------------------------|
| ID        | 706 /0x2C2 (Default)           |
| Data      | Voltage 3dp                    |
| ID Type   | Standard 11-bit identifier     |
| Direction | Transmit from Device           |
| Length    | 8 bytes                        |
| Tx Rate   | Adjustable (50/100/200/500 Hz) |

|           |              |           |               |               |           |
|-----------|--------------|-----------|---------------|---------------|-----------|
| CAN ID    | Name         | Start bit | Length (bits) | Byte Order    | Data Type |
| 706/0x2C2 | AN Voltage 5 | 0         | 16            | Little Endian | Unsigned  |
|           | AN Voltage 6 | 16        | 16            | Little Endian | Unsigned  |
|           | AN Voltage 7 | 32        | 16            | Little Endian | Unsigned  |
|           | AN Voltage 8 | 48        | 16            | Little Endian | Unsigned  |
| 706/0x2C2 | AN Voltage 5 | 0.001      | 0      | V     | 0.0 V | 5.0V | CAN 3046 = 3.046V |
|           | AN Voltage 6 | 0.001      | 0      | V     | 0.0 V | 5.0V |                   |
|           | AN Voltage 7 | 0.001      | 0      | V     | 0.0 V | 5.0V |                   |
|           | AN Voltage 8 | 0.001      | 0      | V     | 0.0 V | 5.0V |                   |

|           |                                |
|-----------|--------------------------------|
| ID        | 707 /0x2C3 (Default)           |
| Data      | Voltage 3dp                    |
| ID Type   | Standard 11-bit identifier     |
| Direction | Transmit from Device           |
| Length    | 8 bytes                        |
| Tx Rate   | Adjustable (50/100/200/500 Hz) |

|           |               |           |               |               |           |
|-----------|---------------|-----------|---------------|---------------|-----------|
| CAN ID    | Name          | Start bit | Length (bits) | Byte Order    | Data Type |
| 707/0x2C3 | AN Voltage 9  | 0         | 16            | Little Endian | Unsigned  |
|           | AN Voltage 10 | 16        | 16            | Little Endian | Unsigned  |
|           | AN Voltage 11 | 32        | 16            | Little Endian | Unsigned  |
|           | AN Voltage 12 | 48        | 16            | Little Endian | Unsigned  |
| 707/0x2C3 | AN Voltage 9  | 0.001      | 0      | V     | 0.0 V | 5.0V | CAN 3046 = 3.046V |
|           | AN Voltage 10 | 0.001      | 0      | V     | 0.0 V | 5.0V |                   |
|           | AN Voltage 11 | 0.001      | 0      | V     | 0.0 V | 5.0V |                   |
|           | AN Voltage 12 | 0.001      | 0      | V     | 0.0 V | 5.0V |                   |

|           |                                |
|-----------|--------------------------------|
| ID        | 708 /0x2C4 (Default)           |
| Data      | Voltage 3dp                    |
| ID Type   | Standard 11-bit identifier     |
| Direction | Transmit from Device           |
| Length    | 8 bytes                        |
| Tx Rate   | Adjustable (50/100/200/500 Hz) |

|           |               |           |               |               |           |
|-----------|---------------|-----------|---------------|---------------|-----------|
| CAN ID    | Name          | Start bit | Length (bits) | Byte Order    | Data Type |
| 708/0x2C4 | AN Voltage 13 | 0         | 16            | Little Endian | Unsigned  |
|           | AN Voltage 14 | 16        | 16            | Little Endian | Unsigned  |
|           | AN Voltage 15 | 32        | 16            | Little Endian | Unsigned  |
|           | AN Voltage 16 | 48        | 16            | Little Endian | Unsigned  |
| 708/0x2C4 | AN Voltage 13 | 0.001      | 0      | V     | 0.0 V | 16.5V | CAN 13046 = 13.046V |
|           | AN Voltage 14 | 0.001      | 0      | V     | 0.0 V | 16.5V |                     |
|           | AN Voltage 15 | 0.001      | 0      | V     | 0.0 V | 16.5V |                     |
|           | AN Voltage 16 | 0.001      | 0      | V     | 0.0 V | 16.5V |                     |


| ID        | 709 /0x2C5 (Default)           |
|-----------|--------------------------------|
| Data      | Frequency 1dp                  |
| ID Type   | Standard 11-bit identifier     |
| Direction | Transmit from Device           |
| Length    | 8 bytes                        |
| Tx Rate   | Adjustable (50/100/200/500 Hz) |


| CAN ID    | Name        | Start bit | Length (bits) | Byte Order    | Data Type |
|-----------|-------------|-----------|---------------|---------------|-----------|
| 709/0x2C5 | Frequency 1 | 0         | 16            | Little Endian | Unsigned  |
|           | Frequency 2 | 16        | 16            | Little Endian | Unsigned  |
|           | Frequency 3 | 32        | 16            | Little Endian | Unsigned  |
|           | Frequency 4 | 48        | 16            | Little Endian | Unsigned  |
| 709/0x2C5 | Frequency 1 | 0.1        | 0      | Hz    | 0   | 20000 | CAN 65201 = 6520.1 |
|           | Frequency 2 | 0.1        | 0      | Hz    | 0   | 20000 |                    |
|           | Frequency 3 | 0.1        | 0      | Hz    | 0   | 20000 |                    |
|           | Frequency 4 | 0.1        | 0      | Hz    | 0   | 20000 |                    |



| ID        | 710 /0x2C6 (Default)       |
|-----------|----------------------------|
| Data      | Sensor Supply              |
| ID Type   | Standard 11-bit identifier |
| Direction | Transmit from Device       |
| Length    | 2 bytes                    |
| Tx Rate   | 20Hz (fixed)               |

| CAN ID    | Name             | Start bit | Length (bits) | Byte Order    | Data Type |
|-----------|------------------|-----------|---------------|---------------|-----------|
| 710/0x2C6 | 5V Analog Supply | 0         | 16            | Little Endian | Unsigned  |
| 710/0x2C6 | 5V Analog Supply | 0.001      | 0      | V     | 0.0 V | 5.5V | CAN 4989 = 4.989V |

EIC10 CAN Data Format


| ID        | 718 /0x2CE (Default)           |
|-----------|--------------------------------|
| Data      | Voltage 3dp                    |
| ID Type   | Standard 11-bit identifier     |
| Direction | Transmit from Device           |
| Length    | 8 bytes                        |
| Tx Rate   | Adjustable (50/100/200/500 Hz) |


| CAN ID    | Name         | Start bit | Length (bits) | Byte Order    | Data Type |
|-----------|--------------|-----------|---------------|---------------|-----------|
| 718/0x2CE | AN Voltage 1 | 0         | 16            | Little Endian | Unsigned  |
|           | AN Voltage 2 | 16        | 16            | Little Endian | Unsigned  |
|           | AN Voltage 3 | 32        | 16            | Little Endian | Unsigned  |
|           | AN Voltage 4 | 48        | 16            | Little Endian | Unsigned  |
| 718/0x2CE | AN Voltage 1 | 0.001      | 0      | V     | 0.0 V | 5.0V | CAN 3046 = 3.046V |
|           | AN Voltage 2 | 0.001      | 0      | V     | 0.0 V | 5.0V |                   |
|           | AN Voltage 3 | 0.001      | 0      | V     | 0.0 V | 5.0V |                   |
|           | AN Voltage 4 | 0.001      | 0      | V     | 0.0 V | 5.0V |                   |


| ID        | 719 /0x2CF (Default)           |
|-----------|--------------------------------|
| Data      | Voltage 3dp                    |
| ID Type   | Standard 11-bit identifier     |
| Direction | Transmit from Device           |
| Length    | 8 bytes                        |
| Tx Rate   | Adjustable (50/100/200/500 Hz) |


| CAN ID    | Name         | Start bit | Length (bits) | Byte Order    | Data Type |
|-----------|--------------|-----------|---------------|---------------|-----------|
| 719/0x2CF | AN Voltage 5 | 0         | 16            | Little Endian | Unsigned  |
|           | AN Voltage 6 | 16        | 16            | Little Endian | Unsigned  |
|           | AN Voltage 7 | 32        | 16            | Little Endian | Unsigned  |
|           | AN Voltage 8 | 48        | 16            | Little Endian | Unsigned  |
| 719/0x2CF | AN Voltage 5 | 0.001      | 0      | V     | 0.0 V | 5.0V | CAN 3046 = 3.046V |
|           | AN Voltage 6 | 0.001      | 0      | V     | 0.0 V | 5.0V |                   |
|           | AN Voltage 7 | 0.001      | 0      | V     | 0.0 V | 5.0V |                   |
|           | AN Voltage 8 | 0.001      | 0      | V     | 0.0 V | 5.0V |                   |


| ID        | 720 /0x2D0 (Default)                |
|-----------|-------------------------------------|
| Data      | Voltage 3dp                         |
| ID Type   | Standard 11-bit identifier          |
| Direction | Transmit from Device                |
| Length    | 6 bytes                             |
| Tx Rate   | Adjustable (50/100/200/500/1000 Hz) |

| CAN ID    | Name               | Start bit | Length (bits) | Byte Order    | Data Type |
|-----------|--------------------|-----------|---------------|---------------|-----------|
| 720/0x2D0 | AN Voltage 9       | 0         | 16            | Little Endian | Unsigned  |
|           | AN Voltage 10      | 16        | 16            | Little Endian | Unsigned  |
|           | 5V Analog Supply   | 32        | 16            | Little Endian | Unsigned  |
|           | Device Temperature | 48        | 8             |               | Unsigned  |
|           | Device Supply      | 56        | 8             |               | Unsigned  |
| 720/0x2D0 | AN Voltage 9       | 0.001      | 0      | V     | 0.0 V | 5.0V | CAN 3046 = 3.046V |
|           | AN Voltage 10      | 0.001      | 0      | V     | 0.0 V | 5.0V |                   |
|           | 5V Analog Supply   | 0.001      | 0      | V     | 0.0 V | 5.5V | CAN 4989 = 4.989V |
|           | Device Temperature | 0.1        | -50    | DegC  | -50   | 250  | CAN 91 = 41DegC   |
|           | Device Supply      | 0.1        | 0      | V     | 0.0 V | 25.5 | CAN 141 = 14.1V   |

| ID        | 721 /0x2D1 (Default)                |
|-----------|-------------------------------------|
| Data      | Frequency 1dp                       |
| ID Type   | Standard 11-bit identifier          |
| Direction | Transmit from Device                |
| Length    | 8 bytes                             |
| Tx Rate   | Adjustable (50/100/200/500/1000 Hz) |

| CAN ID    | Name        | Start bit | Length (bits) | Byte Order    | Data Type |
|-----------|-------------|-----------|---------------|---------------|-----------|
| 721/0x2D1 | Frequency 1 | 0         | 16            | Little Endian | Unsigned  |
|           | Frequency 2 | 16        | 16            | Little Endian | Unsigned  |
|           | Frequency 3 | 32        | 16            | Little Endian | Unsigned  |
|           | Frequency 4 | 48        | 16            | Little Endian | Unsigned  |
| 721/0x2D1 | Frequency 1 | 0.1        | 0      | Hz    | 0   | 20000 | CAN 65201 = 6520.1 |
|           | Frequency 2 | 0.1        | 0      | Hz    | 0   | 20000 |                    |
|           | Frequency 3 | 0.1        | 0      | Hz    | 0   | 20000 |                    |
|           | Frequency 4 | 0.1        | 0      | Hz    | 0   | 20000 |                    |

## Appendix B. Magneto-Resistive Sensors

Magneto-resistive (MR) sensors are commonly used in driver assistance systems such as ABS, TCS and ESP to measure wheel speed, the frequency being proportional to the rotational speed of the wheel. These sensors detect a magnetic field and because there is no electrical contact the sensor can operate across a relatively large air gap. The amplitude of the output signal does not depend on speed.

These are active sensors which means they become “active” when a power supply is connected to it and a digital output waveform is then generated. However, the signal does not switch to ground like a conventional Hall sensor. Instead the signal swings between a high and low voltage, with the swing voltage dependant on the current passing through the sensor, i.e. the value of the pullup or pulldown current limiting resistor. Typical currents required to make to the sensor operate are 4 – 8mA.

Two important checks must be completed.

1. The polarity of the sensor must be correct.
2. The pullup/pulldown resistor might need adjustment to ensure it the digital signal swings within the correct levels. For the EIC16 this is 1.0V low and 1.8V high.

**Sensor Polarity**

The sensor polarity can be determined by measuring the diode voltage drop across the sensor, (sensor resistance cannot be used) using a Multimeter. The direction with the highest voltage drop is the correct polarity. See Table 6.0 as an example. Pin 1 should be connected to the pullup resistor and pin 2 should be connected the ground.

| Diode Voltage Drop | Pin 1    | Pin 2    | Notes              |                                         |
|--------------------|----------|----------|--------------------|-----------------------------------------|
| 1.781 V            | Positive | Negative | Correct Polarity   | {{% icon icon="check" style="green" %}} |
| 0.637 V            | Negative | Positive | Incorrect Polarity | {{% icon icon="xmark" style="red" %}}   |

Table 6.0

**Device Connection**

An MT sensor can be connected directly to an Emtron ECU and the internal Scope function can be used to view the signal. Once you have the signal image, config the pullup resistor and correctly set the arming threshold.

Due to the variation in sensor outputs the EIC Device requires an interface device to condition the signal to match the factory EIC thresholds (1.0V low and 1.8V high).

**Sensor Supply and Wiring**

![](/img/iec/image36.jpg)

The sensor is powered through a pullup resistor. The minimum supply voltage is 8V, ideally a regulated supply should be used to ensure consistent readings. Figure 6.0 illustrates how the sensor should be wired.

**NOTE:** If the pullup resistor is too big there will be insufficient current to make the output switch. Typical Pullup resistor range is 330 Ohms to 1000 Ohms.

**NOTE:** The Low and High outputs levels will vary with different sensors, so for signal integrity each sensor output should be checked using an oscilloscope. Table 6.1 show some typical results from a Toyota Sensor

Figure 6.0. Sensor Wiring

|        |                    |            |             |                  |                                                             |
|--------|--------------------|------------|-------------|------------------|-------------------------------------------------------------|
| Supply | Pullup  Resistance | Low Output | High Output | Switching  Range | Comments                                                    |
| 5V     | 330 Ohms           | 5.2V       | 5.2V        | 0.0V             | {{% icon icon="xmark" style="red" %}} Insufficient Current  |
| 8V     | 330 Ohms           | 3.6V       | 5.9V        | 2.3V             | {{% icon icon="check" style="green" %}}    (see Figure 6.1) |
| 12V    | 330 Ohms           | 7.6V       | 9.9V        | 2.3V             | {{% icon icon="check" style="green" %}}                     |
| 8V     | 470 Ohms           | 5.25V      | 5.25V       | 0.0V             | {{% icon icon="xmark" style="red" %}}  Insufficient Current |
| 12V    | 470 Ohms           | 6.3V       | 9.45V       | 3.15V            | {{% icon icon="check" style="green" %}}                     |

Table 6.1

![](/img/iec/image37.jpeg)

Figure 6.1 shows a scope trace of a MR Sensor with 330R pullup supplied at 8V. The High Output level is 5.9V and the Low Output Level is 3.6V.

Figure 6.1. Scope trace of MR Sensor.
