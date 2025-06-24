---
title: "Launch Arming"
---

## Launch Arming&nbsp;


![Image](</img/Launch 2324.jpg>)


![Image](</img/Launch 24.jpg>)



**\---- Launch Arming Notes -----**

For the Launch System to become armed ALL the following conditions must be true. (This means all these conditions are "ANDed" together)


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


**Launch TP/PP Arming**

The Launch Control system will be ready for arming when the TPS1 or PPS1 (if assigned) is above this value.


\*\*\*NOTES \*\*\*

&#49;: All remaining Arming Conditions MUST be satisfied before the Launch Control becomes armed.

&#50;. The "Launch TP/PP Arming" setting MUST be greater than the "Launch TP/PP Disarming" setting.


&#48;.0% = OFF


**Arming Timer**

Arms Launch Control once all arming condition are meet and this time has been reached.

&#48; = OFF.


**Arming RPM**

The Launch Control system will be ready for arming when the Engine Speed is above this value.


\*\*\*NOTES \*\*\*

&#49;: All remaining Arming Conditions MUST be satisfied before the Launch Control becomes armed.

&#50;. The "Arming RPM" setting MUST be greater than the "Disarming RPM" setting.

&#51;, The "Arming RPM" should be below the Entry Range RPM threshold.


&#48; = OFF


**Clutch Switch Arming**

When set to ON the Clutch Switch can be used to arm the Launch Control System.&nbsp;

(Clutch Switch Status = ON)


\*\*\*NOTES \*\*\*

&#49;: All remaining Arming Conditions MUST be satisfied before the Launch Control becomes armed.

&#50;:&nbsp; Clutch Switch Input Channel MUST be configured&nbsp;


&#48;: OFF

&#49;: ON


**Clutch Position Arming**

The Launch Control system will be ready for arming when the Clutch Position is above this value.


\*\*\*NOTES \*\*\*

&#49;: All remaining Arming Conditions MUST be satisfied before the Launch Control becomes armed.

&#50;. The "Clutch Position Arming" setting MUST be greater than the "Clutch Position Disarming" setting.

&#51;. 100.0% Position = Clutch fully depressed


&#48; = OFF


**Arming Speed**

The Launch Control system will be ready for arming when the Launch Speed Reference Channel input is below this value.&nbsp;

This ensures the vehicle is stationary or very close before allowing the Launch Control to arm.&nbsp;


\*\*\*NOTES \*\*\*

&#49;: All remaining Arming Conditions MUST be satisfied before the Launch Control becomes armed.


**Arming User Channel**

Create a custom Arming method from a User Function. &nbsp;

The Launch Control system will be ready for arming when the User Channel is ON.


\*\*\*NOTES \*\*\*

&#49;: All remaining Arming Conditions MUST be satisfied before the Launch Control becomes armed.


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

