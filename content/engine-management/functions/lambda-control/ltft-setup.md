---
title: "LTFT Setup"
weight: 74
---

## LTFT Setup (Long Term Fuel Trim)

![Image](</img/LTFT Setup.jpg>)

![Image](</img/LTFT Setup 2.jpg>)

* LTFT Post Start Lockout    -    Delay in which LTFT can become active after start up
* LTFT Min Eng Temp Lockout    -    Minimum engine temperature for LTFT to become active
* LTFT Max Eng Temp Lockout    -    Maximum engine temperature for LTFT to become active 
* LTFT Min STFT Lockout (+/-)    -    The minimum STFT allowed before LTFT can start correcting
* LTFT Update Rate        -    Update rate for LTFT
* Long Term Gain        -    Percentage of STFT applied per second

** For STFT Lockout - 

Min STFT Lockout = +/- 2.5% The LTFT will start operating when the STFT is greater the 2.5% or less than -2.5% 

** For Long Term Gain - 

The Gain is percentage of the short term trim applied per second.

Example: Short Fuel Trim = 10.00%

Long Term Gain = 2.0%

Long Term Fuel Trim = 2.0% of 10.00% per second

Long Term Fuel Trim = 0.20%  per second
