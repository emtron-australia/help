---
title: "Torque Management"
---

# Torque Management Introduction


![Image](</img/Torque man.jpg>)

# ECU Torque Calculations


The engine torque produced by combustion is calculated by the ECU using modelled algorithms and is referred to as “Ideal” EngineTorque.&nbsp; The moving parts inside the engine assembly create drag and therefore limit the torque available. The estimate of torque required to overcome this drag effect is called Frictional Loss.


The ECU also produces a calculation for Driver Demand Torque using a weighted mathematic model from multiple inputs. This is explained more in the Driver Demand Torque topic below.&nbsp;


The Engine Torque and Driver Demand Torque calculations have no correlation and operate independently. However both calculations will merge and track very closely, but the accuracy of these calculations will depend on the accuracy of the engine setup and mapping: i.e Injector Data, Fuel Density, VE Model etc. The ECU calculates Torque in the units of Newton-metre (Nm).



The Engine Torque and Driver Demand Torque data can be transmitted over the CAN bus in some OEM applications, which is another reason the accuracy of the calculation is important.


**Engine Torque (Nm)**


The Primary data source for calculating Engine Torque is the Final Air Mass (g/s) entering the engine. The Final Air Mass will be heavily influenced by VE table and Injector size so this data must be as accurate as possible to ensure the accuracy of the Engine Torque calculation.


**Step 1.** Calculate the "Ideal" Engine Torque using the following inputs:


* Final Air Mass (g/s)
* Throttle Area
* Lambda Target
* Stoichiometric Ratio
* Number of cylinders



**Step 2.** Calculate the "uncorrected " Engine Torque accounting for the frictional loss of the engine. It is named "uncorrected" because other inputs can further change the Engine Torque. An Engine Torque Correction

factor can also be applied and is described further down the page.


| **Engine Torque (Uncorrected) =&nbsp; (Engine Torque Ideal - Torque Frictional Loss) x Engine Torque Correction** |
| ----------------------------------------------------------------------------------------------------------------- |



**Step 3.** Calculate the final Engine Torque accounting for the additional inputs that can reduce or increase Engine Torque such as:&nbsp;


* Engine Cutting (Reduce Engine Torque)
* Ignition Retard&nbsp; (The Torque Model assumes the engine has the Ignition tuned for peak torque, so any retard will therefore reduce Engine Torque)
* Throttle (Throttle Mass Flow function(s) can close the throttle plate, reducing the Air Mass and hence Engine Torque. For example VDC control)
* Nitrous (This will increase Engine Torque)



**Driver Demand Torque (Nm)**


The Driver Demand Torque is the torque requested by the driver, primarily as a function of engine speed and pedal position to give a requested throttle area. We know through mathematical modeling that from throttle area

we can calculate airflow and from airflow we can calculate torque.


Apart from some specific exceptions, the engine torque must be controlled by the driver. Some exceptions include: downshifts, traction control (VDC event), pit lane speed limiter and cruise control.


The driver only has control of torque by using the pedal, but other factors get included into the mathematical model to give a final Driver Demand Torque. These include:


* Engine Speed
* Throttle Area and Diameter&nbsp;
* Engine VE
* Charge Temperature
* Boost Target (Used as peak load indicator)
* Lambda Target
* Number of cylinders


All those parameters get included in a complex mathematical model which generates a runtime called "Driver Demand Torque Ideal".


Accounting for frictional loss of the engine the final Driver Demand Torque can be expressed as:



| **Driver Demand Torque =&nbsp; (Driver Demand Torque Ideal - Torque Frictional Loss) x Driver Demand Torque Correction** |
| ------------------------------------------------------------------------------------------------------------------------ |




It is worth mentioning the Boost Target and how the Boost Target table should be setup to help generate a more accurate Driver Demand Torque. The Y-Axis or load axis should be set to "Throttle Area Demand - Pedal" and not the raw Pedal Position Sensor.&nbsp;


![Image](</img/Untitled202.png>)

Nissan GT-R R35 Boost Target table.



**Torque Runtime Data**


Engine Torque and Driver Demand Torque data is available in the Runtime menu(F3) -\> Torque tab.


![Image](</img/Untitled180.png>)


***

**Torque Management Menus**


The Engine Torque and Driver Demand Torque settings are available from the Engine Functions -\> Torque Management menu,.


![Image](</img/Untitled212.png>)

# &nbsp;

# Torque Reduction Ignition Retard Gain Table

This table calibrates the torque reduction % per degree.&nbsp; When a torque request is applied the ECU will calculate how much retard is required to achieve this torque request. &nbsp;


See default table settings below. &nbsp; &nbsp;


![Image](</img/Untitled203.png>)

Torque Reduction Ignition Retard Gain Table

# Torque Reduction Cut Gain Table&nbsp;

This table calibrates the torque reduction % per %cut.&nbsp; When a torque request is applied the ECU will calculate how much cut is required to achieve this torque request. &nbsp;


See default table settings below. &nbsp; &nbsp;


![Image](</img/NewItem218.png>)

Torque Reduction Cut Gain Table


***


Information on the Cranking Throttle Area and Throttle Area Translation are available further down as sub-topics. Before viewing these topics please read [DBW Torque Management](<DBWTorqueMang.md>) &nbsp;



***

