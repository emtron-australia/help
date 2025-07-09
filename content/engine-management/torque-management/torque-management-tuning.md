---
title: "Torque Management Tuning"
draft: true
---

Torque Management Control in Emtune is a comprehensive function with many benefits. There are a some final tuning parameters that must be addressed for it to function to its fullest extent.

Tuning the Emtron Torque model let's the ECU determine Engine Torque in different situations. It can be used to plot data if traditional methods such as; manually retarding ignition, crudely cutting the engine, or adjusting raw throttle position are used.

Or it allows simple targeting of torque values in functions that allow it.

**Drive By Wire**

Drive By Wire targeting in the Emtron system functions as dictating the target of the relative [Throttle Area](<Newtopic77.md>) via the [Pedal Demand](<PedaltoThrottleTranslation.md>) target tables. In most cases, there is no direct relationship between the DBW Servo Position, and the Throttle Body Area. It is important to understand this fundamental difference if expecting the DBW Servo/TPS position behavior. 


The main reason for this is the Throttle Body Area as calculated is the governing factor dictating airflow to the engine, which equals torque. At the same time, the ECU can then abide by functions such as Launch Control, Gearshift Control (application build), and more to limit torque via air flow limitation through the Drive By Wire System (management).

* In DBW applications, Pedal Demand as translated to a tuned Throttle Area table will offer accurate Driver Demand Torque control, as well as being able to use the throttle for torque reduction routines (Launch Control)



**Torque Calculation**
There are a number of "calculated" torque channels that the ECU will produce.


![Image](</img/NewItem798.png>)

These channels can be viewed in Runtimes (F3), under the "Torque Tab".

Engine Torque Ideal = Actual engine torque without any compensation, correction, etc.

Engine Torque (Uncorrected) = Engine torque minus frictional loss (Engine torque that should be at flywheel)

Engine Torque = The actual calculated engine torque at the flywheel including frictional loss and any other compensations (torque reductions, etc)

The Primary data source for calculating Engine Torque is the Final Air Mass (g/s) entering the engine. The Final Air Mass will be heavily influenced by VE table and Injector size so this data must be as accurate as possible to ensure the accuracy of the Engine Torque calculation.


**Steps to Tuning Torque Management**


**Step 1.** Calculating the "Ideal" Engine Torque uses the following inputs:


* Final Air Mass (g/s)

  * Properly tuned ECU will report legitimate values Speed Density (VE table), MAF calculation, or TMF calculation (controlled by "Fuel Model" selection/blending type).
  * \*\* There can be little to/no error in Lambda vs Lambda target, basic errors in engine model (displacement, fuel injector flow, etc), charge temperature model, etc.

* Throttle Area

  * Properly tuned Throttle Area Demand table and Throttle Mass Flow calculation See [Tuning Throttle Body Area](<ThrottleMassFlow1.md>)

* Lambda Target
* Stoichiometric Ratio
* Number of cylinders




**Step 2.** Calculate the "uncorrected " Engine Torque accounting for the frictional loss of the engine. It is named "uncorrected" because other inputs can further change the Engine Torque.

```
Engine Torque (Uncorrected) = (Engine Torque Ideal - Torque Frictional Loss) x Engine Torque Correction
```


See [Frictional Loss](<FrictionalLoss.md>)

See [Torque Correction ](<TorqueCorrection.md>)


**Step 3.** Calculate the final Engine Torque accounting for the additional inputs that can reduce or increase Engine Torque such as:


* Engine Cutting (Reduce Engine Torque)
* Ignition Retard  (The Torque Model assumes the engine has the Ignition tuned for peak torque, so any retard will therefore reduce Engine Torque)
* Throttle (Throttle Mass Flow function(s) can close the throttle plate, reducing the Air Mass and hence Engine Torque. For example VDC control)
* Nitrous (This will increase Engine Torque)


See [Torque Reduction](<TorqueReduction.md>)





