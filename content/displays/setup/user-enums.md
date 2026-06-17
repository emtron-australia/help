---
title: "User Enums"
description: "Define text labels for numeric channel values."
weight: 4
---

**Setup → User Enums**

Enums map numeric values to display text. For example, a gear position channel might map `0` to "N", `1` to "1st", and so on. Gauges and live data views use enum labels when a channel is associated with an enum.

## Creating an Enum

1. Open **Setup → User Enums**.
2. Click **Add** to create a new enum definition.
3. Set the enum **Name**.
4. Add **Values** — each entry pairs a numeric value with display text.

Enums are referenced from user channels, built-in channels (via enum associations), and status gauges on the display.