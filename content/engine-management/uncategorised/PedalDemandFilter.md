---
title: "Pedal Position Demand Filter"
---

**Introduction**


The ECU takes the raw **Pedal Position Sensor 1** input, passes it through exponential filter to help smooth out signal fluctuations, then generates a new runtime **Pedal Position Demand.**


| **Pedal Position Sensor&nbsp; -\> &nbsp; EXPONTENTIAL FILTER&nbsp; -\> Pedal Position Demand**&nbsp; |
| ---------------------------------------------------------------------------------------------------- |




The filter coefficients for the exponential filter are adjustable using a table.&nbsp; These filter coefficients can be used to heavily filter small throttle corrections, while allowing large throttle changes to have little or no filtering. By heavily filtering small throttle corrections, throttle sensitivity can be reduced, helping the throttle "feel" when driving over bumpy roads or when making small throttle changes. Little filtering when making large throttle changes helps to give a fast throttle response when a large acceleration or deceleration is requested.


See the [DBW Torque Management](<DBWTorqueMang.md>)&nbsp; help topic for more information on the process of converting Pedal Position to Throttle Area to DBW Servo target. &nbsp;


***

# Pedal Position Demand Filter Lockouts &nbsp;


These settings allow for the lockout of the pedal filter based on the pedal position. &nbsp;



![Image](</img/NewItem225.png>)


***

# Pedal Position Demand Filter Table&nbsp;


This controls how much filtering is applied.&nbsp; It is common to filter heavily at low rates of pedal position sensor output in order to achieve a smooth driver torque demand.


&#48; = Filtering OFF

&#57;9 = Max Filtering


**Important Note:**&nbsp; It is strongly recommended to span the table axis as follows:


* X - Axis = Rate of Pedal Position sensor change&nbsp;
* Y - Axis = Pedal Position Sensor&nbsp;



**Example**


Using dPedal Position Sensor 1 and Pedal Position Sensor 1, the Throttle Area Demand can be softened at low dPedal rates whilst also giving the ability to change the filtering based on the raw pedal position.&nbsp;



![Image](</img/Untitled183.png>)



Reviewing PC/ECU logs will allow the user to achieve the desired effect. &nbsp;


* Top Plot (white trace) shows Throttle Area Demand&nbsp;
* Bottom Plot shows the Pedal Position Sensor (green trace) vs Pedal Position Demand (white trace)


![Image](</img/NewItem174.png>)



