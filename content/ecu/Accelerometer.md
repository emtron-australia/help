---
title: "Accelerometer"
---

**Overview**


The KV8, KV12, KV16 ECUs have an internal 3-Axis Accelerometer. This can be used to measure:


* Braking and acceleration g-force (longitudinal acceleration)&nbsp;
* Cornering g-force (lateral acceleration)&nbsp;
* Up/down g-force (vertical acceleration)&nbsp;


Other features include:


* &#49;6 Bit Resolution
* \+2g/+4g/+8g dynamically selectable full-scale
* Output Data Rate 500Hz



The digram below shows the orientation of each ECU axis.


![Image](</img/KV8\_white\_inc.jpg>)



The digram below shows the orientation of each axis reference from the vehicle.


![Image](</img/g-force axis diection.jpg>)


The ECU allows each vehicle axis to be assigned to an ECU axis (X,Y,Z) .&nbsp; For example the Longitudinal Axis can be assigned to the ECUs X or Y or Z axis. This allows the ECU to be mounted at any position/orientation within the car.


These settings are available from the Tuning view -\> Vehicle Setup -\> Accelerometer Setup Menu.


**Typical Values:**


Longitudinal **positive** g-force = Acceleration. Typical values 0.3 to 0.5g

Longitudinal **negative** g-force = Braking. Typical values: -1.5 to -1.8g



Lateral **negative** g-force = Turning Left. Typical value for race car on slicks : -1.8g

Lateral **positive** g-force = Turning Right. Typical value for race car on slicks : 1.8g




**Accelerometer Full Range**

This sets the maximum g-force that can be measured in any axis. There are 3 Full Range modes adjustable through EMtune.&nbsp;


* \+2g
* \+4g
* \+8g


Normally **2g** is enough for most racing applications where there is limited downforce. However, on applications with significant downforce such as under-body trays or large wings then the **4g or 8g** option is recommended.

