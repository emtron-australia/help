---
title: "Active Center Differential  Pump Control (ACD)"
weight: 1000
---

## Active Center Differential (ACD) Hydraulic Pump Control

This function reads the pressure from the "Active Center Diff Pressure" input channel and uses this to control the ACD hydraulic pressure. The ECU provides a Pressure Target Table so that different pressures can be targeted under different conditions. 

This function can be enabled when the Motorsport Differential Control Function is ON AND an Output Channel has been assigned.  

![Image](</img/Untitled49.png>)

## ACD Control Output Status

The following Status information is available from the "ACD Output Status" runtime. This can be viewed from ECU runtime menu, under the Motorsport Tab.

0 = Function is OFF

1 = Output OFF

2 = Output ON

3 = Output OFF- RPM Lockout

4 = Output OFF- User Lockout

5 = Output OFF- Timeout

6 = Output OFF- ACD Pressure Input not selected

7 = Output OFF- ACD Input in Fault

## ACD Pump Lockouts

* ACD RPM Lockout: The ACD Pump Output will be switched OFF below this Engine Speed.  Used normally to switch OFF the Pump during low RPM and cranking. 

0 = OFF

Typical Value = 400 RPM

* ACD User Lockout: The ACD Pump Output will be switched OFF when the User Channel is ON/Active.

## ACD Pump Protection

The following features have been implemented to prevent pump damage:

*  
  * ACD Timeout Setting. With the Pump ON, if the Target pressure cannot be reached within this timeout value the Pump will be switched OFF. The timer will only be reset when the Lockouts become active or the ECU power is reset.
  * ACD Pressure Sensor Fault. When the sensor is in fault the Pump will be switched OFF.

## ACD Pump Priming.

The hydraulic system can be primed using the "Test "Output" function. Simply open this menu, set Test Output to ON and the Pump should start.

**CAUTION:** Priming the pump should be done with care as the ECUs safety systems are disabled and pump damage may occur.

![Image](</img/NewItem90.png>)

