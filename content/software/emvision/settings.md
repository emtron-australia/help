---
title: "Settings"
description: "Configure analysis preferences and display options."
weight: 11
---

**File → Settings** (available when a log is open)

## General

| Setting | Description |
|---------|-------------|
| X Axis Channel | Global **Time** or **Distance** mode for plots (same as **F9** / toolbar) |
| Gridline Density | Spacing of plot grid lines (0.1–2.0). Use the slider, type a value, or **Reset** to 1.0 |
| Navigator Channel | Channel drawn on the bottom navigator strip and used as the playback preview guide. Chosen once for the app (not per page) |
| Circuit Speed Channel | Speed source for circuit distance integration |
| Drag Speed Channel | Speed source for drag distance markers |
| Drag Event Trigger Channel | Channel used when generating drag markers from a trigger |
| Track Map | Imported track outline for the [Track Map](plot-types#track-map) plot |

Speed and trigger channels are also used by [Circuit and Drag Analysis](circuit-and-drag-analysis).

## Vehicle

Dimensions used by the track map vehicle marker:

| Setting | Default |
|---------|---------|
| Width | 1.8 m |
| Length | 4.5 m |
| Height | 1.5 m |

## Navigation

Controls keyboard scroll and zoom behaviour on plots:

| Setting | Description |
|---------|-------------|
| Debounce | Delay before key-hold scrolling begins (seconds) |
| Initial Speed | Starting scroll velocity |
| Final Speed | Maximum scroll velocity |
| Acceleration | Scroll acceleration rate |
| Scroll Boost | Multiplier when **Ctrl** is held while scrolling |
| Zoom Boost | Zoom speed multiplier when **Ctrl** is held |

Increase **Scroll Boost** and **Zoom Boost** for faster navigation through long logs. Increase **Debounce** if arrow keys feel too sensitive on the first press.

## Plot-level options

Many display options live on each plot, not in this dialog:

| Where | Options |
|-------|---------|
| Line plot setup (pencil or right-click → **Settings**) | Channels, scaling, events, **Show all events**, axes, milestones |
| Scatter plot setup | X/Y/Z channels, soft falloff, path, compare visibility and marker shapes |
| Lap matrix setup | Channel rows and colour bands |

See [Plot Types](plot-types) for details.
