---
title: "Upshift Setup"
weight: 92
---

## Upshift Debounce Time

The Upshift Paddle must be held for this time for the request to be valid.

This setting prevents accidental requests in harsh Motorsport environments (vibration and vehicle harmonics).

## Upshift Torque Reduction Type

0: Fuel Cut Only

1: Ign Cut Only

2: Fuel + Ign Cut

 \

## Upshift Ign Retard Mode

0: OFF

1: Offset

2: Percentage

Applies the Ignition Retard as either an Offset or Percentage of Current Ign Angle

Example: Current Ignition Angle = 20.0 BTDC

Offset = 15.0 Deg Retard.  

Ignition Angle during Gear Cut is= 20.0 - 15.0 = 5.0 Deg  BTDC

Percentage = 50.0 % Retard. 

Ignition Angle During  Cut := 20 - 50% x 20.0 = 10.0 Deg BTDC

## Upshift Torque Reduction Min Time

The Upshift function works by initially applying Torque Reduction, before then entering the Rev-Matching phase controlled by the Rev-Match Enable Table.  

This setting ensures the Torque Reduction is ALWAYS active at the start of the gearshift for the time entered before the Rev-Matching can occur.

Typcial value : 10 -20ms

## Upshift Throttle Override

0: OFF

1: DBW 1 - Duration Table

2: DBW 1 - Function Controlled

This setting overrides the throttle on upshift .

Duration Table is Open Loop mode and used to control the length of time the DBW is  controlled.

Function Controlled is Closed Loop so the Gearshift Function is used to control the length of time the DBW is controlled.

The goal is to reduce the airflow into the engine to match the engine speed of the requested upshift gear. 

NOTE: The Rev-matching Limit setting can also be switched ON, which limits the engine the to correct rpm.

## Upshift Rev-Matching Limit

Upshift Rev-matching Limit

Rev-matching Upshift Function will Limit the engine RPM to match the requested Upshift gear. The ECU uses Output shaft RPM and Transmission ratios between the current gear and requested gear to calculate a Rev-matched RPM Target. 

i.e. Matching Transmission Input and Output speed referenced by Gear Ratio

NOTE 1: Output Shaft must be configured. This means Wheel Diameter and Final Drive ratios must be set correctly.

NOTE 2: The Gear Ratio Table MUST be completed for this function to operate correctly.  See Vehicle Functions -> Vehicle Dynamics menu.

NOTE 3: It is important the Rev-match RPM limiting starts AFTER the initial Torque Reduction Cut/Retard. This is because the Upshift Rev-Match RPM limit will be  lower than the current  Engine Speed and will most likely take %cut priority,  preventing the initial Torque Reduction Cut/Retard from working.

NOTE 4: Make sure the "Upshift Rev-Match RPM Target Correction" table is setup/initialised correctly

0: OFF

1: ON - Outputshaft Speed

2: ON - Outputshaft Speed Calculated

## Upshift Rev-Match Cut Type

0: Fuel Cut Only

1: Ign Cut Only

2: Fuel + Ign Cut

## Upshift Rev-Match Control Range (-/+)

Example:

Rev-match RPM Target = 4700

Min Cut = 0%

Max Cut = 95%

1) Range = +500 0RPM (Recommended)

Engine Speed:  4700 RPM =  0% Cut, 5300 RPM =  95% Cut

2) Range = -500 RPM 

Engine Speed:  4700 RPM =  95% Cut, 4200 RPM =  0% Cut

## Upshift Rev-Match Max %Cut Clamp

Percentage cut applied to the engine 

at the end of the control range.

## Upshift Next Gear Timeout

The Next Gear MUST be reached within this time forthe Upshift to be valid.  If this does not occur the ECU willre-try the gear  shift by the number of time set in the Upshift  "Upshift Re-retry Count" Setting.

Time starts when Upshift Solenoid is switched ON.

Typical Value = 100ms

## Upshift Re-Try Count

The number of time the ECU will re-attempt a failed Gear Shift.

ONLY Applies when Electronic(Paddle) mode selected

Typical Value = 3

## Upshift Stacking Limit

Sets the maximum number of Upshift Requests 

that can be stacked.

0 =OFF

## Upshift Min Engine Speed

The Engine Speed MUST be greater than this 

value for the UpShift request to be valid

0 = OFF

## Upshift Min Throttle

The Throttle Position MUST be greater than

this value for the UpShift request to be valid

0 = OFF

## Upshift Min Pedal

The Pedal Position 1 MUST be greater than

this value for the UpShift request to be valid

0 = OFF

## Upshift User Enable

The User Channel when selected must be ON

for the UpShift request to be valid.

0: OFF

1: User Channel 1

2: User Channel 2

3: User Channel 3

4: User Channel 4

5: User Channel 5

6: User Channel 6

7: User Channel 7

8: User Channel 8

9: User Channel 9

10: User Channel 10

**Upshift Force Hysteresis**   

Prevents Gearshift re-triggering.

Example:

Gear Force Positive = 8kg

Upshift Force Hysteresis = 60%

Upshift will be triggered when Gear Force > 8kg. 

Once complete the Gear force will not be allowed to trigger the Gearshift until it falls below 60% of 8kg ..ie Force MUST be less than 3.2Kg (8- 4.8)
