---
title: "Lambda Transport Delay Guide"
weight: 66
---

 **Lambda Transport Delay Tuning Guide**

The Lambda Closed Loop system is a fairly standard PID routine (with Proportional, Integral, and Derivative gains).  See the [Lambda Control - Wide Band ](<Newtopic71.md>)section for more details

However, for it to function correctly, latency from o2 sensors signals must be programmed/tuned into the ECU system.  This is known as **"Lambda Transport Delay"**

** Physical location/distance from the engine or pre-/post-turbo configuration of o2 sensors will affect transport delay

Tuning -> Engine Functions -> Lambda Control - Wideband -> Lambda Transport Delay 

![Image](</img/NewItem823.png>)

## Tuning Lambda Transport Delay

Lambda Transport Delay is often confused as a measurement of time it takes for the lambda to reach lambda targets (once lambda is changed), however

Lambda transport delay = the time (in seconds) measured it takes for the lambda ***to start*** once target has changed

A simple way to tune this function is to put the engine at varying loads and make lambda target change while logging.  Measure with the differences cursor ("D") in the logger to see the time it takes for the lambda to change from the original value to the new value.  This is your "Lambda Transport Delay"

![Image](</img/NewItem825.png>)

Next, populate the transport delay value (in seconds), into the "Lambda Transport Delay" table. 

![Image](</img/NewItem826.png>)

** Example shown is 2D following Air Mass Flow Final (g/s) - but a 3D table axis is available for using standard values such as RPMxMAP, etc.  

Repeat the process for varying loads to populate the transport delay table

