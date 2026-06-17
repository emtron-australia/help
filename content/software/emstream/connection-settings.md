---
title: "Connection Settings"
description: "Configure telemetry server connection and credentials."
weight: 4
---

**File → Connection Settings**

Connection settings control how EmStream connects to the telemetry data server to receive live channel values from the vehicle.

## Server

| Setting | Description |
|---------|-------------|
| Server | Preset region — Australia, North America, Europe, or Custom |
| Host | Server hostname (editable only when Custom is selected) |

Regional servers:

| Region | Host |
|--------|------|
| Australia | `telemetry-aus.emtronaustralia.com.au` |
| North America | `telemetry-usa.emtronaustralia.com.au` |
| Europe | `telemetry-eu.emtronaustralia.com.au` |

Select the region closest to the vehicle for lowest latency.

## Credentials

| Setting | Description |
|---------|-------------|
| Saved Vehicles | Quick-select a previously saved vehicle |
| Vehicle Name | Exact name entered during telemetry activation on EmNet |
| Password | Shared team password from activation |
| Use SSL | Must be enabled for official Emtron servers |

These credentials must match those configured in Display Studio under **File → Telemetry Credentials** on the display.

## Connect and Disconnect

Click **Connect** to authenticate and begin receiving data. The toolbar shows the connection status, username, and data rate in kbit/s.

Use **File → Disconnect** or the **Disconnect** button in the settings dialog to end the session.

## Saved Vehicles

**File → Manage Saved Vehicles** stores vehicle name and password pairs locally on your PC. Credentials are saved in the Saved Vehicles list and appear in the dropdown on all connection dialogs.

Select a saved vehicle to populate the name and password fields. Click a list entry to edit, or use **Delete Selected** to remove it.