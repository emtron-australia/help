---
title: "Subaru MY06 - MY12"
weight: 0
---

## CAN Setup
This option will allow the ECU to communication on the Factory Subaru CAN bus system. This includes both transmitting and receiving data. The ECU internally manages the addressing and the individual configuration of each ID

* Select an available CAN node, CAN1 or CAN 2
* Select Baud Rate to 500kbps
* Select a unused CAN Channel on either CAN1 or CAN2 node
* Select DATA Set = Subaru MY07-MY12 (option 20)

**NOTE: All remaining options require no further adjustment.**

The following CAN bus data is available to the ECU:

| **ECU Channel Name** | **ECU Source Input** | **Description** |
| -------------------- | -------------------- | --------------- |
| Vehicle Speed | CAN Bus OEM | This is the average speed of front wheels. |
| Drive Speed Front L | CAN Bus OEM | The ECU will put the Wheel Speed Front Left CAN data into this channel |
| Drive Speed Front R | CAN Bus OEM | The ECU will put the Wheel Speed Front Right CAN data into this channel |
| Drive Speed Rear L | CAN Bus OEM | The ECU will put the Wheel Speed Rear Left CAN data into this channel |
| Drive Speed Rear R | CAN Bus OEM | The ECU will put the Wheel Speed Rear Right CAN data into this channel |
| Steering Angle | CAN Bus OEM | The ECU will put the Steering Angle CAN data into this channel |
| Front Brake Pressure | CAN Bus OEM | The ECU will put the Brake Pressure CAN data into this channel |
