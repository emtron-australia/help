---
title: "Plot Types"
description: "Reference for all EmVision plot and view types."
weight: 5
---

EmVision supports six plot types. Select the type in [Layout Editor](layout-editor) mode, from the plot’s context menu, or when creating a new plot pane.

## Opening plot setup

For line and scatter plots:

- Click the **pencil** (configure) control on the plot, or
- **Right-click** the plot and choose **Settings** at the top of the menu (same dialog as the pencil).

## Line Plot

The primary analysis plot. Displays one or more channels against time or distance on the X-axis.

### Features

- Multiple channels with independent Y-axis scaling
- Event markers along the X-axis
- Lap and sector milestone bands (when enabled)
- Corner and straight segment highlighting
- Channel highlight and hide toggles
- **Drag channels from the Measurements panel** (right-hand drawer) onto the plot to add them quickly

{{% notice style="tip" %}}
Drag any channel from the **right-hand Measurements list** onto a line plot to plot it. No need to open the channel setup dialog first.
{{% /notice %}}

### Configuration tabs

| Tab | Contents |
|-----|----------|
| Channels | Select channels, colours, scaling mode, and Y-axis assignment |
| Events | Select events as vertical markers, or enable **Show all events** |
| Display | Toggle axes, race milestones, corners/straights |

### Show all events

On the **Events** tab, **Show all events** draws every event in the log without picking them one by one. When it is on, the individual event list is disabled. Uncheck it to choose a specific subset of events.

### Scaling modes

| Mode | Description |
|------|-------------|
| Scale to Fit | Y-axis fits the min/max of the channel data in view |
| Scale to Reference | Uses the reference channel's Y-axis range |
| Scale from Database | Uses predefined min/max from the channel database |

## Scatter Plot

Plots one channel against another (X vs Y), with an optional third channel controlling point colour.

### Features

- X, Y, and optional Z (colour) channel assignment
- Connecting lines between sequential points (**Show path**)
- Marker type selection for the reference series
- Colour range boxes for Z-channel segmentation
- Double-click a range box to toggle visibility; drag to apply the same toggle across ranges
- Overlay comparison laps with fixed overlay colours (reference keeps Z/channel colouring and paints on top)

### Scatter setup options

| Option | Description |
|--------|-------------|
| Show path | Draw lines between sequential points |
| Soft falloff | Soft-edged points for dense clouds (easier to read when zoomed out). Adjust **Radius** when enabled |
| Reference shape | Marker style for the reference lap (disabled when soft falloff is on) |
| Show 1st / 2nd compare | Toggle visibility of comparison laps |
| 1st / 2nd compare shape | Marker style for each comparison series |
| Show axis numbers | X and Y axis labels |
| Min/max override | Manual axis limits for X and/or Y |

Open setup with the pencil icon or **right-click → Settings**.

## Track Map

GPS position plot showing the vehicle path around a circuit.

### Features

- Vehicle position marker with configurable dimensions
- Track outline from imported GeoJSON or log GPS data
- Cursor follows vehicle position
- **F10** toggles between track-following and car-following zoom modes

Vehicle dimensions are set in [Settings](settings#vehicle). Import tracks via **File → Import Track File** (see [Opening Logs](opening-logs#import-track-file)). Creating GeoJSON maps is covered under [Creating a Track Map](/motorsport/creating-track-map).

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
