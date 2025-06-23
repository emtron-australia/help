---
title: "Torque Correction"
---

**Torque Correction**


Firstly, the Engine Torque values must be validated on a dyno to ensure the ECU Torque Calculation (Engine Torque Ideal, Engine Torque), are close to the values being produced on the dyno

\*\* If using a dyno where wheel power is reducing values, then this error must be factored in. &nbsp;


A properly tuned engine, with no error in the basic fuel model is the first step.&nbsp; Having proper injector data, engine displacement, fuel type/stoich, and a tuned VE table will already calculate accurate engine torque. &nbsp;



Engine Torque Ideal is based on the following :


* Final Air Mass&nbsp;
* Final Fuel Flow&nbsp;
* Throttle Area
* Lambda Target
* Stoichiometric Ratio
* Number of cylinders


If engine torque is not calculating accurately, Emtron has correction factors under the torque management section -\> Tuning -\> Engine Functions -\> Torque Management -\> Engine Torque Correction Table

![Image](</lib/NewItem799.png>)


**Driver Demand Torque Correction**



**Driver Demand Torque (Nm)**


The Driver Demand Torque is the torque requested by the driver, primarily as a function of engine speed and pedal position to give a requested throttle area. We know through mathematical modeling that from throttle area

we can calculate airflow and from airflow we can calculate torque.


Apart from some specific exceptions, the engine torque must be controlled by the driver. Some exceptions include: downshifts, traction control (VDC event), pit lane speed limiter and cruise control.


The driver only has control of torque by using the pedal, but other factors get included into the mathematical model to give a final Driver Demand Torque. These include:


* Engine Speed
* Throttle Area and Diameter
* Engine VE
* Charge Temperature
* Boost Target (Used as peak load indicator)
* Lambda Target
* Number of cylinders


All those parameters get included in a complex mathematical model which generates a runtime called "Driver Demand Torque Ideal".


Accounting for frictional loss of the engine the final Driver Demand Torque can be expressed as:



| **Driver Demand Torque =  (Driver Demand Torque Ideal - Torque Frictional Loss) x Driver Demand Torque Correction** |
| ------------------------------------------------------------------------------------------------------------------- |


 


Driver Demand channel is used in some OEM applications, but also can be used as a channel in the ECU to feed forward the driver tour requests.&nbsp; The Driver Demand can be corrected via Tuning -\> Engine Functions -\> Torque Management -\> Driver Demand Torque Correction Table

