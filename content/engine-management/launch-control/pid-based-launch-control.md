---
title: "PID Based Launch Control"
weight: 77
---

## PID Based Launch Control:

The Emtron PID based Launch Control will apply gains in the static mode function only, as the PID target is the Launch RPM.  

** RPM Control is the only PID base

This means in "Moving" mode, the ECU will follow Engine reduction calculates via the Torque Reduction Ignition, Torque Reduction Cut, and Throttle Area Demand

## Launch PID Setup

## Launch System Delay

This setting delays  the routine to allow the closed loop system to function, as the torque is *calculated*. 

0 = 10ms

1 = 20ms

2 = 50ms

3 = 100ms

    Typical setting for Ignition Based PID - "2" 

    Typical setting for Throttle Based PID - "1"

## Launch Control Proportional Gain

A value of 1.00 will output +/- 10Nm for every 100 RPM of Target error.

    Typical setting for Ignition Based PID - "3" 

    Typical setting for Throttle Based PID - "0.5"

** Throttle Based PID - the least amount of error in the throttle area/TMF calculation feeds forward this PID

## Launch Control Integral Gain

A value of 1.00 will output +/- 10Nm for every 100 RPM of Target error, but increment/count up to the integral gain limit

    Typical setting for Ignition Based PID - "0.150" 

    Typical setting for Throttle Based PID - "0.050"

** Throttle Based PID - the least amount of error in the throttle area/TMF calculation feeds forward this PID

## Launch Control Derivative Gain

The derivative change of the engine torque vs the target will be affected by this gain value

    Typical setting for Ignition Based PID - "3" 

    Typical setting for Throttle Based PID - "1"

** Throttle Based PID - the least amount of error in the throttle area/TMF calculation feeds forward this PID

