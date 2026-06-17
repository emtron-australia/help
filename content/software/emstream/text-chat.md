---
title: "Text Chat"
description: "Real-time text messaging with the vehicle team."
weight: 12
---

**File → Text Chat Settings** / **File → Connect Text Chat**

Text chat provides real-time messaging with other users connected to the same vehicle. Text is supported on ED7, ED7M, and ED10M displays with an active text license.

Device-side setup is in Display Studio under **Functions → Text Chat** — see [Text Service](/displays/functions/telemetry/telemetry-text).

## Connection Settings

| Setting | Description |
|---------|-------------|
| Server | Australia, North America, Europe, or Custom |
| Display Name | Your name in the chat — must be unique per vehicle session |
| Vehicle Name | Same vehicle name used for telemetry |
| Password | Same password used for telemetry |
| Use SSL/TLS | Enable encrypted connection |

Regional text servers:

| Region | Host |
|--------|------|
| Australia | `text-aus.emtronaustralia.com.au` |
| North America | `text-usa.emtronaustralia.com.au` |
| Europe | `text-eu.emtronaustralia.com.au` |

Click **Connect** to join the chat session. Connection errors are shown in the settings dialog.

## Chat Console

Open the chat console from:

- **View → Show Chat Console**
- The chat icon in the toolbar

The chat window floats above the main view and can be dragged to any position. It shows message history and a text input for sending messages.

Messages are delivered in real time to all connected users on the same vehicle — including users on the display, other EmStream instances, and the web interface.

## Quick Messages

The display can be configured to send automatic quick messages triggered by events (for example, "Pit now" when a condition is met). These appear in the chat history like any other message. Quick message configuration is on the display in Display Studio.