---
title: "Data Logger"
description: "Buffer, pause, and save live telemetry data locally."
weight: 9
---

EmStream buffers all incoming telemetry data in a local data logger. The logger runs continuously while connected and feeds the plot views. Use the logger menu to control recording and export data for later analysis.

## Pause and Resume

| Control | Action |
|---------|--------|
| Toolbar pause button | Toggle pause/resume |
| **Logger → Pause / Resume Logging** | Same as toolbar |

When **paused**, incoming data stops being appended to the buffer. Plots stop scrolling and you can review historical data. When **resumed**, logging continues from the current point.

## Default Window

**Logger → Set Default Window (ms)** sets the default time span visible on plots when paused. Enter the duration in milliseconds — for example, `30000` for a 30-second window.

## Clear Data

**Logger → Clear Logged Data** erases the entire buffer. This cannot be undone. The logger must be paused first.

## Save and Load

| Action | Description |
|--------|-------------|
| Save Log to File | Export the full buffered data as a `.dlf` file |
| Save Visible Window to File | Export only the time range currently visible on plots |
| Load Log from File | Load a previously saved `.dlf` file for review |

All save and load operations require the logger to be paused. The default save folder is remembered between sessions.

Saved `.dlf` files can be reviewed in EmStream without an active telemetry connection.