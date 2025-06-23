---
title: "Torque Limit Strategy"
---

&#53; different Torque Limit strategies can be configured.&nbsp; Different situations and scenarios may call for multiple methods of torque limiting strategies. &nbsp;


Torque Strategies can use a combination of Throttle Area, Ignition Retard, and Cutting to achie ve the requested torque target. A priority system is used to determine the prefferred method of torque reduction, this is particularly useful during long sustained


Torque Limit conditions.


The first priority is always given preference, however should the chosen priority mode not achieve the torque target before hitting a clamp value or during the time it takes for Throttle Air Mass to change, the next priority mode will be used.


Example:

Priority 1 = Throttle Area

Priority 2 = Ignition Retard

Priority 3 = Fuel/Ign Cutting

Ignition Retard Max Clamp Table = 15 deg.


When the Torque Limit is entered, the Throttle Area will begin to transition to the position calculated to acheive the requested torque air mass. During this transition the torque limit will likely not be achieved, so the system will shift to Priority 2 and introduce the calculated Ignition Retard required to achieve the torque target.


Should be torque target still not be met and the Retard applied has reached the max clamp, the system will shift to Priority 3 to complete the torque reduction with cutting.


Similarly, when the Ignition Retard is enough to maintain the torque reduction, the cutting will be removed. Finally, once the Throttle Area is able to sustain the Torque Limit, the Ignition Retard will be removed.
