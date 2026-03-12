---
title: "CAN Bus"
weight: 1
---

## Introduction

The ECU has 2 independent CAN Nodes.; CAN 1 and CAN 2. The Baud rate can be independently set for each node.

The ECU has 128 message boxes. This means the ECU can Receive or Transmits on 128 different Addresses.  This is a very large number and offers great flexibility. In order the simply setup procedure the CAN 1 and CAN 2 will be separated into Channels, with each Channel having a fixed number of available messages boxes/addresses.

## CAN Termination

The ECU does not include an internal 120ohm CAN terminating resistor. This allows the ECU to be placed at any location within the CAN bus system. 

If the ECU is located at the end of the CAN  bus, an external 120 ohm terminating resistor will need to be used.

## CAN Nodes
### CAN 1
CAN 1 node is divided up into 6 Channels, 64 message objects in total

MO = Message Object

| CAN 1 Channel Number | Number of Message          |
| -------------------- | -------------------------- |
| CAN 1 - Channel 1    | 14 CAN message objects |
| CAN 1 - Channel 2    | 10 CAN message objects |
| CAN 1 - Channel 3    | 10 CAN message objects |
| CAN 1 - Channel 4    | 10 CAN message objects |
| CAN 1 - Channel 5    | 10 CAN message objects |
| CAN 1 - Channel 6    | 10 CAN message objects |

### CAN 2
CAN 2 node is divided up into 6 Channels, 64 message objects in total

| CAN 1 Channel Number | Number of Message          |
| -------------------- | -------------------------- |
| CAN 2 - Channel 1    | 14 CAN message objects |
| CAN 2 - Channel 2    | 10 CAN message objects |
| CAN 2 - Channel 3    | 10 CAN message objects |
| CAN 2 - Channel 4    | 10 CAN message objects |
| CAN 2 - Channel 5    | 10 CAN message objects |
| CAN 2 - Channel 6    | 10 CAN message objects |

## Addressing

 - 0: Single (11-BIT)
 - 1: Sequential (11-BIT)
 - 2: Single (29-BIT)
 - 3: Sequential 29-BIT)

### Base Address
Starting CAN Address / PID (Parameter ID).
The CAN Base Address tells the ECU where to *start* transmitting data from. 
>[!INFO] These values are in DECIMAL, not hex.

### Single 
Only the single "CAN Address" is active.
This means data can only be TX/RX **on that single CAN Base Address**

### Sequential
The CAN address starts at the "CAN Address"  defined then sequentially increments that address until all the data has been transmitted

Once the data (TX/RX) on the CAN Base Address is full, the ECU will poll the next address *sequentially* for additional data

IE 1250, 1251, 1252, ...

