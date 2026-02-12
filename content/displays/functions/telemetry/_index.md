---
title: "Telemetry"
weight: 1
---

## Introduction

The Emtron telemetry system provides high speed, fully wireless telemetry services. Telemetry can connect over a 4G wireless modem or a Starlink satellite modem.

Telemetry products can be purchased from the [Emtron](https://emtron.world/) website.

### Data Service

Remote monitoring of channel and event data.

 * **Encrypted and secure** data transmission
 * Up to **64** slow channels (10Hz max)
 * Up to **64** fast channels (50Hz max)
 * Up to **50** events per second
 * **Configurable start/stop conditions** to prevent bandwidth waste

[More Info...](./telemetry-data)

### Voice Service

Voice Communications (Voice Comms) is a real-time audio communication feature that allows you to talk with other users connected to the same vehicle. Whether you're coordinating between multiple operators, communicating with remote technicians, or managing a team during testing, voice comms provides clear, direct communication with built-in priority management.

 * **Encrypted and secure** voice transmission
 * **Real-time voice calls** with other connected users
 * **Automatic speaker management** - System intelligently prioritizes speakers
 * **Push-to-Talk (PTT)** mode - Control when you transmit using a keyboard shortcut
 * **Priority levels** - Higher priority users can interrupt lower priority speakers
 * **Audio activity detection** - Know when audio is being transmitted or received

[More Info...](./telemetry-voice)

### Text Service

Text Communications is a real-time messaging feature that lets you communicate with other users who are connected to the same vehicle or session. Whether you're using the desktop application or accessing the web interface, you can send and receive messages instantly.

 * **Send and receive messages** in real-time with other connected users
 * **Automatic alerts/Quick Messages** - Send quick messages automatically triggered by system events
 * **Triggers** - The display can be configured to act on certain text message commands.
 * **View message history** - See the last messages exchanged in your session
 * **Multiple connection options** - Access the feature via desktop app or web browser

[More Info...](./telemetry-text)

---

## Quick Start

### Activation - License Server

To activate the Telemetry feature on your device, login to the [Emtron License Server](https://license.emtronaustralia.com.au).
Once logged in, from your Dashboard, click the `Activate Telemetry` button.

 * Enter the device serial number.
 * Enter the one time user Telemetry Activation code as provided after purchase.
 * Enter the *Telemetry Vehicle Name*.  This will be used in the telemetry authentication settings.
 * Enter the *Telemetry Password*.  This will be used in the telemetry authentication settings. Use a password you are comfortable sharing with team members as it is used by all software connecting to the vehicle.

Once the details have been filled out, click `Activate Now` to complete the process.

### Setup - ED7/ED10

#### Authentication

In [Display Studio](https://downloads.emtronaustralia.com.au/), the first thing to configure is the authentication settings, found in `File → Telemetry Credentials`.

| Setting                      | Description                                                 |
|------------------------------|-------------------------------------------------------------|
| **Region**                   | Select the region closest to you for lower latency          |
| **Vehicle Name**             | Exact vehicle name entered during the activation step above |
| **Password**                 | The same password entered during the activation step above  |
| **Use SSL**                  | Must be set to **true** when using official Emtron servers  |
| **Validate SSL Certificate** | Optional: Verifies server authenticity.                     |

Ensure to click `Save Telemetry Settings` as these are stored independently of the config.

#### Service Specific Setup

{{% children sort="weight" depth=2 description="false" %}}

---

## Architecture

The following diagram shows the relationships between systems for a telemetry data connection via a RUTM11 4G modem.

{{< mermaid align="center" zoom="true" >}}
erDiagram
"License Server" ||..|| "Telemetry Server": "validates credentials"
"Telemetry Server" ||..o{ "Telemetry Modem (RUTM11)" : "4G internet"
"Telemetry Modem (RUTM11)" ||--|| "Emtron Display (ED10/ED7)" : "PUB: telemetry data"
"Telemetry Server" ||..o{ "Standard Modem" : "internet"
"Standard Modem" ||--o{ "PC with EmStream" : "SUB: telemetry data"

"PC with EmStream" {
    display-name required-text-chat
    vehicle-name REQUIRED
    password REQUIRED
    region REQUIRED
}

"Emtron Display (ED10/ED7)" {
    serial-number built-in
    display-name optional
    vehicle-name REQUIRED
    password REQUIRED
    region REQUIRED
}

{{< /mermaid >}}

---