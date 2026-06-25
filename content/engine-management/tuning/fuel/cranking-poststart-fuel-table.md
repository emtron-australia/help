---
title: "Cranking and Post Start Fuel Tables"
weight: 12
---

## Crank Fuel Table

The Crank Fuel Table defines the fuel delivered while the engine is operating below the configured **Crank Exit RPM** threshold.

During cranking, engine speed is low and fuel atomisation is poor. Additional fuel is required to compensate for fuel condensation on intake and cylinder surfaces and to ensure a combustible air-fuel mixture.

The Crank Fuel Table is typically configured as a function of coolant temperature, with colder engine temperatures requiring greater fuel enrichment.

Fuel from this table is applied continuously while the engine remains in the cranking state.

### 🔧 Tuning Guidelines

- Increase fuel values if the engine struggles to fire or requires excessive cranking time.
- Decrease fuel values if the engine exhibits signs of flooding.
- Cold temperature regions generally require significantly more fuel than warm temperature regions.

---

## Post-Start Fuel Table

The Post-Start Fuel Table provides temporary fuel enrichment immediately after the engine transitions from cranking to running.

When engine speed exceeds the configured **Crank Exit RPM**, the ECU exits the cranking state and begins applying the Post-Start Fuel Table. This additional fuel helps stabilise combustion during the first few seconds of engine operation while fuel films and air-fuel mixture conditions settle.

The Post-Start Fuel Table is typically configured as a function of coolant temperature, with colder engine temperatures requiring greater enrichment.

Post-start fuel compensation gradually decays to zero over a user-configurable period, allowing a smooth transition to normal fuel calculations.

### 🔧 Tuning Guidelines

- Increase fuel values if the engine starts successfully but immediately stumbles, misfires, or stalls.
- Decrease fuel values if the engine starts cleanly but runs excessively rich following start-up.
- Ensure the post-start decay period is long enough to maintain stable combustion, particularly during cold starts.

---

## ℹ️ Crank Exit RPM

The **Crank Exit RPM** setting defines the engine speed at which the ECU transitions from the **Crank Fuel Table** to the **Post-Start Fuel Table**.

Once engine speed exceeds the configured Crank Exit RPM, the engine is considered to be running and post-start fueling becomes active.

> **Note:** Crank Exit RPM is a global ECU setting and may also be used by other ECU functions to determine whether the engine is in a cranking or running state.
> 

Setting Location: Config -> Engine Setup -> Cranking RPM Entry/Exit

![Image](</img/NewItem356.png>)


