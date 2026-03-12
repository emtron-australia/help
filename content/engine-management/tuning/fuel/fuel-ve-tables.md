---
title: "VE Tables"
---

Emtune has multiple tables for many engine functions.  The table behavior is based on comprehensive selections in Tuning under the respective function (IE, Fuel, Ignition, DBW, Cam control).  Some functions have many tables that can be enabled such as Fuel and Ignition tabs.  These main functions allow you to enable a variety of compensations, modifiers, individual trims, and more.  

For main table controls, the selections are mostly universal.  

(Fuel example shown)

![Image](</img/NewItem117.png>)

Not all of the above example will be available for every function, but generally most functions are the same.  

**ON – Table *** enable those respective tables always. 

**Cal Slot** enables which table is currently being commanded by the Cal Slot Control (see Cal Slot Control)

**Z-Axis** uses a separate X axis lookup that can allow the blending of all the available tables.  

![Image](</img/NewItem116.png>)

Any runtime can be used, and the units equal which table to run in this case.  You can see in the above example the ECU will switch (and interpolate in between) the three different tables available based on TP1 position.  

*** Blend** tables allow switching between two tables only.  

## Main VE Table

![Image](</img/AAAA72.jpg>)

This table represents the Volumetric Efficiency (VE) of the engine.  

VE describes the efficiency of an engine and its ability to fill the swept engine capacity with air. 

By definition its a ratio or percentage of the volume of air drawn into the cylinder vs the actual cylinder volume displacement under static conditions. 

Normally VE is less than 100% and whilst this is considered impossible for an engine to attain 100% in practice is possible to due to dynamic effects of air flow. 

Before manipulating this table the [Lambda Target Tables](<Newtopic142.md>) must be set.

The VE is then manipulated to agree with the Lambda Target table.

The two tables are intrinsically linked and the Target must be set before the result is affected 

Typical values range from 35-40% at idle and under full load VE can reach  80-90%.

![Image](</img/VE Table.jpg>)

The above Mitsubishi EVO IX VE table example shows the typical range of values         

### Tuning Tip 
![Image](</img/Tuning Tip.jpg>)   

*The VE table is validated by manipulating the table to concur with the Lambda target table referenced.* 

*This process is most efficient when the ECU has a wideband lambda input enabled.*

*Once completed the volumetric efficiency will have been determined and the engine will essentially be tuned.*

*Your goal should be to eliminate or minimise any error between the VE table & the Lambda target table.*

*This can be tested by manipulating the Lambda target table at the desired load* 

*This will cause the resultant AFR to meet the new target without need to alter the VE*

*If the VE requires adjustment, error remains in the system*

*When closed loop Lambda control is activated, the VE table then becomes the feed forward for the closed loop PID routine.*

## Main VE Table Z-Axis Setup

![Image](</img/Z Axis1.jpg>)

The Z-Axis activates a user definable X-Axis to swap or blend between VE tables based on the selected runtime

![Image](</img/Z Axis2.jpg>)

HONDA Vtec cam switch status Z-Axis shown as an example