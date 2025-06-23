---
title: "Sync Position %"
---

**Sync Position %**

Sync position refers to the point in which the ECU is identifying the Sync Edge location.&nbsp; This reference point can be critical as if there is any discrepancy to this position mechanically (wandering between the crank and cam trigger due to slack in cam belt/chain), it can cause crank/sync errors, engine cycle change, or even the firing order to change (especially in the case of non-missing crank trigger setup). &nbsp;

Emtron calculates the following channel for monitoring, diagnosis, and logging purposes - **Sync Position %**&nbsp;

The Sync Position % is calculated by factoring the position of the Sync Edge between consecutive Crank Teeth. &nbsp;

![Image](</lib/NewItem351.png>)

Looking at falling edges, the distance between crank teeth can be identified by the green lines, and the sync edge is identified by the yellow arrow.&nbsp; The value would be **Sync Position % - 33%** approximately in this case.

Best practice is to aim for a **Sync Position % - 50%**. &nbsp;

\*\* Note - The higher the crank tooth count, the less resolution this runtime generally will have.&nbsp; IE a 60-2 trigger will have a much more unstable Sync Position % value vs a 1-Tooth Per TDC


