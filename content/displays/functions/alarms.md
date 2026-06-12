---
title: "Alarms"
---
# Alarms

Alarms monitor the system at runtime and notify the operator when something requires attention. Each alarm evaluates a set of trigger conditions every update cycle and, when active, broadcasts its message through dedicated system channels.

---

## Alarm List and Priority

Alarms are processed in list order — position 1 is the highest priority, position 2 is lower, and so on. When multiple alarms are active simultaneously, only the **highest-priority active alarm** (lowest list index) is shown on the alarm channels at any given time.

The alarm list can be reordered by dragging, and individual alarms can be exported to `.alarm` files for reuse.

---

## Settings

### Identity

| Field       | Description                                                                                                                      |
|-------------|----------------------------------------------------------------------------------------------------------------------------------|
| **Message** | The text displayed on the alarm message channel.                                                                                 |
| **Enabled** | When unchecked the alarm is permanently disabled and will never fire. Disabled alarms are indicated by "(Disabled)" in the list. |

### Trigger Conditions

Defines when the alarm becomes active. Uses the standard condition editor — see [Conditions](conditions.md) for full details on comparisons, CH mode, and logic operators.

The alarm activates on the first update cycle where all conditions evaluate to true (subject to the hold-off timer — see Timing below).

### Acknowledgement

| Field                          | Description                                                                                                                     |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| **Auto Acknowledge**           | When enabled, the alarm clears itself automatically after a fixed duration.                                                     |
| **Auto Acknowledge After (s)** | Duration in seconds before the alarm auto-clears. Only visible when Auto Acknowledge is on.                                     |
| **Acknowledge on Event**       | An event channel that, when it fires, immediately clears the alarm regardless of whether the trigger conditions are still true. |

Manual and automatic acknowledgement both set the alarm inactive and clears the auto-acknowledge timer.

### Timing

| Field                   | Description                                                                                                                                                 |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Repeat Hold Off (s)** | Minimum time (seconds) before the same alarm can fire again after it clears. Prevents rapid re-triggering if the condition oscillates around the threshold. |

**With Auto Acknowledge:** the hold-off starts from when the alarm auto-clears.

**Without Auto Acknowledge:** the hold-off starts the moment the alarm first fires, so the alarm can only re-fire this many seconds after it was last triggered.

### Output

| Field                     | Description                                                                                                                                                                                                                  |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Show Value From**       | A channel whose live value is formatted and written to the alarm value channel alongside the message. Useful for showing e.g. "Water Temp: 102.4 °C". The format respects the channel's configured decimal places and units. |
| **Active Status Channel** | A channel that is set to `1` while this alarm is active and `0` otherwise. Wire this to anything that needs to react to one specific alarm independently of priority.                                                        |

---

## Channels

While any alarm is active, the device writes the winning alarm's data to system-wide channels every update cycle:

| Channel            | Content                                                                                                                   |
|--------------------|---------------------------------------------------------------------------------------------------------------------------|
| **Alarm Message**  | The `message` string of the highest-priority active alarm. Set to `"No Alarms"` when all alarms clear.                    |
| **Alarm Value**    | The formatted value of the alarm's "Show Value From" channel, e.g. `"102.4 °C"`. Empty string if no value channel is set. |
| **Alarm Priority** | 1-based index of the highest-priority active alarm. Set to `(total alarms + 1)` when all clear.                           |
| **Alarm Begin**    | An event fired once when the system transitions from no active alarms to one or more active alarms.                       |
| **Alarm End**      | An event fired once when the last active alarm clears.                                                                    |

These channels can be used to drive displays, overlays, logging triggers, or any other part of the system.

---

## Tips

- **Order matters.** If two alarms can be active at the same time, place the more critical one higher in the list so it takes priority on the alarm channels.
- **Use Hold Off to avoid flicker.** If a channel is noisy near a threshold, set a hold-off of a few seconds to prevent repeated firing.
- **Active Status Channel for independent reactions.** The alarm channels only show the highest-priority alarm. If you need a specific lower-priority alarm to also drive an output (LED, relay, log trigger), use its Active Status Channel.
- **Always False / Always True conditions.** An alarm with a single "Always True" condition fires immediately on startup — useful for testing the notification pipeline. An "Always False" condition is equivalent to disabling the alarm but leaves the configuration intact.
