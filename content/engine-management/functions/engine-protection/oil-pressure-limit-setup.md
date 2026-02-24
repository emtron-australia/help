---
title: "Oil Pressure Limit Setup"
weight: 0
---

![Image](</img/4.jpg>)

![Image](</img/5.jpg>) 

## Engine Speed Limit

Engine speed limit applied when limit is active

## Control Range (-/+)

Engine Speed Limit control range in RPM when limit is active

## Minimum %Cut Clamp

Percentage cut applied to the engine at the start of the control range.

The cut type is defined in the Function Output.

## Maximum %Cut Clamp

Percentage cut applied to the engine at the end of the control range 

The cut type is defined in the Function Output

## Limit Hysteresis

Oil Pressure must return to the (Limit Value + Hysteresis value) for the "Recovery Hold Time" entered before the Limit is switched OFF.

## Post Start Lockout

Will prevent the limit operating during crank and for a time after the engine has started.

## Limit Recovery Mode

Controls the limit exit strategy.

**Mode 0:** Oil Pressure > (Target Limit Pressure + Hysteresis) for the specified Hold Time.

**Mode 1:** Oil Pressure > (Target Limit Pressure + Hysteresis) for the specified Hold Time.

AND      Engine Speed must have reached the value in the Engine Speed Limit setting

0: Mode 0

1: Mode 1

## Limit Recovery Hold Time

When the Engine Protection limit is activated a time delay can be applied before the engine can recover.  

This to prevent premature engine recovery from an Engine Protection event.

## Limit Recovery Cut Time

Allow the cut to be progressively removed from the engine.

## User Lockout

Allows the user to Lockout the Limit.

When the selected User Channel is ON a Limit request will still be generated but the engine will not be limited. ie %Cut will be zero.

Used for situations when you want to generate a Limit Request but not actually limit/cut the engine.

Example: During a Launch the Oil Pressure may temporally drop below the Limit Target. 

                A User Channel can be configured to lockout this limit during the first stages of Launch Control.

0: OFF

1: User Channel 1

2: User Channel 2

3: User Channel 3

4: User Channel 4

5: User Channel 5

6: User Channel 6

7: User Channel 7

8: User Channel 8

9: User Channel 9

10: User Channel 10

## Oil Pressure Limit Table

![Image](</img/78.jpg>)

User defined oil pressure limit table. Limit is active above kPa input values.

## Oil Pressure Limit - Turn ON Delay Table (Sec)

![Image](</img/8.jpg>)

User defined limit activation delay table in seconds.
