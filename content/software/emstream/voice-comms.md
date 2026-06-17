---
title: "Voice Comms"
description: "Real-time voice communication with the vehicle team."
weight: 11
---

**File → Voice Settings** / **File → Connect Voice**

Voice communications let you talk with other users connected to the same vehicle session. Voice is supported on ED7M and ED10M displays with an active voice license.

Device-side setup is in Display Studio under **Functions → Voice Comms** — see [Voice Service](/displays/functions/telemetry/telemetry-voice).

## Connection Settings

| Setting | Description |
|---------|-------------|
| Server | Australia, North America, Europe, or Custom |
| Vehicle Name | Same vehicle name used for telemetry |
| Password | Same password used for telemetry |
| Use SSL/TLS | Enable encrypted connection |
| Priority | Speaking priority when multiple users talk (0 = highest, 10 = lowest) |

Regional voice servers:

| Region | Host |
|--------|------|
| Australia | `voice-aus.emtronaustralia.com.au` |
| North America | `voice-usa.emtronaustralia.com.au` |
| Europe | `voice-eu.emtronaustralia.com.au` |

Click **Connect** to join the voice session. The toolbar microphone icon turns green when voice activity is detected.

## Push-to-Talk

Push-to-Talk (PTT) mode requires holding a key to transmit:

| Setting | Description |
|---------|-------------|
| Enable Push-to-Talk | When enabled, voice transmits only while the PTT key is held |
| PTT Key | Keyboard key used for push-to-talk (default F1) |

Click **Rebind** and press a key to change the PTT binding. PTT settings can only be changed while disconnected.

When PTT is disabled, voice uses automatic voice activity detection — the microphone transmits when you speak.

## Audio Settings

| Setting | Description |
|---------|-------------|
| Enable Audio Playback | Hear other users' audio through your PC speakers |

## Priority System

Lower priority numbers win when multiple users speak simultaneously. A user with priority 0 can interrupt a user with priority 5. Set your priority to match your role — for example, the driver might use a lower number than a pit lane engineer.

The display-side **Broadcast Priority** setting in Display Studio should be configured to complement EmStream priorities.