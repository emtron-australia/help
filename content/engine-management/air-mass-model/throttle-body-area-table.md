---
title: "Throttle Body Area Table"
weight: 94
---

## Throttle Body Area Table

## Tuning –> Engine Functions –> Throttle Body Model –> Throttle Body Area Table

![Image](</img/AAAA78.jpg>)

The Throttle Body Area table is a 40-cell correlation table; it gives the direct relationship between Throttle Area and Throttle Position (Servo Position). The ECU uses this table to convert any Throttle Area request into Servo Position which is then used as the DBW Target. Throttle Body templates are available to load into the ECU from the File -> Import Module File menu.

## Example:

Throttle Area Demand from the pedal = 4.37%

Using the table in the below image, the ECU would find the 4.37% area and correlate this to 9.0% Servo Position. The DBW Servo Position Target therefore becomes 9.0%

i.e the ECU is asking for 4.37% area and moves the throttle plate to 9.0% servo position to achieve this. 

![Image](</img/Throttle Body Area Table1.jpg>)

Nissan GT-R R35 Throttle Body Area table

[](<ThrottleMassFlow.md>)

Throttle body templates are also available to load into the ECU from the **File -> Import Module File menu**

There are multiple ways to calibrate the appropriate throttle area.  

## Method 1 – MAF verification

If the application is using a calibrated MAF sensor.  Then the throttle area % can be adjusted and matched to TMF air mass VS MAF air mass at different throttle/DBW servo positions.  

## Method 2 – Matching Lambda

If no MAF sensor is available, setting fuel trims to 0 (or near 0), you can adjust the throttle area to match the target mixture very quickly.  

** The only way to truly validate error in the TMF calculation is to use Method 1

** Some extreme applications where live Lambda is unstable may be more difficult to map with Method 2

See [Torque Management Tuning Guide](<TorqueManagementTuningGuide.md>), [Throttle Mass Flow](<ThrottleMassFlow.md>), and [Torque Reduction](<TorqueReduction.md>)(throttle) sections for more specific information, and guides on how to tune. 

![Image](</img/Tuning Tip.jpg>)            

**Tuning Tip**: 

*Per the Matching Lambda validation method, the Throttle Area Table is used to quickly tune the engine operating in TMF by simply manipulating the table at the various throttle areas to match the Lambda Target Table values for that given load. When the correct air fuel ratio is achieved, the Throttle Area Table is essentially validated for the purpose of running the engine. To do this the wideband lambda control should be turned off and the blend bias toward TMF be set to 100%.* 

