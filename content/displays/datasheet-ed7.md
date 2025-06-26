---
title: "Emtron ED7 Datasheet"
revision: 1
---

![ED7 Front View](/img/ed7_front.png)
![ED7 Rear View](/img/ed7_rear.png)

## 1.0 General

### Power Supply

- Operating voltage: 7.20V to 20.0V DC
- Operating current: 800 mA at 14.0V 50% Backlight Duty Cycle(excluding
  sensor and load currents)
- Reverse battery protection

### Operating Temperature

- Max operating range: -30 to 85°C (-22 to 230°F)

### Physical

- Aluminium 6061 grade CNC billet enclosure
- Enclosure size 284 X 140mm
- Weight: 1310g
- Connector system: 55 Pin Circular Mil Spec Series III Connector
- Pin diameter: 1 mm
- Current rating: maximum 5.0A per pin at 22AWG

### Internal: Specification of the SoM

- NXP® i.MX 8M Plus Quad Core 
- 4 x Arm Cortex A-53
- 1 x Arm Cortex-M7 CPU 1.8GHz Core
- Arm Cortex M4 170MHz Microcontroller
- eMMC 32GB + 32GB external = 64GB total storage
- Gigabit Ethernet 
- On-Board 6-axis IMU with 3-axis accelerometer and 3-axis gyroscope

## 2.0 Main Features

- 7.0 inch TFT Screen -- 1280 x 768 Resolution
- Anti Glare / Scratch Resistant Optical Bonded Glass
- 16x High Intensity RGB  LEDs
- High Speed Gigabit Ethernet 1000Mbps 
- High Speed Logging (Up to 2000Hz)
- eMMC 64GB On-board logging memory
- Real-Time clock for datalogging
- 3-axis Accelerometer and 3-axis Gyroscope
- 2x CAN Bus
- 2x Video Input
- 6 x Analog External 0.0 -5.0V Inputs (see Pinout)
- Selectable CAN 120 Ohm Termination

## 4.0 Analog Inputs

6x Analog Voltage

- Accepts a 0.0 - 5.0V Analog input. Resolution is 1.22mV (12-Bit)
- Selectable 1k Ohm pull-up resistor to 5V Sensor Supply on ANV1 -- ANV4
- Selectable Range control on ANV5 -- ANV8; 0.0- 5.0V or 0.0 - 15.6V
- Input Impedance 100k Ohms to ground
- Sample Rate 2000Hz

## 5.0 Frequency Inputs

4x Frequency Inputs

- Tolerant of inputs signals -50.0V to 50.0V
- Accepts Magnetic and Hall effect signals.
- User adjustable trigger thresholds from -10.0V to 10.0V with 0.25V
  built in hysteresis.
- Range 0.1Hz up to 20,000.0Hz, Resolution. 0.1Hz
- Input Impedance 100k Ohms to ground
- Selectable 4k7 Ohm pull-up resistor to 8.5V

## 6.0 Analog Video Inputs

- Accepts Analog baseband video signals.
- 2x Composite Inputs OR 1x S-Video Inputs

## 7.0 Communications

- 1x High Speed Gigabit Ethernet 1000Mbps IPv6
  - Auto IP Config
- 2x CAN 2.0B
  - ESD Protection
  - Selectable 120 Ohm Termination Resistors
- 1 x RS232
- 1 x USB C
- 1 x Wi-Fi IEEE 802.11 ac/a/b/g/n Dual-Band (2.4/5 GHz)
- 1 x Bluetooth 5/BLE

## 8.0 Infield firmware update

Full In-field firmware updatable over Ethernet using the Emtron Display
Setup Tool

## 9.0 Voltage and Ground Supplies

### 1x 14V Supply Input
- 5.0A Max (pin limited)
- 7.2V - 20.0V Range
- Supplies Device power

### 1x Backup Supply Input
- 5.0A Max (pin limited)
- 7.2V - 20.0V Range
- Supplies device power during shutdown

### 1x 5.0V Sensor Supply
- 5V Sensor Supply, Output current 400mA
- Accuracy: +/- 0.8% at 25 °C
- Short circuit, Reverse Battery Protection, Thermal overload protection
- Operating temperature range -40°C \~ 85°C

### 1x 12.0V Regulated Output
- 12V Regulated Supply, Output current 700mA
- Accuracy: +/- 1.0% at 25 °C
- Short circuit, Reverse Battery Protection, Thermal overload protection
- Operating temperature range -40°C \~ 85°C

### 1x Main Ground
- 5.0 A pin Limited

### 1x Analog Input 0V Reference
- Analog Sensor 0V Reference with short to battery protection

### 1x Speed 0V Reference
- Speed Sensor 0V Reference with short to battery protection

## 10.0 Pinout {#pinout}

Connector Superseal 34-Way KEY 1

![Image](</img/superseal-34-key1.png>)

| Pin | Channel Name              | Pin | Channel Name                   |
|:---:|:--------------------------|:---:|:-------------------------------|
|  1  | 14V Switched Supply       | 18  | Gigabit Ethernet +Tx/Rx Pair 1 |
|  2  | 14V Backup Supply         | 19  | Gigabit Ethernet -Tx/Rx Pair 1 |
|  3  | Sensor Supply: 5.0V       | 20  | Gigabit Ethernet -Tx/Rx Pair 3 |
|  4  | Analog Input Channel 1    | 21  | Gigabit Ethernet +Tx/Rx Pair 3 |
|  5  | Analog Input Channel 2    | 22  | Speed Input 1                  |
|  6  | Analog Input Channel 3    | 23  | Speed Input 2                  |
|  7  | Analog Input Channel 4    | 24  | Speed Input 3                  |
|  8  | Analog Input Channel 5    | 25  | Speed Input 4                  |
|  9  | Analog Input Channel 6    | 26  | Gigabit Ethernet +Tx/Rx Pair 2 |
| 10  | 12V Regulated Output 2    | 27  | Gigabit Ethernet -Tx/Rx Pair 2 |
| 11  | RS232 Transmit Output     | 28  | Gigabit Ethernet +Tx/Rx Pair 4 |
| 12  | RS232 Receive Input       | 29  | Gigabit Ethernet -Tx/Rx Pair 4 |
| 13  | 0V Reference OUT          | 30  | CAN 1 High                     |
| 14  | Analog Input 0V Reference | 31  | CAN 1 Low                      |
| 15  | Video 0V Reference        | 32  | CAN 2 High                     |
| 16  | Video Input 1             | 33  | CAN 2 Low                      |
| 17  | Video Input 2             | 34  | Ground                         |

## Function Pin Assignment

### Power

| Pin | Channel Name        |
|-----|---------------------|
| 1   | 14V Supply +        |
| 34  | Ground -            |
| 2   | 14V Backup Supply + |

### Sensor Supply

| Pin | Channel Name        |
|-----|---------------------|
| 3   | Sensor Supply 5V    |
| 14  | Sensor 0V Reference |

### Gigabit Ethernet Communications T-568A Standard

| Emtron Pin | RJ45 Pin T-568A | Description             | Cat5e Wire Colour |
|------------|-----------------|-------------------------|-------------------|
| 18         | 1               | Ethernet Tx/Rx + Pair 1 | Green/White       |
| 19         | 2               | Ethernet Tx/Rx - Pair 1 | Green             |
| 26         | 3               | Ethernet Tx/Rx + Pair 2 | Orange/White      |
| 27         | 6               | Ethernet Tx/Rx - Pair 2 | Orange            |
| 20         | 4               | Ethernet Tx/Rx + Pair 3 | Blue              |
| 21         | 5               | Ethernet Tx/Rx - Pair 3 | Blue/White        |
| 28         | 7               | Ethernet Tx/Rx + Pair 4 | Brown/White       |
| 29         | 8               | Ethernet Tx/Rx - Pair 4 | Brown             |

> NOTE: The Orange/White and Brown/White can often look very similar in colour so make sure the correct wire is used

### CAN Communications

| Pin | Channel Name |
|-----|--------------|
| 30  | CAN 1 High   |
| 31  | CAN 1 Low    |
| 32  | CAN 2 High   |
| 33  | CAN 2 Low    |

### RS232/LIN Communications

| Pin | Channel Name          |
|-----|-----------------------|
| 11  | RS232 Transmit Output |
| 12  | RS232 Receive Input   |
| 13  | 0V Reference Out      |

{{% badge style="note" %}}[See Important Wiring Notes below](#rs232-communications){{% /badge %}}

### Analog Inputs

| Pin | Channel Name              | Voltage Range         |
|-----|---------------------------|-----------------------|
| 4   | Analog Input Channel 1    | 0 – 5.0V              |
| 5   | Analog Input Channel 2    | 0 – 5.0V              |
| 6   | Analog Input Channel 3    | 0 – 5.0V              |
| 7   | Analog Input Channel 4    | 0 – 5.0V              |
| 8   | Analog Input Channel 5    | 0 – 5.0V or 0 – 16.0V |
| 9   | Analog Input Channel 6    | 0 – 5.0V or 0 – 16.0V |
| 14  | Analog Input 0V Reference |                       |


> NOTE: ANV 5-6 pins have selectable input ranges; 0 – 5.0V or 0 – 16.0V

### Speed Inputs

| Pin | Channel Name                   |
|-----|--------------------------------|
| 22  | Speed Input 1                  |
| 23  | Speed Input 2                  |
| 24  | Speed Input 3                  |
| 25  | Speed Input 4                  |
| 13  | 0V Reference Out (if required) |

### Video Inputs

| Pin | Channel Name       |
|-----|--------------------|
| 16  | Video Input 1      |
| 17  | Video Input 2      |
| 15  | Video 0V Reference |

## 10.2 Important Wiring Notes

### 14V Switched Supply (Pin 1)

This is a switched 14V supply. Constant power should not be supplied on this pin.

### 14V Backup Supply (Pin 2)

A Constant 14V supply should be wired to this pin. When the power is removed from pin "14V Switched Supply" the ED10M automatically switches to the " 14V Backup Supply” to keep itself powered.  This will allow the ED10M to complete critical tasks before shutting itself down (for example data logging storage).

NOTE: When the “14V Backup Supply” is wired to the ED10M, no additional current is drawn when the device is OFF.

### Analog Sensor 0V Reference (Pin 14)

As the name indicates these should be connected directly to the 0V (Ground) pin on any low current analog sensor, for example Pressure or Temperature.

* {{% icon style="warning" %}} **DO NOT** connect these pins directly to the Engine Block or ED10M Ground. These are dedicated and specialised ground outputs for all analog channels and should be connected directly to the sensor.
* {{% icon style="warning" %}} **DO NOT** connect speed-based sensors to this ground, use the Speed 0V Reference Pin 51.

### Mic 0V Reference Pin 46

This is a dedicated 0V reference for the microphone.

{{% badge style="warning" %}}Do not share this pin{{% /badge %}}

### Video Input Config

Video inputs are multiplexed, only one input can be captured at a time.

 * x4 Composite Video
 * x2 S-Video:
   * Y input on AIN1
   * C input on AIN2
   * Y input on AIN3
   * C input on AIN4

### RS232 Communications

Pin 40 is the ED10M RS232 Transmit Output.  As the name suggests this is an Output and should be connected to the Receive Input of the wired external device.

Pin 41 is the ED10M RS232 Receive Input.  As the name suggests this is an Input and should be connected to the Transmit Output of the wired external device.

This is the wiring standard when working with RS232 communications.

### ED10M Recovery (Pin 55)

In the unlikely event the SOM becomes bricked after a software update, grounding this pin at power-on allows the device to be recovered by loading software through the USB Port. (Normally this would be done over Ethernet using the Display Editor software )

