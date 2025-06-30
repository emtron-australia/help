---
title: "Emtron Lambda to CAN (ELC/ELCM) Setup"
---

For details :&nbsp;


**Emtron Lambda CAN Manual**



Click the link below to download or visit Emtron www Downloads


ELC



**Reset CAN IDs to Default**


&#48;: OFF

&#49;: ON


This will reset the ELC CAN IDs back to their default values


Channel 1 = 671, Channel 2 = 672


Set back to zero when finished.


**Enable Heater Override**&nbsp;

\
&#48;: OFF

&#49;: ON


When enabled, the ECU controls when the Lambda heater is ON or OFF. This is done through&nbsp; the "ELC HEater RPM Lockout" and "ELC Heater Post Start Lockout: settings.&nbsp;


When disable the ELC controls the heater(s) which will turn On 15 secs after the device power up.


**Enable EMAP**&nbsp;

\
&#48;: OFF

&#49;: ON


When enabled, the ECU will send EMAP data to the ELC. This units should be in kPa


\*\* When enabled please make sure the EMAP is configured correctly inside the ECU.


**ELC Heater RPM Lockout**&nbsp;

\
RPM Below which heater will be locked out


**ELC Heater Post Start Lockout**&nbsp;

\
Timer before which heater will turned on Post Start up


**ELC Lambda 1 Test Enable**&nbsp;

\
Forces the ELC to send this Test Value over the CAN bus.


Allows the user to confirm the ECU calibration is setup correctly.


&#48; = OFF


**ELC Lambda 2 Test Enable**&nbsp;

\
Forces the ELC to send this Test Value over the CAN bus.


Allows the user to confirm the ECU calibration is setup correctly.


&#48; = OFF

