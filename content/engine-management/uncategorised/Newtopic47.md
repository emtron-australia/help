---
title: "DBW Closed Loop tables"
---

**DBW Feed Forward %DC Table**&nbsp;

![Image](</img/DBW 9.jpg>)

Emtron uses a Feed Forward Table to provide a base duty for the PID function to operate from.&nbsp;

This allows for very fast response as the ECU has an initial lookup table before any PID is applied. &nbsp;

This table can be expanded into 3D (X axis enabled), and any runtime can be used.&nbsp;


**DBW Proportional Gain Table**

![Image](</img/DBW 10.jpg>)

Proportional gain controls how aggressive instantaneous correction must be.&nbsp;

This table can be expanded into 3D (X axis enabled), and any runtime can be used.&nbsp;

Above is an example where the change Proportional Gain is spanned across Battery Voltage.


**DBW Integral Gain Table**

![Image](</img/DBW 11.jpg>)

Integral gain controls how much adaptive correction is needed.&nbsp;

This table can be expanded into 3D (X axis enabled), and any runtime can be used.&nbsp;


**DBW Derivative Gain Table**

![Image](</img/DBW 12.jpg>)

Derivative gain controls predictive correction where gain is based on the rate of change of error.&nbsp;

This function is used to prevent overshooting targets by looking at a number of factors like rate of change, and P and I gain.&nbsp;

This table can be expanded into 3D (X axis enabled), and any runtime can be used.&nbsp;


**DBW Min Duty Clamp Table**

![Image](</img/DBW 13.jpg>)

Allows the user to set the minimum duty cycle that can be used by the closed loop system.&nbsp;

This table can be expanded into 3D (X axis enabled), and any runtime can be used.&nbsp;


**DBW Max Duty Clamp Table**

![Image](</img/DBW 14.jpg>)

Allows the user to set the maximum duty cycle that can be used by the closed loop system.&nbsp;

This table can be expanded into 3D (X axis enabled), and any runtime can be used.&nbsp;


**DBW Pos Integral Limit Table**

![Image](</img/DBW 15.jpg>)

Allows the user to set the maximum I gain compensation used by the closed loop system.&nbsp;

This table can be expanded into 3D (X axis enabled), and any runtime can be used.&nbsp;


**DBW Neg Integral Limit Table**

![Image](</img/DBW 16.jpg>)

Allows the user to set the minimum I gain compensation used by the closed loop system.&nbsp;

This table can be expanded into 3D (X axis enabled), and any runtime can be used.&nbsp;


**NOTE:**

\*\* If using dual DBW, then axis for target errors should be selected as “shared” runtimes.&nbsp; This tells the PID system to look at the respective DBW to apply closed loop gains


![Image](</img/NewItem206.png>)


### Tuning DBW PID

The DBW servo position is controlled in the Torque Management section.

The Pedal to Throttle Area Demand Translation Tables control the driver demand translation into throttle area demand.

The relationship between throttle area demand \& DBW servo position is validated in Throttle Body Model \> Throttle Body Area Table

The Pedal to Throttle Area Demand Translation Table does not relate to DBW servo position directly


To tune the DBW PID, it is useful to reconfigure the target function \& zero the Pedal Position Demand Filter

For the purpose of tuning the PID, change the Pedal to Throttle Area Demand Translation Tables and the Throttle Body Area Table to be linear.

This will deliver a 1:1 relationship

Once PID control is validated, return to non linear Pedal to Throttle Area Demand Translation Tables \& validate the Throttle Body Area Table&nbsp; &nbsp;


See Torque Management – Throttle Mass Flow

See Torque Management – Pedal to Throttle Demand Translation Table

See Throttle Body Setup - Throttle Body Area Table

