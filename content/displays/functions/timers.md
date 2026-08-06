---
title: "Timers"
description: "Configurable start, stop, and reset logic for time-based channels."
weight: 5
---

**Functions → Timers**

Timers produce a time value (seconds) on an output channel with configurable start, stop, and reset logic.

![Timers](/img/ed_timers.png)
> Example: hide the camera view 10 seconds after reverse gear is deselected.

## Settings

### Output Channel

Channel that holds the running time in seconds.

### On Expired Event

Event triggered when the timer reaches **Max Time**.

### Max Time

Maximum time in seconds. **0** = no time limit.

### Reset Mode

| Mode | Behaviour |
|------|-----------|
| Never | Timer never auto-resets |
| On Timer Start | Time resets to 0 when the timer starts |
| On Timer Stop | Time resets to 0 when the timer stops |
| On Condition | Time resets to 0 when the **Reset Condition** is true |

### Start Condition

When the start condition is true **and** the stop condition is false, the timer runs. The stop condition takes precedence.

### Stop Condition

When true, the timer stops. If no stop conditions are set, the result is always false (does not force a stop by itself).

### Reset Condition

When true, the timer resets to 0. Only used when **Reset Mode** is **On Condition**. If no reset conditions are set, the result is always false.
