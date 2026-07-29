---
title: "User Channels"
description: "Define custom channel and event names for analysis in EmVision."
weight: 8
---

**File → User Channels**

User channels and user events in EmVision are **client-side definitions** stored with the application configuration. They let you name and style custom channels for maths, plots, and display — separate from channels that were recorded inside a log file.

## Channels and Events tabs

| Tab | Purpose |
|-----|---------|
| **Channels** | Named value channels (units, colour, and related properties). |
| **Events** | Named event definitions for use where event markers apply. |

## Creating a channel

1. Open **File → User Channels**.
2. On the **Channels** tab, click **Add Channel**.
3. Set **Name**, **Units**, and **Colour** as needed.
4. Close the dialog — definitions are kept in client config and become available in channel pickers.

Creating an event uses the **Events** tab and **Add Event**.

## How this differs from Display Studio user channels

| | EmVision (this dialog) | Display Studio |
|--|------------------------|----------------|
| Menu | **File → User Channels** | **Setup → User Channels** |
| Scope | Client config on the PC (analysis / maths) | Vehicle display configuration |
| Logged data | Does not rewrite historical samples in the open log | Channels can be written by functions and logged on the device |

Display Studio’s setup guide is still useful for the general idea of custom channels — see [User Channels (Display Studio)](/displays/setup/user-channels). EmVision uses a separate ID range for client user channels so they do not collide with custom channels already stored inside a log file.

## User channels vs math channels

| | User channels | Math channels |
|--|---------------|---------------|
| Role | Define channel **identity** (name, units, colour) | Compute **values** from expressions or function pipelines |
| Values | Not a formula engine by themselves | Produce a full time series from the open log |
| Typical use | Naming targets for maths output, gauges, or project-specific labels | Derived signals (ratios, filters, blends) |

For expressions and function libraries, see [Math Channels](math-channels). Full **emexpr** syntax is documented under Display Studio: [Math Functions](/displays/functions/maths).

## Tips

- Prefer built-in log channels when the data already exists in the file.
- Use user channels when you need a stable custom name or presentation for analysis-only work.
- Use [math channels](math-channels) when the goal is a calculated series over the log.
