---
title: "Fuel Model Blending control"
weight: 29
---

## Fuel Model Blending Control

The Fuel Model Blending Control Table is available when "Blend" modes are being used.  

Common uses for Fuel Model Blending would be when switching between MAF and Speed Density (when MAF resolution may become ineffective for the application), or Throttle Mass Flow and Speed Density (when Throttle Pressure Ratio doesn't support TMF measurement). 

** Note the Blend Function actually connects to MAP Modeling which allows for further blending of fuel model modes additionally.  See - MAP Modeling

![Image](</img/AAAA113.jpg>)

Select "blending" - Modes 3 or 4 in :

    Config -> Fuel -> Fuel Model Setup

![Image](</img/NewItem353.png>)

This table is available for the user to control the ratio of which model is used. 

![Image](</img/NewItem183.png>)

MODE 3:

0.0%   : Air Mass =  All MAP Modelled

100.0% : Air Mass =  All Throttle Mass Flow

MODE 4:

0.0%   : Air Mass =  All MAP Modelled

100.0% : Air Mass =  All Mass Air Flow Sensor

