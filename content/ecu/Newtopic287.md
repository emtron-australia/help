---
title: "Idle Ignition Lockouts"
---

**Idle Ignition Lockouts**


![Image](</lib/Idle Ignition 3.jpg>)


**TP1/PP1 Lockout**


Throttle position below which Idle Ignition Control can become active


When "Pedal Position 1" input is active this channel will be used. Otherwise 'Throttle Position 1"input is used.


Typical : 2%


**Speed Channel**


Used to define how the “Speed Lockout” is used. &nbsp;


&#48;: OFF

&#49;: Drive Speed

&#50;: Ground Speed

&#51;: Drive Speed Front L

&#52;: Drive Speed Front R

&#53;: Drive Speed Rear L

&#54;: Drive Speed Rear R

&#55;: Undriven Speed Front L

&#56;: Undriven Speed Front R

&#57;: Undriven Speed Rear L

&#49;0: Undriven Speed Rear R

&#49;1: Front Axle Speed

&#49;2: Rear&nbsp; Axle Speed

&#49;3: Vehicle Speed


\*\*\* Speed inputs must be defined and properly calibrated under “Input Setup”\*\*


**Speed Lockout**


Locks out Idle Ignition Control when the speed is greater than or equal to this value (KPH).


Typical : 5.0


\*\* Speed Channel must be defined. &nbsp;


**Idle Range Lockout**


The engine speed must fall below the Idle Target + Idle Range Lockout before Idle Ignition Control becomes active.&nbsp;


Example:

Idle Target = 800 (set from Idle Speed Control menu)

Idle Range Lockout = 400.


Idle Speed Control will become active when the engine speed falls below 1200 RPM.


Typical: 400 RPM


**Post Start Delay**


Delay after the engine speed has exceeded the crank exit RPM before Idle Ignition Control becomes active.&nbsp;


Typical : 2 sec


**Re-entry Delay**


Delay once all lockouts are cleared before Idle Ignition Control becomes active.