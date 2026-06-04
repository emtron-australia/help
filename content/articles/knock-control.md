---
title: Knock Control
weight: 1
---

Knock (detonation) is one of the biggest killers of a performance engine. Emtron ECUs monitor individual cylinder knock and make cylinder-specific ignition adjustments to keep the engine safe without unnecessarily impacting performance through a global ignition trim.

The log below is taken from a mildly tuned EVO IX engine:

- **Top group** — engine speed, ignition angle, and knock short/long-term statuses
- **Second group** — knock level per cylinder as processed by the ECU from the knock sensor, with knock level thresholds shown
- **Third group** — short-term timing retard applied per cylinder
- **Fourth group** — long-term timing retard per cylinder, generated as a proportion of the short-term retard value to reintroduce ignition timing more gradually over a longer period

{{< figure src="../../img/knock-control/image.png" caption="Knock Control Log – EVO IX" >}}

In this example, Knock Level Cyl 1 and Knock Level Cyl 2 each show a knock event where the level exceeded the knock threshold. The ECU detected the knock and pulled 6.5° from Cylinder 1 and 4.4° from Cylinder 4 via short-term retard. The long-term retard also reduced timing advance by a moderate amount.

This data allows each cylinder to be individually trimmed with ignition or fuel adjustments to optimise power and manage knock events. If knock does occur, the ECU will retard timing automatically — provided the system is correctly configured.
