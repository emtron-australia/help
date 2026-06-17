---
title: "EmStream User Guide"
description: "Overview of EmStream live telemetry monitoring software."
weight: 2
---

EmStream is the PC application for receiving live telemetry data from Emtron displays. It subscribes to the telemetry stream published by an ED7 or ED10 display and presents real-time channel values, plots, and track position. EmStream also supports [voice communications](voice-comms) and [text chat](text-chat) when licensed on the vehicle.

EmStream is available via [EmUpdater](https://emnet.emtronaustralia.com.au/downloads).

## Prerequisites

Before using EmStream, the vehicle display must be configured and activated for telemetry:

1. Activate telemetry on [EmNet](https://emnet.emtronaustralia.com.au/) — see [Telemetry Activation](/displays/functions/telemetry/#activation---license-server).
2. Configure telemetry credentials on the display in Display Studio — see [Authentication](/displays/functions/telemetry/#authentication).
3. Enable and configure the telemetry provider on the display — see [Data Service](/displays/functions/telemetry/telemetry-data).

EmStream uses the same **vehicle name** and **password** entered during activation.

## Main Window

| Area | Description |
|------|-------------|
| Centre | Active view — grid, plots, track map, or a combination |
| Right drawer | Live Data panel showing all channel values and events |
| Toolbar | Connection status, pause logging, chat console |

The title bar shows connection status for all three services:

| Indicator | Service |
|-----------|---------|
| Telemetry | Data stream with username and data rate (kbit/s) |
| Voice | Voice comms connection and activity |
| Chat | Text chat connection |

## Toolbar

| Button | Action |
|--------|--------|
| Pause / Resume | Pause or resume the local data logger |
| Chat icon | Open the floating chat console |

## Menu Reference

### File

| Item | Description |
|------|-------------|
| Connect / Disconnect | Connect to the telemetry data server |
| Connect Voice / Disconnect Voice | Connect to the voice server |
| Connect Text Chat / Disconnect Text Chat | Connect to the text chat server |
| Connection Settings | Telemetry server and credentials — see [Connection Settings](connection-settings) |
| Voice Settings | Voice server, PTT, and audio — see [Voice Comms](voice-comms) |
| Text Chat Settings | Text server and display name — see [Text Chat](text-chat) |
| Manage Saved Vehicles | Store vehicle name/password pairs for quick login |
| Language | Change the UI language |
| Exit | Close EmStream |

### Logger

Local data recording — see [Data Logger](data-logger):

| Item | Description |
|------|-------------|
| Pause / Resume Logging | Stop or start buffering incoming data |
| Set Default Window (ms) | Default time window for plots (when paused) |
| Clear Logged Data | Erase the buffered data |
| Save Log to File | Export full buffer as `.dlf` |
| Save Visible Window to File | Export only the currently visible time window |
| Load Log from File | Load a previously saved `.dlf` file |

### View

| Item | Description |
|------|-------------|
| Show Chat Console | Open the floating text chat window |
| Window Count | 1, 2, 3, or 4 simultaneous windows |
| Type | View layout for the current window — see [View Layouts](view-layouts) |
| Set Track File | Load a `.geojson` track outline |
| Set GPX File | Load a `.gpx` route or waypoint file |
| Connect Waypoints | Draw lines between GPX waypoints |

### Help

| Item | Description |
|------|-------------|
| Release Notes | Version history |

## Typical Workflow

1. Open EmStream and enter credentials in **File → Connection Settings**.
2. **Connect** to the telemetry server.
3. Optionally **Connect Voice** and **Connect Text Chat**.
4. Choose a **view layout** (Grid, Plots, or Track) from **View → Type**.
5. Configure channels in the view setup (pencil icon on Grid or Plots views).
6. Monitor values in the **Live Data** drawer on the right.
7. **Pause** logging and **Save Log to File** to archive a session.