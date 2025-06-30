---
title: "Driver Demand Torque Correction Table"
---

# Driver Demand Torque Correction Table&nbsp;

![Image](</img/Torque man 5.jpg>)


Driver Demand Torque is calculated based on various parameters in the ECU along with driver controlled pedal inputs. &nbsp;

If however there are correlation errors between the actual Engine Torque and Driver Demand torque, these can be trimmed using this table.&nbsp;


The range is 0.000 to 2.000. A value of 1.000 being equivalent to the calculated torque demand without correction. As with the Engine torque correction table the default table is produced using only the the X axis as an example. However both the X \& Y axis are available and can be enabled at any time in the axis setup form.


![Image](</img/Torque man 6.jpg>)


**Note:** The Driver Demand Torque is calculated fully Independent to the Engine Torque, so there will always be a small error between the two. A normal and acceptable error is around 10%. For example Driver Demand Torque might be 470Nm and Engine Torque 490Nm. This is an acceptable error \& not unusual.
