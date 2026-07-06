---
title: "Fuel Bank Trim Tables"
weight: 25
---

## Bank Trims

### Bank Trims

- **Bank Trims** allow fuel mass percentage corrections to be applied independently to each cylinder bank.  
- Each cylinder can be assigned to either **Bank 1** or **Bank 2**, enabling separate fuel control for grouped cylinders.  
- **Bank 1** and **Bank 2** each include a dedicated 3D correction table, used to apply fuel compensation based on engine operating conditions such as engine speed and load.  
- These trims are typically used to correct for bank-to-bank fuel distribution differences, sensor tolerances, or airflow imbalance between intake paths.

![Image](</img/Z Axis14.jpg>)


> **ℹ️ Important**
>
> Cylinder-to-bank assignment is required for this function. Each cylinder must be mapped to either Bank 1 or Bank 2 to ensure accurate fuel trim application across all cylinders.
>
> > See Config -> Engine Setup -> Bank Cylinder Setup

![Image](</img/NewItem357.png>)

---

## Table Control 

Bank Trims are enabled from Fuel -> Bank Fuel Trims -> Bank Trim Table Control

**OFF** - The Trim Table is Off <br>
**ON** - The Trim Table is On 