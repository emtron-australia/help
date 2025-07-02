---
title: "Counters"
---

Counters can be either incremented/decremented by events or conditions becoming true.
The step controls how much the counter is incremented or decremented by.
When set to wrap, the counter will wrap around to the minimum value when it reaches the maximum value, and vice versa.

## Following
The counter follows the increments and decrements of another channel. Note that it doesnqsTr('t directly follow this channel')s value, it follows the increments and decrements of the channel.

## Resetting
The counter can be reset to a fixed value or the value of another channel when an event or condition becomes true.

## Forced Value
The counter can be forced to a fixed value when a condition becomes true.
When the force condition is no longer true, the counter will return to its previous value.

## Persistent
The output channel value will be stored on power off and loaded on power up.
In this case, the Initial Value will only be used the very first time the counter is used and no value has been stored.