---
title: "Engine Torque Setup"
---

**Engine Torque Setup**



![Image](</lib/Untitled281.jpg>)


![Image](</lib/Untitled282.jpg>)

# Torque Reduction Ignition Retard Clamp&nbsp;


This clamp value sets the maximum amount of ignition timing retard the ECU is able to apply during a torque reduction event.&nbsp;

**Note**: An insufficient clamp value will result in an insufficient torque reduction when requested resulting in an failed torque reduction event


# Torque Nitrous Gain&nbsp;

In applications where Nitrous is used to increase torque.&nbsp; The ECU calculates this torque increase however if required the gain of this torque increase can be used to trim the output. &nbsp;


# BSFC &nbsp;

The brake specific fuel consumption of an engine depends on many factors including thermal efficiency, mechanical efficiency and air to fuel ratios.


Brake specific fuel consumption should be set at Lambda 1.000. The ECU will automatically scale this value based on Lambda Target. The assumption is the engine is tuned to this Target.


Typical Value = 304 - 243 g/kW.h&nbsp;


**Note 1:**&nbsp;

&#51;64 g/kW.h  = 0.60 lb/hp.h&nbsp;

&#51;04 g/kW.h  = 0.50 lb/hp.h&nbsp;

&#50;44 g/kW.h  = 0.40 lb/hp.h


**Note 2:**

At this time, Brake Specific Fuel Consumption torque calculation is not used by the ECU however it can be useful when calibrated correctly to cross check the ECU calculated torque levels.
