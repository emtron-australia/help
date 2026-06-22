---
title: "Clutch Capacity Adaption"
---

The [Clutches Geometry Model](./clutch-geometry.md) and engine inertia value will control the majority of the clutch torque applied during a shift. During a shift, the closed loop PID algorithm will make adjustments to the final clutch torque to try and keep the slip curve on target. After a shift, as long as the conditions are met, the Clutch Capacity Adaption system will look at the previous shift's closed loop output and make small adjustments to the relevant clutch's Learned Capacity Scaler.

## Clutch Learned Capacity Scaler Tables
Each Clutch has a Learned Capacity Scaler Table. 
 - A value of 100% means no correction is applied. `Clamping pressure remains unchanged`.
 - A value below 100% suggests that the actual clutch capacity is less than described by the clutch geometry model. `More clamping pressure will be applied`.
 - A value above 100% suggests that the actual clutch capacity is higher than described by tge clutch geometry model. `Less clamping pressure will be applied`.

 These tables are stored automatically on power off. 
 
 >[!INFO]Uploading a cal file will NOT overwrite the tables.

 >[!IMPORTANT]
 >Clutch Learned Capacity Scaler Table's have strict axis requirements:
 > - X Axis: MUST be Transmission Fluid Temperature.
 > - Y Axis: MUST be Gear or Off.
 > - Z Axis: Not used.