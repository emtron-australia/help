---
title: "Camshaft Closed Loop Control - PID Setup"
---

**PID Setup**&nbsp;


**Applicable to both intake \& exhaust PID setup**


![Image](</img/VVT 15.jpg>)


The positioning control of the Camshaft(s) is governed by the Emtron PID closed loop function.


![Image](</img/VVT 16.jpg>) &nbsp;


**Intake Deadband +/-**&nbsp;


The output control signal is held constant when the Input Signal (Cam Position) falls within the deadband range of the Target.&nbsp;

This helps reduce steady state error and oscillations.


\*\*BMW Motorsport VANOS systems switches off the control signal automatically when in deadband to hydraulically lock the cam position.&nbsp;


Typical : 0.5 degrees


**Integral Positive Clamp**

Allows the user to set the the maximum Integral gain compensation used by the closed loop system. &nbsp;


**Integral Negative Clamp**

Allows the user to set the minimum Integral gain compensation used by the closed loop system


**Feed Forward**&nbsp;

Having a correct feed forward duty cycle value allows for more precise control.

This feed forward value is added to the control signal before the PID is applied. &nbsp;

![Image](</img/Tuning Tip.jpg>) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;

**Tuning Tip**:&nbsp;

*This is the expected duty cycle of the solenoid to hold the camshaft in a given position.*

*It can be quickly determined by commanding the camshaft to a position \& witnessing the required duty to do so.*

*Commanding an alternative angle will deliver a similar result, the average of these is your feed forward value.*


**Intake Target Filter**

Filters the Target signal to help smooth out any pulsations.


Typical Value: 5 ( 0 = OFF)


**VVTiE Base Control Frequency**

Toyota 2URFSE/2URGSE VVTiE Base frequency setting at 1000rpm


**For PID Exhaust setup**

![Image](</img/VVT 1718.jpg>)



