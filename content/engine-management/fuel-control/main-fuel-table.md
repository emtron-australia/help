---
title: "Main VE Tables"
weight: 75
---

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

![Image](</img/Tuning Tip.jpg>)            

**Tuning Tip**: 

*The VE table is validated by manipulating the table to concur with the Lambda target table referenced.* 

*This process is most efficient when the ECU has a wideband lambda input enabled.*

*Once completed the volumetric efficiency will have been determined and the engine will essentially be tuned.*

*Your goal should be to eliminate or minimise any error between the VE table & the Lambda target table.*

*This can be tested by manipulating the Lambda target table at the desired load* 

*This will cause the resultant AFR to meet the new target without need to alter the VE*

*If the VE requires adjustment, error remains in the system*

*When closed loop Lambda control is activated, the VE table then becomes the feed forward for the closed loop PID routine.*

