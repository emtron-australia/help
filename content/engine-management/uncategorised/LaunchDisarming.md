---
title: "Launch Disarming"
---

**Launch Disarming**&nbsp;


![Image](</img/Launch 7.jpg>)


![Image](</img/Launch 8.jpg>)


**Launch Disarming Notes:**

For the Launch System to become disarmed any the following conditions must be true with the exception of the User Channel.

(This means all these conditions are "ORed" together except the User Channel which is ANDed with all other conditions)


&#49;) Throttle/Pedal \< Launch TP/PP Disarming&nbsp;

&nbsp;&nbsp; &nbsp; &nbsp; \*\*\* OR \*\*\*

&#50;) Engine Speed \< Disarming RPM &nbsp;

&nbsp;&nbsp; &nbsp; &nbsp; \*\*\* OR \*\*\*

&#51;) Clutch Switch Status = OFF (when enabled)&nbsp;

&nbsp;&nbsp; &nbsp; &nbsp; \*\*\* OR \*\*\*

&#52;) Clutch Position \< Clutch Position Disarming (when enabled)&nbsp;

&nbsp;&nbsp; &nbsp; &nbsp; \*\*\* OR \*\*\*

&#53;) Speed \< Disarming Speed&nbsp;

&nbsp;&nbsp; &nbsp; &nbsp; \*\*\* AND \*\*\*

&#54;) User Channel = ON (when enabled)&nbsp;

&nbsp;&nbsp; &nbsp; &nbsp; \*\*\* AND \*\*\*

&#55;) Disarming time \> Disarming Timer settings (s)


**Launch TP/PP Disarming**

The Launch Control system will be immediately disarmed when the TPS1 or PPS1 (if assigned) is less than this value&nbsp;

AND "Disarming User Channel = ON" (when assigned)&nbsp;

AND "Disarming Timer" has finished .


\*\*\*NOTE \*\*\*

The "Launch TP/PP Arming" setting MUST be greater than the "Launch TP/PP Disarming" setting.


&#48;.0% = OFF


**Disarming Timer**


Disarms Launch Control once all disarming condition are meet and this time has been reached.


&nbsp;0 = OFF.


**Disarming RPM**

The Launch Control system will immediately disarm when the Engine Speed is below this value&nbsp;

AND "Disarming User Channel" is ON (when enabled)&nbsp;

AND "Disarming Timer" has finished.


\*\*\*NOTE \*\*\*

The "Arming RPM" setting MUST be greater than the "Disarming RPM" setting.


&#48; = OFF


**Clutch Switch Disarming**

When enabled, the Launch Control system will immediately disarm when the Clutch Switch is OFF &nbsp;

AND "Disarming User Channel" is ON (when enabled)&nbsp;

AND "Disarming Timer" has finished.


\*\*\*NOTE \*\*\*

&#49;:&nbsp; Clutch Switch Input Channel MUST be configured&nbsp;


&#48; = OFF

&#49; = ON


**Clutch Position Disarming**

When enabled, the Launch Control system will immediately disarm when the Clutch Position is less than this value &nbsp;

AND "Disarming User Channel "is ON (when enabled)&nbsp;

AND "Disarming Timer" has finished.


\*\*\* NOTES \*\*\*

&#49;) The "Clutch Position Arming" setting MUST be greater than the "Clutch Position Disarming" setting.

&#50;) 100.0% = Clutch fully depressed


&#48; = OFF


**Disarm Speed**

The Launch Control system will immediately disarm when the Launch speed reference channel input is greater than this value &nbsp;

AND "Disarming User Channel "is ON (when enabled)&nbsp;

AND "Disarming Timer" has finished.


NOTE: The "Disarming Speed MUST always be greater than "Arming Speed".

