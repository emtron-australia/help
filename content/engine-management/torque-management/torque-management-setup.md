---
title: "Torque Management Setup"
weight: 75
---

![Image](</img/Untitled281.jpg>)

![Image](</img/Untitled282.jpg>)

## Torque Reduction Ignition Retard Clamp
This clamp value sets the maximum amount of ignition timing retard the ECU is able to apply during a torque reduction event.

> **Note**: An insufficient clamp value will result in an insufficient torque reduction when requested resulting in an failed torque reduction event

## Torque Nitrous Gain
In applications where Nitrous is used to increase torque. The ECU calculates this torque increase however if required the gain of this torque increase can be used to trim the output.

## BSFC
The brake specific fuel consumption of an engine depends on many factors including thermal efficiency, mechanical efficiency and air to fuel ratios.

Brake specific fuel consumption should be set at Lambda 1.000. The ECU will automatically scale this value based on Lambda Target. The assumption is the engine is tuned to this Target.

**Typical Value:** 304 - 243 g/kW.h

## Conversion:
 - 364 g/kW.h = 0.60 lb/hp.h
 - 304 g/kW.h  = 0.50 lb/hp.h
 - 244 g/kW.h  = 0.40 lb/hp.h

{{% badge style="info" %}}At this time, Brake Specific Fuel Consumption torque calculation is not used by the ECU however it can be useful when calibrated correctly to cross check the ECU calculated torque levels.{{% /badge %}}

