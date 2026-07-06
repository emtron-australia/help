---
title: "Pre-Crank Fuel"
weight: 11
---
## Overview

Pre-crank fuel is used to establish an initial fuel film on the intake port and valve surfaces before the engine begins cranking. This helps compensate for fuel that would otherwise be lost to wall wetting during the first combustion events, improving engine start quality and reducing cranking time.

Pre-crank fuel is calibrated using a three-dimensional **Pre-Crank Fuel Table**. The table allows the amount of fuel delivered during each pre-crank injection event to be varied over two configurable operating axes, providing flexibility for different engine and fuel combinations.

In most applications, the table is configured as a function of **Engine Coolant Temperature** only (effectively operating as a 2D table), with colder engine temperatures requiring greater pre-crank fuel.

The fuel quantity defined in this table is applied whenever a pre-crank injection event is triggered via the **Pre-Crank Injection Mode** setting .

### 🔧 Tuning Guidelines

- Increase fuel values if the engine requires excessive cranking before firing.
- Increase fuel values if the engine struggles to fire during cold starts.
- Decrease fuel values if the engine exhibits signs of flooding, spark plug wetting, or excessively rich starts.
- Ethanol-based fuels typically require significantly more pre-crank fuel than gasoline-based fuels.
- Large increases in fuel quantity are often better achieved using multiple pulses rather than a single large pulse. Refer to **Pre-Crank Pulse Count** and **Pre-Crank Multi-Pulse Interval** for additional tuning options.

### ⚠️ Important Notes

- Excessive pre-crank fuel can result in spark plug wetting and poor start quality.
- The optimum fuel quantity will vary depending on fuel type, injector location, engine design, and ambient temperature.
- Pre-crank fuel should be used to improve initial combustion quality, not to compensate for incorrectly calibrated cranking fuel.

### Pre-Crank Fuel Settings

See here for more information on Starting Fuel Settings : [Starting Fuel Overview](fuel-starting-setup)

## ⚙️ Starting Fuel Table Control

See here for more information: [Starting Fuel Table Control](starting-fuel-table-control-setup.md)