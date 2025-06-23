---
title: "Air Mass Modelled Setup"
---

![Image](</lib/Untitled258.png>)

![Image](</lib/Untitled259.png>)

This function blends the Air Mass (g/cyl) selected in Parameter 1 and 2 to give a&nbsp; "Air Mass Modelled" runtime in g/cyl.&nbsp;

This runtime can be used throughout the ECU. As an example it can be used used to run the Fuel Model, you can blend the air mass from&nbsp;

Throttle Mass Flow (TMF) to Speed Density (MAP) and use that result to run the engine i.e you can “favour” the TMF under lite to mid throttle and blend to MAP&nbsp;

under high load conditions (Fuel Model setting 3). See [Fuel Model Setup ](<FuelModelSetup.md>)for Fuel Model information.&nbsp;

Air Mass Modelled Blend Parameters have the following options. Choose what two air flow calculations to use in the blend table:


&#48;: OFF.&nbsp; Function is off

&#49;: Manifold Pressure Sensor.&nbsp; &nbsp; Manifold Pressure&nbsp;

&#50;: Manifold Pressure Bank 1. &nbsp; &nbsp; Bank 1 Manifold Pressure

&#51;: Manifold Pressure Bank 2.&nbsp; &nbsp; Bank 2 Manifold Pressure

&#52;: Manifold Pressure + Manifold&nbsp; Bank 1 Sensor Average. Average of MAP and MAP Bank 1

&#53;: Manifold Pressure + Manifold&nbsp; Bank 2 Sensor Average. Average of MAP and MAP Bank 2

&#54;: Manifold&nbsp; Pressure Bank 1/Bank 2&nbsp; Average. Average of MAP Bank 1 and Bank 2

&#55;: MAF Meter 1. MAF Sensor 1

&#56;: MAF Meter 2.MAF Sensor 2&nbsp;

&#57;: MAF Meter Bank 1.&nbsp; &nbsp; Bank 1 MAF Sensor

&#49;0: MAF Meter Bank 2.Bank 2 MAF MeSensorter

&#49;1: MAF Meter Bank 1/ Bank 2 Average, Average of MAF Bank 1 and Bank 2

&#49;2: Throttle Mass Flow 1.Throttle Mass Flow Bank 1

&#49;3: Throttle Mass Flow 2. Throttle Mass Flow Bank 2

&#49;4: Throttle Mass Flow 1 /2 Average. Average of TMF Bank 1 and Bank 2

&#49;5: Manifold Pressure Estimate. Estimated Manifold Pressure

