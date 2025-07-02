---
title: "Knock Control Setup"
---

**Tuning Knock Control**


Tuning -\> Engine Functions -\> Knock Control -\> Knock Control Setup


![Image](</img/NewItem293.jpg>)


**Knock Control Setup**


![Image](</img/NewItem292.jpg>)


* Knock Gain&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -&nbsp; &nbsp; Gain added to knock signal (can multiply)
* Knock Mode&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -&nbsp; &nbsp; 0 = Global 1 = Individual (allows ECU to detect per cyl)
* Short Term Retard Gain &nbsp; &nbsp; -&nbsp; &nbsp; Retard for each percentage over the knock threshold
* Short Term Advance Rate&nbsp; &nbsp; -&nbsp; &nbsp; Rate at which timing is reintroduced when Short Term Retard is 0
* Short Term Retard Limit&nbsp; &nbsp; -&nbsp; &nbsp; Maximum Short Term Retard that can be applied
* Long Term Retard Gain&nbsp; &nbsp; -&nbsp; &nbsp; Long Term Retard applied based on Short Term Retard&nbsp;
* Long Term Advance Rate&nbsp; &nbsp; -&nbsp; &nbsp; Rate at which timing is reintroduced to Long Term Trim when Short Term Retard is 0
* Long Term Retard Limit&nbsp; &nbsp; -&nbsp; &nbsp; Maximum Long Term Retard that can be applied &nbsp; &nbsp;
* Knock Window Start Angle&nbsp; &nbsp; -&nbsp; &nbsp; Point at which ECU will start to sample the Knock Signal
* Knock Window Angle&nbsp; &nbsp; &nbsp; &nbsp; -&nbsp; &nbsp; The length in degrees in which the ECU will sample the Knock Signal



\*\* Knock Window Angle must be less than the angle between TDCs

&nbsp; &nbsp; \<90 degrees V8

&nbsp; &nbsp; \<60 degrees V12

&nbsp;&nbsp; &nbsp;

**Knock Lockouts**


* RPM Lo Lockout&nbsp; &nbsp; &nbsp; &nbsp; -&nbsp; &nbsp; Knock Control will be OFF below this RPM
* RPM Hi Lockout&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -&nbsp; &nbsp; Knock Control will be OFF above this RPM
* Post Start Delay &nbsp; &nbsp; &nbsp; &nbsp; -&nbsp; &nbsp; Delay in which Closed Loop Knock detection is active
* TP Lockout&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -&nbsp; &nbsp; Minimum Throttle Position before Knock detection is active
* dTP Lockout&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -&nbsp; &nbsp; Maximum Throttle Rate of Change in which Knock detection can become active
* dMAP Lockout&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -&nbsp; &nbsp; Maximum Manifold Pressure Rate of Change in which Knock detection can become active&nbsp;
* User Lockout&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -&nbsp; &nbsp; Allows user to create custom lockout channel


**Knock Channel Cylinder**


Select the appropriate Knock Channel (Knock Sensor) for each cylinder


![Image](</img/NewItem122.png>)

Example - 6 cylinder with two knock inputs


**Knock Threshold Table**


Table in which the maximum allowable measured Knock Level is allowed


**Knock Threshold Cyl Gain Table**


Used to multiply the signal gain per cylinder&nbsp;


\*\* The X-Axis MUST be set to the Cylinder Numbers


**Knock Level Cyl Gain Table**


Used to multiple the knock level per cylinder


\*\* The X-Axis MUST be set to the Cylinder Numbers



