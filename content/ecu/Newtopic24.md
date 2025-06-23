---
title: "Idle Speed Control Configuration (TMF)"
---

**This section assumes the DBW has been configured and operating correctly.**


The following steps should be used to configure the Idle Speed control system to work using Throttle Mass Flow.


1. Configure the Throttle Mass Flow Idle Speed Control output function type using the menu: &nbsp;

&nbsp; &nbsp; &nbsp; **Config&nbsp; -\> Functions -\> Function Output Setup -\> Engine Functions Tab -\> Idle Speed Control**


Select either DBW 1 TMF or DBW 1 + 2 TMF


![Image](</lib/Untitled215.png>)




2. Configure the throttle body model using the menu: Tuning -\> Engine Function -\> Throttle Body&nbsp; Model -\> Throttle Body Setup


&nbsp; &nbsp; &nbsp; See [Throttle Body Setup](<ThrottleBodySetup.md>) help topic for more information&nbsp;


3. Configure the Throttle Mass Flow model using the menu: Tuning -\> Engine Function -\> Throttle Body&nbsp; Model -\> Throttle Mass Flow Setup


![Image](</lib/Untitled219.png>)


**Step 1-** Select the throttle mass flow enable type that is applicable to your configuration. Example: ON x 1 DBW Throttle Body


* TMF idle valve option is for TMF fuel model on cable throttle engines \& is not applicable to DBW TMF idle speed control.&nbsp;
* The TMF idle valve size input is also only applicable to cable throttle TMF applications


**Step 2 -** Set Throttle 1 before plate pressure source


* If you intend to use TMF in areas other than idle, there should be a pressure sensor already fitted before the throttle plate and this should be selected.&nbsp;

&nbsp; &nbsp; &nbsp; Example: Boost Pressure Sensor &nbsp;

&nbsp; &nbsp; &nbsp; In the case of only wanting to achieve TMF Idle Speed Control and there is no sensor fitted before the plate, simply select the internal &nbsp; &nbsp; &nbsp; Barometric Pressure sensor.&nbsp;

&nbsp; &nbsp; &nbsp; Other more complicated methods are also available for advanced users..


![Image](</lib/Untitled217.png>)


**Step 3.** Set the Throttle 1 After Plate Pressure source. This is normally the MAP sensor


**Step 4.** Set the Throttle 1 Temperature source. This is normally set to charge temperature


Repeat for Throttle 2 if applicable&nbsp;


4. Throttle Body Area Table. See [Throttle Body Setup](<ThrottleBodySetup.md>) help topic for more information&nbsp;


5. Confirm the Throttle Mass Flow calculations are operating, the data can be viewed from the Runtime menu (F3) -\> Engine Data Calculated tab


![Image](</lib/Untitled221.png>)


