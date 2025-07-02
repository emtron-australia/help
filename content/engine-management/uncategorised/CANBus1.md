---
title: "CAN Bus 1/2"
---

**Introduction**


The ECU has 2 independent CAN Nodes.; CAN 1 and CAN 2. The Baud rate can be independently set for each node.


The ECU has 128 message boxes. This means the ECU can Receive or Transmits on 128 different Addresses.&nbsp; This is a very large number and offers great flexibility. In order the simply setup procedure the CAN 1 and CAN 2 will be separated into Channels, with each Channel having a fixed number of available messages boxes/addresses.


**CAN Termination**&nbsp;


The ECU does not include an internal 120ohm CAN terminating resistor. This allows the ECU to be placed at any location within the CAN bus system.&nbsp;


If the ECU is located at the end of the CAN&nbsp; bus, an external 120 ohm terminating resistor will need to be used.