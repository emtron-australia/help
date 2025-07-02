---
title: "DBW Calibration Guide"
---

&nbsp;**DBW Calibration Guide**



**Steps to Calibrating and Tuning DBW**




1. Set up Output and Input configuration functions for your ECU type as instructed here -\> [Drive by Wire (DBW)](<DBW.md>)


2. Once Inputs and Outputs are set up, select a "Module File" that is closest to your throttle system

&nbsp;![Image](</img/NewItem869.png>)![Image](</img/NewItem870.png>)

This will pre-populate all basic settings for DBW throttle PID, response time, delay, etc. &nbsp;


&#51;. &nbsp; Calibrate Pedal, See "Quick Calibrations" here -\> [Basic Configuration](<Newtopic18.md>)

Validate the Pedal is channels are tracking correctly in Runtimes (F3)&nbsp;

![Image](</img/NewItem871.png>)


&#52;. &nbsp; Calibrate DBW positions using Auto Calibrate Procedure, See "DBW Calibrate Plate" here -\> [DBW 1/2 Configuration](<DBWSetup.md>)

Validate the DBW Servo Position channels are tracking correctly in Runtimes (F3)

![Image](</img/NewItem872.png>)


&#53;. &nbsp; Adjust PID to suit the throttle if is not moving/tracking appropriately -\> [DBW Closed Loop tables](<Newtopic47.md>)


