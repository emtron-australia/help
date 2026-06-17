---
title: "EmVision User Guide"
description: "Overview of EmVision log analysis software."
weight: 2
---

EmVision is Emtron's log analysis application for reviewing data recorded by ECUs, displays, and PC logging. It is available via [EmUpdater](https://emnet.emtronaustralia.com.au/downloads).

Use EmVision to open log files, compare laps, overlay multiple sessions, build custom analysis layouts, and create math channels for derived measurements.

## Main Window

The EmVision window is divided into three areas:

| Area | Description |
|------|-------------|
| Left drawer | Log Explorer, Page Explorer, and Workspace Explorer |
| Centre | Plot panes showing the active analysis pages |
| Right drawer | Cursor measurements for all channels at the current position |

The title bar shows the current workspace, X-axis mode (Time or Distance), and open log files. A progress bar at the bottom indicates log loading status.

## Toolbar

| Button | Action |
|--------|--------|
| Play / Stop | Animate the cursor through the log in time mode |
| Edit Layout | Toggle layout editing mode to change plot types and split panes |
| Show/Hide Laps | Toggle lap and sector markers on plots |
| Time / Distance (F9) | Switch the X-axis between time and distance |
| Circuit/Drag mode | Cycle analysis mode — see [Circuit and Drag Analysis](circuit-and-drag-analysis) |
| Pane count | Cycle between 1, 2, 3, and 4 plot panes (Ctrl+1 through Ctrl+4) |

## Menu Reference

### File

| Item | Description |
|------|-------------|
| Open Log | Open an `.elo` or `.elf` log file — see [Opening Logs](opening-logs) |
| Close Log | Close the current log |
| Settings | Open analysis settings — see [Settings](settings) |
| Math Channels | Create formula and function math channels — see [Math Channels](math-channels) |
| Log Download | Download logs from a connected display or ECU |
| Import Track File | Import a `.geojson` track map for GPS overlay |
| Create Window | Open an additional EmVision window (up to 4) |
| Close Window | Close the current secondary window |
| Quit | Exit EmVision |

### Workspace

| Item | Description |
|------|-------------|
| Workspace list | Switch between saved workspace layouts |
| Add Floating Gauge | Add a floating gauge overlay — see [Floating Gauges](floating-gauges) |

### Tools

Drag strip analysis tools — see [Circuit and Drag Analysis](circuit-and-drag-analysis):

- Generate drag distance markers from cursor
- Generate drag distance markers from trigger channel
- Clear drag distance markers on selected section

### Help

| Item | Description |
|------|-------------|
| Keyboard Shortcuts | Full shortcut reference — see [Keyboard Shortcuts](keyboard-shortcuts) |
| About / Release Notes | Version history |

## Typical Workflow

1. **Open a log** via File → Open Log, or download from a device via File → Log Download.
2. Select laps in the **Log Explorer** — set a reference lap and up to two overlay laps for comparison.
3. Open or create **pages** with the plot types you need — see [Plot Types](plot-types).
4. Use the **cursor** to inspect values at any point — see [Cursors and Measurements](cursors-and-measurements).
5. Create **math channels** for derived calculations.
6. Save your layout as a **workspace** for reuse on future logs.

## Multi-Window

EmVision supports up to four simultaneous windows. The first window is the **Primary** window and hosts the Workspace Explorer. Secondary windows share the same log data but can show different page layouts.

Use **File → Create Window** to open additional windows. Each window maintains its own pane layout and page selection.