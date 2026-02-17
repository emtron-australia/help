---
title: "Sequential Addressing"
weight: 1053
---

Many CAN data sets in the ECU use a sequential addressing approach. This simply means that each message is on an ID that is some offset from the "Base Address".

![Image](</img/NewItem994.png>)

In the above example, Pre-defined Tx Set 1 send it's first frame on ID 1250. The whole data set contains 10 frames. They're sent out incrementally from 1250.

eg: 1250, 1251, 1252, 1253 ... 1259.

## Custom Rx Data Sets

All parameters are received as 16 bit unsigned integers.

A CAN frame holds up to 8 bytes of data which means each frame can hold up to 4 parameters. 

Each parameter must occupy 2 bytes. 

When the receiving CAN Channel is set to Sequential, the ID must be increased by 1 every 4 channels so 

that the whole data set can be processed.

## Example:

Custom Rx Data 1 set contains 5 or more parameters.

CAN Channel 1 is set to Receive Custom Tx Data Set 1, Sequentially, on ID 1000.

Parameters 1-4 will be read from ID 1000,

    Bytes 0+1, 2+3, 4+5, 6+7.

Paramerers 5-8 will be read from ID 1001, 

    Bytes 0+1, 2+3, 4+5, 6+7.

Paramerers 9-12 will be read from ID 1002, 

    Bytes 0+1, 2+3, 4+5, 6+7.

And so on....
