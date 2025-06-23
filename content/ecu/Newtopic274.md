---
title: "LTFT Setup"
---

**LTFT Setup (Long Term Fuel Trim)**


![Image](</lib/LTFT Setup.jpg>)


![Image](</lib/LTFT Setup 2.jpg>)


* LTFT Post Start Lockout&nbsp; &nbsp; -&nbsp; &nbsp; Delay in which LTFT can become active after start up
* LTFT Min Eng Temp Lockout&nbsp; &nbsp; -&nbsp; &nbsp; Minimum engine temperature for LTFT to become active
* LTFT Max Eng Temp Lockout&nbsp; &nbsp; -&nbsp; &nbsp; Maximum engine temperature for LTFT to become active&nbsp;
* LTFT Min STFT Lockout (+/-)&nbsp; &nbsp; -&nbsp; &nbsp; The minimum STFT allowed before LTFT can start correcting
* LTFT Update Rate&nbsp; &nbsp; &nbsp; &nbsp; -&nbsp; &nbsp; Update rate for LTFT
* Long Term Gain&nbsp; &nbsp; &nbsp; &nbsp; -&nbsp; &nbsp; Percentage of STFT applied per second


\*\* For STFT Lockout -&nbsp;


Min STFT Lockout = +/- 2.5% The LTFT will start operating when the STFT is greater the 2.5% or less than -2.5%&nbsp;


\*\* For Long Term Gain -&nbsp;


The Gain is percentage of the short term trim applied per second.


Example: Short Fuel Trim = 10.00%


Long Term Gain = 2.0%


Long Term Fuel Trim = 2.0% of 10.00% per second


Long Term Fuel Trim = 0.20%&nbsp; per second
