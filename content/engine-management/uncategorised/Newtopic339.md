---
title: "Gearshift Setup"
---

**Gear Position Order**


&#48;: N123456

&#49;: RN123456

&#50;: 1N23456


This settings allows the ECU can determine the correct shift and half-shift&nbsp; sequence


Option 1: RN123456.

In some transmissions neutral is located half-way between R and 1st.&nbsp; To allow Neutral to be selected, the "Half-Shift" setting should be enabled.


NOTES:

\*\* 1st -\> Neutral will require a Half-Shift. (Downshift Solenoid will be modulated)

\*\* Reverse -\> Neutral will require a Half-Shift&nbsp; (Upshift Solenoid will be modulated)

\*\* Neutral to reverse Half-Shift is not required as reverse gear is located at the end of the shift drum.


Option 2: 1N23456

In this configuration neutral is located half-way between 1st and 2nd. To allow Neutral to be selected, the "1st -\> N Half-Shift" setting should be enabled.


NOTES:

\*\* 1st -\> Neutral will require a Half-Shift (Upshift Solenoid will be modulated)

\*\* N -\> 1st upshift request, the ECU will activate the downshift solenoid

\*\*&nbsp; Neutral to 1st Half-Shift is not required as 1st gear is located at the end of the shift drum.


**Gear Position Tracking**&nbsp;


&#48;: OFF

&#49;: RPM/Speed Ratio

&#50;: Gear Detection Voltage 2

&#51;: InputShaft /Output Shaft Speed Ratio


Gearshift tracking feature helps reduce transmission damage by cross referencing two independent Gear positions at the start of a gearshift. The ECU uses the Main and Tracking Gear Positions to achieve this.&nbsp;


It is HIGHLY recommended to use this feature.&nbsp;


&#49;) Main/Primary Gear Position: The Gear Position Voltage 1 Input channel is used.

&#50;) Tracking Gear Position: This is selectable under this setting. &nbsp;


When the Main and Tracking Gear positions don't match the actual Gear Position cannot be determined with absolute certainty.&nbsp; This can be caused by a sensor entering a Fault condition or an absolute tracking error.&nbsp;


To prevent transmission damage the following precautions are used:


&#49;) The ECU requires the clutch to be depressed before a shift can occur. The ECU checks this condition by looking at the Clutch Switch Status or Clutch Pressure. The ECU will NOT upshift or downshift until the clutch is depressed.

&#50;) The Gearshift runs in open-loop mode. The gearshift time is calculated from the "Fault Mode Cut Time" table and does not use the "next gear stable" strategy.

&#51;) Rev-matching is disabled.


In the event the Main Gear position enters a Fault condition, the Tracking Gear position will be loaded as the main Gear Position.&nbsp;


NOTE: Gear Position Gear Tracking is always locked out in the following gears : R, N, 1st


**Gear Tracking Clutch Pressure Threshold**&nbsp;


When a Gear Position tracking error occurs the clutch pressure MUST exceed this setting before the ECU will allow a downshift or upshift.&nbsp;


NOTE: Clutch Pressure or Clutch Switch can be used but MUST be configured.&nbsp;


**&#49;st -\> N Half-Shift Enable**


&#48;: OFF

&#49;: ON


&#49;) Neutral Gear Ordering RN12345 - Neutral placed half-way between R and 1st.


This setting allows the ECU to "Half-Shift" when selecting 1st -\> Neutral.&nbsp; It does this by appling a PWM signal to the downshift solenoid with a user adjustable duty cycle and ramp rate


&#50;) Neutral Gear Ordering 1N2345 - Neutral placed half-way between 1st and 2nd.


This setting allows the ECU to "Half-Shift" when selecting 1st -\> Neutral.&nbsp; It does this by appling a PWM signal to the&nbsp; upshift solenoid with a user adjustable duty cycle and ramp rate


**&#49;st -\> N Half-Shift Start Duty Cycle**


Start Duty Cycle in Half Shift Mode applied to the gear solenoid. The solenoid used will depend on the Gear Position Order.


NOTE: The "Next Gear Timeout" can be overwritten in Half-Shift Mode by holding the Downshift Paddle. For a maximum of 2 seconds the Half-Shift mode will operate until the paddle is released.&nbsp; The Half-shift mode will switch OFF when next stable is reached overriding any paddle input.


Freq fixed at 20Hz


Typical Value = 50 %DC

Resolution 2.0%


**&#49;st -\> N Half-Shift Ramp Rate**


The Duty Cycle will be increased by this amount per cycle.&nbsp;


Typical Value = 4 %DC

Resolution 2.0%


Example: &nbsp;

Half-Shift Start Duty Cycle = 50.0%

Half-Shift Ramp Rate = 6.0%


&#49;st PWM Pulse = 50% DC

&#50;nd PWM Pulse =56% DC

&#51;rd PWM Pulse = 62% DC


The PWM will be switched OFF when the next gear has been detected or when the paddle is released.


Maximum Time limited to 2 seconds.


**&#49;st -\> N Half-Shift Max Duty Cycle**


Maximum duty cycle allowed on the solenoid during Half-Shift operation.


Resolution 2.0%


**&#49;st -\> N Half-Shift Duty Cycle - Opposite**


Fixed Duty Cycle to be used on the opposing gearshift solenoid. This can be used as a "brake" and help prevent over rotation of the shift drum. This PWM runs in-phase with the "1st -\> N: Half-Shift Start Duty Cycle" PWM signal.


&#48; = OFF

Typical Value = 10 %DC

Resolution 2.0%


**Rev -\> N Half-Shift Enable**


&#48;: OFF

&#49;: ON


&#49;) Neutral Gear Ordering RN12345 - Neutral placed half-way between R and 1st.


This setting allows the ECU to "Half-Shift" when selecting Reverse -\> Neutral.&nbsp; It does this by appling a 20Hz PWM signal to the upshift solenoid with a user adjustable duty cycle and ramp rate.


**Rev -\> N Half-Shift Start Duty Cycle**


Start Duty Cycle in Half Shift Mode applied to the gear solenoid. The solenoid used will depend on the Gear Position Order.


NOTE: The "Next Gear Timeout" can be overwritten in Half-Shift Mode by holding the Downshift Paddle. For a maximum of 2 seconds the Half-Shift mode will operate until the paddle is released.&nbsp; The Half-shift mode will switch OFF when next stable is reached overriding any paddle input.


Freq fixed at 20Hz


Typical Value = 50 %DC

Resolution 2.0%


**Rev -\> N Half-Shift Ramp Rate**


The Duty Cycle will be increased by this amount per cycle.&nbsp;


Typical Value = 4 %DC

Resolution 2.0%


Example: &nbsp;

Half-Shift Start Duty Cycle = 50.0%

Half-Shift Ramp Rate = 6.0%


&#49;st PWM Pulse = 50% DC

&#50;nd PWM Pulse =56% DC

&#51;rd PWM Pulse = 62% DC


The PWM will be switched OFF when the next gear has been detected or when the paddle is released.


Maximum Time limited to 2 seconds.


**Rev -\> N Half-Shift Max Duty Cycle**


Maximum duty cycle allowed on the solenoid during Half-Shift operation.


Resolution 2.0%


**Rev -\> N Half-Shift Duty Cycle - Opposite**


Fixed Duty Cycle to be used on the opposing gearshift solenoid. This can be used as a "brake" and help prevent over rotation of the shift drum. This PWM runs in-phase with the "Rev -\> N: Half-Shift Start Duty Cycle" PWM signal.


&#48; = OFF

Typical Value = 10 %DC

Resolution 2.0%
