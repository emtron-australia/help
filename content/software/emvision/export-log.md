---
title: "Export Log"
description: "Export the reference log to CSV or Emtron log format."
weight: 3
---

**File → Export Log** (requires an open reference log)

Export writes selected channels from the **reference** log to a file on disk. Comparison overlays are not included.

## Export Formats

| Format | Extension | Use when |
|--------|-----------|----------|
| **CSV** | `.csv` | Spreadsheet or third-party analysis. Wide table: one column per channel, rows forward-filled in time. |
| **Emtron Log** | `.elo` | Re-open in EmVision or other Emtron tools that accept display-style logs. |

## Range

| Option | Description |
|--------|-------------|
| **Entire log** | Export the full reference log from start to end. |
| **Visible window** | Export only the time (or distance) range currently shown on the plots. Useful for extracting a single run or lap region. |

## Channel Selection

When the dialog opens, **no channels are selected**. Choose what to export:

1. Use the filter box to narrow the list by name.
2. Tick individual channels, or click **All** / **None**.
3. At least one channel must be selected before **Export…** is enabled.

Only channels available on the reference log appear in the list. Math channels computed in EmVision may not be listed for export — export native log channels, or re-create derived values after import if needed.

## Exporting

1. Open a log and ensure the section you care about is the **reference**.
2. Optionally zoom the plots so the **visible window** matches the range you want.
3. **File → Export Log**.
4. Choose **Format** and **Range**.
5. Select channels.
6. Click **Export…**, pick a destination path, and confirm.

A progress bar shows status. On success the dialog shows **Export complete.** Failures show an error message (for example if the destination is not writable).

## Tips

- For drag or circuit analysis in another tool, export **CSV** with speed and GPS-related channels, and match the same units you use in EmVision.
- Prefer **Visible window** when the log is long and you only need one pass or session.
- Export does not modify the original log file.
