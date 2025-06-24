---
title: "Crank Index Offset Setup"
---

**Crank Index Offset Setup**


The Crank Index Offset Setup is a critical configuration step.&nbsp; It is the point in which the ECU has latched onto the "timing" of the engine as a reference of TDC #1 Compression.&nbsp; Depending on the trigger decoding mode selected, the ECU will latch onto a an "Index Tooth", and this Index point generally does not reference TDC (Top Dead Center) cylinder #1 compression.&nbsp; The Crank Index Offset Position is what allows the ECU to *offset* the Index Tooth *position* to allow the ECU to keep time the engine appropriately.&nbsp; &nbsp;


The Crank Index Offset Value = TDC Compression Number 1 is X.X number of degrees BEFORE "Index Tooth" position


The Crank Index Offset **MUST** always be checked regardless of trigger pre-configuration.&nbsp;


![Image](</img/AAA.jpg>)


**&#49;)**&nbsp; **Always check crank index position at ignition lock angle 0.0** (especially when running waste spark).&nbsp;

**&#50;)**&nbsp; Ignition delay time should be validated at this time and adjusted.

**&#51;)**&nbsp; As RPM is increased, timing should stay at the ignition lock angle. &nbsp;

&nbsp;&nbsp; &nbsp; If this does not occur - Adjust the ignition delay time until this is achieved. &nbsp;


\*\* In Wasted Spark mode, set ignition lock angle to 0.0 due to timing light identifying the wrong RPM reading and mis-calculating advance

\*\* When Ignition Lock Enable is ON, Ignition Lock Angle value overrides all other timing values in ECU


![Image](</img/Tuning Tip.jpg>) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;

**Tuning Tip**:&nbsp;

*The fuel injectors can be disabled to validate the initial Crank Index Offset value.prior to starting the engine.*

***Config -\> Fuel -\> Fuel Main -\> Injection Mode -\> Off***

*Direct fire engines may be 360deg out of cycle which can be corrected numerically.*
