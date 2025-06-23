---
title: "0: Speed Density (MAP)"
---

**Speed Density (MAP Sensor)**


![Image](</lib/Config Fuel10.jpg>)


The ECUs primary Fuel Model is Speed Density(MAP Sensor).&nbsp; The basis of this calculation is derived using the Ideal Gas Law;&nbsp; PV = nRT.


The ECU calculates the injection time for speed density using the following information:


Displacement volume per cylinder (cc).&nbsp;

Intake Manifold Air Pressure - MAP(kPa)

Lambda Target (La)

Stoichiometric Ratio of the Fuel (Stoich)

Injector Flow rate (cc/min)

Charge Temperature (DegC)

Fuel Density (g/ml)

Fuel Pressure (kPa)

Engine VE (%)

Gas Constant - R = 287J/Kg/K for Dry Air.


The Fuel Mass (g)&nbsp; is calculated as:


Fuel Mass (g) =&nbsp; MAP x Volume Per Cylinder &nbsp; &nbsp; &nbsp; x&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 1 &nbsp; &nbsp; &nbsp; &nbsp; x &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 1&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; x &nbsp; Engine %VE&nbsp; &nbsp; &nbsp;

&nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 287J/Kg/K x (Charge Temp(DegK) &nbsp; &nbsp; &nbsp; Stoich &nbsp; &nbsp; &nbsp; Lambda Target&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;


**Example 1:**


MAP =&nbsp; 252kPa

Charge Temperature = 30.7 DegC

Volume Per Cylinder = 666.6&nbsp;

Stoich Ratio = 9.9

Lambda Target = 0.785

Engine VE&nbsp; = 96.6 %


**Fuel Mass (g)** = 0.2395


In this basic example, if the cylinder is filling to 96.6% of its volume, then 0. 2395grams of fuel is required to achieve a Lambda Target of&nbsp; 0.785. &nbsp;


The Fuel Table(s)are used to compensate for the volumetric efficiency (VE)&nbsp; of the engine at varying Engine Speeds and Loads. These tables represent the True VE of the engine. A typical table is shown in Figure 3 for a turbo charged engine.


![Image](</lib/Untitled236.png>)

Figure 3: Fuel VE Table


Also, the Stoichiometric Ratio will vary with Fuel Type. A Single Zone if the fuel type is fixed (Figure 4) can be used or a Table allowing the ECU to constantly correct for&nbsp; varying&nbsp; alcohol content. See Figure 5.


![Image](</lib/Untitled237.png>)

Figure 4: Stoich Ratio setup (single )



![Image](</lib/Untitled233.png>)

Figure 5: Stoich Ratio setup (table)



Once the Fuel Mass is determined, the Effective Injector Pulse Width can be calculated using&nbsp;

* &nbsp;
  * Injector Size
  * Fuel Density. Fuel Density can be a function of both Fuel Temperate and Alcohol Content. A typical table will look as shown in Figure 6:
  * Fuel Pressure Correction.&nbsp; The&nbsp; Fuel Pressure Correction is a Fluid Dynamics equation, also called **Bernoulli's equation.** It allows the injector Flow Rate to be adjusted as the differential pressure across the injector changes. **NOTE**: This correction MUST be enabled using the "Fuel Model : Fuel Pressure" setting


![Image](</lib/Untitled238.png>)

**Figure 6: Fuel Density Table**



**Flow Chart Overview for Speed Density Fuel Model:**

![Image](</lib/SD Flow Chart4.jpg>)


&nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;