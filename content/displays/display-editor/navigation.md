---
title: "Navigation"
description: "Configure screen switching and the startup screen."
weight: 4
---

**Display → Navigation**

Navigation settings control how the driver moves between screens and which screen appears at startup.

## Settings

| Setting | Description |
|---------|-------------|
| Starting Screen | The screen shown when the display powers on |
| Next Screen Event | Event that advances to the next screen |
| Previous Screen Event | Event that goes to the previous screen |
| Wrap | When enabled, navigating past the last screen returns to the first |

## Wiring Navigation

Map physical buttons or CAN keypad inputs to the next/previous screen events. For example:

- **Page Up** button on the connector → Previous Screen Event
- **Page Down** button → Next Screen Event

Layer groups within a screen have their own independent next/previous layer events, configured on the Layer Group Gauge itself.