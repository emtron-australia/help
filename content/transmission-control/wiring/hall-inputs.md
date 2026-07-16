---
title: "Hall Effect Inputs"
---

## Dedicated 2-Wire Hall Effect Inputs
The TCM contains 4 dedicated 2-wire hall effect inputs. These inputs are suitable for speed sensors found in many transmissions and ABS systems.

Unlike normal digital inputs, they actually provide the sensor with a regulated current source at the system's battery voltage. When the sensing target passes the sensor, the current draw from the sensor will change. This change in current is used to determine an "edge".

| Input          | TCM Pin   |
| -------------- | ----- |
| Hall Input 1   | C10   |
| Hall Input 2   | C11   |
| Hall Input 3   | C12   |
| Hall Input 4   | C13   |

>[!INFO] 
> The power supply for the hall inputs is sourced from Aux 1-4 Supply (Pin C2).

**Each Hall Input outputs the following data:**
 - Frequency (0.5 – 20 KHz)
 - Duty Cylce (%)
 - Period (ms)
 - Pulse Width (ms)

### Known Applications
 - BMW / Getrag GS7 DCT Input Shaft Speed & Clutch Speeds
 - Toyota GT86 ABS Sensors

### Wiring
| Sensor Pin     | TCM Pin        |
| -------------- | -------------- |
| Sensor Pin 1   | Hall Input 1-4 |
| Sensor Pin 2   | GND            |
>**Note:** The sensor may be grounded remotely.

![Hall Input Wiring](/img/tm16/hall_wiring.png)

There's no requirement to set arming thresholds or pulldown resistors.

---

## Hall Inputs on DI 1-8
It's possible to use 2-wire hall effect sensors on DI-18, and in some cases this is required.

The principle is similar but the wiring is very different. The sensor needs to be supplied with a regulated voltage (eg: 8.0V) and the signal wire goes to a digital input where it's grounded through the internal pulldown resistor. This creates a measurable voltage that the TCM can use to measure rising and falling edges.

### Known Applications
 - ZF 8HP Input Shaft Speed & Output Shaft Speed

### Wiring
| Sensor Pin     | TCM Pin        |
| -------------- | -------------- |
| Sensor Pin 1   | 8.0V           |
| Sensor Pin 2   | DI 1-8 *(Pulldown ON)*       |

>[!IMPORTANT] 
> The input pin's pulldown resistor must be enabled and the arming thresholds set correctly.

### Arming Thresholds
The high and low arming thresholds must be set correctly to detect the speed signal. You can watch the raw voltage of the digital input pin to determine the thresholds.

 - The low threshold must be ABOVE the sensor voltage at rest.
 - The high threshold must be BELOW the maximum voltage when the sensor is active.

![8HP Speed Sensor Arming](/img/8hp/8hp-speed-arming.png)

>[!TIP]: If the voltage is near 0V or near the 8V supply, the sensor is probably wired wrong. 