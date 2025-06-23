---
title: "Launch PID Setup"
---

## Launch PID Setup


![Image](</lib/Launch 21.jpg>)


![Image](</lib/Launch 22.jpg>)


**Launch System Delay**

This is the time delay for the system to react to changes.&nbsp; It is used to help integral gain windup.&nbsp; Typical setting is 100ms.&nbsp; &nbsp;

&#48; = 10ms

&#49; = 20ms

&#50; = 50ms

&#51; = 100ms


**Launch Control Proportional Gain**

Proportional gain controls how aggressive instantaneous correction must be.&nbsp;

Example:

A value of 1.00 will output +/- 10Nm

for every 100 RPM of Target error.


**Launch Control Integral Gain**

Integral gain controls how much adaptive correction is needed.


**Launch Control Derivative Gain**

Derivative gain controls predictive correction where gain is based on the rate of change of error. &nbsp;


**Launch Control Integral Positive Clamp**

Positive clamp value for Integral Gain&nbsp;

Units - NM


**Launch Control Integral Negative Clamp**

Negative clamp value for Integral Gain&nbsp;

Units - NM


**Launch Control Max Torque Clamp**

Positive clamp value for Torque Launch Control&nbsp;

Units - NM


**Launch Control Min Torque Clamp**

Minimum clamp value for Torque Launch Control&nbsp;

Units - NM

