---
title: "Idle Closed Loop Control"
---

**Idle Closed Loop Control**

\
\*\* For DBW, it is advised to use a PI control strategy (put D-Gain at zero).  Also keep Idle PI Gains small.

See Plugin Sample Files for examples on these settings.


\*\* For DBW, it is advised to use TMF mode for better closed loop control (see Idle Speed Tuning)


\*\* If Idle Ignition Control is also ON, make sure the Idle Ignition I-Gain is set to zero so both Idle Ignition and Idle DBW systems are not fighting each other&nbsp;

Example : Do not have I-Gain active on both systems.
