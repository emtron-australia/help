---
title: "Launch Arming"
weight: 61
---

## Launch Arming

![Image](</img/Launch 5.jpg>)

![Image](</img/Launch 6.jpg>)

**Launch Arming Notes:**   

For the Launch System to become armed ALL the following conditions must be true.

 (This means all these conditions are "ANDed" together)

1) Throttle/Pedal > Launch TP/PP Arming 

          *** AND ***

2) Engine Speed > Arming RPM 

          *** AND ***

3) Clutch Switch Status = ON (when enabled)

          *** AND ***

4) Clutch Position > Clutch Position Arming (when enabled)

          *** AND ***

5) Speed > Arming Speed

          *** AND ***

6) User Channel = ON (when enabled)

          *** AND ***

7) Arming time > Arming Timer settings (s)

## Launch TP/PP Arming

The Launch Control system will be ready for arming when the TPS1 or PPS1 (if assigned) is above this value.

***NOTES ***

1: All remaining Arming Conditions MUST be be satisfied before the Launch Control becomes armed.

2. The "Launch TP/PP Arming" setting MUST be greater than the "Launch TP/PP Disarming" setting.

0.0% = OFF

## Clutch Switch Arming

Enables the Clutch Switch as an arming input for the Launch Control System. (Clutch Switch Status = ON)

***NOTES ***

1: All remaining Arming Conditions MUST be be satisfied before the Launch Control becomes armed.

2:  Clutch Switch Input Channel MUST be configured 

0 = OFF

1 = ON

## Arming Timer

Once all the arming conditions are meet this timer will start. After this time is past the Launch Control system will become Armed.

 0 = OFF.

## Arming RPM

The minimum engine speed to exceed to arm the Launch control system.

***NOTES ***

1: All remaining Arming Conditions MUST be be satisfied before the Launch Control becomes armed.

2. The "Arming RPM" setting MUST be greater than the "Disarming RPM" setting.

0 = OFF

## Clutch Position Arming

The minimum clutch position percentage to arm the Launch control system. Values above this amount are armed

***NOTES ***

1: All remaining Arming Conditions MUST be be satisfied before the Launch Control becomes armed.

2. The "Clutch Position Arming" setting MUST be greater than the "Clutch Position Disarming" setting.

3. 100.0% Position = Clutch fully depressed

0 = OFF

## Arming Speed

The Launch Control speed reference channel input source value below which the Launch Control system is armed

This ensures the vehicle is stationary or near stationary for Launch Control arming.

***NOTES ***

1: All remaining Arming Conditions MUST be be satisfied before 

the Launch Control becomes armed.

## Arming User Channel

Create a custom Arming method from a User Function.  

The Launch Control system will be ready for arming when the User Channel is ON.

***NOTES ***

1: All remaining Arming Conditions MUST be be satisfied before the Launch Control becomes armed.

0: OFF

1: User Output Channel 1

2: User Output Channel 2

3: User Output Channel 3

4: User Output Channel 4

5: User Output Channel 5

6: User Output Channel 6

7: User Output Channel 7

8: User Output Channel 8

9: User Output Channel 9

10: User Output Channel 10

.
