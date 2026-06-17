---
title: "Getting Started"
description: "First-time setup and connection to a vehicle."
weight: 3
---

## Install EmStream

Download and install EmStream via [EmUpdater](https://emnet.emtronaustralia.com.au/downloads).

## Activate Telemetry on the Display

Telemetry must be licensed and configured on the display before EmStream can connect. Complete these steps on the vehicle side first:

1. **Activate** on [EmNet](https://emnet.emtronaustralia.com.au/) — enter the display serial number, activation code, vehicle name, and password.
2. In **Display Studio**, open **File → Telemetry Credentials** and enter the region, vehicle name, password, and SSL settings. Click **Save Telemetry Settings**.
3. In Display Studio, open **Functions → Telemetry** and configure the telemetry provider — enable it, set start conditions, and select channels to transmit.

Full details are in the [Telemetry](/displays/functions/telemetry/) documentation.

## Connect from EmStream

1. Launch EmStream.
2. Open **File → Connection Settings**.
3. Select the **Server** region closest to you (Australia, North America, or Europe).
4. Enter the **Vehicle Name** and **Password** from activation.
5. Ensure **Use SSL** is enabled.
6. Click **Connect**.

The toolbar shows **Telemetry Connected** with your username and the current data rate when the connection succeeds.

## Save Credentials

To avoid re-entering credentials for frequently monitored vehicles:

1. Open **File → Manage Saved Vehicles**.
2. Enter the vehicle name and password.
3. Click **Save**.

Saved vehicles appear in the dropdown on the Connection Settings, Voice Settings, and Text Chat Settings pages.

## Connect Voice and Chat

Voice and text require separate connections:

- **File → Connect Voice** — see [Voice Comms](voice-comms)
- **File → Connect Text Chat** — see [Text Chat](text-chat)

Voice is supported on ED7M and ED10M. Text is supported on ED7, ED7M, and ED10M.