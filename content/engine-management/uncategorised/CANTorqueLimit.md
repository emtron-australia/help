---
title: "CAN Torque Limit"
---

# CAN Torque Limit


The ECU can receive Torque Limit Request(s) over the CAN Bus. This is available on firmware 2.20.0 or later.


The torque limit frame can be received from 3 different data sets. If more than one are received they are used with the following priority:

1. &nbsp;
   1. Emtron CAN Torque Limit (ID 1428).
   1. Advanced Rx Data Set 1
   1. Pre-defined Rx Set 1 v0.1 - Message 5 (ID 1428).


This is an **Absolute** Engine Torque Limit Request. Eg: If 350.0Nm is requested the Torque Limiting function will target 350.0Nm from the engine.


The frame contains 2 torque limits, the lowest one will be applied (assuming it's the lowest of all other active torque limits).


**CAN Rx ID: 1428 (0x594)**

| **Signal**                      | **Start Bit** | **Length** | **Factor** | **Offset** | **Note**                                                                                                                                                                                     |
| ------------------------------- | ------------- | ---------- | ---------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CAN Torque Limit 1 (NM)         | &#48;         | &#49;6     | &#48;.1    | \-500      | Absolute engine torque limit. -500 = Off.                                                                                                                                                    |
| CAN Torque Limit 2 (NM)         | &#49;6        | &#49;6     | &#48;.1    | \-500      | Absolute engine torque limit. -500 = Off.                                                                                                                                                    |
| CAN Torque Limit 1 Strat Select | &#51;2        | &#52;      | &#49;      | &#48;      | Selects the torque limit strategy used to apply the torque limit.                                                                                                                            |
| CAN Torque Limit 2 Strat Select | &#51;6        | &#52;      | &#49;      | &#48;      | Selects the torque limit strategy used to apply the torque limit.                                                                                                                            |
| CAN Torque Limit 1 User Mode    | &#52;0        | &#52;      | &#49;      | &#48;      | Can be used to span a table axis. Values of 0-15.                                                                                                                                            |
| CAN Torque Limit 2 User Mode    | &#52;4        | &#52;      | &#49;      | &#48;      | Can be used to span a table axis. Values of 0-15.                                                                                                                                            |
| CAN Torque Loss                 | &#52;8        | &#49;0     | &#49;      | &#48;      | Applies a reduction to the ECU's Uncorrected Torque calculation. Can be used to account for drive train losses.&nbsp; **Should always be 0 unless you have very good reason to change it\!** |


*All data is Unsigned, Little Endian (LSB First) format.*



Example CAN Channel Setup:

![Image](</img/NewItem996.png>)



Received raw data can be viewed in the F3 window on the CAN Tab.

![Image](</img/NewItem997.png>)



Final CAN Torque limit result is shown here:

![Image](</img/NewItem998.png>)


The CAN Torque Limit User Mode 1 \& 2 values are available to be used anywhere in the ECU as table axis' or inputs to user functions.



To use the incoming torque limit, you must setup a User Torque Limit. This allows the tuner to decide how they want the ECU to act on the incoming torque limit request.

To use the CAN Torque Limit Strat Select value, set the Strat Mode to CAN Tq Request, otherwise you can force a Strat of your choosing.

![Image](</img/NewItem999.png>)

*Note: If the CAN Torque Limit Strat Select value is zero and The User Torque Limit Strat Mode is set to CAN Tq Strat Request, no limit will be applied.*


Setup the Torque Limit's Main Table to utilize the CAN Rx Torque Limit value. You can also use the CAN Torque Limit User Modes like in the example below.

Here you can see the incoming request for is being modified for User Modes above 0.

![Image](</img/NewItem1000.png>)

