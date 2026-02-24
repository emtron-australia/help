---
title: "DBW Calibration Guide"
weight: 79
---

 **DBW Calibration Guide**

## Steps to Calibrating and Tuning DBW

1. Set up Output and Input configuration functions for your ECU type as instructed here -> [Drive by Wire (DBW)](<dbw.md>)

2. Once Inputs and Outputs are set up, select a "Module File" that is closest to your throttle system

 ![Image](</img/NewItem869.png>)![Image](</img/NewItem870.png>)

This will pre-populate all basic settings for DBW throttle PID, response time, delay, etc.  

3.   Calibrate Pedal, See "Quick Calibrations" here -> [Basic Configuration](<Newtopic18.md>)

Validate the Pedal is channels are tracking correctly in Runtimes (F3) 

![Image](</img/NewItem871.png>)

4.   Calibrate DBW positions using Auto Calibrate Procedure, See "DBW Calibrate Plate" here -> [DBW 1/2 Configuration](<dbw-setup.md>)

Validate the DBW Servo Position channels are tracking correctly in Runtimes (F3)

![Image](</img/NewItem872.png>)

5.   Adjust PID to suit the throttle if is not moving/tracking appropriately -> [DBW Closed Loop tables](<Newtopic47.md>)

