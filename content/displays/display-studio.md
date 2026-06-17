---
title: "Display Studio"
description: "Overview of the Display Studio configuration application for ED7 and ED10 displays."
weight: 5
---

Display Studio is the PC application used to configure Emtron ED7 and ED10 series displays. It is available via [EmUpdater](https://emnet.emtronaustralia.com.au/downloads).

Use Display Studio to build dash layouts, wire up inputs and outputs, configure timing and logging, and write the finished configuration to the display over Ethernet or Wi-Fi.

## Connecting to a Display

1. Power on the display and connect it to the same network as your PC (Ethernet or Wi-Fi).
2. Launch Display Studio. The **Home** view searches for connected devices automatically.
3. When connected, the live dash preview and communications status appear on the Home screen.

If the display is not found, work through [Connection Troubleshooting](troubleshooting/connection-troubleshooting).

To work offline without a connected device, use **File → Open Config** (or the toolbar **Open** button) to load a saved configuration file.

## Toolbar

The toolbar provides quick access to common file and device operations:

| Button | Action |
|--------|--------|
| Open | Open a configuration file from disk |
| Save | Save the active configuration to its current path |
| Save As | Save the configuration to a new file |
| Close | Close the active configuration |
| Read from device | Download the configuration currently stored on the display |
| Write to device (F4) | Upload the active configuration to the display |
| Back / Forward | Navigate through recently visited pages |
| Sync indicator | Shows whether the loaded config matches the device |

When a device is **locked**, configuration read and write operations are disabled until the device is unlocked via **File → Unlock Device**.

## Menu Reference

The application menus mirror the configuration structure. Pages marked *(device)* are stored on the display hardware rather than in the configuration file.

### File

| Item | Description |
|------|-------------|
| Open / Save / Save As / Close | Manage configuration files (`.edconfig`) |
| Read from Display | Download config from a connected display |
| Write to Display | Upload config to a connected display |
| Channel Preferences | Set display units and channel formatting — see [Channel Preferences](device/channel-preferences) |
| Wi-Fi Setup *(device)* | Configure the display Wi-Fi network — see [Wi-Fi](functions/wifi) |
| Bluetooth Settings *(device)* | Pair Bluetooth audio devices — see [Bluetooth](device/bluetooth) |
| Device Settings *(device)* | Time zone and other hardware settings — see [Device Settings](device/device-settings) |
| Telemetry Credentials *(device)* | Authentication for telemetry services — see [Telemetry](functions/telemetry/) |
| Language | Change the Display Studio UI language |
| Firmware Upgrade | Update display firmware — see [Firmware Upgrade](device/firmware-upgrade) |
| Connection Mode | Standard or Localhost Only (for development) |
| Lock / Unlock Device | Prevent accidental config changes on the display |
| Exit | Close Display Studio |

### View

| Item | Description |
|------|-------------|
| Home | Device connection status, live dash preview, and log download |
| Show Live Data (F8) | Toggle the live data drawer showing real-time channel values |

### Setup

Configuration metadata and custom channel definitions — see [Setup](setup/).

| Item | Page |
|------|------|
| Details | [Vehicle Details](setup/vehicle-details) |
| User Channels | [User Channels](setup/user-channels) |
| User Events | [User Events](setup/user-events) |
| User Enums | [User Enums](setup/user-enums) |
| Enum Associations | [Enum Associations](setup/enum-associations) |

### Inputs/Outputs

Hardware interfaces and bus configuration — see [Inputs/Outputs](inputs-outputs/).

| Item | Page |
|------|------|
| CAN | [CAN Bus](inputs-outputs/can-bus) |
| RS232 | [RS232](inputs-outputs/rs232) |
| RS232 Console | Serial terminal for debugging |
| LIN | [LIN Bus](functions/lin-bus) |
| Frequency Inputs | [Frequency Inputs](inputs-outputs/frequency-inputs) |
| Analog Inputs | [Analog Inputs](inputs-outputs/analog-inputs) |
| Virtual Inputs | [Virtual Inputs](inputs-outputs/virtual-inputs) |
| Cameras | [Cameras](inputs-outputs/cameras) |

### Functions

Processing, timing, and data features — see [Functions](functions/).

| Item | Page |
|------|------|
| Shift Lights | [Shift Lights](functions/shift-lights) |
| Logging | [Logging](functions/logging) |
| Alarms | [Alarms](functions/alarms) |
| Counters | [Counters](functions/counters) |
| Timers | [Timers](functions/timers) |
| Conditional Logic | [Conditional Logic](functions/conditional-logic) |
| Switch Logic | [Switch Logic](functions/switch-logic) |
| Persistent Channels | [Persistent Channels](functions/persistent-channels) |
| PID Control | [PID Controllers](functions/pid-controllers) |
| Track Setup | [Track Setup](functions/track-setup) |
| Lap Timing | [Lap Timing](functions/lap-timing) |
| Drag Race Timing | [Drag Race Timing](functions/drag-race-timing) |
| Speed Fusion | [Speed Fusion](functions/speed-fusion) |
| Math | [Math Functions](functions/maths) |
| Tables | [Tables](functions/tables) |
| Odometer | [Odometer](functions/odometer) |
| IMU | [IMU](functions/imu) |
| Telemetry | [Telemetry](functions/telemetry/) |
| Voice Comms | [Voice Service](functions/telemetry/telemetry-voice) |
| Text Chat | [Text Service](functions/telemetry/telemetry-text) |

### Display

Dash layout and visual assets — see [Display Editor](display-editor/).

| Item | Page |
|------|------|
| Screen Editor | [Screen Editor](display-editor/screen-editor) |
| Layer Editor | [Layer Editor](display-editor/layer-editor) |
| Overlay Editor | [Overlay Editor](display-editor/overlay-editor) |
| Navigation | [Navigation](display-editor/navigation) |
| Images | [Images](display-editor/images) |
| Fonts | [Fonts](display-editor/fonts) |
| Media | [Media](display-editor/media) |
| Brightness Control | [Brightness Control](display-editor/brightness-control) |

### Diagnostics

| Item | Description |
|------|-------------|
| Test Functions | Manually trigger events and test outputs on a connected display |
| Live Plots | Real-time channel plotting |
| Upload Crash Report | Send a crash report to Emtron support |
| Download Debug File | Download diagnostic data from the display |

### Help

| Item | Description |
|------|-------------|
| Datasheets | Open product datasheets |
| Online Help | Open this help manual |
| Release Notes | View Display Studio release notes |

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| F4 | Write configuration to device |
| F7 | Toggle left navigation panel |
| F8 | Toggle live data drawer |
| Alt+Left / Alt+Right | Navigate back / forward |
| Ctrl+Z | Undo |
| Ctrl+Y / Ctrl+Shift+Z | Redo |
| Escape | Open the menu bar |

## Configuration Workflow

A typical configuration session follows these steps:

1. **Connect** to the display or open an existing config file.
2. **Read from Display** to pull the current configuration (or start from a template).
3. Configure **Inputs/Outputs** — CAN messages, analog and frequency inputs.
4. Set up **Functions** — shift lights, logging, lap timing, and so on.
5. Build the dash in the **Display** editor — screens, gauges, and navigation.
6. **Write to Display** to upload the configuration.
7. **Save** the configuration file for backup and future editing.

> **TIP:** Use the **Details → All** tab to search for any channel or setting across the entire configuration.