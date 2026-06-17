---
title: "Plot Types"
description: "Reference for all EmVision plot and view types."
weight: 5
---

EmVision supports six plot types. Select the type in [Layout Editor](layout-editor) mode, or when creating a new plot pane.

## Line Plot

The primary analysis plot. Displays one or more channels against time or distance on the X-axis.

### Features

- Multiple channels with independent Y-axis scaling
- Event markers along the X-axis
- Lap and sector milestone bands (when enabled)
- Corner and straight segment highlighting
- Channel highlight and hide toggles
- Drag-and-drop channels from the measurements panel

### Configuration

Click the configure (pencil) icon on a line plot to open the setup dialog:

| Tab | Contents |
|-----|----------|
| Channels | Select channels, colours, scaling mode, and Y-axis assignment |
| Events | Select events to display as vertical markers |
| Display | Toggle axes, race milestones, corners/straights |

### Scaling Modes

| Mode | Description |
|------|-------------|
| Scale to Fit | Y-axis fits the min/max of the channel data in view |
| Scale to Reference | Uses the reference channel's Y-axis range |
| Scale from Database | Uses predefined min/max from the channel database |

## Scatter Plot

Plots one channel against another (X vs Y), with an optional third channel controlling point colour.

### Features

- X, Y, and optional Z (colour) channel assignment
- Connecting lines between sequential points
- Marker type selection
- Colour range boxes for Z-channel segmentation
- Double-click a range box to toggle visibility; drag to apply the same toggle across ranges

## Track Map

GPS position plot showing the vehicle path around a circuit.

### Features

- Vehicle position marker with configurable dimensions
- Track outline from imported GeoJSON or log GPS data
- Cursor follows vehicle position
- **F10** toggles between track-following and car-following zoom modes

Vehicle dimensions are set in [Settings](settings#vehicle).

## Lap Timing

Split time table showing sector and lap times in a grid format.

### Features

- Sector times per lap in columns
- Best sector and best lap highlighting
- Special lap columns (in-lap, out-lap)
- Totals row

This plot reads directly from the log's lap timing data — no additional configuration is required.

## Gauge Area

Dashboard-style gauge display showing channel values at the cursor position.

### Features

- Multiple gauge styles in a single pane
- Values update as the cursor moves through the log
- Useful for replicating a dash layout view during playback

## Lap Matrix

Colour-coded matrix comparing channel statistics across laps.

### Features

- Configure which channels appear as rows
- Colour bands highlight value ranges
- Drag rows to reorder
- Quickly identify which lap had the highest/lowest value for each channel

Open the Lap Matrix settings from the toolbar button within the plot to add channels and configure colour bands.