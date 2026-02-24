---
title: "Speed Inputs"
weight: 17
---

Normally these are frequency based inputs and should be connected between Digital Input 1 - 8. The ECU can can read a frequency range on these input from 0Hz - 25kHz (25000Hz).

The following Speed Options are available:
* Left Drive Speed.
* Right Drive Speed
* Left Drive Speed 2
* Left Drive Speed 2
* Left Ground Speed
* Right Ground Speed
* Drive Speed
* Ground Speed
* Turbo Speed 1
* Turbo Speed 2
* Input Shaft Speed
* Tail Shaft Speed

## Sources
The following channel assigns are recommended.

### Four Wheel Drive
If the speed data is collected by the ECU on all 4 wheels, then assign the front wheels to the Left and Right Drive Speed Channels and the rear wheels to the Left an Right Speed 2 Channels

### Gearbox Output
Assign this to the Drive Speed Channel.

### CAN
CAN Data: Input Source = `CAN Bus OEM`

This allows speed data that is available on a factory CAN bus to be displayed. The following channels can be used for different CAN bus systems.

> **NOTE:** When the Input Source is selected as "CAN Bus OEM" only the Filter setting is used. All other settings are not required as the data is already calibrated.

See [Build Packages](../builds) for application specific information.

## Configuration
Each Speed Input has a range of settings that must to be configured to match the input type.

### Sensor Type
* Magnetic. 
* Hall Effect
* Logic 
* Switch.

### Active Edge
* Rising
* Falling
* Both
* Off

### Pull Up
Can be used to switch on a 9V pull up resistor.

### Scaler
Scales the frequency based input into kph or into the units that have been selected. The raw frequency value can be viewed from the Runtime Menu -> Raw Inputs Tab.

### Arming Thresholds
Each channel when assigned between DI 1-8 can have two options for arming threshold control; 2 point or Table.

> **NOTE:** It is recommended on ALL frequency based **Magnetic** inputs that the Table option is used. This allows better signal integrity control due to the improved functionality offered by the table.

### Scaler Calculation

```
Scaler = Number of Sensor Teeth / Wheel Diameter(cm) * 3180
```

Scaler = 360 when using CAN Speed Inputs
