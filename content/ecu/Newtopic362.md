---
title: "Torque Limit Gain Tables"
---

# Torque Limit Ignition Retard Gain Table

![Image](</img/Untitled283.jpg>)


This table calibrates the torque reduction % per degree.&nbsp; When a torque request is applied the ECU will calculate how much retard is required to achieve this torque request. &nbsp;


Example : 1.5%/ Deg.&nbsp;

The Engine is running at&nbsp; 600Nm and a Torque Reduction to 400Nm is requested.&nbsp;


This is a 33% reduction in Torque so at 1.5%/Deg the ECU will Retard the Ignition 22 Degrees.

(33% / 1.5%/deg = 22 Deg)


Example : 16 degrees of ignition trims (Ignition Trims Total) are being applied - for any reason (comps, secondary load, etc)&nbsp;

The ECU will calculate 20% of torque reduction - can be observed with Runtime "Torque Reduction - Retard (Nm)"


See default table settings below. &nbsp; &nbsp;


![Image](</img/NewItem941.png>)


Torque Reduction Ignition Retard Gain Table

# Torque Limit Cut Gain Table&nbsp;



![Image](</img/Untitled284.jpg>)


This table calibrates the torque reduction % per %cut.&nbsp; When a torque request is applied the ECU will calculate how much cut is required to achieve this torque request. &nbsp;


See default table settings below. &nbsp; &nbsp;

![Image](</img/Torque man 14.jpg>)

Torque Reduction Cut Gain Table



# Torque Limit Boost Target Margin Table&nbsp;


![Image](</img/Untitled285.jpg>)



During Torque Limiting the ECU calculates (when enabled) the Minimum Boost Target required for the engine to achieve this Torque. The engine actually needs more than this minimum for the Throttle Mass Limiting to be effective so the " Boost Target Margin" is added to this value.


Example:&nbsp; ECU calculates a Boost Target of 150 kPa. If Boost Target Margin is 20kPa, the final Boost Target during Throttle Mass Flow Limiting will be 170kPa
