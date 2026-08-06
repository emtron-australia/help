---
title: "Log Replay"
description: "Upload, select, and replay log files through Display Studio."
weight: 4
---

**Diagnostics → Log Replay**

Log Replay plays back recorded channel data so you can review a run without the vehicle running. Use it with logs downloaded from the display or files you upload from the PC.

## Logs list

| Action | Description |
|--------|-------------|
| **Refresh** | Reload the list of available logs |
| **Upload…** | Add a log file from the PC (e.g. `.elo` / product log types supported by the dialog) |
| **Delete** | Remove an **Uploaded** log from the local list (device logs are not deleted from the display here) |

Select a log in the list to load it for replay.

## Channels

After a log is selected, pick which channels to include in the replay stream. Use the search field to find channels by name.

## Playback

Use the replay controls (play / pause / seek as provided on the page) to move through the recording. Live data and gauges that listen to the same channel stream will follow the replayed values while playback is active.

## Related

- Configure what the display records: [Logging](../functions/logging)
- Live plotting while connected: [Live Plots](live-plots)
