---
title: "VVT Cam Control"
weight: 1
---

# VVT Cam Control Setup

All Emtron ECU’s can support variable camshaft position control (VVT – Variable Valve Timing).  Up to 4 Cam Control channels can be configured depending on the ECU model (two intake, two exhaust).  

Select the control system and appropriate outputs: 

Config View -> Function Setup -> Engine Functions -> Cam Control 

OFF = Function is switched off and the selected output channels are deallocated.

ON = Function is switched on

## Function Type

Choose the supported VVT system from the list.  

## Output Channel Selection

All Emtron outputs can be configured for Cam Control, however standard Aux Channels should be prioritized for this.  Most of Emtron Aux Channels are flexible in regards to output polarity as well (dependant on VVT system being used.  All Cam Control systems used closed loop position control - see Cam Switch for open loop control)

* Sl4/SL8                 -     Aux 1 – 8 Low side, Aux 5 – 8 High side, Aux 9 – 10 Half bridge
* KVx Rev 1     -     Aux 1 – 8 Low/High side, Aux 9 – 12 Half bridge, Aux 13 – 16 Low side
* KV8 Rev 2     -     Aux 1 – 8, 13 - 16 Low/High side, Aux 9 – 12 Half bridge 
* KV12 Rev 2    -     Aux 1 – 8 Low/High side, Aux 9 – 16 Half bridge 
* KV16 Rev 2    -     Aux 1 – 8 Low/High side, Aux 9 – 16 Half bridge 

******* Spare fuel and ignition channels are Low side.  Prioritize VVT channels to Aux channels.***

Channel selection is as follows 

* Inlet LH         -     Bank 1 intake camshaft
* Exhaust LH     -     Bank 1 exhaust camshaft
* Inlet RH         -     Bank 2 intake camshaft
* Exhaust RH     -     Bank 2 exhaust camshaft

## Driver Type

Select either Low side, or High side depending on the VVT system being used.  

******* See engine wiring schematic.  VVT solenoids are normally supplied with constant 12V+ or ground (use opposite control polarity).  ***

![Image](</img/NewItem106.png>)

![Image](</img/NewItem105.png>)
