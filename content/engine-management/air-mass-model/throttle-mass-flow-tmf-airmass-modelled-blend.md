---
title: "Throttle Mass Flow (TMF) + AirMass Modelled (Blend)"
weight: 97
---

## Throttle Mass Flow (TMF) + Air Mass Modelled (Blend)

![Image](</img/Untitled272.png>)

A Blend Table generates a Final Air Mass using a ratio from Throttle Mass Flow (TMF) and Air Mass Modelled.

When this mode gets enabled, the Fuel Model Blending Control table becomes active in tuning:  

Tuning -> Fuel -> Fuel Model Blending Control

![Image](</img/Config Fuel15.jpg>)

![Image](</img/Config Fuel16.jpg>)

0%     = Air Mass Modelled

100% = Throttle Mass Flow (TMF)

Throttle Mass Flow setup must be configured - [Throttle Mass Flow Setup](<ThrottleMassFlow.md>)  

Air Mass Modelled setup must be configured - [MAP Modelled Setup](<air-mass-modelled-setup.md>)

Above 0.9 throttle pressure ratio, TMF must be blended into the user defined AirMass Modelled alternative air mass calculation.

** Blend tables must be configured completely before tuning

TMF tuning is accomplished by validating the [Throttle Body Area Table](<Newtopic77.md>)
