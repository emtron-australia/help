---
title: "Clutch Touch Points"
---

One of the most important things to setup on a new installation is the clutch touch points.

The touch point refers to the amount of pressure applied to the clutch before any meaningful torque capacity is applied.

 - **Below** the touch point, the clutch is fully slipping.
 - **Above** the touch point, the clutch is starting to hold torque.

The clutch's torque capacity starts at the touch point. It's effective pressure is it's total pressure less it's touch point. For example:
```
Touch Point: 1.0 Bar
Torque to Pressure Ratio (simplified): 50 Nm/Bar
Torque Capacity @ 0.5 Bar = 0 Nm
Torque Capacity @ 1.0 Bar = 0 Nm << Touch Point
Torque Capacity @ 1.5 Bar = 25 Nm
Torque Capacity @ 2.0 Bar = 50 Nm
```

>[!WARNING] The user MUST find the touch point of each clutch. Failing to do so will result in poor drivability and shifting.

## Touch Point Tuning

![alt text](/img/tm16/touch_points_1.png)

To find the touch points, the following condition must be met:
 - Transmission Fluid Temperature: 60-90°C
 - Gear: Neutral
 - Brake: ON
 - Input Shaft Speed: 500-2000 RPM
 - Output Shaft Speed: 0 RPM

### Automated Touch Point Learning
You can put the TCM into automated learning mode for a given clutch. For this system to work, the engine idle speed needs to be very stable. On engines where the idle speed is rough (large camshafts etc), it's likely better to do manually.

Set the clutch to be tested and the TCM will engage all relevant surrounding clutches that would result in a driving gear using the clutch in question. It will then slowly ramp the clutch pressure up and look for a dip in Input Shaft Speed. This process will be repeated 5 times and the result of those tests will be averaged to find the final touch point.

The test will exit if the entry conditions are no longer met, Eg: The user releases the brake.

>[!CAUTION] If the automated test errors out, an erroneous value may be applied to the clutch's touch point and the test should be run again.

### Manual Touch Point Learning
1. Set the clutch to be tested and the TCM will engage all relevant surrounding clutches that would result in a driving gear using the clutch in question. 
2. Slowly increase the Touch Point Setting and watch for the moment where the clutch starts to drag on the input shaft.
3. The actual touch point will be a little before this, where any more pressure results in noticeable drag.

![alt text](/img/tm16/touch_points_2.png)
> In this example, as Clutch B reaches ~1.85 Bar, the Input Shaft Speed begins to noticeably dip as drag is applied to the input shaft. The actual touch point, before the clutch begins to drag on the input shaft, would be slightly before that at about 1.75 Bar.

## Touch Point Correction
A correction scaler can be applied on either a global or per-clutch level. If you find that at varying fluid temperatures the touch points need adjustment, these corrections can address that.

![alt text](/img/tm16/touch_point_correction.png)
> Here, at 20°C a nominal Touch Point of 1.75 Bar would become 1.57 Bar.