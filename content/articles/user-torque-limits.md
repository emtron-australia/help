---
title: User Torque Limits
weight: 5
---

The V2.19.0 firmware release in EMtune introduced a major expansion of the ECU's engine output control capabilities. While Emtron ECUs have had torque control for several years, it was previously only available within specific dedicated functions or OEM application builds — limiting flexibility for custom and motorsport applications.

The new **User Torque Limits** section changes this. There are now five fully user-configurable torque limits that can be assigned to any purpose. As shown in Screenshot 1, each limit is enabled and labelled independently.

{{< figure src="../../img/user-torque-limits/image.png" caption="Screenshot 1: Torque Limit Control – User 1" >}}

## Setup

Screenshot 2 shows the main setup screen, where you configure:

- The **Strategy (Strat) type** — how the ECU will reduce torque
- Whether torque is **normalised to gear ratio**
- Which **User Output channel** activates the torque limit

{{< figure src="../../img/user-torque-limits/image-1.png" caption="Screenshot 2: Torque Limit Setup" >}}

Once setup is complete, a 16×12 cell table defines the desired torque target based on nearly any ECU channel. A **Torque Limit Correction** table is also available to adjust this target by a set percentage. When the assigned User Output channel activates, the ECU monitors engine torque output and applies the configured strategy to meet the limit.

## Example

Screenshot 3 shows a log from a high-performance turbocharged four-cylinder Time Attack engine. The Strat mode uses a combination of throttle reduction and ignition retard to achieve a 600 Nm torque limit.

- **Engine Torque (Uncorrected)** — what the engine would produce without torque reduction
- **Engine Torque (Nm)** — the ECU's calculated output after limiting

In this example the strategy heavily favours throttle control, so the margin between corrected and uncorrected torque is small — the throttle is handling most of the airflow reduction, with ignition retard making up the balance to hit 600 Nm. The ECU continuously adjusts both throttle area demand and ignition angle, resulting in an extremely smooth 600 Nm output.

{{< figure src="../../img/user-torque-limits/image-2.png" caption="Screenshot 3: Example Logging Data – 600 Nm torque limit active" >}}

For more detail on the available strategy types, see the [Torque Limit Strategies](torque-limit-strategies) article.
