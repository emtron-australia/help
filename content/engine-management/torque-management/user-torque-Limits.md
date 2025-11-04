---
title: "User Torque Limits"
---

In addition to Motorsport and special features included in the firmware that utilize Torque Management (Launch Control, Traction Control, Engine Speed limiting), there are 5 User Configurable Torque Limits.

## User Torque Limits 1-5

### User Torque Limit Function Setup
The User Torque Limits must be enabled in the Function Output Setup

Furthermore, a Custom Label can be assigned to the function


![Image](/img/NewItem944.png)


**Torque Limit Control Setup**
![Image](</img/NewItem943.png>)

Choose [Strat](./TorqueLimitStrats.md) to use for each Torque Limit


Choose Target Gear for Normalised Torque target

**Example Below:** (Gear Ratio Table MUST be setup)
 - 1 = 3.266
 - 2 = 2.130
 - 3 = 1.517
 - 4 = 1.212
 - 5 = 0.972
 - 6 = 0.780

**Normalised Gear =** 2 (which is Ratio 2.130)

**Feedforward Torque** = 300Nm


**Torque Target:**
```
Gear 1 = 2.130/3.266 = 0.652 * 300 = 195.7Nm
Gear 2 = 2.130/2.130 = 1 * 300 = 300Nm
Gear 3 = 2.130/1.517 = 1.404 * 300 = 421.22Nm
```

Select Tq Limit User Enable


### User Torque Limit Main Table (Nm)


This entry value in Nm is the torque target when the limit is active.


![Image](</img/NewItem945.png>)


### User Torque Limit Correction Table (%)
This entry will compensate the torque target table. Values entered are +/- %.



