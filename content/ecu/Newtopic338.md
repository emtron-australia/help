---
title: "Gearshift Compressor Setup"
---

**Gearshift Compressor Setup**

\
**Gearshift Comp Pressure Target**


Pressure Target for Compressor. The Output will be switch off when the pressure is reached.\

**Gearshift Comp Pressure Hysteresis**&nbsp;

\
This value is subtracted from the Pressure Target and determines when the Output will be switched&nbsp; back ON.


Pressure Target = 150.0 PSI

Pressure Hysteresis = 10.0 PSI


The Pump will stay ON until 150.0 PSI is reached. The Pump will then turn OFF. When the pressure drops to 140 PSI to pump will switch back ON\

**Gearshift Comp Voltage Lockout**&nbsp;


The Gearshift Compressor Output will be switched OFF below this Voltage.&nbsp; Used normally to switch OFF the Compressor to prevent battery drain in Low Voltage situations.


&#48; = OFF\

**Gearshift Comp RPM Lockout**&nbsp;


The Gearshift Compressor Output will be switched OFF below this Engine Speed.&nbsp; Used normally to switch OFF the Pump during low RPM and cranking.


&#48; = OFF


Typical Value = 400 RPM


**Gearshift User Lockout**&nbsp;


The Gearshift Compressor Output will be switched OFF when the User Channel is ON/Active.


&#48;: OFF

&#49;: User Channel 1

&#50;: User Channel 2

&#51;: User Channel 3

&#52;: User Channel 4

&#53;: User Channel 5

&#54;: User Channel 6

&#55;: User Channel 7

&#56;: User Channel 8

&#57;: User Channel 9

&#49;0: User Channel 10


**Gearshift Comp Timeout**&nbsp;


With the Compressor ON, if the Target pressure cannot be reached within this timeout value the Output will be switched OFF. The timer will only be reset when the Lockouts become active OR the Re-try Interval is reached/used.


&#48; = OFF


Typical Value = 30secs


**Gearshift Comp Re-try Interval**&nbsp;


In the event the Timeout is reach and the output is switched OFF the system will switch the ouput back ON at this interval in an attempt to keep system pressure.&nbsp; This event normally occurs when the feedback input fails.


&#48; = OFF
