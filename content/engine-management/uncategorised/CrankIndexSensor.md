---
title: "Crank Index Sensor"
---

**Crank Index Sensor**


![Image](</img/AAA3.jpg>)


**Crank Sensor Type**


![Image](</img/AAA4.jpg>)

Inputting a numerical value from 0 to 2 enables setting of the crank sensor type.


&#48;: Magnetic&nbsp;

&#49;: Hall Effect or Optical Sensor

&#50;: Proximity

&#51;: Logic (Available in future)


Magnetic sensors are voltage generators.&nbsp; They produce voltage, so they will produce a sign wave signal, and generally produce higher voltages as the tone ring speed (engine speed) increases.&nbsp; They can be identified easily by usually having TWO WIRES only.&nbsp; Almost all of them will have a third wire, but this is almost always a *shield* wire, which must be connected to the ECU shield pin. &nbsp;

Wiring for Magnetic sensors is particularly sensitive, as since they can produce low voltages (especially at lower engine speeds), they can be more susceptible to interference issues.&nbsp; Proper wiring practices must be adhered to without fail especially with magnetic sensors.&nbsp; Always use the dedicated trigger input pins on the ECU (Crank +/- Sync +/-), with correct sensor polarity. &nbsp;


\*\* Polarity of Magnetic sensors must be correct.&nbsp; See Uses of Scope - Improper Crank/Sync Sensor Polarity


Hall Effect sensors produce square wave signals.&nbsp; They require a voltage source (Emtron has a dedicated 8V voltage source pin for CAS), and can be identified generally by usually having THREE WIRES.&nbsp; Supply, signal, and ground. &nbsp;

Always use the dedicated trigger input pins on the ECU (Crank +/- Sync +/-)

&nbsp;&nbsp; &nbsp;

**\*\* Do not connect Hall Effect (or any other "Pulsed" sensor grounds) to Analog Volt Ground pins**


**Crank Sensor Edge**


![Image](</img/AAA5.jpg>)

Inputting a numerical value from 0 to 2 enables setting of the crank sensor edge type.


&#48;: Rising

&#49;: Falling

&#50;: Rising \& Falling


Edge configuration should only be adjusted when using **non Pre-Defined Engine Decoding Modes**


\*\* When Selecting ANY Pre-Defined Engine Decoding mode (3 +), Crank/Sync Sensor type, Edge configuration, Pull up configuration is all pre-configured for the user.&nbsp; The user should not need to adjust these.


When using any other decoding mode (1 tooth per TDC, or Multi-Tooth Custom), **USE FALLING EDGE** unless otherwise instructed specifically by Emtron support.&nbsp;


Both Magnetic and Hall effect sensors have “fast” performance when the tone ring teeth pass the sensors on falling edge consistently.&nbsp;


![Image](</img/NewItem344.png>) &nbsp;

An example of a magnetic sensors fast edge being the falling.


![Image](</img/NewItem343.png>)

An example of a hall senor fast edge being the falling. &nbsp;


Triggering off the rising edge in either of the two above examples will cause the timing of the engine to wander at different RPMs.&nbsp;



**Crank Sensor Pullup**


![Image](</img/AAA6.jpg>)

The numerical disable/enable input to control the 5volt pull-up available for Hall Effect, Optical \& Proximity Crank sensors.


&#48;: OFF

&#49;: ON
