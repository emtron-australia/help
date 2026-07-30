---
title: "Nissan GR6"
---

## Wiring
Refer to the [Emtron TM16-R35 Adapter Kit Datasheet](https://docs.emtronaustralia.com.au/transmission-control/datasheets/tm16-r35-adapter).

---

## Gear Ratios
| Gear | Ratio  |
| ---- | ------ |
| R	   | -3.383 |
| 1st  | 4.056  |
| 2nd  | 2.301  |
| 3rd  | 1.595  |
| 4th  | 1.248  |
| 5th  | 1.001  |
| 6th  | 0.796  |
| FD   | 3.700  |

---

## Shift Forks
| Fork | Gear Low | Gear High |
| ---- | -------- | --------- |
| 1    | R        | 1         |
| 2    | 2        | 4         |
| 3    | 3        | 5         |
| 4    | 6        | -         |

### Gear to Fork Mapping
| Gear | Fork  | Position | Volts |
| ---- | ----- | -------- | -------------- |
| R    | 1-L   | -9.0mm   | 1.300 / 3.800* |
| N    | *ALL* | 0.0mm    | 2.500 |
| 1    | 1-H   | 9.0mm    | 3.800 / 1.300* |
| 2    | 2-L   | 9.0mm    | 1.300 |
| 3    | 3-L   | 9.0mm    | 1.300 |
| 4    | 2-H   | -9.0mm   | 3.800 |
| 5    | 3-H   | -9.0mm   | 3.800 |
| 6    | 4-L   | 9.0mm    | 1.300 |
> \* Fork 1 has two position sensors.

--- 

## Shift Solenoids
| Solenoid | Function          |
| -------- | ----------------- |
| 1        | 4 / N             |
| 2        | 2 / 6             |
| 3        | R / 5             |
| 4        | 1 / 3             |
| 5        | Fork 3 & 4 Select |

### Shift Solenoid Truth Table
| Fork        | Gear | Sol 1 | Sol 2 | Sol 3 | Sol 4 | Sol 5 |
| ----------- | ---- |:-----:|:-----:|:-----:|:-----:|:-----:|
| **1 (1/R)** | R << |       |       | X     |       |       |
| **1 (1/R)** | >> 1 |       |       |       | X     |       |
| **2 (2/4)** | 2 << |       | X     |       |       |       |
| **2 (2/4)** | >> 4 | X     |       |       |       |       |
| **3 (3/5)** | 3 << |       |       |       | X     | X     |
| **3 (3/5)** | >> 5 |       |       | X     |       | X     |
| **4 (6/N)** | 6 << |       | X     |       |       | X     |
| **4 (6/N)** | >> N | X     |       |       |       | X     |

---

## Axis Feed Pressure Solenoids
### Active Axis/Clutch Behavior
Maintains about 3.5 bar above the active clutch pressure target.

### Inactive Axis/Clutch Behavior
Holds 10 bar at most times.
During fork movement, the inactive axis pressure is used to control the shift fork movement force and velocity. Once the fork is in position it returns to 10 bar.

---

## Lubricating Flow Solenoid
Remains active by default, allowing fully lubrication and cooling flow.
During a shift or high torque demand it will close off, to reduce pressure drop and allow maximum line pressure availability.

---

## Known Issues / Limitations
### Start Button Hold to Start
The R35 TCM is responsible for determining that the engine is safe to crank and supplies the positive side of the starter relay with power when the transmission is in Park or Neutral.
The window of time for this to happen when the start button is held from fully off, with brake applied, is only a couple of hundred milliseconds. The TM16's boot up process takes slightly longer than the factory TCM because it runs a very complex CPU & FPGA. As a result, the starter relay receives power too late. The starter solenoid will click but the BCM will have already given up.
The R35 base cal has a deliberate delay added to the user function that drives the starter relay power so that the one shot hold to start does not work at all. Instead the ignition will turn on normally, and **the engine will start with a second press of the start button**.

### Hill Hold
The OEM hill hold function that tells the ABS module to lock the brakes on a hill is not currently supported. We intend to add support for this function in a future update.

### Limp Home Skip Shifting
When an axis/clutch detects an error the OEM TCM will lockout the problem axis and skip shift (eg 2 to 4 to 6, ignoring 1,3,5 or visa versa). Current firmware does not support this function. Full fault detection is implemented and every shift fork is monitored for correct positioning at all times including before a shift can occur. In the event of a fault (such as a fork being stuck in the wrong position), rather than skip shift, the transmission will remain in whatever gear is currently driving.
Full limp home skip shifting is planned for a future update.
