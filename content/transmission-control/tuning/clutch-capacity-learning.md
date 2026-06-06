---
title: "Clutch Capacity Adaption"
---

The [Clutches Geometry Model](./clutch-geometry.md) and engine inertia value will control the majority of the clutch torque applied during a shift. During a shift, the closed loop PID algorithm will make adjustments to the final clutch torque to try and keep the slip curve on target. After a shift, as long as the conditions are met, the Clutch Capacity Adaption system will look at the previous shift's closed loop output and make small adjustments to the relevant clutch's Learned Capacity Scaler.