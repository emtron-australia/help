---
title: "Lambda Target Tables"
weight: 6
---

The Lambda Target table enables the user to define the desired Lambda target across the operating range of the engine.

The Lambda Target is a primary input to the ECU airflow and fuel model and therefore directly influences the final calculated fuel mass injected into the engine.

Once the Engine VE (Volumetric Efficiency) table is correctly calibrated to achieve the commanded Lambda Target, the engine’s lambda target can be adjusted simply by changing the Lambda Target value, without requiring changes to the main fuel calibration.

This target must be defined prior to calibration of the VE table.

For example, if the Main Fuel Table is calibrated such that the engine operates at **1.00 Lambda** when the Lambda Target is **1.00**, then reducing the Lambda Target to **0.80** will result in the ECU automatically increasing fuel delivery to achieve **0.80 Lambda**, without any changes to the Main Fuel Table.

> **Note:** If a change in Lambda Target (e.g. from 1.00 to 0.80) does not result in the measured Lambda matching the target, this indicates an error in the fuel system model, most commonly incorrect injector characterisation which should be corrected before continuing calibration.


### Why Lambda is used instead of AFR

Lambda is used as the primary combustion target because it represents the **relative air–fuel ratio to stoichiometric**, rather than an absolute fuel value.

Since different fuels have different stoichiometric air–fuel ratios, the same AFR value does not represent the same combustion condition across fuels. For example, petrol, ethanol blends, and methanol all require different AFR values to achieve the same combustion state.

Lambda removes this dependency by normalising the mixture to stoichiometric:

- Lambda = 1.00 → stoichiometric combustion (regardless of fuel type)
- Lambda < 1.00 → rich mixture
- Lambda > 1.00 → lean mixture

Because of this, a single Lambda Target can be used across all fuels, while the equivalent AFR target would change depending on fuel composition.

This allows calibration to remain consistent when fuel type changes, while still maintaining the same combustion behaviour.

For this reason, Lambda Targets are preferred over AFR Targets in the ECU fuel model, as they provide a universal reference independent of fuel stoichiometry.

## Lambda Target Tables

Two Lambda Target tables are available within the ECU. Either table can be used to define the engine’s Lambda target across the operating range.

The active table is selected using the **Lambda Target Table Control** setting.

Only the selected (active) table is used by the ECU for fuel model calculations and closed-loop control. The inactive table has no effect on engine operation until it is selected as the active source.

Normally Lambda Target Table 1 is used. Setting of table use is via [Fuel Table Control](<fuel-table-control.md>)

![Image](</img/AAAA91.jpg>)

![Image](</img/AAAA92.jpg>)


Should an actual Air Fuel Ratio be required to be displayed, this can be achieved by right mouse click on table and selecting **AFR Unit** 

Once activated, if the fuel model is set to a single fuel type, the Lambda Table 1 will be displayed in regular AFR units.

⚠️ **Warning:**
This feature will not work with flex or dual fuel models - see [Stoich Ratio Setup](<stoich-ratio-setup.md>)

![Image](</img/Lam 1.jpg>)

**Example 1: Gasoline fuel AFR shown**

![Image](</img/Lam 2.jpg>)

**Example 2: Methanol fuel AFR shown**

![Image](</img/Lam 3.jpg>)


## Lambda Target Offset Table

The Lambda Target Offset is applied as an absolute correction applied to the base Lambda Target value defined in the Lambda Target table.

For example, if the Lambda Target table value is **1.000** and a Lambda Target Offset of **-0.150 Lambda** is applied, the resulting effective Lambda Target becomes:

**1.000 + (-0.150) = 0.850**

This offset is absolute (not percentage-based) and directly adds or subtracts from the base Lambda Target value.

It allows the final Lambda Target to be adjusted dynamically without modifying the base calibration table.

![Image](</img/AAAA94.jpg>)

## Lambda Target Table Control

See here for more information: [Lambda Target Table Control](lambda-target-table-control-setup.md)