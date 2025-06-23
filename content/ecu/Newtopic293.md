---
title: "Idle Speed Control Lockouts"
---

**Idle Speed Lockouts**

\

**TP1/PP1 Lockout**

\

% below in which Idle Speed Control system becomes active.  

\

\- Throttle Position 1 used on Solenoid and Stepper systems

\- Pedal Position 1 used on DBW systems

\

**Speed Channel**

\
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

\

\*\* Speed inputs must be defined and properly calibrated under “Input Setup”

\

**Speed Lockout**

\
Locks out Idle Speed Control when the speed is greater than or equal to this value (KPH).

\

Typical : 5.0

\

\*\* Speed Channel must be defined.  

\

**Idle Range Lockout**

\
The engine speed must fall below the Idle Target + Idle Range Lockout before Idle Speed Control becomes active.

\

Example:

Idle Target = 800 (set from Idle Speed Control menu)

Idle Range Lockout = 400.

\

Idle Speed Control will become active when the engine speed falls below 1200 RPM.

\

Typical: 400 RPM
