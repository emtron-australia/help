---
title: "Closed Loop and PID"
---

**Closed loop and PID**


The function “Closed Loop” is defined as a control system's ability to react automatically based on a form of feedback (position, calculated value, frequency, etc). &nbsp;

This is usually dependent on some sort of PID strategy. &nbsp;


The Emtron ECU has closed loop controls for many Functions throughout the ECU. &nbsp;

Common functions that rely on closed loop are:


Closed Loop Lambda Control&nbsp;

Idle speed control&nbsp;

Idle Ignition Control

VVT Cam control

DBW Control

Boost Control

Launch Control - Torque Limiting

Traction Control&nbsp;


All Emtron PID configurations can be very comprehensive.&nbsp; .


**Proportional Gain:** controls how aggressive instantaneous correction is based on the current target error.&nbsp; &nbsp;

Correction based on proportional error&nbsp;


Example 1 -


Boost Target Error = 10%

P Gain Table Entry = 1.0

P Gain Correction = 10% \* 1.0 = 10%&nbsp;


Example 2 -


Boost Target Error = 10%

P Gain Table Entry = 2.0

P Gain Correction = 10% \* 2.0 = 20%&nbsp;



**Integral gain:** controls how much adaptive correction is needed over time after the application of proportional control. &nbsp;


The Integral Gain will multiply the gain value vs the target error at the control rate speed.&nbsp;


**Derivative gain:** controls predictive correction.&nbsp; It is based on the rate of change of the error.&nbsp; &nbsp;


The target error rate of change will multiply vs the Derivative gain.



A delicate balance of these values is normally needed to provide accurate and precise control of the closed loop system. &nbsp;


To provide more accurate closed loop control, Emtron allows values can be spanned in 3D to allow a look up table to actively adjust based on whatever runtime is desired. &nbsp;

This allows the user to fine tune the closed loop functions without just relying on the target error solely. &nbsp;


**Feed forward functions**


The feed forward value allows the PID function to operate with greater accuracy if drive duty can be predicted.&nbsp;


**Min/Max limits**&nbsp;


These are used to clamp the PID functional range if necessary. &nbsp;

