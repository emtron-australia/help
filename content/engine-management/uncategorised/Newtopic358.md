---
title: "Engine Torque Correction"
---

# Engine Torque Correction Table


![Image](</img/Torque man 3.jpg>)


The ECU accurately calculates the Engine Torque, however if any calibration errors lead to incorrect readings, this table allows the user to adjust the gain based on any parameter listed in the axis setup form.&nbsp; &nbsp;


The range is 0.000 to 2.000, a value of 1.000 being equivalent to the calculated torque demand without correction. The default table is produced using only the X axis as an example. The Y axis is available and can be enabled at any time in the axis setup form.


![Image](</img/Torque man 4.jpg>)


**Example**

Engine Torque Ideal = 490Nm

Frictional Loss Total = -88Nm

Engine Torque Correction = 0.985


**Engine Torque (Uncorrected) = (490Nm - 88Nm ) x 0.985 = 396Nm**
