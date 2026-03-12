---
title: "Fuel Compensations"
---

## Compensations

All Fuel Compensations (other than **Charge Temperature Estimate** and **Charge Temperature Offset**) are percentage compensations added/subtracted onto Final Fuel Mass calculations :

Fuel Mass Final Uncorrected = 0.0367g

Injector Mass Flow = 309 g/sec

User Comp 1 = +19.5%

 

Fuel Mass Final Corrected = 0.0367 x 1.195 = 0.0438g

 

Effective Pulsewidth Effective = Fuel Mass Final Corrected x  (1/Injector Mass Flow )x 60

Effective Pulsewidth Effective = 0.0438 x 1/309 x 60 = 8.515ms

![Image](</img/AAAA114.jpg>)

## Compensation Tables
Fuel Sec Load (Secondary Load Compensation) can be turned on/off.  

The compensation can be turned on/off or be selected to be on via a User Function (only active when User Function is active).  

![Image](</img/NewItem738.png>)

**OFF –** The Compensation Table is Off

**ON –** The Compensation Table is always On

**User Function 1-10 –** The Compensation Table is on only when the selected User Function is Active 

**MAF Scaling –** The Compensation is a "Scaler" (in %) of the MAF signal * Used for Sec Load Table

