---
title: "Closed Loop and PID"
weight: 0
---

The function “Closed Loop” is defined as a control system's ability to react automatically based on a form of feedback (position, calculated value, frequency, etc).  

This is usually dependent on some sort of PID strategy.  

The Emtron ECU has closed loop controls for many Functions throughout the ECU.  

Common functions that rely on closed loop are:

Closed Loop Lambda Control 

Idle speed control 

Idle Ignition Control

VVT Cam control

DBW Control

Boost Control

Launch Control - Torque Limiting

Traction Control 

All Emtron PID configurations can be very comprehensive.  .

**Proportional Gain:** controls how aggressive instantaneous correction is based on the current target error.   

Correction based on proportional error 

Example 1 -

Boost Target Error = 10%

P Gain Table Entry = 1.0

P Gain Correction = 10% * 1.0 = 10% 

Example 2 -

Boost Target Error = 10%

P Gain Table Entry = 2.0

P Gain Correction = 10% * 2.0 = 20% 

**Integral gain:** controls how much adaptive correction is needed over time after the application of proportional control.  

The Integral Gain will multiply the gain value vs the target error at the control rate speed. 

**Derivative gain:** controls predictive correction.  It is based on the rate of change of the error.   

The target error rate of change will multiply vs the Derivative gain.

A delicate balance of these values is normally needed to provide accurate and precise control of the closed loop system.  

To provide more accurate closed loop control, Emtron allows values can be spanned in 3D to allow a look up table to actively adjust based on whatever runtime is desired.  

This allows the user to fine tune the closed loop functions without just relying on the target error solely.  

## Feed forward functions

The feed forward value allows the PID function to operate with greater accuracy if drive duty can be predicted. 

## Min/Max limits

These are used to clamp the PID functional range if necessary.  

