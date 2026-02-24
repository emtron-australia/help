---
title: "DTC's"
weight: 86
---

![Image](</img/NewItem989.png>)

## Diagnostic Trouble Codes (DTC's)

System errors within the ECU  show up as DTC Errors illuminated in red in the Emtune software.                                                                                                         

They are also associated with the engine check light, should one be configured

![Image](</img/NewItem988.png>)

The source of the error is straight forward to determine.

Click on the red DTC tab & a breakout DTC list will appear. 

This list will contain all of the current errors.

For this example, we will look at P0107 - Manifold Absolute Pressure Circuit Low Input.

![Image](</img/NewItem987.png>)

Step 1 

Press F3 to open the ECU Runtime Values Tab

Using the Raw inputs tab, determine if the voltage observed at the input is within the defined range of operation

Ensure the input calibration error threshold is set outside the normal operating range of the sensor.

If the calibration data is correct together with correctly set error thresholds.

The error can be considered valid and should be investigated.

A valid version of the example error (P0107) may indicate a dead short or simply the sensor is unplugged

