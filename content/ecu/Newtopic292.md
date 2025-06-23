---
title: "Idle Speed Control Setup"
---

**Idle Speed Control Setup**

\
**Control Method**

\
Used to select either Open or Closed Loop.

Open Loop mode is generally used to setup initial settings before using Closed Loop mode.

&#48;: Open Loop

&#49;: Closed Loop


\*\* Closed Loop applies PID functions to Idle Feed Forward

\*\* Idle Feed Forward is derived from Idle Initial Position + any comp tables&nbsp;

\

**Startup Idle Hold Time**

\
Time delay before idle speed control is active after startup

\


**Startup Idle Decay Rate**


Decay rate (in RPM/sec) after Startup Idle Hold Time expires

\

**Stepper Direction**

\
Used to set polarity of the stepper motor.

\

&#48;: Normal

&#49;: Reversed

\

**Stepper Position Full Reset**

\
Used to reset the stepper motor to its fully closed position. When set to ON the ECU will command the stepper motor to move 200 steps. Once complete the motor is returned to its default position.

\

This setting should be used on first installation when the position of the stepper motor is unknown.

\

Can be switched back to OFF at any time without effecting stepper motor operation.

\

&#48;: OFF

&#49;: ON

\

**Stepper Reset**

\
When set to Key-On the ECU will command the stepper motor to move 200 steps fully closed at Key-On.

Once completed the motor is returned to its default position.

\

The Key-OFF option requires the ECU EFI Relay control on be connected and working correctly (recommended).

&#48;: Key-ON

&#49;: Key-OFF
