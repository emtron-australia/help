---
title: "Cal Control"
---

**Cal Slot Control**


This function in an extremely powerful feature which allow the user to customize special calibration slots. &nbsp;

There are 4 calibration slots available.


There are 4 Calibration slots which the user may configure.&nbsp; The cal slot is controlled through the 3D user table "Cal Slot Control".&nbsp; Below is a simple example of how the cal slots could be switched.&nbsp; In this case AN Volt1 has been configured on the X axis.&nbsp; If AN Volt 1 is between 0.0V and 1.49V then Cal Slot 1 will be selected.&nbsp; If AN Volt 1 is between 1.50V and 2.49V then Cal Slot 2 will be selected and so on. &nbsp;


![Image](</img/cal slot control.png>)


&nbsp;The corresponding table must be configured to be Cal Slot controlled.&nbsp; In this case the Fuel Tables will be configured to be controlled by the Cal Slot. &nbsp; &nbsp;


![Image](</img/fuel table control.png>)


Below is the Cal Config table.&nbsp; This is where the tables are linked to the Cal Slot.&nbsp; In the below example Table 1 is used no matter what Cal Slot is selected.&nbsp;


![Image](</img/calconfig.png>)



The slot positon is defined by the setup of the Cal Slot Control table. &nbsp;

The Cal Slot Control table can be expanded into a 3D axis and any runtimes can be used to select each slot.&nbsp; This can be setup to use simple digital switch inputs, rotary position sensors, and/or any other runtime the user needs.&nbsp; This includes live runtime data that can aid in “automatic” cal switching. &nbsp;


Examples table axis:


Simple digital input

Rotary position switch

Analog voltage input

Temperature runtimes

Dual tune enable runtimes

Engine load runtimes


![Image](</img/NewItem112.png>)

The above example looks at Dual Tune Enable switch as a condition for the Y axis, but the slot position is still dependant on Throttle Position on the X axis.&nbsp; If the engine is throttled past 20%, the ECU will automatically switch back to Cal Slot 1. &nbsp;


\*\*\*In order for the Cal Slot configuration to work properly, under all Table Controls (see Table Control) being used, “Cal Slot” must be selected\*\*\*


![Image](</img/NewItem111.png>)


