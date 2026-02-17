---
title: "Launch Disarming"
weight: 68
---

## Launch Disarming

![Image](</img/Launch 7.jpg>)

![Image](</img/Launch 8.jpg>)

**Launch Disarming Notes:**

For the Launch System to become disarmed any the following conditions must be true with the exception of the User Channel.

(This means all these conditions are "ORed" together except the User Channel which is ANDed with all other conditions)

1) Throttle/Pedal < Launch TP/PP Disarming 

       *** OR ***

2) Engine Speed < Disarming RPM  

       *** OR ***

3) Clutch Switch Status = OFF (when enabled) 

       *** OR ***

4) Clutch Position < Clutch Position Disarming (when enabled) 

       *** OR ***

5) Speed < Disarming Speed 

       *** AND ***

6) User Channel = ON (when enabled) 

       *** AND ***

7) Disarming time > Disarming Timer settings (s)

## Launch TP/PP Disarming

The Launch Control system will be immediately disarmed when the TPS1 or PPS1 (if assigned) is less than this value 

AND "Disarming User Channel = ON" (when assigned) 

AND "Disarming Timer" has finished .

***NOTE ***

The "Launch TP/PP Arming" setting MUST be greater than the "Launch TP/PP Disarming" setting.

0.0% = OFF

## Disarming Timer

Disarms Launch Control once all disarming condition are meet and this time has been reached.

 0 = OFF.

## Disarming RPM

The Launch Control system will immediately disarm when the Engine Speed is below this value 

AND "Disarming User Channel" is ON (when enabled) 

AND "Disarming Timer" has finished.

***NOTE ***

The "Arming RPM" setting MUST be greater than the "Disarming RPM" setting.

0 = OFF

## Clutch Switch Disarming

When enabled, the Launch Control system will immediately disarm when the Clutch Switch is OFF  

AND "Disarming User Channel" is ON (when enabled) 

AND "Disarming Timer" has finished.

***NOTE ***

1:  Clutch Switch Input Channel MUST be configured 

0 = OFF

1 = ON

## Clutch Position Disarming

When enabled, the Launch Control system will immediately disarm when the Clutch Position is less than this value  

AND "Disarming User Channel "is ON (when enabled) 

AND "Disarming Timer" has finished.

*** NOTES ***

1) The "Clutch Position Arming" setting MUST be greater than the "Clutch Position Disarming" setting.

2) 100.0% = Clutch fully depressed

0 = OFF

## Disarm Speed

The Launch Control system will immediately disarm when the Launch speed reference channel input is greater than this value  

AND "Disarming User Channel "is ON (when enabled) 

AND "Disarming Timer" has finished.

NOTE: The "Disarming Speed MUST always be greater than "Arming Speed".

