---
title: "VVT Cam Control"
---

# VVT Cam Control Setup


All Emtron ECU’s can support variable camshaft position control (VVT – Variable Valve Timing).&nbsp; Up to 4 Cam Control channels can be configured depending on the ECU model (two intake, two exhaust). &nbsp;


Select the control system and appropriate outputs:&nbsp;

Config View -\> Function Setup -\> Engine Functions -\> Cam Control&nbsp;


OFF = Function is switched off and the selected output channels are deallocated.

ON = Function is switched on


**Function Type**


Choose the supported VVT system from the list. &nbsp;


**Output Channel Selection**


All Emtron outputs can be configured for Cam Control, however standard Aux Channels should be prioritized for this.&nbsp; Most of Emtron Aux Channels are flexible in regards to output polarity as well (dependant on VVT system being used.&nbsp; All Cam Control systems used closed loop position control - see Cam Switch for open loop control)


* Sl4/SL8 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - &nbsp; &nbsp; Aux 1 – 8 Low side, Aux 5 – 8 High side, Aux 9 – 10 Half bridge
* KVx Rev 1 &nbsp; &nbsp; - &nbsp; &nbsp; Aux 1 – 8 Low/High side, Aux 9 – 12 Half bridge, Aux 13 – 16 Low side
* KV8 Rev 2 &nbsp; &nbsp; - &nbsp; &nbsp; Aux 1 – 8, 13 - 16 Low/High side, Aux 9 – 12 Half bridge&nbsp;
* KV12 Rev 2&nbsp; &nbsp; - &nbsp; &nbsp; Aux 1 – 8 Low/High side, Aux 9 – 16 Half bridge&nbsp;
* KV16 Rev 2&nbsp; &nbsp; - &nbsp; &nbsp; Aux 1 – 8 Low/High side, Aux 9 – 16 Half bridge&nbsp;

**\*\*\***&#8202;Spare fuel and ignition channels are Low side.&nbsp; Prioritize VVT channels to Aux channels.\*\*\*

Channel selection is as follows&nbsp;

* Inlet LH &nbsp; &nbsp; &nbsp; &nbsp; - &nbsp; &nbsp; Bank 1 intake camshaft
* Exhaust LH &nbsp; &nbsp; - &nbsp; &nbsp; Bank 1 exhaust camshaft
* Inlet RH &nbsp; &nbsp; &nbsp; &nbsp; - &nbsp; &nbsp; Bank 2 intake camshaft
* Exhaust RH &nbsp; &nbsp; - &nbsp; &nbsp; Bank 2 exhaust camshaft


**Driver Type**


Select either Low side, or High side depending on the VVT system being used. &nbsp;


**\*\*\*** See engine wiring schematic.&nbsp; VVT solenoids are normally supplied with constant 12V+ or ground (use opposite control polarity).&nbsp; \*\*\*


![Image](</lib/NewItem106.png>)

![Image](</lib/NewItem105.png>)
