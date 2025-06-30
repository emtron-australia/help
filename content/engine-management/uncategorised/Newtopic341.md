---
title: "Upshift Setup"
---

**Upshift Debounce Time**


The Upshift Paddle must be held for this time for the request to be valid.


This setting prevents accidental requests in harsh Motorsport environments (vibration and vehicle harmonics).


**Upshift Torque Reduction Type**&nbsp;

\
&#48;: Fuel Cut Only

&#49;: Ign Cut Only

&#50;: Fuel + Ign Cut

&nbsp;\

**Upshift Ign Retard Mode**&nbsp;


&#48;: OFF

&#49;: Offset

&#50;: Percentage


Applies the Ignition Retard as either an Offset or Percentage of Current Ign Angle


Example: Current Ignition Angle = 20.0 BTDC


Offset = 15.0 Deg Retard. &nbsp;

Ignition Angle during Gear Cut is= 20.0 - 15.0 = 5.0 Deg&nbsp; BTDC


Percentage = 50.0 % Retard.&nbsp;

Ignition Angle During&nbsp; Cut := 20 - 50% x 20.0 = 10.0 Deg BTDC


**Upshift Torque Reduction Min Time**&nbsp;

\
The Upshift function works by initially applying Torque Reduction, before then entering the Rev-Matching phase controlled by the Rev-Match Enable Table. &nbsp;


This setting ensures the Torque Reduction is ALWAYS active at the start of the gearshift for the time entered before the Rev-Matching can occur.


Typcial value : 10 -20ms


**Upshift Throttle Override** &nbsp;


&#48;: OFF

&#49;: DBW 1 - Duration Table

&#50;: DBW 1 - Function Controlled

\
This setting overrides the throttle on upshift .


Duration Table is Open Loop mode and used to control the length of time the DBW is&nbsp; controlled.


Function Controlled is Closed Loop so the Gearshift Function is used to control the length of time the DBW is controlled.


The goal is to reduce the airflow into the engine to match the engine speed of the requested upshift gear.&nbsp;


NOTE: The Rev-matching Limit setting can also be switched ON, which limits the engine the to correct rpm.


**Upshift Rev-Matching Limit** &nbsp;

\
Upshift Rev-matching Limit


Rev-matching Upshift Function will Limit the engine RPM to match the requested Upshift gear. The ECU uses Output shaft RPM and Transmission ratios between the current gear and requested gear to calculate a Rev-matched RPM Target.&nbsp;


i.e. Matching Transmission Input and Output speed referenced by Gear Ratio


NOTE 1: Output Shaft must be configured. This means Wheel Diameter and Final Drive ratios must be set correctly.


NOTE 2: The Gear Ratio Table MUST be completed for this function to operate correctly.&nbsp; See Vehicle Functions -\> Vehicle Dynamics menu.


NOTE 3: It is important the Rev-match RPM limiting starts AFTER the initial Torque Reduction Cut/Retard. This is because the Upshift Rev-Match RPM limit will be&nbsp; lower than the current&nbsp; Engine Speed and will most likely take %cut priority,&nbsp; preventing the initial Torque Reduction Cut/Retard from working.


NOTE 4: Make sure the "Upshift Rev-Match RPM Target Correction" table is setup/initialised correctly


&#48;: OFF

&#49;: ON - Outputshaft Speed

&#50;: ON - Outputshaft Speed Calculated


**Upshift Rev-Match Cut Type** &nbsp;

\
&#48;: Fuel Cut Only

&#49;: Ign Cut Only

&#50;: Fuel + Ign Cut


**Upshift Rev-Match Control Range (-/+)** &nbsp;

\
Example:


Rev-match RPM Target = 4700

Min Cut = 0%

Max Cut = 95%


&#49;) Range = +500 0RPM (Recommended)

Engine Speed:&nbsp; 4700 RPM =&nbsp; 0% Cut, 5300 RPM =&nbsp; 95% Cut


&#50;) Range = -500 RPM&nbsp;

Engine Speed:&nbsp; 4700 RPM =&nbsp; 95% Cut, 4200 RPM =&nbsp; 0% Cut


**Upshift Rev-Match Max %Cut Clamp** &nbsp;

\
Percentage cut applied to the engine&nbsp;

at the end of the control range.


**Upshift Next Gear Timeout** &nbsp;

\
The Next Gear MUST be reached within this time forthe Upshift to be valid.&nbsp; If this does not occur the ECU willre-try the gear&nbsp; shift by the number of time set in the Upshift&nbsp; "Upshift Re-retry Count" Setting.


Time starts when Upshift Solenoid is switched ON.


Typical Value = 100ms


**Upshift Re-Try Count** &nbsp;

\
The number of time the ECU will re-attempt a failed Gear Shift.


ONLY Applies when Electronic(Paddle) mode selected


Typical Value = 3


**Upshift Stacking Limit** &nbsp;

\
Sets the maximum number of Upshift Requests&nbsp;

that can be stacked.


&#48; =OFF


**Upshift Min Engine Speed** &nbsp;

\
The Engine Speed MUST be greater than this&nbsp;

value for the UpShift request to be valid


&#48; = OFF


**Upshift Min Throttle** &nbsp;

\
The Throttle Position MUST be greater than

this value for the UpShift request to be valid


&#48; = OFF


**Upshift Min Pedal** &nbsp;

\
The Pedal Position 1 MUST be greater than

this value for the UpShift request to be valid


&#48; = OFF


**Upshift User Enable** &nbsp;

\
The User Channel when selected must be ON

for the UpShift request to be valid.


&#48;: OFF

&#49;: User Channel 1

&#50;: User Channel 2

&#51;: User Channel 3

&#52;: User Channel 4

&#53;: User Channel 5

&#54;: User Channel 6

&#55;: User Channel 7

&#56;: User Channel 8

&#57;: User Channel 9

&#49;0: User Channel 10


**Upshift Force Hysteresis**&nbsp; &nbsp;

\
Prevents Gearshift re-triggering.


Example:

Gear Force Positive = 8kg

Upshift Force Hysteresis = 60%


Upshift will be triggered when Gear Force \> 8kg.&nbsp;


Once complete the Gear force will not be allowed to trigger the Gearshift until it falls below 60% of 8kg ..ie Force MUST be less than 3.2Kg (8- 4.8)
