---
title: "3: Throttle Mass Flow (TMF) + AirMass Modelled (Blend)"
---

**Throttle Mass Flow (TMF) + Air Mass Modelled (Blend)**


![Image](</lib/Untitled272.png>)


A Blend Table generates a Final Air Mass using a ratio from Throttle Mass Flow (TMF) and Air Mass Modelled.


When this mode gets enabled, the Fuel Model Blending Control table becomes active in tuning: &nbsp;


Tuning -\> Fuel -\> Fuel Model Blending Control


![Image](</lib/Config Fuel15.jpg>)


![Image](</lib/Config Fuel16.jpg>)


&#48;% &nbsp; &nbsp; = Air Mass Modelled

&#49;00% = Throttle Mass Flow (TMF)


Throttle Mass Flow setup must be configured - [Throttle Mass Flow Setup](<ThrottleMassFlow.md>) &nbsp;

Air Mass Modelled setup must be configured - [MAP Modelled Setup](<AirMassModelledSetup.md>)


Above 0.9 throttle pressure ratio, TMF must be blended into the user defined AirMass Modelled alternative air mass calculation.


\*\* Blend tables must be configured completely before tuning


TMF tuning is accomplished by validating the [Throttle Body Area Table](<Newtopic77.md>)
