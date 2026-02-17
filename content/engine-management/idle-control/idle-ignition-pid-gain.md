---
title: "Idle Ignition PID Gain"
weight: 50
---

## Idle Ignition PID Gain

![Image](</img/Idle Ignition 6.jpg>)

## Proportional Gain

Proportional gain controls how aggressive instantaneous correction must be. 

## Integral Gain Table

Integral gain controls how much adaptive correction is needed.

## Derivative Gain Table

Derivative gain controls predictive correction.  This function is used to prevent overshooting targets by looking at a number of factors like rate of change, and P and I gain. 

Commonly the I gain is not used and this allows the control oscillate over and below the Base Ignition Timing value.  

This can be important when operating the system in conjunction with an Idle Control valve so the valve position required can remain close to it’s Feed Forward value.  

