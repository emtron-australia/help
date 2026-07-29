---
title: "Getting Started"
description: "Install EmVision and complete a first analysis session."
weight: 2
---

## Install

1. Download and install EmVision via [EmUpdater](https://emnet.emtronaustralia.com.au/downloads).
2. Launch EmVision from the Start menu or EmUpdater.

No separate licence activation is required for offline log analysis. Network features such as log download need the PC to reach the display or ECU on the LAN.

## First session

### 1. Open a log

- **File → Open Log**, or drag an `.elo` / `.elf` file into the window.
- Sample content may be available under the EmVision install folder (`samples/logs` and `samples/pages` when shipped with the installer).
- Opening a log sets it as the **reference**. Progress is shown on the bottom bar.

See [Opening Logs](opening-logs) for formats, lap selection, and download.

### 2. Explore the main window

| Area | What to try |
|------|-------------|
| Left drawer (**F7**) | **Log Explorer** — pick reference and comparison laps |
| Centre | Plots for the active page |
| Right drawer (**F8**) | Channel values at the cursor |

Click a plot to place the cursor. Use arrow keys to pan; hold **Ctrl** for faster movement.

### 3. Open a sample page

1. Select the **Page Explorer** tab in the left drawer.
2. Open a page that matches your interest (for example **Boost**, **Knock**, **Track**, or **Traction Control**).
3. Pages appear as tabs on the plot panes. Use **Page Up** / **Page Down** to switch tabs.

If you prefer a blank layout, use the layout tools later — see [Workspaces and Pages](workspaces-and-pages) and [Layout Editor](layout-editor).

### 4. Compare laps

In **Log Explorer**:

1. Set one lap as **reference** (crosshairs).
2. Set up to two other laps as **comparison** overlays.
3. Align overlays on a line plot with **Shift+drag** (comparison 1) or **Alt+Shift+drag** (comparison 2), or use the offset shortcuts in [Opening Logs](opening-logs).

### 5. Inspect values and add channels

- Single cursor: click the plot.
- Dual cursor: press **D** — see [Cursors and Measurements](cursors-and-measurements).
- Toggle **time** vs **distance** with **F9** when the log has distance data.
- **Tip:** Drag a channel from the **right-hand Measurements list** onto a line plot to add it without opening plot setup.

### 6. Save a workspace

When the layout is useful:

1. Create or rename a workspace from the **Workspace** menu or Workspace Explorer.
2. The workspace stores panes, pages, plot setup, and floating gauges for the next log.

## What to learn next

| Topic | Page |
|-------|------|
| Features overview | [EmVision Features](emvision-features) |
| Menus and multi-window | [EmVision User Guide](emvision) |
| Plot types | [Plot Types](plot-types) |
| Math expressions | [Math Channels](math-channels) (syntax: [Math Functions](/displays/functions/maths)) |
| Export for spreadsheets | [Export Log](export-log) |
| Download from a device | [Opening Logs](opening-logs#log-download) |
| Keyboard map | [Keyboard Shortcuts](keyboard-shortcuts) |

## Typical full workflow

1. Open or download a log.
2. Choose reference (and optional comparison) laps.
3. Open or build pages with the plot types you need.
4. Use the cursor and measurements panel.
5. Add [math channels](math-channels) if you need derived signals.
6. Optionally [export](export-log) CSV for external tools.
7. Save the workspace for the next session.
