---
title: "Injection Timing Secondary"
---

**Injection Timing Secondary**


![Image](</lib/AAAA103.jpg>)


![Image](</lib/AAAA105.jpg>)


Injector timing units are values in degrees.

Units are described as an "Advance Table", so values are BTDC.

IE - 400 degrees = 400 degrees before TDC Cylinder 1 compression, or also 40 degrees before TDC between exhaust and intake stroke (overlap) - Valves Closed&nbsp;

&#51;60 degrees = TDC between exhaust and intake stroke (overlap period)

&#51;00 degrees = 60 degrees after intake valve has opened&nbsp;


SOI/EOI (Determines start of injection or end of injection) function is controlled under : [Injection Timing Sec](<StagingStartHysteresis.md>)

Config -\> Fuel -\> Fuel Secondary Setup -\> Injection Timing Sec


![Image](</lib/Z Axis26.jpg>)


Allows the Timing of the Secondary Injectors to operate independently of the Primary Injectors.&nbsp; The Sec Injectors can be advanced up during the initial transition into staged mode to help improve the overall smoothness during this event,


Table Size: 22 columns x 12 rows

Resolution: 0.1 Deg

Range: 0.0 - 720.0 Degs


This table 3D table is user definable across any available runtime


![Image](</lib/Secondary inj timing.jpg>)


Above example is spanned across intake camshaft target angle \& fuel mass final (g/cyl)
