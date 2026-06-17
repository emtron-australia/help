---
title: "Persistent Channels"
description: "Retain channel values across power cycles."
weight: 5
---

**Functions → Persistent Channels**

Persistent channels save their values to non-volatile storage on the display. Values are restored when the device powers on, surviving power loss and config reloads.

## Use Cases

- Store user-adjustable settings (shift point offsets, display preferences)
- Retain counter values that must survive ignition cycles
- Hold calibration offsets set by the driver

## Configuration

1. Open **Functions → Persistent Channels**.
2. Click **Add** to add a channel to the persistent list.
3. Select the **Channel** to persist.

Both numeric and string channels are supported.

## Behaviour

- On startup, stored values are loaded from the device and written to the configured channels.
- On power-down (or when a **Store** event is triggered), current channel values are written to storage.
- Only channels in the persistent list are saved — other channel values are lost on power cycle.

> **Note:** Only one function should write to a given channel. Do not configure the same channel as both a persistent channel and an active output from another function.