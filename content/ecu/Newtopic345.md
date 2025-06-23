---
title: "2: Mass Air Flow Sensor (MAF)"
---

**Mass Air Flow Sensor**


![Image](</lib/Untitled273.png>)


The Air Flow Sensor(s) provides a measured Air Mass Flow in g/s.&nbsp; The ECU then converts this into air mass per cylinder (g/cyl)&nbsp; giving actual Air Mass into the Engine.&nbsp;


The following MAF input channels can be used:

* Mass Air Flow Sensor(s) 1 and 2&nbsp;

OR

* Mass Air Flow Bank Sensor(s) 1 and 2&nbsp; can be used


The ECU will search which channel(s) are enabled and use those inputs.&nbsp; "Mass Air Flow Sensor" takes priority over "Mass Air Flow Bank Sensor". For example if both

Mass Air Flow Sensor1 and Mass Air Flow Sensor2 input channels are configured the ECU will automatically use both inputs.



MAF systems are more flexible in their ability to compensate for engine changes(like altitude and IAT) since they actually measure airflow instead of calculating it like the Speed Density Fuel Model. It also greatly reduces the tune time as you no longer need to adjust the fueling based on the VE of the Engine... its automatically accounted for by the MAF sensor. &nbsp;

However they also have limitations around restriction and sensor range on high power engines.


Once the Mass Air has been measured, if the MAF requires further scaling this can be done using a 3D Table. In the real world "small" corrections will need to be applied. This can be done using the Secondary Load Table which will allow a +/- percentage correction to be applied.&nbsp;


A Typical example is shown in below. Table Control should be used to put the Secondary Load Table into this "special" mode shown below


![Image](</lib/Untitled66.png>)

**Secondary Load Table used for MAF Sensor**


![Image](</lib/Untitled67.png>)

**Table Control for Secondary Load Table**


Once the Air Mass has been determined, the Stoichiometric Ratio and Lambda Target are used to generate a Fuel Mass (g). The Stoichiometric Ratio will vary with Fuel Type. A Single Zone if the fuel type is fixed can be used or a&nbsp; Table allowing the ECU to constantly correct for varying&nbsp; alcohol content.


Once the Fuel Mass is determined, the Effective Injector Pulse Width can be calculated using:

* &nbsp;
  * Injector Size
  * Fuel Density. Fuel Density can be a function of both Fuel Temperate and Alcohol Content.
  * Fuel Pressure Correction.&nbsp; The&nbsp; Fuel Pressure Correction is a Fluid Dynamics equation, also called **Bernoulli's equation.**&nbsp;

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; It allows the injector Flow Rate to be adjusted as the differential pressure across the injector changes.&nbsp;

**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; NOTE**: This correction MUST be enabled using the "Fuel Model : Fuel Pressure" setting



**Flow Chart Overview for Mass Air Flow Sensor Fuel Model:**


![Image](</lib/MAF Flow Chart2.jpg>)


