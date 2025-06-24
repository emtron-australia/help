---
title: "Gear Detection"
---


**Gear Detection**


Emtron has various methods of Gear Detection.&nbsp; See -\> [Gear Detection Setup](<Newtopic480.md>)

Proper gear detection and channel calculation such as **Input shaft Speed (Calc)** are important for functions in the ECU such as Motorsport Gearshift control (regarding rev matching control), some Application Build systems (CAN Integration), and other general functions in the ECU that may be being used.



**Input/Outputshaft Speed Calculations**



Inputshaft speed Calculated can be derived from looking at Outputshaft Speed Channels -\> Vehicle Dynamics -\> Inputshaft Speed Calculated


![Image](</img/NewItem884.png>)


"1" Output Shaft Speed Calculated is derive from selecting a calibrated speed channel.&nbsp; -\>&nbsp; Vehicle Functions -\> Vehicle Dynamics -\> Outputshaft Speed Calculated


![Image](</img/NewItem880.png>)



\*\* The ECU generates this channel by deriving the speed through the wheel circumference and final drive under Vehicle Dynamics -\> Vehicle Main Setup -\>&nbsp;


![Image](</img/NewItem883.png>)



The Inputshaft speed is calculated furthermore through the Transmission Ratio Table.&nbsp; Vehicle Dynamics -\> Transmission Gear Ratio Table -\>

![Image](</img/NewItem885.png>)




**Validating Inputshaft speed (Calc) channel**


To validate Inputshaft speed (Calc), logging engine speed vs Inputshaft Speed (Calc) can be plotted -\>&nbsp;



![Image](</img/NewItem887.png>)




Also by looking at runtimes for channel comparisons can be done -\>&nbsp;


![Image](</img/NewItem886.png>)


\*\* Note Gear Ratio (Input/Outputshaft) *(calculated from Input shaft speed (Calc) vs Output shaft Speed (Calc)* vs Gearbox Ratio *(Transmission Ratio tabe)* is the same

\*\* Note Clutch Slip Channels are near 0% *(calculated % difference between Engine Speed and Clutch Slip Source Channel)*

&nbsp;*(define clutch slip in Tuning -\> Vehicle Functions -\> Vehicle Dynamics -\> Clutch Slip = Currently Set to Inputshaft Speed Calculated)*



\*\* If there is error in Input shaft Speed (Calc) vs Engine Speed *(therefore there will be error in Gear Ratio (Input/Outputshaft) and Clutch Slip)*, then settings/calibration needs attention in regards to speed sensor calibration, wheel diameter, final drive, or transmission ratios


