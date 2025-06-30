---
title: "Fuel Pressure Limit Setup"
---

**Fuel Pressure Limit Setup**

![Image](</img/9.jpg>)


![Image](</img/10.jpg>)&nbsp;


**Engine Speed Limit**

Engine speed limit applied when limit is active


**Control Range (-/+)**

Engine Speed Limit control range in RPM when limit is active


**Minimum %Cut Clamp**

Percentage cut applied to the engine at the start of the control range.

The cut type is defined in the Function Output.


**Maximum %Cut Clamp**

Percentage cut applied to the engine at the end of the control range&nbsp;

The cut type is defined in the Function Output


**Limit Hysteresis**

Fuel Pressure must return to the (Limit Value + Hysteresis value) for the "Recovery Hold Time" entered before the Limit is switched OFF.


**Post Start Lockout**

Will prevent the limit operating during crank and for a time after the engine has started.


**Limit Recovery Mode**

Controls the limit exit strategy.


**Mode 0:** Fuel Pressure \> (Target Limit Pressure + Hysteresis) for the specified Hold Time.

**Mode 1:** Fuel Pressure \> (Target Limit Pressure + Hysteresis) for the specified Hold Time.

AND&nbsp; &nbsp; &nbsp; Engine Speed must have reached the value in the Engine Speed Limit setting


&#48;: Mode 0

&#49;: Mode 1


**Limit Recovery Hold Time**

When the Engine Protection limit is activated a time delay can be applied before the engine can recover. &nbsp;

This to prevent premature engine recovery from an Engine Protection event.


**Limit Recovery Cut Time**

Allow the cut to be progressively removed from the engine.


**User Lockout**

Allows the user to Lockout the Limit.

When the selected User Channel is ON a Limit request will still be generated but the engine will not be limited. ie %Cut will be zero.


Used for situations when you want to generate a Limit Request but not actually limit/cut the engine.


&#48;: OFF

&#49;: User Channel 1

&#50;: User Channel 2

&#51;: User Channel 3

&#52;: User Channel 4

&#53;: User Channel 5

&#54;: User Channel 6

&#55;: User Channel 7

&#56;: User Channel 8

&#57;: User Channel 9

&#49;0: User Channel 10


**Fuel Pressure Limit Table**

![Image](</img/11.jpg>)

User defined Fuel differential offset pressure limit table. Limit is active below the offset kPa input values.

Fuel Pressure 1 Differential Offset runtime value is utilised


**Fuel Pressure Limit - Turn ON Delay Table (Sec)**

![Image](</img/12.jpg>)

User defined limit activation delay table in seconds.

