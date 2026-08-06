---
title: "Counters"
description: "Event- and condition-driven counters with wrap, follow, reset, and force."
weight: 4
---

**Functions → Counters**

Counters hold a numeric value that changes when events fire or conditions become true. Typical uses include counting gear shifts, button presses, or how many times a threshold was crossed.

## Increment and decrement

Each counter can increase or decrease based on:

- An **event**, or
- A **condition becoming true**

**Step** (increment / decrement amount) controls how much the value changes each time.

## Wrap

When **Wrap** is enabled, the counter wraps to the minimum when it exceeds the maximum (and the reverse when decreasing). When wrap is off, the value clamps at the limits if clamp options are used.

## Following

A counter can **follow** another channel: it tracks the *increments and decrements* of that channel rather than copying its absolute value. Use a follow condition when the follow behaviour should only apply in certain states.

## Resetting

Reset the counter to a **fixed value** or to the value of another **channel** when an event or condition becomes true.

## Forced value

While a **forced condition** is true, the counter is held at a **forced value**. When the condition clears, the counter returns to its previous value.

## Persistent

If **Persistent** is enabled, the counter value is stored on power off and restored on power up. The **initial value** is only used the first time, before any value has been stored.

See also [Persistent Channels](persistent-channels) for retaining arbitrary channels across power cycles.
