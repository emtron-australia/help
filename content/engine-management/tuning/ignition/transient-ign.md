---
title: "Transient Ignition"
---

## Transient Ignition

Tuning transient functions in Emtune is done through a combination of function setup and table settings.  

The following runtimes are generated which are applied/added/subtracted to final base Ignition calculations.  
 - Ignition Rate of Change     – The current ignition rate of change in degrees per second
 - Ign Accel Trim                     – Ignition retard trim being added by accel trim function 
 - Ign Decel Trim         – Ignition advance trim being added by decal trim function

## Transient Ignition Setup

Tuning -> Ignition -> Transient -> Ignition Transient Setup

![Image](</img/NewItem237.png>)

## Enable functions
Turn on and off Accel and/or Decel modes here.  

## Ign Accel/Decel Mode
Choose pedal position, throttle position, or MAP sensor to initiate the function.  This configures what runtime the threshold lockout looks at.  

## Accel/Decel Threshold (+/-)
The minimum rate of change required to initiate the accel/decel function – related to Acce/Decel Mode

## Ign Accel Sens Table
Control the amount of Ignition Accel Retard for a given Rate of Change.

Ignition Accel Retard = Rate of Change x Sens.

Example: 

dTP1 = 5.0%/sec

Sens = 4.5

Ignition Retard = 5.0%/sec * 4.5 = 22.5 of ignition retard.

## Ign Accel Clamp Table

Clamps the maximum amount of accel timing allowed by accel ignition.  

Example:

Accel Clamp = 10 degrees (retard)

Ignition base angle = 35 degrees

Ignition angle = 25 degrees

## Ign Accel Decay Table

Controls the percentage Ign Accel Decay per Engine Cycle

Example: 

Ign Accel = -10.0 Retard start value

Ign Decay = 10.0%.

Ignition Accel will decay back to zero at 1.0 degree per engine cycle.

## Ign Decel Sens Table
Control the amount of Ignition Decel Advance for a given Rate of Change

Ignition Decel Advance = Rate of Change x Sens.

Example: 

dTP1 = 8.0%/sec

Sens = 1.5

Ignition Advance = 8.0 %/sec x 1.5 = 12.0 of ignition advance

## Ign Decel Clamp Table

Clamps the Maximum Ignition Decel Advance

Example:

Accel Clamp = 10 degrees (advance)

Ignition base angle = 20 degrees

Ignition angle = 30 degrees

## Ign Decel Decay Table

Controls the percentage Ign Decel Decay per Engine Cycle

Example: 

Ign Decel = 10.0 Adv start value

Ign Decay = 10.0%.

Ignition Decel will decay back to zero at 1.0 degree per engine cycle.