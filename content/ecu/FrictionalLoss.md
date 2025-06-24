---
title: "Frictional Loss"
---


**Frictional Loss**


Frictional loss is instrumental in torque management tuning.&nbsp; If any function in the ECU requires torque targeting, feeding error here will cause the system to not function correctly. &nbsp;


Tuning the Frictional Loss tables when the engine is in "maintenance" free revving range (neutral) is the simplest way to do this -&nbsp;

Example - change the engine speed in neutral (with nothing dragging on the engine) and adjust the frictional loss table until Engine Torque (Uncorrected) = 0


**\*\* Note - engine temperature, oil temperature, and other factors will greatly affect Frictional loss.&nbsp; There are two offset tables available to adjust for those factors.**&nbsp;

**\*\* Error in fuel model or basic setup will cause base torque values to not calculate correctly.&nbsp; Make sure there is no error in lambda target during tests.** &nbsp;


![Image](</img/NewItem801.png>)


Torque Frictional Loss = -76.0

Engine Torque Ideal = 74.4

Engine Torque Uncorrected = -1.6


Tuning -\> Engine Functions -\> Torque Management -\> Frictional Loss Table


![Image](</img/NewItem802.png>)



This procedure teaches the ECU how much "Ideal" torque is required to achieve different engine speeds, and is instrumental in RPM targeting the engine for any kind of function requiring that (RPM limiting, Launch Limiting, etc)
