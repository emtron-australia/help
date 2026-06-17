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

### Section Offsets

When comparing overlay laps, adjust the **offset** to align laps at a common point (for example, synchronise at the start/finish line). Use the offset editor on each lap row, or keyboard shortcuts:

| Key | Action |
|-----|--------|
| `,` / `.` | Decrease / increase offset |
| `Ctrl+,` / `Ctrl+.` | Fast decrease / increase offset |
| `'` | Set offset to cursor (single cursor) or adjust by cursor difference (dual cursor) |
| `[` / `]` | Select previous / next active section |
| `;` | Toggle visibility of the selected section |

### Log Summary Bar

The coloured icons in the title bar provide quick access to the reference and overlay sections currently loaded.

## Log Download

**File → Log Download** connects to an Emtron display or ECU on the network and downloads available log files to your PC.

1. Open the Log Download dialog.
2. Set the **Save to** folder.
3. Select logs from the available list.
4. Click download.

Downloaded `.elo` files can then be opened directly in EmVision.

## Import Track File

**File → Import Track File** loads a `.geojson` track outline for use with the [Track Map](plot-types#track-map) plot. Imported tracks appear in **Settings → Track Map**.