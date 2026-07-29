---
title: "Opening Logs"
description: "Open, compare, and download log files."
weight: 3
---

## Supported File Formats

| Extension | Source |
|-----------|--------|
| `.elo` | Emtron display logs (ED7, ED10, etc.) |
| `.elf` | Emtron ECU and PC logs |

Open a log via **File → Open Log** or by dragging a file into EmVision. The default folder is remembered between sessions.

## Log Explorer

The **Log Explorer** tab in the left drawer lists all open log files and their laps.

### Lap Selection

Each lap row provides controls for comparison:

| Icon | Purpose |
|------|---------|
| Crosshairs (blue) | Set as **reference** lap — the primary data shown on plots |
| Circle markers (orange/green) | Set as **overlay 1** or **overlay 2** for comparison |
| Flag | Indicates the fastest lap |
| Best | Marks the best lap time |

Only one lap can be the reference at a time. Up to two additional laps can be overlaid for comparison. Overlay data appears in contrasting colours on plots.

### Aligning overlays

Align comparison laps with the reference so features line up at a common point (for example start/finish):

| Method | Action |
|--------|--------|
| **Shift+drag** on a line plot | Adjust comparison 1 offset interactively |
| **Alt+Shift+drag** on a line plot | Adjust comparison 2 offset |
| Keyboard | Fine-tune offset (below) |

| Key | Action |
|-----|--------|
| `,` / `.` | Decrease / increase offset |
| `Ctrl+,` / `Ctrl+.` | Fast decrease / increase offset |
| `'` | Set offset to cursor (single cursor) or adjust by cursor difference (dual cursor) |
| `[` / `]` | Select previous / next active section |
| `;` | Toggle visibility of the selected section |

In-laps and out-laps can be set as reference or comparison the same way as flying laps.

### Log Summary Bar

The coloured icons in the title bar provide quick access to the reference and overlay sections currently loaded. Lap markers use primary blue for the reference, with distinct colours for comparison 1 and 2.

## Log Download

**File → Log Download** connects to an Emtron display (or compatible unit) on the network and lists logs available for download.

1. Open the Log Download dialog (EmVision refreshes the available list).
2. Set the **Save to** folder with the folder control.
3. **Refresh** if the device list looks stale.
4. Download individual logs from the list, or use **Download all** to fetch every missing or out-of-date log in one step.
5. Optional tools on the dialog: finish the current device log, delete all logs on the device (confirm first), and view storage used on the unit.

Downloaded `.elo` files can then be opened directly in EmVision. The PC must reach the display on the network (typical mDNS/hostname or configured unit URL).

## Export

To write the reference log to CSV or Emtron log format, see [Export Log](export-log).

## Import Track File

**File → Import Track File** loads a `.geojson` track outline for use with the [Track Map](plot-types#track-map) plot. Imported tracks appear in **Settings → Track Map**.