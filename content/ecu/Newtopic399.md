---
title: "Downshift Setup"
---

**Downshift Debounce Time**


The Downshift Paddle must be held for this time for the request to be valid.


This setting prevents accidental requests in harsh Motorsport&nbsp;

environments (vibration and vehicle harmonics).



**Downshift Torque Reduction Type**&nbsp;

\
&#48;: Fuel Cut Only

&#49;: Ign Cut Only

&#50;: Fuel + Ign Cut

&#51;: Off

&nbsp;\

**Downshift Ign Retard Mode**&nbsp;


&#48;: OFF

&#49;: Offset

&#50;: Percentage


Applies the Ignition Retard as either an Offset or Percentage of Current Ign Angle


Example: Current Ignition Angle = 20.0 BTDC


Offset = 15.0 Deg Retard. &nbsp;

Ignition Angle during Gear Cut is = 20.0 - 15.0 = 5.0 Deg&nbsp; BTDC


Percentage = 50.0 % Retard.&nbsp;

Ignition Angle During&nbsp; Cut : = 20 - 50% x 20.0 = 10.0 Deg BTDC


**Downshift Pre-Cut Percentage Cut**&nbsp;


Fuel and/or Ignition Cut Percentage used in the Downshift Precut.


**Downshift Throttle Override** &nbsp;


&#48;: OFF

&#49;: DBW 1 - Duration Table

&#50;: DBW 1 - Function Controlled

&#51;: Throttle Solenoid - Duration Table

&#52;: Throttle Solenoid - Function Controlled

\
This setting overrides or "blips" the thottle on downshift .


Duration Table is Open Loop mode and used to control the length of time the DBW or Solenoid is held open.


Function Controlled is Closed Loop so the Gearshift&nbsp;


Function is used to control the length of time the DBW or Solenoid is held open.


The goal is to increase the airflow into the engine to match the engine speed of the requested downshift gear.&nbsp;


NOTE: The Rev-matching Limit setting can also be switched ON, which limits the engine to the correct rpm assuming enough air has benn introduced into the engine.


**Downshift Rev-Matching Limit** &nbsp;


&#48;: OFF

&#49;: ON - Outputshaft Speed

&#50;: ON - Outputshaft Speed Calculated


Rev-matching Downshift Function will Limit the engine RPM to match the requested Downshift gear. The ECU uses Output shaft RPM and Transmission ratios between the current gear and requested gear to calculate a Rev-matched RPM Target.&nbsp;


i.e. Matching Transmission Input and Output speed referenced by Gear Ratio


Make sure the "Downshift Rev-Match RPM Target Correction "table is setup/Initialised correctly


You also MUST introduce extra air into the engine either by using the DBW or a solenoid to manual open the throttle.

(Select this from the Downshift Throttle Override setting)


Example:


Current rpm = 6000, In 4th gear and downshifting to 3rd

Gear ratio 4th = 1.000

Gear ratio 3rd = 1.230


Target Downshift Engine Speed RPM = 6000 x 1.230/1.000

Target Downshift Engine Speed RPM = 7380


So the ECU will Limit the Engine Speed to 7380 assuming sufficient air has been introduced


NOTE: The Gear Ratio Table MUST be completed for this function to operate correctly. See Vehicle Functions -\> Vehicle Dynamics menu.


**Downshift Rev-Match Control Range (-/+)** &nbsp;

\
Example:


Rev-match RPM Target = 4000

Min Cut = 0%

Max Cut = 95%


&#49;) Range = +500 0RPM,&nbsp;

Engine Speed:&nbsp; 4000 RPM =&nbsp; 0% Cut, 4500 RPM =&nbsp; 95% Cut


&#50;) Range = -500 RPM (Recommended)

Engine Speed:&nbsp; 4000 RPM =&nbsp; 95% Cut, 3500 RPM =&nbsp; 0% Cut


**Downshift Rev-Match End Timeout** &nbsp;

\
Once DBW has returned to within 5% of the Target this timeout gets applied. When Time = 0 the Rev-match limit is then removed.


ONLY applies to DBW applications.&nbsp;


**Downshift Next Gear Timeout** &nbsp;

\
The Next Gear MUST be reached within this time for the Downshift to be valid.&nbsp; If this does not occur the ECU will re-try the gear&nbsp; shift by the&nbsp; number of times set in the Upshift&nbsp; "Downshift Re-retry Count" Setting.


Time starts when Downshift Solenoid is switched ON.


Typical Value = 100ms


**Downshift Re-Try Count** &nbsp;

\
The number of time the ECU will re-attempt a failed Gear Shift.


ONLY Applies when Electronic(Paddle) mode selected


Typical Value = 3


**Downshift Stacking Limit** &nbsp;

\
Sets the maximum number of Upshift Requests that can be stacked.


&#48; =OFF


**Downshift Min Engine Speed** &nbsp;

\
The Engine Speed MUST be less than this value for the Downshift request to be valid


&#48; = OFF


**Downshift Min Throttle** &nbsp;

\
The Throttle Position MUST be less than this value for the Downshift request to be valid


&#48; = OFF


**Downshift Max Pedal** &nbsp;

\
The Pedal Position 1 max position for Dowshift request to be valid


&#48; = OFF


**Downshift User Enable** &nbsp;

\
The User Channel when selected must be ON

for the Downshift request to be valid.


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


**Downshift Force Hysteresis**&nbsp; &nbsp;

\
Prevents Gearshift re-triggering.


Example:

Gear Force Positive = 8kg

Downshift Force Hysteresis = 60%


Downshift will be triggered when Gear Force \> 8kg.&nbsp;


Once complete the Gear force will not be allowed to trigger the Gearshift until it falls below 60% of 8kg ..ie Force MUST be less than 3.2Kg (8- 4.8)
