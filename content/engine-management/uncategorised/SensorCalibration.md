---
title: "Heater Control and Sensor Calibration"
---


**Heater Control**


During engine start-up, condensation forms in the exhaust which may damage the sensor.&nbsp; It is recommended to only start heating the LSU sensor after the engine is running and the moisture content in the exhaust has evaporated. The ECU has settings to prevent this damage;&nbsp; "Heater RPM Lockout" and "Heater Post Start Lockout"


Typical Values: &nbsp; &nbsp;

Heater RPM Lockout = 500 RPM &nbsp; &nbsp;

Heater Post Start Lockout = 4.0 Sec



**Calibration**&nbsp;


The sensor is calibrated automatically by the ECU on power up. During the calibration process two important pieces of data are read:


* The optimal **Nernst Cell Temperature** which is used for sensor heater control. The ELC applies duty cycle and a PID routine to maintain a constant and accurate heater temperature which results in a very stable and accurate Lambda value.&nbsp;
* The **Pump Current** that corresponds to a Lambda reading of 1.000 Lambda.



**NOTE:** A Free-Air Calibration is NOT required on the LSU4.9. The sensor uses a reference pump current instead of reference air. The big advantage with this is that the reference is a calibrated electrical signal and remains constant.

