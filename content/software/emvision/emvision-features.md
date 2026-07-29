---
title: "EmVision Features"
description: "Feature overview of EmVision log analysis software."
weight: 2
---

EmVision is Emtron's PC log analysis application for reviewing data recorded by ECUs, displays, and PC logging. It is available via [EmUpdater](https://emnet.emtronaustralia.com.au/downloads).

This page is a high-level features list. For a first session, see [Getting Started](getting-started). For menus and layout, see the [EmVision User Guide](emvision).

## Log Files and Data Sources

- Open Emtron display logs (`.elo`) from ED7, ED10, and related products
- Open Emtron ECU and PC logs (`.elf`)
- Open logs via **File → Open Log** or drag-and-drop
- Download logs over the network from a connected display or ECU (**File → Log Download**)
- **Download all** to fetch every missing or out-of-date log in one step
- Export the reference log to **CSV** or **Emtron log** (whole log or visible window, channel selection) — see [Export Log](export-log)
- Import **GeoJSON** track maps for circuit GPS overlay

## Lap Comparison and Overlay

- Set one **reference** lap as the primary analysis section
- Overlay up to **two comparison laps** (same log or other open logs)
- In-laps and out-laps can be used as reference or comparison
- Automatic best-lap and fastest-lap indication in the Log Explorer
- Align overlays on the plot with Shift+drag (comparison 1) and Alt+Shift+drag (comparison 2)
- Keyboard offset controls for fine alignment
- Section visibility toggle and section cycling

## Workspaces and Pages

- **Workspaces** save pane layout, open pages, plot configuration, and floating gauges
- Create, rename, duplicate, and switch workspaces from the Workspace menu or Workspace Explorer
- Workspace search (**Ctrl+W**)
- **Pages** are reusable analysis layouts stored as individual files (`.elp`)
- Page Explorer and page search (**Ctrl+P**)
- Up to **four plot panes** per window (**Ctrl+1**–**Ctrl+4**)
- Auxiliary full-width page row above the main grid (**Ctrl+`**)
- Sample pages included for common analysis themes (boost, knock, traction, track, torque, and more)

## Multi-Window

- Up to **four simultaneous EmVision windows**
- Primary window hosts the Workspace Explorer
- Secondary windows share open log data and can show different page layouts

## Plot Types

Six plot and view types, mixable in any page layout:

| Type | Purpose |
|------|---------|
| **Line Plot** | Multi-channel traces vs time or distance |
| **Scatter Plot** | X–Y channel relationship with optional Z colour |
| **Track Map** | GPS vehicle path on circuit outline |
| **Lap Timing** | Sector and lap split time table |
| **Gauge Area** | Dashboard-style gauges at the cursor |
| **Lap Matrix** | Colour-coded channel statistics across laps |

### Line Plot

- Multiple channels with independent Y-axis scaling
- Scaling modes: scale to fit, scale to reference, scale from channel database
- Event markers (individual selection or **show all events**)
- Lap and sector milestone bands
- Corner and straight segment highlighting
- Drag-and-drop channels from the measurements panel
- Channel highlight and hide toggles

### Scatter Plot

- X, Y, and optional Z (colour) channel assignment
- Connecting lines and marker type selection
- Colour range boxes for Z-channel segmentation
- Overlay comparison laps with distinct colours and shapes
- Soft falloff option for dense point clouds
- Show/hide comparison toggles and per-compare marker shapes

### Track Map

- Vehicle position marker with configurable vehicle dimensions
- Track outline from imported GeoJSON or log GPS data
- Track-following or car-following zoom (**F10**)
- Smooth pan and zoom

### Lap Timing

- Sector times per lap, best sector and best lap highlighting
- Special lap columns (in-lap, out-lap)
- Totals row from log lap timing data

### Gauge Area

- Multiple gauge styles in a single pane
- Values update as the cursor moves during analysis and playback

### Lap Matrix

- Configurable channel rows with colour bands
- Drag rows to reorder
- Quick identification of highest/lowest values per channel across laps

## Layout Editor

- Change plot type per cell
- Nested horizontal and vertical splits within a page
- Drag dividers to resize; ratios saved with the page
- Right-click a plot to change type, split, or delete without full edit mode
- Maximise a single plot to fill its pane
- Navigator channel (global under Settings) for playback preview

## Cursors and Measurements

- Single cursor with click-to-position and keyboard pan/zoom
- **Dual cursor** mode (**D**) with swap (**S**) and align secondary (**B**)
- Delta values between cursors in the measurements panel
- Playback animation of the cursor through the log (time mode)
- Measurements panel (**F8**): sector/lap context, all channel values and units
- Click a measurement to highlight the channel on plots
- **Time** or **distance** X-axis (**F9**)

## Math Channels

- Offline analysis maths using **emexpr** (same language as Display Studio)
- Full syntax reference: [Math Functions](/displays/functions/maths) — see also [Math Channels](math-channels)
- Math channels can reference other math channels
- Enum lookup for status channels — insert named state values into expressions
- Binary (`0b`) and hex (`0x`) integer literals
- Client [user channels](user-channels) for custom names alongside maths
- Not written back into the original log file

## Circuit and Drag Analysis

- Auto-detect **circuit** vs **drag** analysis mode, with forced overrides
- Circuit: lap and sector milestones from GPS and race data
- Drag: distance-based strip markers (60 ft, 330 ft, 660 ft, 1320 ft, etc.)
- Generate drag markers from cursor or from a trigger channel
- Clear drag markers on the selected section
- Configurable circuit speed, drag speed, and drag trigger channels

## Floating Gauges

- Draggable, resizable overlays above all plot content
- Gauge types: bar, radial, steering wheel, force vector
- Colour bands, min/max range, and fill direction
- Saved and restored with the workspace

## Navigation and Usability

- Full keyboard shortcut set (see [Keyboard Shortcuts](keyboard-shortcuts))
- Configurable scroll/zoom acceleration and boost
- Left drawer: Log Explorer, Page Explorer, Workspace Explorer (**F7**)
- Right drawer: live measurements at the cursor
- Progress bar for log loading
- Enum-aware status channel display (named states instead of raw numbers)
- Multi-language UI support

## Performance and Platform

- Fast log open, pan, zoom, and cursor interaction
- Efficient multi-lap comparison on the same log
- Responsive math editing and channel add/remove
- Windows crash dumps on unhandled exceptions (rich mini dump by default)

## Related Pages

- [Getting Started](getting-started)
- [EmVision User Guide](emvision) — main window, menus, and typical workflow
- [Opening Logs](opening-logs) · [Export Log](export-log)
- [Workspaces and Pages](workspaces-and-pages)
- [Plot Types](plot-types)
- [Math Channels](math-channels) · [User Channels](user-channels)
- [Math Functions](/displays/functions/maths) — emexpr syntax (Display Studio docs)
- [Circuit and Drag Analysis](circuit-and-drag-analysis)
- [Release Notes](emvision-release-notes)
