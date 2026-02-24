---
title: "Launch PID Setup"
weight: 71
---

## Launch PID Setup

![Image](</img/Launch 21.jpg>)

![Image](</img/Launch 22.jpg>)

## Launch System Delay

This is the time delay for the system to react to changes.  It is used to help integral gain windup.  Typical setting is 100ms.   

0 = 10ms

1 = 20ms

2 = 50ms

3 = 100ms

## Launch Control Proportional Gain

Proportional gain controls how aggressive instantaneous correction must be. 

Example:

A value of 1.00 will output +/- 10Nm

for every 100 RPM of Target error.

## Launch Control Integral Gain

Integral gain controls how much adaptive correction is needed.

## Launch Control Derivative Gain

Derivative gain controls predictive correction where gain is based on the rate of change of error.  

## Launch Control Integral Positive Clamp

Positive clamp value for Integral Gain 

Units - NM

## Launch Control Integral Negative Clamp

Negative clamp value for Integral Gain 

Units - NM

## Launch Control Max Torque Clamp

Positive clamp value for Torque Launch Control 

Units - NM

## Launch Control Min Torque Clamp

Minimum clamp value for Torque Launch Control 

Units - NM

