---
title: "Boost Target Table 1/2/3"
---

**Boost Target Table**


Used by the ECU to determine the base Boost Pressure Target


Boost Control Target can be selected as Absolute or Gauge. **NOTE**: The ECU will always generate the final Boost Target as Absolute value.


**Absolute Mode**.&nbsp; This is the Target Boost Pressure **independent** of Barometric Pressure.

**Gauge Mode**.&nbsp; &nbsp; &nbsp; This is the Target Boost Pressure **above** Barometric Pressure&nbsp;


Example.


**Absolute Mode**. Target = 250kPa. The ECU will Target an Absolute pressure of 250kPa. Boost Pressure inside the engine will increase as Barometric pressure reduces.&nbsp;

Barometric Pressure of 100kPa. Boost pressure inside the engine will be 150kPa.

Barometric Pressure of 80kPa. Boost pressure inside the engine will be 170kPa. (250kPa - 80kPa)


**Gauge Mode**. Target = 150kPa. The ECU will Target a boost pressure of 150kPa above Barometric pressure.

Barometric Pressure of 100kPa. ECU Boost Target will be 250kPa, boost pressure inside the engine will be 150kPa.

Barometric Pressure of 80kPa. ECU Boost Target will be 230kPa, boost pressure inside the engine will be 150kPa


**Boost Target Table 1/2/3**



![Image](</img/NewItem712.png>)


&#51; tables are available depending on CAL slot control or Boost Table Control

Table are active when closed loop boost control are active


