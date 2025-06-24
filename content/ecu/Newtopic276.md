---
title: "Lambda Transport Delay"
---

**Lambda Transport Delay**


![Image](</img/Transport Delay.jpg>)


&#51;D table that defines the delay in which the Lambda sensor reports its input &nbsp;

\*\* A sensor placed very far down the exhaust stream will have a larger delay

\*\* Transport delay is dependent on engine load. &nbsp; Higher exhaust velocity reduces delay


![Image](</img/NewItem120.png>)

Axis is spanned via RPM x TP.&nbsp; Any runtime can be used&nbsp;


\*\*\*Transport delay can affect closed loop fuel PID routine. &nbsp;


![Image](</img/Tuning Tip.jpg>) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;

**Tuning Tip**:&nbsp;


*The Lambda Transport Delay table time factor can be validated using the Emtune Logger by changing the Lambda Target table at varying loads.*&nbsp;

*By utilizing the Differences mode of the logger to measure the time it takes for the Lambda to start changing after the Lambda Target table is manipulated, you are able to verify \& validate your Lambda Transport Delay Table time factor is correct.*

*Bare in mind, once the engine is tuned. IE: The VE table agrees with the Lambda Target Table.*&nbsp;

*The VE table then becomes the feed forward value for the closed loop Wideband Lambda control PID routine.*

*The more accurate your transport delay table is. The better your closed loop Wideband Lambda control will be.*

*See [Lambda Transport Delay Guide*](<Newtopic466.md>)
