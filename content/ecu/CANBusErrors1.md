---
title: "CAN Bus Errors"
---


CAN Diagnostics information can be found under the Communications Tab in the Runtime (F3) menu.


**Last Error Code Status**


* Ack Error. This normally indicates the ECU cannot communicate with other devices on the BUS. Check all devices are running the same BUS Baud rate.
* BIT 0 Error. If this error is constant, it normally indicates a direct short between CAN Lo and CAN Hi.
* BIT 1 Error. If this error is constant, it normally indicates a direct short between CAN Lo and CAN Hi.
* BIT 0 \& Ack Error. If the error is toggling between these two messages, this normally indicates the CAN Lo and CAN Hi are reversed.&nbsp;


**Command Bus Errors**


* Emtron Transmitting data , but receiving device is missing from the CAN Bus.


![Image](</lib/e.png>)



* Emtron Transmitting data , but receiving device is missing from the CAN Bus **and** 120 Ohm terminating resistor **missing.**


![Image](</lib/Untitled38.png>)
