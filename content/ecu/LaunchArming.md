---
title: "Launch Arming"
---

**Launch Arming**&nbsp;

![Image](</img/Launch 5.jpg>)


![Image](</img/Launch 6.jpg>)


**Launch Arming Notes:**&nbsp; &nbsp;

For the Launch System to become armed ALL the following conditions must be true.

&nbsp;(This means all these conditions are "ANDed" together)


&#49;) Throttle/Pedal \> Launch TP/PP Arming&nbsp;

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; \*\*\* AND \*\*\*

&#50;) Engine Speed \> Arming RPM&nbsp;

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; \*\*\* AND \*\*\*

&#51;) Clutch Switch Status = ON (when enabled)

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; \*\*\* AND \*\*\*

&#52;) Clutch Position \> Clutch Position Arming (when enabled)

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; \*\*\* AND \*\*\*

&#53;) Speed \> Arming Speed

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; \*\*\* AND \*\*\*

&#54;) User Channel = ON (when enabled)

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; \*\*\* AND \*\*\*

&#55;) Arming time \> Arming Timer settings (s)


**Launch TP/PP Arming**&nbsp;

The Launch Control system will be ready for arming when the TPS1 or PPS1 (if assigned) is above this value.


\*\*\*NOTES \*\*\*

&#49;: All remaining Arming Conditions MUST be be satisfied before the Launch Control becomes armed.

&#50;. The "Launch TP/PP Arming" setting MUST be greater than the "Launch TP/PP Disarming" setting.


&#48;.0% = OFF


**Clutch Switch Arming**

Enables the Clutch Switch as an arming input for the Launch Control System. (Clutch Switch Status = ON)


\*\*\*NOTES \*\*\*

&#49;: All remaining Arming Conditions MUST be be satisfied before the Launch Control becomes armed.

&#50;:&nbsp; Clutch Switch Input Channel MUST be configured&nbsp;


&#48; = OFF

&#49; = ON


**Arming Timer**&nbsp;

Once all the arming conditions are meet this timer will start. After this time is past the Launch Control system will become Armed.


&nbsp;0 = OFF.


**Arming RPM**

The minimum engine speed to exceed to arm the Launch control system.


\*\*\*NOTES \*\*\*

&#49;: All remaining Arming Conditions MUST be be satisfied before the Launch Control becomes armed.

&#50;. The "Arming RPM" setting MUST be greater than the "Disarming RPM" setting.


&#48; = OFF


**Clutch Position Arming**

The minimum clutch position percentage to arm the Launch control system. Values above this amount are armed


\*\*\*NOTES \*\*\*

&#49;: All remaining Arming Conditions MUST be be satisfied before the Launch Control becomes armed.

&#50;. The "Clutch Position Arming" setting MUST be greater than the "Clutch Position Disarming" setting.

&#51;. 100.0% Position = Clutch fully depressed


&#48; = OFF


**Arming Speed**

The Launch Control speed reference channel input source value below which the Launch Control system is armed

This ensures the vehicle is stationary or near stationary for Launch Control arming.


\*\*\*NOTES \*\*\*

&#49;: All remaining Arming Conditions MUST be be satisfied before&nbsp;

the Launch Control becomes armed.


**Arming User Channel**

Create a custom Arming method from a User Function. &nbsp;


The Launch Control system will be ready for arming when the User Channel is ON.


\*\*\*NOTES \*\*\*

&#49;: All remaining Arming Conditions MUST be be satisfied before the Launch Control becomes armed.


&#48;: OFF

&#49;: User Output Channel 1

&#50;: User Output Channel 2

&#51;: User Output Channel 3

&#52;: User Output Channel 4

&#53;: User Output Channel 5

&#54;: User Output Channel 6

&#55;: User Output Channel 7

&#56;: User Output Channel 8

&#57;: User Output Channel 9

&#49;0: User Output Channel 10

.
