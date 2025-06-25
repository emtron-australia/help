---
title: "Pinout - ED7"
---

## Connector: Superseal 34-Way KEY 1

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
| 13  | 0V Reference Ou       |

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

## Important Notes

### 14V Switched Supply (Pin 1)

This is a switched 14V supply. Constant power should not be supplied on this pin.

### 14V Backup Supply (Pin 2)

A Constant 14V supply should be wired to this pin. When the power is removed from pin "14V
Switched Supply" the ED7 automatically switches to the " 14V Backup Supply” to keep itself
powered. This will allow the ED7 to complete critical tasks before shutting itself down (for example data logging storage).

NOTE: When the “14V Backup Supply” is wired to the ED7, no additional current is drawn when the
device is OFF.

### Analog Sensor 0V Reference (Pin 14)

As the name indicates these should be connected directly to the 0V (Ground) pin on any low current analog sensor, for example Pressure or Temperature.

*  DO NOT connect these pins directly to the Engine Block or ED7 Ground. These are dedicated
and specialised ground outputs for all analog channels and should be connected directly to
the sensor.
*  DO NOT connect speed-based sensors to this ground, use the 0V Reference Out Pin 13.

### RS232

Pin 11 is the ED7 RS232 Transmit Output. As the name suggests this is an output and should be connect to the Receive Input of the wired external device.

Pin 12 is the ED7 RS232 Receive Input. As the name suggests this is an input and should be connect to the Transmit Output of the wired external device.

Pin 13 can be used as the ground reference

### Ground Reference Out

This is a protected ground reference for frequency-based signals. It is rated at 1A continuous. For
example, this pin can be used as an RS232 ground reference and/or a Speed Sensor ground
reference