---
title: "Lambda LSU4.9 Sensor Control"
---

**Introduction**


The KV series ECU has the ability to interface directly to a Bosch Lambda Sensor(s), model LSU4.9.&nbsp;


To achieve the optimal control of this sensor, the ECU uses a genuine Bosch Integrated Circuit technology. It provides very accurate data on pump current which equates to Lambda

and also Nernst Cell Temperature which is used for precise heater control.


The ECU assigns the correct the Heater Output Channel based on ECU Type and Serial Number. The only setup required to enable the Internal Lambda 1 or 2 control is from the Config View -\> Inputs-\> Engine tab.


* If "Lambda 1" Input Channel has the Input Source selected to "Internal Lambda 1" the function becomes enabled.
* If "Lambda 2" Input Channel has the Input Source selected to "Internal Lambda 2" the function becomes enabled


![Image](</img/Untitled43.png>)



Adjustments to the operation of On-board Lambda Sensor Control can be made from the Tuning view -\> Engine Functions -\> Internal LSU Sensor Control


The ECU uses all 6 sensor wires per sensor.&nbsp;



**Sensor Shock**&nbsp;


In some situations during normal operation, the sensor will temporally shutdown for between 0.5 sec to 2.5 secs. This is usually caused by a combination of sensor incorrect placement and Fuel type resulting in the sensor being "shocked" ; either thermally or by a pressure wave inside the exhaust system.&nbsp; For the correct sensor placement please read the [Sensor Installation and Wiring](<SensorInstallation.md>) topic.


Although the sensor shutdown is outside the ECU's control, the status is constantly monitored. In the event of a shutdown the heater control is put into a Hold mode as it the Closed Loop Lambda.&nbsp;



![Image](</img/LSU 49 Pinout - A11.jpg>)



