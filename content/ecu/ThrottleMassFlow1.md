---
title: "Tuning Throttle Body Area"
---

# Tuning Throttle Body Area


Throttle Mass Flow (TMF) as the name indicates, is the rate at which **air mass** is flowing through a throttle body in units of grams/second (g/s). Using the throttle body size, throttle area, temperature, pre and post throttle pressures,the ECU can very accurately calculate air flow through the throttle body and therefore into the engine; this is known as the TMF Calculation. Other sensors that also generate air mass flow (g/s) data are Manifold Pressure and MAF sensors. The TMF Calculation is just another method of determining air mass flow and has benefits over MAP and MAF as discussed further down.


The image below illustrates the basic elements required to calculate TMF.



![Image](</img/Throttle Drawing13.jpg>)



Getting into more detail, the flow through a throttle body is governed by three physical elements, Conversation of mass, Newtons second law of motion for fluids and Conservation of energy. By combining these elements the ECU can model the flow of fluid through the throttle body accounting for throttle plate thickness and throttle shaft size.&nbsp; By then including real-time data such as the **pressure ratio** across the throttle plate and the instantaneous **throttle area,** the ECU can precisely calculate the mass flow rate through a throttle body.


Although these calculation are complex, the TMF setup process for the user is kept as simple as possible with the following inputs and setup required:


***


**Example workflow of validating TMF air flow, Throttle Body Area, and properly blending dynamically into different air mass measurement functions.**&nbsp;


* Base Engine Setup Critical

  * Displacement, Injector Data, etc

* Throttle Body size, PID fully sorted.
* Sensors, calibration, location&nbsp;

  * Pre-throttle MAP (absolute) proper calibration
  * Post-throttle MAP proper calibration
  * IAT calibration&nbsp;

* Correct Selection/assignment of sensors and Enabling of TMF

![Image](</img/NewItem912.png>)

* Fuel Model Mode selection \*\* Note – if TMF is Enabled above – it will generate channels regardless of the Fuel Model Mode Selection

![Image](</img/NewItem911.png>)

* If Outflow is scaled – TMF Air Mass will read same as MAP air mass (speed density) as above. &nbsp;

  * This could enable 100% TMF usage all the time
  * Outflow uses VE table and dynamic airmass measurement to generate values

    * Requires tuned SD values

* Tune TMF by adjusting Throttle Area Table&nbsp;

  * Comparing valid MAP/MAF air mass values to TMF

    * Requires tuned SD values

  * Blend to 100% TMF and adjust until within Lambda Target

    * Usually faster and quicker to finish than people think &nbsp;

* Eventually at higher pressure ratios, TMF may not be as accurate as other air mass measurements (SD, etc).&nbsp; Use logging or live data to generate blend areas for TMF to SD or other dynamic airmass functions.

![Image](</img/NewItem910.png>)

Orange – Indicates area where TMF is beginning go outflow (this will vary)

Blue – Note pressure ratio and other data to use in Blend Table at this point

Green – Fully configured “Outflow Scaler” is generating TMF Air Mass the same as MAP Air Mass

![Image](</img/NewItem909.png>)

&#49;00 = TMF

&#48; = SD


Depending on specific application, throttle area demand/effective area vs pressure ratio, you may find that all of, or most of the part throttle SD feed forward VE table is no longer necessary. &nbsp;





***


**TMF becoming unstable**



![Image](</img/NewItem179.png>)&nbsp;

In this particular case the TMF signal at around 0.830 throttle pressure ratio is being unusable. &nbsp;

At this same moment, the Air Mass Modelled/blended calculation is stable and can be blended in. &nbsp;


Tuning/Using "Outflow Scaler"


The Outflow Scaler allows the TMF to calculate air flow when the pressure ratio is unfavorable (when it shouldn't be).&nbsp; The ECU uses multuple outflow cauculations, and filtering functions to generate this.&nbsp; It also looks automatically at dynamic air flow parameters (SD) to function. &nbsp;


When the pressure ratio is near 1 and TMF cannot read, it will generate a TMF value still. &nbsp;

Use the Outflow scalar to correct the TMF Air Mass calculations, and also the TMF Correction Table which will be enabled under the Tuning -\> Fuel section. &nbsp;


![Image](</img/NewItem818.png>)

Improper "Outflow Scale" setting.&nbsp; Adjust Throttle Mass Flow Outflow Scaler to correct

\*\* If TMF is lower than it should be, *decrease* value

\*\* If TMF is higher than it should be, *increase* value


![Image](</img/NewItem819.png>)


![Image](</img/NewItem892.png>)

A correctly configured TMF outflow scaler should also translate to torque calculations. &nbsp;

**\*\* Torque can also be used as a "compare" channel.&nbsp; In some cases, this allows you to validate torque calculation, frictional losses, etc - at the same time.** &nbsp;

\*\* Testing at heavy load ensures the outflow scaler is in its functional range, and then can be compared to properly calculating channel like Engine Torque (Uncorrected) (Nm) in this example

\*\* This can be done live very quickly by holding the engine in a steady state and looking at live runtimes/charts in the dash panel

\*\* Throttle Mass Flow Air Flow values can only be compared to validated/tuned air flow values (tuned) such as MAP Air Mass or MAF Air Mass. This means that there can be no error in these calculated values (lambda target vs lambda error)



**Tuning the Throttle Body Area Table**


The Throttle Body Area table tells the ECU how much actual throttle area is effective at different throttle positions.&nbsp; This is key to the ECUs further Torque Managing functions, as accurate air mass measurement and actual engine torque go hand in hand. &nbsp;


\*\* For torque management, Throttle Area Demand can be manipulated which will be directly proportional to air mass when this is configured correctly


Tuning -\> Engine Functions -\> Throttle Body Model -\> Throttle Body Area Table


![Image](</img/NewItem178.png>)


This 2D table is all that is needed to appropriately map the given throttle area vs throttle position.&nbsp; As mentioned previously, this allows for extremely fast and accurate mapping of the engine when TMF is active. &nbsp;


&nbsp; &nbsp; It is important to understand that the Pedal Demand and other targeting of throttle area will target the "unit location" in this table, which will then correspond to the DBW Servo Position. &nbsp;


**This means, there could be little relationship between Throttle Area Demand and actual DBW Servo Position on fully tuned setups.** &nbsp;



There are multiple ways to calibrate the appropriate throttle area. &nbsp;



**Method 1 – Matching Lambda**&nbsp;


If no MAF sensor is available, setting fuel trims to 0 (or near 0), you can adjust the throttle area to match the target mixture very quickly. &nbsp;


\*\* Some extreme applications where live Lambda is unstable may be more difficult to map with Method 1



**Method 2 – Matching other forms of Air Mass measurement**


If the application is using a calibrated MAF sensor.&nbsp; Then the throttle area % can be adjusted and matched to TMF air mass VS MAF air mass at different throttle/DBW servo positions. &nbsp;

The same can be done matching TMF air mass VS MAP air mass

\*\* MAF/MAP air mass must be validly running the engine - running the commanded lambda target, etc



![Image](</img/Tuning Tip.jpg>) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;

**Tuning Tip**:&nbsp;


*Per the Matching Lambda validation method, the Throttle Area Table is used to quickly tune the engine operating in TMF by simply manipulating the table at the various throttle areas to match the Lambda Target Table values for that given load. When the correct air fuel ratio is achieved, the Throttle Area Table is essentially validated for the purpose of running the engine. To do this the wideband lambda control should be turned off and the blend bias toward TMF be set to 100%.*&nbsp;



Comparing validated and air mass torque channels can be done various ways.&nbsp; Sweeping the throttle throughout it's range, or by temporarily using the Pedal to Throttle Area Demand Translation Clamp table :


![Image](</img/NewItem913.png>)


**Validating Throttle Area Torque (Engine Torque - TMF) using Launch Control**


Another way to validate Throttle Area and TMF Torque, would be to force the ECU into a "Torque Management" function (such as with **Throttle Plate(PID)** Torque Managed - [Launch Control](<LaunchControl.md>)) -\> ![Image](</img/NewItem805.png>)


Once a torque target is selected/forced, the "Engine Torque TMF" channels should match the standard Engine Torque channels, otherwise the Throttle Area table is incorrect (Throttle Area under -\> Tuning -\> Engine Functions -\> Throttle Body Model -\> Throttle Body Area


![Image](</img/NewItem809.png>)

Example of where Engine Torque TMF and Engine Torque are not matching due to incorrect Throttle Area settings


![Image](</img/NewItem810.png>)

Corrected Throttle Area table so Engine Torques further aligned


TMF Correction Table (Tuning -\> Fuel -\> TMF Correction Table) becomes active when TMF Version 1.1 is switched on.&nbsp;

\*\* This replaces VE table 3

**\*\* Correct values to 0.00 after enabling Version 1.1 to start**


**\*\*\* When Fuel Table Control "Z-Axis" enabled, TMF Correction Table cannot be used/is hidden.&nbsp; If VE table blending is needed, you must use "VE Blend" function**


This correction table essentially exists to help remove an error remaining in the system across a wide variety of load \& rpm conditions.

![Image](</img/NewItem828.png>)

![Image](</img/NewItem829.png>)

Demonstrating error in TMF Calculation that needs to be corrected in TMF Correction Table


