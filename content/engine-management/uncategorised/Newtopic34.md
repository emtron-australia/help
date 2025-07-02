---
title: "Idle Speed Control Lockouts (TMF)"
---


**Idle speed control lockouts (TMF)**

**Tuning –\> Engine Functions –\> Idle Speed control –\> Idle Speed Control lockouts (TMF)**


![Image](</img/AAAA83.jpg>)


![Image](</img/Idle speed control lockouts TMF.jpg>)


**TP1/PP1 Lockout**


For TMF idle speed control, this is a Pedal Position 1 lockout target.

This feature uses a 0.5% hysteresis in its application.

Example: TP1/PP1 Lockout = 1.5%

PP1 \< 1.5% Closed Loop becomes active

PP1 \>= 2.0% Closed Loop goes into hold.


A typical value is 0.5% Pedal Position


**Speed Channel**


Used to define how the “Speed Lockout” is used.  


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

&#49;2: Rear Axle Speed

&#49;3: Vehicle Speed


**\*\* Speed inputs must be defined and properly calibrated under “Input Setup”**


Speed Lockout

\
Locks out Idle Speed Control when the speed is greater than or equal to this value (KPH).


A typical value is 5.0


**\*\*Note: A Speed Channel must be defined to function\*\***


Idle Target Tracking RPM Range

\
The engine speed must fall to the Idle Target + Idle Target Tracking RPM Range. This is the rpm threshold for TMF idle speed control activation.

Example:

Idle Target rpm (Plus any Offsets applied) = 800&nbsp;

Idle Target Tracking RPM Range = 350

TMF Idle Speed Control will become active when the engine speed falls to equal 1150 RPM.

A typical vale is 350 RPM


Idle Target Tracking Decay – Neutral

This function sets the rate of decay to idle in rpm per second that the engine speed reduction is applied once the engine speed is within the Idle Target Tracking RPM Range and the transmission is regarded to be in Neutral

A typical value is 250 rpm/sec


Idle Target Tracking Decay – In Gear

This function sets the rate of decay to idle in rpm per second that the engine speed reduction is applied once the engine speed is within the Idle Target Tracking RPM Range and the transmission is regarded to be in Gear

A typical value is 250 rpm/sec

