---
title: "Sync Sensor"
---

**Sync Sensor**&nbsp;


![Image](</img/AAAA1.jpg>)



**Sync Sensor Type**&nbsp;


![Image](</img/AAAA2.jpg>)

Inputting a numerical value from 0 to 2 enables setting of the sync sensor type.


&#48;: Magnetic

&#49;: Hall/Opto

&#50;: Proximity

&#51;: Logic (Available in future)


Magnetic sensors are voltage generators.&nbsp; They produce voltage, so they will produce a sign wave signal, and generally produce higher voltages as the tone ring speed (engine speed) increases.&nbsp; They can be identified easily by usually having TWO WIRES only.&nbsp; Almost all of them will have a third wire, but this is almost always a *shield* wire, which must be connected to the ECU shield pin. &nbsp;

Wiring for Magnetic sensors is particularly sensitive, as since they can produce low voltages (especially at lower engine speeds), they can be more susceptible to interference issues.&nbsp; Proper wiring practices must be adhered to without fail especially with magnetic sensors.&nbsp; Always use the dedicated trigger input pins on the ECU (Crank +/- Sync +/-), with correct sensor polarity. &nbsp;


\*\* Polarity of Magnetic sensors must be correct.&nbsp; See Uses of Scope - Improper Crank/Sync Sensor Polarity


Hall Effect sensors produce square wave signals.&nbsp; They require a voltage source (Emtron has a dedicated 8V voltage source pin for CAS), and can be identified generally by usually having THREE WIRES.&nbsp; Supply, signal, and ground. &nbsp;

Always use the dedicated trigger input pins on the ECU (Crank +/- Sync +/-)

&nbsp;&nbsp; &nbsp;

**\*\* Do not connect Hall Effect (or any other "Pulsed" sensor grounds) to Analog Volt Ground pins**


**Sync Sensor Edge**&nbsp;


![Image](</img/AAAA3.jpg>)

Inputting a numerical value from 0 to 2 enables setting of the sync sensor edge type.


&#48;: Rising

&#49;: Falling

&#50;: Rising and Falling


Edge configuration should only be adjusted when using **non Pre-Defined Engine Decoding Modes**


\*\* When Selecting ANY Pre-Defined Engine Decoding mode (3 +), Crank/Sync Sensor type, Edge configuration, Pull up configuration is all pre-configured for the user.&nbsp; The user should not need to adjust these.


In general as stated under Crank Index Sensor, falling edge would be the "fast" edge for sensor signals, but sync sensors are not generally used for "timing" of the engine, and more for synchronization of engine cycles.&nbsp; Therefore, edge configuration has more options. &nbsp;


For example, rising OR falling edge options could be deemed best depending on where the sync tooth position is in relation to the Crank "Index Tooth".&nbsp; In some cases, if the Sync Edge is too close to the Index Tooth edge, there could be issues with identifying the engine stroke, especially at different engine speeds if there any chance of mechanical wandering of the sync trigger (IE - fixed crank trigger and belt driven cam trigger).&nbsp; Using the Scope can identify these issues, and potentially changing the sync sensor edge can correct theses issues


\*\* Note - Sync Lockout is also an option with an unreliable Sync Signal (only to be used with Missing Tooth Crank Trigger)


Rising and Falling


Engines with multi-tooth sync sensors usually will have a “long” tooth during the “crank index point”.&nbsp; Normally, a custom decoding mode is needed to run the engine with multiple sync teeth, but in this case because there is a clear difference in signal on the sync input on each stroke (low vs high), the ECU can determine the stroke immediately (this is the fastest way to decode starting/720 sync).&nbsp; Set Sync Sensor Edge configuration to Rising and Falling for these trigger types. &nbsp;


![Image](</img/NewItem342.png>)



**Sync Sensor Pullup**&nbsp;


![Image](</img/AAAA4.jpg>)

The numerical disable/enable input to control the 5volt pull-up available for Hall Effect, Optical \& Proximity Sync sensors.


&#48;: OFF

&#49;: ON