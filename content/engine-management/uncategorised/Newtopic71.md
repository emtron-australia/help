---
title: "Lambda Control - Wide Band"
---

**Lambda Control - Wideband**


All Emtron ECU’s can support closed loop wideband lambda control using various methods.&nbsp; KV series ECUs have two internal wideband control systems that allow the user to wire lambda sensors directly to the ECU.&nbsp; In addition to this, Emtron ELC (Emtron Lambda to CAN) devices may be connected over CAN networking (included in all Emtron ECUs), and even an external Lambda controller that has a standard AV output can be used. &nbsp;


**Hardware specification**&nbsp;


* SL4/SL8 &nbsp; &nbsp; - &nbsp; &nbsp; No internal lambda control.&nbsp; Use ELC, standard AV, user CAN
* KV8/12/16 &nbsp; &nbsp; - &nbsp; &nbsp; Dual internal lambda control, and/or ELC, standard AV, user CAN


Select the control system and appropriate outputs:&nbsp;

Config View -\> Function Setup -\> Engine Functions -\> Closed Loop Lambda Control&nbsp;


OFF = Function is switched off and the selected output channels are deallocated.

ON = Function is switched on


**Function Type**


* Wideband Control – Lambda 1 Channel = Single Lambda input using Lambda Channel 1
* Wideband Control – Lambda 2 Channel = Single Lambda input using Lambda Channel 2
* Wideband Dual Control (La1 + La2) = Dual Lambda inputs using Lambda Channel 1 and 2
* Narrowband Control – Sensor 1 = Single narrowband input on channel 1(See Narrowband Lambda)
* Narrowband Control – Sensor 2 = Single narrowband input on channel 2 (See Narrowband Lambda)
* Dual Narrowband Control (Sensor 1+2) = Dual narrowband input on both channels (See Narrowband Lambda)



**Input Channel Selection**


Emtron Lambda inputs must be defined under input selection. &nbsp;

Config View -\> Inputs -\> Input Pin Setup -\>Engine -\>&nbsp;


Lambda 1 – Select input

Lambda 2 – Select input&nbsp;


Input selection is as follows&nbsp;

* Internal Lambda 1&nbsp; &nbsp; - &nbsp; &nbsp; Uses internal lambda controller #1 (KV series only)
* Internal Lambda 2&nbsp; &nbsp; - &nbsp; &nbsp; Uses internal lambda controller #2 (KV series only)
* CAN ELC #x Ch-x&nbsp; &nbsp; - &nbsp; &nbsp; Defines which ELC channel to use (See Emtron ELC)
* ANV x&nbsp; &nbsp; &nbsp; &nbsp; -&nbsp; &nbsp; Define and calibrate as standard AV input&nbsp;
* CAN Lambda x &nbsp; &nbsp; -&nbsp; &nbsp; Define input as user received CAN input (see CAN Bus)
* CAN NTK EL-4 x&nbsp; &nbsp; -&nbsp; &nbsp; For use with NTL Lambda Controller EL-4


**Input options**


* Pressure Correction&nbsp; &nbsp; -&nbsp; &nbsp; Lambda sensors can have EMAP compensation enabled (see Exhaust Back Pressure)&nbsp;
* Calibration Type &nbsp; &nbsp; -&nbsp; &nbsp; Select Custom for configuring ANV input, or Predefined if using internal Lambda controller,&nbsp;

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Emtron ELC, or NTK EL-4

* Predefined Calibration&nbsp; &nbsp; -&nbsp; &nbsp; Select LSU internal or NTK EL-4



