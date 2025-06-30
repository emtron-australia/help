---
title: "Pre-defined Rx Set 1"
---

# Pre-defined Rx Set 1


![Image](</img/NewItem1004.png>)


This data set allows a huge range of parameters to be read from the CAN bus and used by the ECU.&nbsp;


The DBC file is available at [downloads.emtronaustralia.com.au](<https://downloads.emtronaustralia.com.au/> "target=\"\_blank\"")


The data is received sequentially from ID 1424 to 1433.


Message 5 (ID 1428) includes the [Emtron CAN Torque Limit Rx](<CANTorqueLimit.md>) frame. It is received as part of this data set with the lowest priority.


Raw data received is displayed in the F3 window on the CAN Tab.


![Image](</img/NewItem1001.png>)



To use the data you must set the relevant input channel's source to "CAN Predef Rx 1/Custom Rx1".


**Example: Wheel Speed Channels:**

![Image](</img/NewItem1002.png>)


**Example: Gear Detection:**

![Image](</img/NewItem1003.png>)
