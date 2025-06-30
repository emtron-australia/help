---
title: "Aux Output Supplement"
---

**Aux Output Supplement**


Emtron ECU systems have a high number auxiliary outputs on all products offered in addition to being able to utilize unused fuel and ignition channels as additional outputs.&nbsp; These extra outputs can be used for various functions such as solenoid control, relay control (fans, fuel pumps, etc), PWM systems, and more.&nbsp; Keeping with the concept of Emtron flexibility, the Aux Outputs match these needs. &nbsp;

Regardless of this added flexibility, careful planning for best output use is still necessary. &nbsp;

&nbsp;&nbsp; &nbsp;

**Aux Output Connections**


**SL Series ECU – 10 Aux Outputs**

Auxiliary 1-4: Low side

&nbsp; &nbsp; Outputs rest at 0V when ECU is powered off

Outputs are open when not being commanded on

&nbsp; &nbsp; &nbsp; &nbsp; Low side control of relays, solenoids, lights, etc

Auxiliary 5-8: High side/Low side

&nbsp; &nbsp; Outputs rest at 0V when ECU is powered off

&nbsp; &nbsp; Outputs are open when not being commanded on regardless of polarity

&nbsp; &nbsp; &nbsp; &nbsp; Low side or high side control of relays, solenoids, lights, etc&nbsp;

Auxiliary 9-10: Half bridge (DC motor control – DBW)

&nbsp; &nbsp; Outputs rest at 0V when ECU is off&nbsp;

&nbsp; &nbsp; Outputs command the opposite polarity when off

&nbsp; &nbsp; &nbsp; &nbsp; IE – High side output as commanded on is low side when off

**KV Series ECU – 16 Aux Outputs**

Auxiliary 1-8: High side/Low side

Outputs rest at 0V when ECU is powered off

&nbsp; &nbsp; Outputs are open when not being commanded on/off regardless of polarity

&nbsp; &nbsp; &nbsp; &nbsp; Low side or high side control of relays, solenoids, lights, etc&nbsp;

Auxiliary 9-16: Half bridge (DC motor control – DBW – Aux 9-12 KV8 ONLY)

Outputs rest at 0V when ECU is off&nbsp;

&nbsp; &nbsp; Outputs command the opposite polarity when off

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; IE – High side output as commanded on is low side when off


\*\* KV8 Aux 13-16 cannot be used as DBW control, but the functionality regarding output state is the same


**Common Issues**&nbsp;


When using an Aux Output to control a low side output that is connected to constant power. &nbsp;

The result is the output is ON when the ECU is powered off.


See KV Series Hardware Manual - Section 3.6

&nbsp;&nbsp;

This is why the control side of many systems (relays, solenoids, etc) is switched on with ignition supply (OEM). &nbsp;

Due to the flexibility of the output, controlling the system as High Side instead can resolve this issue.&nbsp;

When using a Half Bridge output on a circuit that is sensitive to reverse polarity, this can create issues with actuation if that particular output is expecting an open circuit when commanded off. &nbsp;


**\*\* For output specifications (frequency, PWM, current ratings), see ECU specification sheets.**