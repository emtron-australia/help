---
title: "ORFC Setup"
---

**ORFC Setup**


![Image](</lib/ORFC 1.jpg>)


![Image](</lib/ORFC 2.jpg>)\

**ORFC TP/PP Select**


Selects which input is used to control the ORFC


&#48;: Throttle Position 1

&#49;: Pedal Position&nbsp;


**ORFC TP/PP Threshold**


When the TPS 1 or PPS value is below this setting the Over Run Fuel Cut can become active. &nbsp;


\*\* Follows ORFC TP/PP Select

\

**Post Start Delay**


Delay after the engine has been started before ORFC can become active



**Ignition Retard**


Ignition Retard from the total ignition advance when ORFC is active



**Ignition Recovery rate**


Rate which the ignition Overrun Fuel Cut Ignition Retard is decayed to 0 once the engine has recovered.&nbsp;

Typical : 10 deg / sec



**Engine Temperature Lockout**


Engine Temperature that must be exceeded before ORFC can become active


**Speed Channel**


Used to define how the “Speed Lockout” is used.  

\

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

&#49;2: Rear  Axle Speed

&#49;3: Vehicle Speed

&#49;4: Engine Speed

&#49;5: Input Shaft Speed

&#49;6: Output Shaft Speed

\

\*\* Speed inputs must be defined and properly calibrated under “Input Setup”


**Speed Lockout Range Lo**

\

Speed below which ORFC cannot become active\

**Speed Lockout Range Hi**

\

Speed above which ORFC cannot become active\

**Speed Range Hysteresis**&nbsp;

\

Hysteresis to prevent Overrun Fuel Cut becoming active on the threshold of a speed lockout value.


Example : A speed Lockout Range Hi setting of 60 and a Speed Range Hysteresis setting of 5 will not allow Overrun Fuel Cut to become active until Speed has reduced to 55 after being over 60.


**ORFC Cut Ramp Time**

\

Used to progressively increase the cut from 0% to 100% over the specified time.


Allows for a smoother transition into the Fuel Cut.





