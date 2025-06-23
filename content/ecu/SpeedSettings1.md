---
title: "Speed Settings"
---

Each Speed Input has a range of settings that must to be configured to match the input type.


**Sensor Type**


* Magnetic.&nbsp;
* Hall Effect
* Logic&nbsp;
* Switch.


**Active Edge**


* Rising
* Falling
* Both
* Off



**Pull Up**


Can be used to switch on a 9V pull up resistor.



**Scaler**


Scales the frequency based input into kph or into the units that have been selected. The raw frequency value can be viewed from the Runtime Menu -\> Raw Inputs Tab.



**Arming Thresholds**


Each channel when assigned between DI 1-8 can have two options for arming threshold control; 2 point or Table.


**NOTE:** It is recommended on ALL frequency based **Magnetic** inputs that the Table option is used. This allows better signal integrity control due to the improved functionality offered by the table.


**Scaler Calculation**


Scaler = Number of Sensor Teeth / Wheel Diameter(cm) \* 3180

Scaler = 360 when using CAN Speed Inputs
