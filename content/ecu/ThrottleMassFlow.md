---
title: "Throttle Mass Flow Setup"
---

# Throttle Mass Flow Setup


![Image](</lib/TMF Setup.jpg>)


Throttle Mass Flow (TMF) as the name indicates, is the rate at which **air mass** is flowing through a throttle body in units of grams/second (g/s). Using the throttle body size, throttle area, temperature, pre and post throttle pressures,the ECU can very accurately calculate air flow through the throttle body and therefore into the engine; this is known as the TMF Calculation. Other sensors that also generate air mass flow (g/s) data are Manifold Pressure and MAF sensors. The TMF Calculation is just another method of determining air mass flow and has benefits over MAP and MAF as discussed further down.


The image below illustrates the basic elements required to calculate TMF.



![Image](</lib/Throttle Drawing13.jpg>)



Getting into more detail, the flow through a throttle body is governed by three physical elements, Conversation of mass, Newtons second law of motion for fluids and Conservation of energy. By combining these elements the ECU can model the flow of fluid through the throttle body accounting for throttle plate thickness and throttle shaft size.&nbsp; By then including real-time data such as the **pressure ratio** across the throttle plate and the instantaneous **throttle area,** the ECU can precisely calculate the mass flow rate through a throttle body.


Although these calculation are complex, the TMF setup process for the user is kept as simple as possible with the following inputs and setup required:


**Sensor Inputs required**

1. Pressure Before the throttle Plate&nbsp;
1. Pressure After the throttle Plate&nbsp;
1. Temperature


**Setting required**&nbsp;

1. Throttle Body Size
1. Throttle Area to Servo Position Correlation Table (Throttle Body Area Table)&nbsp;



The TMF calculation can summarised in the below equation :


| **Throttle Mass Flow (g/s) = ( Pafter /&nbsp; Pbefore)&nbsp; x Throttle Area x&nbsp; Modelled throttle body fluid dynamics equation** |
| ------------------------------------------------------------------------------------------------------------------------------------- |



***

**Settings**


**Tuning -\> Engine Functions -\> Throttle Body Model -\> Throttle Mass Flow Setup**


![Image](</lib/TMF Setup 2.jpg>)


**Throttle Mass Flow Enable**


Allows the TMF function to be enabled. At this point the ECU is only calculating air mass flow into the engine. Once setup other functions like the Fuel Model and Idle Speed Control can be configured to use the TMF calculated air mass data.&nbsp;


Select which type of throttle system you have:

&nbsp; &nbsp; 1x DBW Throttle

&nbsp; &nbsp; 2x DBW Throttle

&nbsp; &nbsp; 1x Cable Throttle


**Throttle Mass Idle Valve Enable**


Enables the Idle Valve Area to be accounted for in the TMF calculation; the Throttle Body Area AND Idle Valve Area are used to give a Total Area.

**NOTE:** Normally only required on a Cable Throttle when an external Idle Air Bleed is used.


**Throttle Before Plate Pressure**


Pressure source before throttle plate


\*\* Commonly Boost Pressure

\*\* Also referred to as Charge Pressure

\*\* Normally aspirated vehicles can use Barometric Pressure as Pre Throttle pressure source


**Throttle After Plate Pressure**


Pressure source after throttle plate


\*\* Commonly Manifold Pressure


**Throttle Temperature Source**


The Air temperature input used in the TMF Calculation


**Throttle Body Size**


The Throttle Body inside diameter in millimeters. **See Tuning -\> Engine Functions -\> Throttle Body Model -\> Throttle Body Setup**


**Throttle Body Area**


Gives the direct relationship between Throttle Area and Servo Position. **See Tuning -\> Engine Functions -\> Throttle Body Model -\> Throttle Body Area Table**


***

**Throttle Mass Flow Runtimes**


The following TMF calculated runtimes are generated. See the Runtime menu (F3) Engine Data Calculated tab.


![Image](</lib/Untitled232.png>)


* Throttle Air Mass calculations report in units of g/s or g/cyl
* Throttle Pressure Ratio is the ratio of Pre Throttle Pressure sensing vs Post Throttle pressure sensing (Boost Pressure vs MAP Pressure most commonly)
* Throttle Eff Area is the calculated Throttle Area using the Servo Position and the Throttle Body Area lookup table.&nbsp;


\*\* All these runtimes can be utilized within other functions. &nbsp;


***

**Functions that can utilize the TMF Calculation**


The following functions can use the air mass data generated from the TMF calculation:&nbsp;


**Fuel Model**


Option 3: Blend - MAP Modelled + Throttle Mass Flow. TMF Fuel Model calculations can offer advantages when the throttle pressure ratio is low (partial throttle) and respond much faster in transient conditions.&nbsp; &nbsp;

For more information see the Fuel Model section.


**Idle Speed Control**&nbsp;


Option 6: DBW 1 TMF

Option 7: DBW 1+2 TMF


This allows the Idle Speed control to target Mass Flow Rate of g/s. The Throttle Mass Flow (TMF) idle speed control function delivers extremely accurate and rapid idle calculation based on actual engine’s airflow requirements. See [TMF Idle Speed Control section for more information](<Newtopic33.md>)


**Launch Control**


Option 2: Torque Limiting.


The TMF is used to control throttle plate position to achieve a target torque and target launch engine speed.


***

**Tuning TMF**


Once TMF is appropriate set up, it can make mapping the engine when it is in use very fast.&nbsp; Using TMF wherever possible is strongly advised by Emtron, especially depending on what kind of dynamometer being used, test conditions, and more – often part throttle and proper transient setup is often forgiven due to time constraints. &nbsp;



Version 1.0


Due to strictly calculating airflow via pressure ratio, the calculation will become invalid at a near equal pressure ratio through the throttle. &nbsp;


Gradually accelerate the engine under load and increase to increase the throttle area demand/effective area. &nbsp;


\*\* Final air mass calculation which can be affected by engine speed (and more) can affect the optimal blend point.&nbsp; This is why most default configurations for the Fuel Model Blend Table include Air Mass Final runtimes. &nbsp;




![Image](</lib/NewItem179.png>)&nbsp;

In this particular case the TMF signal at around 0.830 throttle pressure ratio is being unusable. &nbsp;


At this same moment, the Air Mass Modelled/blended calculation is stable and can be blended in. &nbsp;

And/or TMF Out-flowing can generate correct TMF values. &nbsp;

\*\* TMF Outflowing calculates TMF airflow when pressure ratio cannot. &nbsp;


![Image](</lib/NewItem955.png>)


![Image](</lib/NewItem818.png>)

Improper "Outflow Scale" setting.&nbsp; Adjust Throttle Mass Flow Outflow Scaler to correct


![Image](</lib/NewItem819.png>)


\*\* Throttle Mass Flow Air Flow values can only be compared to validated/tuned air flow values (tuned) such as MAP Air Mass or MAF Air Mass.&nbsp;


**TMF Correction Table**


This correction table essentially exists to help remove an error remaining in the system across a wide variety of load \& rpm conditions.


![Image](</lib/NewItem956.png>)



![Image](</lib/NewItem829.png>)

Demonstrating error in TMF Calculation that needs to be corrected in TMF Correction Table


**Tuning the Throttle Body Area Table**


The Throttle Body Area table tells the ECU how much actual throttle area is effective at different throttle positions.&nbsp; This is key to the ECUs further Torque Managing functions, as accurate air mass measurement and actual engine torque go hand in hand. &nbsp;


\*\* For torque management, Throttle Area Demand can be manipulated which will be directly proportional to air mass when this is configured correctly


Tuning -\> Engine Functions -\> Throttle Body Model -\> Throttle Body Area Table


![Image](</lib/NewItem178.png>)


This 2D table is all that is needed to appropriately map the given throttle area vs throttle position.&nbsp; As mentioned previously, this allows for extremely fast and accurate mapping of the engine when TMF is active. &nbsp;


&nbsp; &nbsp; It is important to understand that the Pedal Demand and other targeting of throttle area will target the "unit location" in this table, which will then correspond to the DBW Servo Position. &nbsp;


**This means, there could be little relationship between Throttle Area Demand and actual DBW Servo Position on fully tuned setups.** &nbsp;


\*\* Blend tables must be configured completely before tuning


There are multiple ways to calibrate the appropriate throttle area. &nbsp;



**Method 1 – Torque verification**&nbsp;


With calculated torque channels configured and functional, tuning the Engine Torque (TMF) channels to match the standard Engine Torque channels will allow full mapping of the Throttle Area table.&nbsp; See [Torque Management Tuning](<TorqueManagementTuningGuide.md>)


**Method 2 – Matching other forms of Air Mass measurement**


If the application is using a calibrated MAF sensor.&nbsp; Then the throttle area % can be adjusted and matched to TMF air mass VS MAF air mass at different throttle/DBW servo positions. &nbsp;

The same can be done matching TMF air mass VS MAP air mass

\*\* MAF/MAP air mass must be validly running the engine - running the commanded lambda target, etc


**Method 3 – Matching Lambda**&nbsp;


If no MAF sensor is available, setting fuel trims to 0 (or near 0), you can adjust the throttle area to match the target mixture very quickly. &nbsp;


\*\* Some extreme applications where live Lambda is unstable may be more difficult to map with Method 3


![Image](</lib/Tuning Tip.jpg>) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;

**Tuning Tip**:&nbsp;


*Per the Matching Lambda validation method, the Throttle Area Table is used to quickly tune the engine operating in TMF by simply manipulating the table at the various throttle areas to match the Lambda Target Table values for that given load. When the correct air fuel ratio is achieved, the Throttle Area Table is essentially validated for the purpose of running the engine. To do this the wideband lambda control should be turned off and the blend bias toward TMF be set to 100%.*&nbsp;





....

