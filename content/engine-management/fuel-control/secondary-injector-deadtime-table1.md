---
title: "Secondary Injector Deadtime Table"
weight: 87
---

![Image](</img/Z Axis68.jpg>)

![Image](</img/Z Axis69.jpg>)

The Injector Dead Time Table (Sec) is utilized by the ECU to compensate for the latency (or Deadtime) of the Secondary injectors

The injector deadtime is the time factor in milliseconds when no fuel is injected accounting for the reaction time of the injector.

Setting the correct deadtime of an injector is critical for ECU fuel mass calculations.  

All injectors have a deadtime which may be affected by a number of factors.  

The voltage at the injector generally has the highest influence on the injector deadtime. 

Other factors such as fuel pressure also have a major affect on the injector deadtime.

Saturated injectors tend to have longer deadtimes when compared to peak & hold injectors

The Emtune software has commonly used Injector Deadtime Tables available in it that are only a right click of the mouse away.

![Image](</img/Z Axis70.jpg>)

![Image](</img/Z Axis71.jpg>)

![Image](</img/Tuning Tip.jpg>)            

**Tuning Tip**: 

*Secondary Injector Dead times can be validated using the Emtune Software by using the Wideband Lambda control. Once the secondary blend is biased 100% towards the secondary injectors. If you add 10% to your VE table (@ 3000rpm / 80kpa load for example), you should see a corresponding negative 10% trim applied via the Wideband lambda control. If you don't, then you know your dead times need some attention.*

*By utilizing a dead time table available in your Emtune software that is close. The correct dead time for your injector can be quickly arrived at by simply globally moving the table up & down. The voltage slop of the dead times can be further validated by removing the alternator charge and allowing the supply voltage to drop away. Correct dead times allow the engine to operate correctly over a wide range of variable conditions*

* *                                 

