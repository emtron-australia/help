---
title: "Starting Fuel Setup"
---

# Starting Fuel Overview

Engine starting fuel requirements differ significantly from those required during normal engine operation. At low engine speeds and temperatures, a portion of the injected fuel does not immediately contribute to combustion as it can condense on intake port surfaces, intake valves and cylinder walls. Additional fuel compensation is therefore required to ensure sufficient combustible fuel reaches the cylinder during the starting process.

The starting fuel strategy consists of three distinct phases:

## Phase 1 – Pre-Crank Fuel

Pre-crank fuel is delivered before or at the beginning of engine cranking. The purpose of this fuel is to establish an initial fuel film on the intake port and valve surfaces, reducing the amount of fuel lost to wall wetting during the first combustion events.

Correctly calibrated pre-crank fuel can improve start quality, reduce cranking time, and promote faster engine burst.

## Phase 2 – Crank Fuel

During cranking additional fuel enrichment is required to compensate for fuel condensation and poor fuel vaporisation, particularly at lower engine and ambient temperatures.

Crank fuel provides the additional fuel necessary to achieve a combustible air-fuel mixture while the engine is rotating below its self-sustaining speed. Fuel requirements during this phase are highly dependent on coolant temperature, fuel characteristics, engine design and injector placement.

## Phase 3 – Post-Start Fuel

Once the engine has fired and transitioned from cranking to running, additional fuel compensation is typically required for a short period. The Fuel films established during the starting process continues to evolve and combustion stability may not yet be fully established.

Post-start fuel provides a temporary enrichment immediately after engine burst and gradually decays over time. This ensures a smooth transition from starting operation to normal fuel calculations while maintaining stable combustion and drivability. As the post-start compensation decays to zero, fueling returns entirely to the standard operating fuel model with no additional start-related compensation applied.


## ⚙️  Pre-Crank Fuel Enable

Enables and configures a pre-crank fuel injection event. This feature can improve engine start-up by providing an initial fuel charge before or during cranking, helping the engine fire more quickly.

### Options

| Value | Mode |
|---------|---------|
| 0 | Off |
| 1 | Start Position |
| 2 | First Crank Index Signal (Single Event) |
| 3 | Key On |
| 4 | First Crank Index Signal (Multiple Events) |

### Mode Descriptions

#### Off

Disables all pre-crank injection events.

#### Start Position

Triggers a pre-crank injection event when the configured Start Position Switch becomes active.
The Start Position Switch must be configured for this mode to operate.

#### First Crank Index Signal (Single Event)

Triggers a single pre-crank injection event when the first crank index signal is detected after ECU power-up.

#### Key On

Triggers a single pre-crank injection event when the ignition is switched to the ON position after ECU power-up.


#### First Crank Index Signal (Multiple Events)
---
Triggers the pre-crank injection event on the first crank index signal detected during engine cranking.
Unlike the other modes, this mode automatically re-arms after the engine has stopped, allowing the pre-crank injection event to occur again on subsequent start attempts without requiring an ECU power cycle.
To prevent repeated pre-crank injection events during unsuccessful starts or engine stalls, a lockout mechanism is applied. Before another pre-crank event can occur, the engine re-arming conditions must be met:

Exceed 400 RPM.
Remain above 400 RPM for at least 1 second.

Once these conditions have been satisfied and engine speed subsequently returns to 0 RPM, the pre-crank injection event will be re-enabled and available for the next engine start.

### Notes

- Modes 1, 2 and 3 perform only a single pre-crank injection event after ECU power-up. The ECU power must be cycled before another pre-crank injection event can occur using the Modes.
- Mode 4 the pre-crank event can be re-triggered automatically once the re-arming conditions have been met.


## ⚙️ Pre-Crank Pulse Count
Sets the number of fuel injection pulses during the pre-crank priming event. Using multiple shorter pulses helps improve fuel atomisation and distribution while reducing the risk of liquid fuel accumulation.

For example on ethanol-based fuels, increased pre-crank fuel is often required for reliable starting. However, long single injection pulses can cause fuel wall-wetting and plug wetting, reducing start quality.

Higher values = more pulses using shorter individual pulse widths

## ⚙️ Pre-Crank Pulse Interval
Sets the time delay between consecutive pre-crank injection pulses. This parameter only applies when Pre-Crank Pulse Count is greater than  1.

It controls the spacing between each injection pulse during the pre-crank event, allowing adjustment of fuel delivery timing and mixture preparation.

- Short interval: higher fuel density, increased wetting risk.
- Long interval: improved atomisation, reduced total delivery rate.

## ⚙️ Table Editing

See the below link(s) for table editing:

See here for more information on Pre Crank Tables : [Pre Crank Tables](<pre-crank-tables.md>)<br>
See here for more information on Cranking Tables : [Cranking Tables](<cranking-table.md>)<br>
See here for more information on Cranking Tables : [Post Start Tables](<post-start-comp-table-1.md>)<br>