---
title: "Initial Position Table"
weight: 85
---

## Initial Position Table

Used by the ECU as the main feed forward value to determine the output duty cycle.

This table is used in Open Loop Mode

![Image](</img/NewItem693.png>)

Initial position is the feed forward for Boost Valve Position %, and the closed loop PID if CL is active.  

**Note

Boost Valve Deadtime is pre-calculated and added to Initial Position.  

**Note – Push/Pull Solenoid Control

Will require no/very little initial position 

