---
title: "Transient Fuel"
---

![Image](</img/Z Axis30.jpg>)

Tuning transient functions in Emtune is done through a combination of function setup and table settings. 

The following runtimes are generated which are applied/added/subtracted to final injection PW.  
 - Accel Fuel                    – Added fuel PW (added to final injection PW)
 - Accel Clamp                    – The maximum PW that can be added at that moment
 - Decel Fuel                     – Decreased fuel PW (subtracted from final injection PW)
 - Decel Clamp                     – The maximum PW that can be decreased at that moment 
 - Fuel Acce/Decel Scaler     – The amount of PW governed by Engine Temperature Comp multiplier

## Transient Setup

![Image](</img/Z Axis31.jpg>)

![Image](</img/Z Axis32.jpg>)

**Accel Enable:** Enable or Disable Transient Acceleration fuel mode, 

**Decel Enable:** Enable or Disable Transient Deceleration fuel mode, 

**Accel/Decel Mode:** Configures runtime input for transient function initiation. 

0: TPS 1 - Throttle position sensor 1 or Drive By Wire Servo Position Sensor 1

1: MAP - Manifold Absolute Pressure Sensor

2: PP 1 - Pedal Position Sensor 1

**Accel/Decel Threshold (+/-):** The rate of change threshold or lockout of the Accel/Decel mode runtime.

This value is set as a percentage of change over a second over it's previous state.

Lower numbers increase the sensitivity in initiating the transient fuel function.

A typical value is 1.0 %/sec.

## Accel Sens Table

![Image](</img/Z Axis35.jpg>)

![Image](</img/Z Axis36.jpg>)

The Accel Sensitivity Table is the multiplication factor as a percentage of fuel added, based on the rate of change of the Accel/Decel mode 

Note: Must be set to PP or TP

Example:

dTP1 = 20%/sec

Accel Sense = 10%

Fuel base pulse width = 5.0ms

Accel PW = 20 * 0.10 = 2.0ms

Total fuel pulse width = 5.0ms + 2.0ms = 7ms 

## Accel Clamp Table

![Image](</img/Z Axis33.jpg>)

![Image](</img/Z Axis34.jpg>)

The Accel Clamp Table limits the maximum amount of increased PW (percentage vs calculated PW) allowed.  

Example:

Accel Clamp = 50%

Fuel base pulse width = 4.0ms

Max Accel Fuel PW allowed = 2.0ms 

Total fuel pulse width = 6.0ms

## Accel Engine Temperature Comp Table

![Image](</img/Z Axis39.jpg>)

![Image](</img/Z Axis40.jpg>)

The Accel Engine Temperature Compensation Table introduces a multiplier of the calculated accel fuel value against engine temperature

Example:

Accel fuel = 10ms

Engine Temp Comp = 1.5

Total Accel fuel = 10 * 1.5 = 15.0ms

## Accel Decay Table

![Image](</img/Z Axis37.jpg>)

![Image](</img/Z Axis38.jpg>)

The Accel Decay Table controls the rate of decay or how quickly the added accel fuel is removed as a percentage of an engine cycle.  

Example:

Accel decay = 10

Accel fuel will decay back 10% every cycle
