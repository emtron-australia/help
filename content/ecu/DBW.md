---
title: "Drive by Wire (DBW)"
---

# Drive By Wire (DBW)&nbsp; Application Guide


All KV Series and SL Series ECU’s support from 1 up to 4 independently controlled Drive by Wire (DBW) Systems. The DBW availability is ECU based and summarized below: &nbsp;

SL4 and SL8 &nbsp; &nbsp; &nbsp; &nbsp; – &nbsp; &nbsp; &nbsp; &nbsp; 1 motor

KV8 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; –&nbsp; &nbsp; &nbsp; &nbsp; 2 motor

KV12, KV16 (Rev2) &nbsp; &nbsp; – &nbsp; &nbsp; &nbsp; &nbsp; 4 motor

Select the control system and appropriate outputs from : Config View -\> Function Setup -\> Engine Functions -\> DBW Control&nbsp;

### Function Enable

OFF = Function is switched off and the selected output channels are deallocated.

ON = Function is switched on


![Image](</img/DBW 56.jpg>)


### Function Type

&#52;x DBW channels: (3 and 4 channels are only available on KV12/KV16 Serial Number \> 1350)


* Single DBW &nbsp; &nbsp; - &nbsp; &nbsp; Using 2 Half-Bridge Drivers
* Dual DBW &nbsp; &nbsp; &nbsp; &nbsp; - &nbsp; &nbsp; Using 4 Half-Bridge Drivers
* &#51; Channel &nbsp; &nbsp; &nbsp; &nbsp; - &nbsp; &nbsp; Using 6 Half-Bridge Drivers
* &#52; Channel &nbsp; &nbsp; &nbsp; &nbsp; - &nbsp; &nbsp; Using 8 Half-Bridge Drivers

\*\* See graphic above – Yellow&nbsp;


### Output Channel Selection

There are dedicated paired outputs for each DBW channel.


DBW x Motor +ve (Positive) = Auxiliary 9 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - 5A Continuous 8A Limit

DBW x Motor -ve (Negative) = Auxiliary 10&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - 5A Continuous 8A Limit


OR


DBW x Motor +ve (Positive) = Auxiliary 11 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - 5A Continuous 8A Limit

DBW x Motor -ve (Negative) = Auxiliary 12&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - 5A Continuous 8A Limit


OR&nbsp; KV12 and KV16&nbsp; Rev2&nbsp;


DBW x Motor +ve (Positive) = Auxiliary 13 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - 10A Continuous 20A Limit

DBW x Motor -ve (Negative) = Auxiliary 14 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - 10A Continuous 20A Limit

.

OR&nbsp; KV12 and KV16 Rev2&nbsp;


DBW x Motor + (Positive) = Auxiliary 15&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - 10A Continuous 20A Limit

DBW x Motor - (Negative) = Auxiliary 16&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - 10A Continuous 20A Limit


\*\* See graphic above – Yellow&nbsp;

**NOTE:&nbsp; DBW +ve (Positive) and DBW – ve (Negative) polarity is defined as fully opening the throttle plate when +12V and Ground is respectively applied to these pins.**

### Driver Type

Select "Half-Bridge Driver" in both the “DBW Motor +” and “DBW Motor – "&nbsp; tabs.


### Frequency

In most situations select 2000Hz. A range of 500Hz to 10kHz is available.&nbsp;


**NOTE:&nbsp; Select the same frequency in both the DBW Motor + and DBW Motor – tabs for each respective motor.** &nbsp;

### DBW Relay

This relay will supply +12V to the ECU pin "Aux9-12 " (and/or Aux13-16) which will power the Half-Bridge drivers used to control the DBW Motor.&nbsp;


For safety reasons the DBW system will not operate until an Output Channel has been assigned.


When the ECU detects one of the following system errors the DBW relay will be switched off, shutting the DBW system down.

* Target Tracking Error&nbsp;
* Servo Position Tracking Error


### Input Servo Position Channels

For safety reasons, there are redundant inputs for pedal position and drive by wire servo position.&nbsp; Once the sensors are setup and calibrated, these positions are used to define the DBW target in closed loop. &nbsp;


![Image](</img/NewItem213.png>)


There are pre-configured functions to help quickly calibrate the pedal position sensors, and throttle position sensors.&nbsp; See&nbsp;


Each DBW Channel has 2 dedicated inputs for Position Feedback. These are:


**DBW 1 Channel Position Feedback**

DBW 1 Servo Position Main = Analog Volt 1 - 16

DBW 1 Servo Position Sub = Analog Volt 1 – 16&nbsp;

\*Or Maximum ANV channel count depending on ECU model


**DBW 2 Channel Position Feedback**

DBW 2 Servo Position Main = Analog Volt 1 - 16

DBW 2 Servo Position Sub = Analog Volt 1 – 16&nbsp;


**DBW 3 Channel Position Feedback**

DBW 3 Servo Position Main = Analog Volt 1 - 16

DBW 3 Servo Position Sub = Analog Volt 1 – 16&nbsp;


**DBW 4 Channel Position Feedback**

DBW 4 Servo Position Main = Analog Volt 1 - 16

DBW 4 Servo Position Sub = Analog Volt 1 – 16&nbsp;


### Input Pedal Position Channels

Pedal Position 1 = Analog Volt 1 - 16

Pedal Position 2 = Analog Volt 1 - 16


### Sensor Calibration

The positioning sensors for the system must be calibrated like any other sensor.&nbsp; This can be done manually using the Calibration Table or there is an auto calibrate function described below. &nbsp;



![Image](</img/Untitled159.png>)


**Auto Calibration of Pedal Sensors**&nbsp;

See the following menu:&nbsp; Config View -\> Engine Setup -\> PPS closed and PPS open calibrate.&nbsp; &nbsp;


![Image](</img/DBW 6.jpg>)


### Throttle Position Input Channel

The Throttle Position Input channel is NOT required in DBW applications as the DBW uses Servo Positions Inputs;&nbsp; the Throttle Position Input channel can be switch OFF.&nbsp;

The ECU will automatically copy the DBW 1 Servo Position Main into the Throttle Position 1 runtime.&nbsp;

This will allow functions requiring this input (gauges, logging, ORFC, Lockouts) to continue working.
