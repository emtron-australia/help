---
title: "Cursors and Measurements"
description: "Inspect channel values at any point in the log."
weight: 7
---

## Cursor

Click on any plot to position the **cursor** at that point. The cursor reads channel values at the selected time or distance and displays them in the Measurements panel.

### Navigation

| Input | Action |
|-------|--------|
| Click on plot | Move cursor to clicked position |
| Arrow keys | Scroll/pan the plot view (hold for accelerated scrolling) |
| Ctrl + arrow keys | Faster scrolling and zooming |
| Play button | Animate cursor through the log (time mode only) |

Scroll and zoom behaviour is configured in [Settings → Navigation](settings#navigation).

## Dual Cursor Mode

Press **D** to toggle dual cursor mode. Two cursors appear on plots:

| Key | Action |
|-----|--------|
| `S` | Swap primary and secondary cursor positions |
| `B` | Move secondary cursor to the primary position |

In dual cursor mode, the Measurements panel shows values at both cursor positions and the delta between them. This is useful for comparing channel values at two points in a lap.

When aligning overlay laps, **'** (apostrophe) adjusts the overlay offset by the difference between the two cursors.

## Measurements Panel

The **Measurements** panel is the right-hand drawer (**F8** to toggle). It shows:

- Current sector name, distance, and time at the cursor
- Current lap distance and time at the cursor
- All channel values at the cursor position, with units
- Delta values when in dual cursor mode

Channel values update in real time as the cursor moves. Click a channel in the measurements list to highlight it on plots.

## X-Axis Modes

Press **F9** or click the time/distance icon in the toolbar to switch the X-axis:

| Mode | X-Axis |
|------|--------|
| Time | Elapsed time from log start |
| Distance | Integrated distance (requires distance data in the log) |

Distance mode is essential for drag strip analysis and distance-based channel comparison. If the log contains no distance data, distance mode and drag tools are unavailable.