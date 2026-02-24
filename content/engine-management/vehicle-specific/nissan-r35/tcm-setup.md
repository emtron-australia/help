---
title: "Nissan GTR R35 TCM Setup"
weight: 32
---

## TCM Setup

## Nissan Transmission Control Module (TCM)

The transmission control module is responsible for anything related to the transmission.

The ECU does not control any part of the transmission,

However, it is responsible for obeying torque requests accurately which are sent to it via the CAN bus.

The ECU is responsible for reducing torque by closing the throttle and by retard.

Emtron has the ability to adjust torque requests requested by the TCM.

![Image](</img/AAAA70.jpg>)

## TCM Torque Limit Output Filter - Throttle

![Image](</img/AAAA51.jpg>)

The TCM requests a Torque Limit (Nm) which gets converted by the ECU

into the reduced Throttle Area called "Throttle Area Demand - TCM"

This setting controls the rate at which the TCM Throttle Torque Limit

can reduce the Throttle Area Demand.

0 = OFF (more aggressive TCM Control)

5 = Max Filtering

Plot "Throttle Area Demand %"  vs "Throttle Area Demand - VDC"  for tuning.

## TCM Torque Limit Retard Gain

![Image](</img/AAAA52.jpg>)

During a TCM Torque Reduction request the ECU can retard the timing to reduce Torque.

This setting indicates to the ECU the percentage of Torque reduced for every 1%/ Deg of Ignition Retard.

Example 1.5%/ Deg.

The Engine is running at  600Nm and a Torque

Reduction to 400Nm is requested.

This is a 33% reduction in Torque so at 1.5%/Deg

the ECU will Retard the Ignition 22 Degrees.

(33% / 1.5%/deg = 22 Deg)

## TCM Throttle Area Demand Gain

![Image](</img/AAAA53.jpg>)

When the current Engine Torque is less than the TCM Torque Demand the Throttle Area will need to be increased.

To overcome inertia and other factors the plate needs to be momentary increased before it comes back to its calculated position.

This setting is primarily  used in Launch Control to ensure the ECU tracks the TCM Torque Demand

Gain 0 = OFF

Gains up to the maximum of 5 can achieve good results.

