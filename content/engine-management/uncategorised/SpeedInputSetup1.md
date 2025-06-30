---
title: "Speed "
---

Normally these are frequency based inputs and should be connected between Digital Input 1 - 8. The ECU can can read a frequency range on these input from 0Hz - 25kHz (25000Hz).


The following Speed Options are available:


* Left Drive Speed.
* Right Drive Speed
* Left Drive Speed 2
* Left Drive Speed 2
* Left Ground Speed
* Right Ground Speed
* Drive Speed
* Ground Speed
* Turbo Speed 1
* Turbo Speed 2
* Input Shaft Speed
* Tail Shaft Speed


The following channel assigns are recommended.&nbsp;


Four wheel drive&nbsp;

If the speed data is collected by the ECU on all 4 wheels, then assign the front wheels to the Left and Right Drive Speed Channels and the rear wheels to the Left an Right Speed 2 Channels


Gearbox Output

Assign this to the Drive Speed Channel.




**CAN Data: Input Source = Factory CAN bus**&nbsp;


This allows speed data that is available on a factory CAN bus to be displayed. The following channels can be used for different CAN bus systems.


**NOTE: When the Input Source is selected as "Factory CAN" only the Filter setting is used. All other settings are not required as the data is already calibrated.**&nbsp;


Subaru MY06-12 CAN Bus


**ECU Channel Name&nbsp; &nbsp; ECU Source Input&nbsp; &nbsp; Description**&nbsp;


Drive Speed &nbsp; &nbsp; &nbsp; &nbsp; Factory CAN Bus &nbsp; &nbsp; This is the average speed of the front wheels.


Left Drive Speed&nbsp; &nbsp; &nbsp; &nbsp; Factory CAN Bus&nbsp; &nbsp; The ECU will put the Wheel Speed Front Left CAN data into this channel

Right Drive Speed&nbsp; &nbsp; Factory CAN Bus&nbsp; &nbsp; The ECU will put the Wheel Speed Front Right CAN data&nbsp; into this channel

Left Drive 2 Speed&nbsp; &nbsp; Factory CAN Bus&nbsp; &nbsp; The ECU will put the Wheel Speed Rear Left CAN data into this channel

Right Drive 2 Speed&nbsp; &nbsp; Factory CAN Bus&nbsp; &nbsp; The ECU will put the Wheel Speed Rear Right CAN data into this channel


More information on the Subaru CAN bus is available here: Subaru MY06- MY12 CAN Setup
