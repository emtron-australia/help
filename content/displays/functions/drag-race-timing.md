---
title: "Drag Race Timing"
description: "Measure elapsed time and speed at drag strip distance markers."
weight: 3
---

**Functions → Drag Race Timing**

Drag Race Timing measures elapsed time and speed from a standing start, recording results at standard drag strip distance markers. Distance is calculated by integrating the configured speed channel.

## Enabling

Check **Enable** to activate the function.

## Configuration

| Setting | Description |
|---------|-------------|
| Speed Channel | Source speed in km/h — required for distance integration |
| Arm Conditions | [Conditions](conditions) that must become true before a run can start |
| Start Conditions | Conditions that trigger the run start on a rising edge |
| Abort Threshold | Run is aborted if speed drops below this value (km/h) |

### Typical Setup

1. **Arm** when the vehicle is staged (for example, a staging light input or speed below 2 km/h).
2. **Start** when the vehicle begins moving (for example, speed exceeds 2 km/h, or a launch event fires).

## Distance Markers

When a run is active, the function records time and speed at each marker:

| Marker | Distance |
|--------|----------|
| 0–60 ft | Start line |
| 60 ft | 18.3 m |
| 330 ft | 100.6 m |
| 1/8 Mile (660 ft) | 201.2 m |
| 1000 ft | 304.8 m |
| 1/4 Mile (1320 ft) | 402.3 m |

The run completes automatically when the 1/4 mile distance is reached, or aborts if speed falls below the abort threshold.

## Output Channels

The function writes elapsed time and trap speed at each marker, plus cumulative **Drag Time** and **Drag Distance** channels during a run. A live drag time slip preview is shown on the configuration page when a device is connected.

## Displaying Results

Map the drag timing output channels to Value or Time gauges on a screen. For example, show **1/4 Mile Time** and **1/4 Mile Speed** on a dedicated drag page.

Drag timing can also work alongside [Lap Timing](lap-timing) — use a finish beacon on a drag strip start/finish line for point-to-point events.