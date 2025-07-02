---
title: "TCM Setup"
---


**TCM Setup**


**Nissan Transmission Control Module (TCM)** &nbsp;


The transmission control module is responsible for anything related to the transmission.&nbsp;

The ECU does not control any part of the transmission,&nbsp;

However, it is responsible for obeying torque requests accurately which are sent to it via the CAN bus.&nbsp;

The ECU is responsible for reducing torque by closing the throttle and by retard.&nbsp;

Emtron has the ability to adjust torque requests requested by the TCM.&nbsp;


![Image](</img/AAAA70.jpg>)


**TCM Torque Limit Output Filter - Throttle**&nbsp;


![Image](</img/AAAA51.jpg>)


The TCM requests a Torque Limit (Nm) which gets converted by the ECU

into the reduced Throttle Area called "Throttle Area Demand - TCM"


This setting controls the rate at which the TCM Throttle Torque Limit&nbsp;

can reduce the Throttle Area Demand.


&#48; = OFF (more aggressive TCM Control)

&#53; = Max Filtering


Plot "Throttle Area Demand %"&nbsp; vs "Throttle Area Demand - VDC"&nbsp; for tuning.


**TCM Torque Limit Retard Gain**&nbsp;


![Image](</img/AAAA52.jpg>)


During a TCM Torque Reduction request the ECU can retard the timing to reduce Torque.&nbsp;

This setting indicates to the ECU the percentage of Torque reduced for every 1%/ Deg of Ignition Retard.


Example 1.5%/ Deg.&nbsp;

The Engine is running at&nbsp; 600Nm and a Torque&nbsp;

Reduction to 400Nm is requested.&nbsp;


This is a 33% reduction in Torque so at 1.5%/Deg&nbsp;

the ECU will Retard the Ignition 22 Degrees.


(33% / 1.5%/deg = 22 Deg)


**TCM Throttle Area Demand Gain**&nbsp;


![Image](</img/AAAA53.jpg>)&nbsp;


When the current Engine Torque is less than the TCM Torque Demand the Throttle Area will need to be increased.&nbsp;

To overcome inertia and other factors the plate needs to be momentary increased before it comes back to its calculated position.&nbsp; &nbsp;


This setting is primarily&nbsp; used in Launch Control to ensure the ECU tracks the TCM Torque Demand&nbsp;


Gain 0 = OFF

Gains up to the maximum of 5 can achieve good results.&nbsp;

