---
title: "Voice Service"
weight: 2
description: "Real-time audio communication feature allowing users to conduct voice calls with automatic speaker management, push-to-talk control, and priority-based communication"
---

## Quick Start

### Setup: ED7M/ED10M

Assuming you have an active voice license and the [authentication settings](telemetry#authentication) configured in Display Studio, you can now configure the voice comms function.

#### Settings

Voice chat settings can be accessed from the main menu: `Functions → Voice Comms`.

| Setting                    | Description                                                                                              |
|----------------------------|----------------------------------------------------------------------------------------------------------|
| **Enable**                 | Globally activate/deactivate voice communications                                                        |
| **Broadcast Priority**     | Speaking [priority](#priority-system) when there are multiple users. (0 = highest priority, 10 = lowest) |
| **Push to Talk Condition** | When the conditions are met, voice will be transmitted.                                                  |

Once configured, 'Write' the config.

#### Functions

| Function                | Description                    |
|-------------------------|--------------------------------|
| **Push to Talk On**     | Forces push to talk on         |
| **Push to Talk Off**    | Forces push to talk off        |
| **Push to Talk Toggle** | Toggles the push to talk state |

#### Events

The following events can be triggered in the system to control the push to talk feature (the above function buttons emit these events).

| Event                   | Action                         |
|-------------------------|--------------------------------|
| **Push to Talk On**     | Forces push to talk on         |
| **Push to Talk Off**    | Forces push to talk off        |
| **Push to Talk Toggle** | Toggles the push to talk state |

#### Channels

The following channels are available to monitor the status of the system.

| Channel                 | Description                                |
|-------------------------|--------------------------------------------|
| Voice Connection Status | The connection status to the voice server  |
| Voice Connection Error  | The reason for connection failure on error |
| Voice Tx State          | Shows either: Silent or Speaking           |
| Voice Rx State          | Shows either: Silent or Speaking           |

**Important:** The connection status is the status of connection to the voice server. It doesn't know if EmStream is also connected.

### Setup: EmStream

EmStream stores authentication information per service type rather than in one place for flexibility.

The data service settings can be found in `File → Voice Settings`.

| Setting                   | Description                                                                                                    |
|---------------------------|----------------------------------------------------------------------------------------------------------------|
| **Host**                  | Enter the host from the below table based on the region configured in the device                               |
| **Vehicle Name**          | Exact vehicle name entered during the activation step above                                                    |
| **Password**              | The same password entered during the activation step above                                                     |
| **Use SSL**               | Must be set to **true** when using official Emtron servers                                                     |
| **Priority**              | Your speaking [priority](#priority-system) when there are multiple users. (0 = highest priority, 10 = lowest). |
| **Enable Push-to-Talk**   | If enabled, your voice will only be transmitted when the bound button is held down.                            |
| **PTT Key**               | The configured push to talk key, click rebind to change this.                                                  |
| **Enable Audio Playback** | Uncheck this only if you want to be able to transmit, but not hear anything from others.                       |

| Region        | Host                               |
|---------------|------------------------------------|
| Australia     | `voice-aus.emtronaustralia.com.au` |
| North America | `voice-usa.emtronaustralia.com.au` |

Once entered, select `Connect` to connect to the voice server. Once connected you will see `Voice Connected` in the top right hand corner.

If connection fails, the reason will be shown in the `Voice Settings` popup.

If push to talk is **active**, your voice will be transmitted only when the bound key is held down.

If push to talk is **inactive**, EmStream will attempt to detect your voice and transmit it when you are speaking. Silence will not be transmitted.

## Details

### Priority System

#### How It Works

The voice server manages multiple speakers using a **priority system**:

- **Your priority number** is set in Voice Settings (0 = highest, 10 = lowest)
- When multiple people try to speak:
  - **Lower number = gets to speak first**
  - **Higher number = gets interrupted by lower numbers**
  - System automatically manages silence between speakers

#### Practical Examples

**Scenario 1: Small team (1-2 people)**
- Priority system is relaxed
- Everyone can speak simultaneously
- Useful for open discussion between two people

**Scenario 2: Three or more people connected (3+ people)**
- Race Engineer (Priority 0) - Always gets to speak first
- Driver (Priority 1) - Can speak if engineer is not speaking.
- Technician (Priority 4) - Speaks only if both driver and engineer are silent
- Priority system becomes strict
- Only one person speaks at a time (based on priority)
- Higher priority users can interrupt lower priority users
- Prevents audio chaos in crowded rooms

#### Setting Your Priority

**Use Case Guidelines:**

| Priority | Person                         | Best For                                  |
|----------|--------------------------------|-------------------------------------------|
| 0-1      | Driver, Race Engineer          | Must speak first; critical communications |
| 3-5      | Regular technician, Supervisor | Normal priority                           |
| 6-8      | Support staff, Assistant       | Lower priority                            |
| 9-10     | Observers, Remote listeners    | Minimal speaking                          |

