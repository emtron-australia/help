---
title: "Starting Fuel Setup"
weight: 10
---

## Starting Fuel Overview

Engine starting fuel requirements differ significantly from those required during normal engine operation. At low engine speeds and temperatures, a portion of the injected fuel does not immediately contribute to combustion as it can condense on intake surfaces, intake valves and cylinder walls. Additional fuel compensation is therefore required to ensure sufficient combustible fuel reaches the cylinder during the starting process.

The starting fuel strategy consists of three distinct phases:

## Phase 1 – Pre-Crank Fuel

Pre-crank fuel is delivered before or at the beginning of engine cranking. The purpose of this fuel is to establish an initial fuel film on the intake port and valve surfaces, reducing the amount of fuel lost to wall wetting during the first combustion events.

Correctly calibrated pre-crank fuel can improve start quality, reduce cranking time and promote faster engine burst.

## Phase 2 – Cranking Fuel

During cranking additional fuel enrichment is required to compensate for fuel condensation and poor fuel vaporisation, particularly at lower engine and ambient temperatures.

Cranking fuel provides the additional fuel necessary to achieve a combustible air-fuel mixture while the engine is rotating below its self-sustaining speed. Fuel requirements during this phase are highly dependent on coolant temperature, fuel characteristics, engine design and injector placement.

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

Increasing the pulse count can be beneficial when using fuels that require significantly more fuel for cold starting, such as ethanol-based fuels. Rather than using a single large injection pulse, the required fuel can be distributed across multiple smaller pulses.

This approach can improve fuel atomisation and reduce the likelihood of fuel pooling or entering the cylinder in a liquid state, which can lead to spark plug wetting and poor starting performance.

Typical Applications:

- Ethanol and high-ethanol-content fuels.
- Engines requiring large amounts of pre-crank fuel.
- Situations where a single large pulse results in poor start quality.

## ⚙️ Pre-Crank Pulse Interval
Sets the time delay between consecutive pre-crank injection pulses. This parameter only applies when Pre-Crank Pulse Count is greater than  1.

It controls the spacing between each injection pulse during the pre-crank event, allowing adjustment of fuel delivery timing and mixture preparation.

- Short interval: higher fuel density, increased wetting risk.
- Long interval: improved atomisation, reduced total delivery rate.

The interval should be long enough to allow fuel from each pulse to disperse and form a stable fuel film before the next pulse is delivered. Excessively short intervals may reduce the benefit of using multiple pulses, while excessively long intervals can unnecessarily delay the start sequence.

## 🔧 Tuning Guidelines

When additional pre-crank fuel is required, it is generally preferable to increase the Pre-Crank Pulse Count rather than significantly increasing the fuel delivered in a single pulse.

A good starting point is:

- Set Pre-Crank Multi Pulse Interval to approximately 10 ms.
- Increase Pre-Crank Pulse Count by one pulse at a time.
- Evaluate cold start performance after each adjustment.
- Continue increasing the pulse count until no further improvement in start quality is observed.

Typical applications require between 1 and 6 pulses, with higher pulse counts generally only required for ethanol-based fuels or engines requiring large amounts of pre-crank fuel.

## ⚙️ Table Editing

See the below link(s) for table editing:

See here for more information on Pre Crank Fuel Tables : [Pre Crank Fuel Tables](<pre-crank-tables.md>)<br>
See here for more information on Cranking Fuel Tables : [Cranking Fuel Tables](<cranking-poststart-fuel-table>)<br>
See here for more information on Post Start Fuel Tables : [Post Start Fuel Tables](<cranking-poststart-fuel-table>)<br>