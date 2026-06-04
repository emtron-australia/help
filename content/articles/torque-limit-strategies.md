---
title: Torque Limit Strategies
---

When announcing new firmware functions, we discussed the addition of the User Engine Torque Limits function and how Strategy (Strat) modes control how the ECU limits torque output. Screenshot 1 shows where the Torque Limit Strategies are configured. There are five Strat modes available. At the time of writing, the functions that can be linked to these strategies are: Traction Control (Torque Mode), Launch Control (Torque Mode – Static), Launch Control (Torque Mode – Moving), and User Torque Limits. Using the same 600Nm example from our last post, we will look at the Strat mode used to achieve that target.

{{< figure src="../../img/torque-limit-strategies/image.png" caption="Screenshot 1: Engine Torque Limit Strategy Setup – Torque Limit Strat 1 Setup" >}}

Screenshot 2 shows the Torque Limit Strat 1 Setup, which is the core configuration dictating how the ECU reduces engine torque. There are three limit priorities, and the ECU works through them in order — Priority 1, then Priority 2, then Priority 3 — until the Torque Target is met. As seen in Screenshot 1, each torque limiting method has an associated clamp table that controls how much the ECU can use that method before moving to the next priority.

In this example, only Priority 1 (Throttle Area) and Priority 2 (Ignition Retard) are used. When a torque limit is requested, the ECU calculates the required throttle reduction using Throttle Mass Flow calculations, then monitors the Throttle Area Min Clamp Table. If the Torque Target is reached before hitting the clamp limit, only Priority 1 is needed. If engine torque remains above the target, the ECU moves to Priority 2 (Ignition Retard) to make up the difference. Provided the Ignition Retard Max Clamp Table allows sufficient retard, the target will be met. If not, the ECU falls through to Priority 3 — set to OFF in this example — making it essential that the Priority 1 and 2 clamps together allow enough torque reduction to reach the target.

Cutting (fuel, ignition, or both) is not used here but is a highly effective torque reduction method. Note that the Engine Torque channel is derived from Air Mass Final in the ECU. Any discrepancy between the Throttle Mass Flow calculated value and Air Mass Final will affect torque reduction accuracy. When throttle reduction is the primary method, it is recommended that Air Mass Final uses a strong blend of Throttle Mass Flow Calculated to minimise errors.

The ECU can also leverage fuel cut, ignition cut, or a combination of both. Cutting provides fast, near-instantaneous torque reduction, typically used for short durations. Further examples will be covered in future posts.

**Boost Target Override** is another Strat Mode feature that allows the ECU to calculate a reduced boost target during torque reduction. While not covered in detail here, it is particularly useful when there is a large gap between airflow-generated torque and the torque target — it is impractical to produce 1000Nm of airflow torque and then request only 50Nm of output. It also helps reduce throttle closure levels during active torque limiting by reducing airflow relative to driver demand.

{{< figure src="../../img/torque-limit-strategies/image-1.png" caption="Screenshot 2: Torque Limit Strat 1 Setup" >}}
