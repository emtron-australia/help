---
title: "Fuel Model Blending control"
---

**Fuel Model Blending Control**&nbsp;


The Fuel Model Blending Control Table is available when "Blend" modes are being used. &nbsp;

Common uses for Fuel Model Blending would be when switching between MAF and Speed Density (when MAF resolution may become ineffective for the application), or Throttle Mass Flow and Speed Density (when Throttle Pressure Ratio doesn't support TMF measurement).&nbsp;


\*\* Note the Blend Function actually connects to MAP Modeling which allows for further blending of fuel model modes additionally.&nbsp; See - MAP Modeling


![Image](</img/AAAA113.jpg>)


Select "blending" - Modes 3 or 4 in :

&nbsp; &nbsp; Config -\> Fuel -\> Fuel Model Setup

![Image](</img/NewItem353.png>)


This table is available for the user to control the ratio of which model is used.&nbsp;


![Image](</img/NewItem183.png>)


MODE 3:

&#48;.0% &nbsp; : Air Mass =&nbsp; All MAP Modelled

&#49;00.0% : Air Mass =&nbsp; All Throttle Mass Flow


MODE 4:

&#48;.0% &nbsp; : Air Mass =&nbsp; All MAP Modelled

&#49;00.0% : Air Mass =&nbsp; All Mass Air Flow Sensor

