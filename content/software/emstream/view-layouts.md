---
title: "View Layouts"
description: "Choose how data is displayed across windows and panes."
weight: 5
---

**View → Type**

EmStream supports six view layouts for the main content area. Each layout presents telemetry data differently. The active layout applies to the current window.

## Layout Types

| Layout | Description |
|--------|-------------|
| Grid | Channel values in a configurable grid of numerical gauges — see [Data Grid](data-grid) |
| Plots | Scrolling time plots of selected channels — see [Live Plots](live-plots) |
| Track | GPS track map with live vehicle position — see [Track Map](track-map) |
| Track + Grid | Track map on the left, data grid on the right |
| Plot + Grid | Time plots on the left, data grid on the right |
| Plot + Plot | Two independent plot areas side by side |

Split layouts remember their divider position between sessions.

## Multi-Window

**View → Window Count** opens 1 to 4 simultaneous EmStream windows. Each window can use a different layout type independently — for example, one window showing the track map and another showing plots.

All windows share the same telemetry connection and receive the same live data.

## Switching Layouts

1. Open **View → Type**.
2. Select the desired layout.
3. The main area reloads immediately.

Configure the channels and appearance for each layout using the setup dialogs — the pencil icon on Grid and Plots views opens the relevant setup page.