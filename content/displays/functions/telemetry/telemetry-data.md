---
title: "Data Service"
weight: 1
description: "Real-time cloud-based data streaming platform enabling vehicles to broadcast live sensor and performance data to authorized users"
---

## Quick Start

### Telemetry Provider vs Telemetry Consumer ###

**Telemetry Provider** is the standard operating mode for most applications and is the subject of this help topic.

**Telemetry Consumer** is for advanced usage and should be `DISABLED` for a standard telemetry setup.

### Setup: ED7/ED10

Assuming you have an active telemetry license and the [authentication settings](telemetry#authentication) configured in Display Studio, you can now configure the telemetry function.

#### Settings

Telemetry data settings can be accessed from the main menu: `Functions → Telemetry`. Ensure the `Telemetry Provider` tab is selected.

| Setting                   | Description                                                            |
|---------------------------|------------------------------------------------------------------------|
| **Enable**                | Globally activate/deactivate telemetry streaming                       |
| **Data Mode**             | Always set to compressed                                               |
| **Active When**           | When the conditions are met, data will begin streaming. e.g. RPM > 300 |
| **Slow Tx Rate**          | Transmission Rate of the slow data set                                 |
| **Fast Tx Rate**          | Transmission Rate of the fast data set                                 |
| **Transmit Events**       | Enable to send all system events over telemetry                        |
| **Channel Configuration** | Allocate channels you want to be sent in the appropriate group         |

**Best practice:** Only include channels you actually monitor. Unnecessary channels waste bandwidth.

Once configured, 'Write' the config.

#### Functions

| Function                    | Description                                                       |
|-----------------------------|-------------------------------------------------------------------|
| **Export Telemetry Config** | Exports (excluding authentication) telemetry settings to a file   |
| **Import Telemetry Config** | Imports (excluding authentication) telemetry settings from a file |

#### Channels

The following channels are available to monitor the status of the system.

| Channel                                    | Description                                          |
|--------------------------------------------|------------------------------------------------------|
| Telemetry Provider Status                  | The connection status to the telemetry server        |
| Telemetry Provider Error                   | The reason for connection failure on error           |
| Telemetry Provider Raw Tx Bandwidth        | The current uncompressed bandwidth being transmitted |
| Telemetry Provider Compressed Tx Bandwidth | The current compressed bandwidth being transmitted   |
| Telemetry Provider Compression Ratio       | The ratio of compressed to decompressed data         |

**Important:** The connection status is the status of connection to the telemetry server. It doesn't know if EmStream is receiving data.

### Setup: EmStream

EmStream stores authentication information per service type rather than in one place for flexibility.

The data service settings can be found in `File → Connection Settings`.

| Setting          | Description                                                                      |
|------------------|----------------------------------------------------------------------------------|
| **Host**         | Enter the host from the below table based on the region configured in the device |
| **Vehicle Name** | Exact vehicle name entered during the activation step above                      |
| **Password**     | The same password entered during the activation step above                       |
| **Use SSL**      | Must be set to **true** when using official Emtron servers                       |

| Region        | Host                                   |
|---------------|----------------------------------------|
| Australia     | `telemetry-aus.emtronaustralia.com.au` |
| North America | `telemetry-usa.emtronaustralia.com.au` |

Once entered, select `Connect` to connect to the telemetry server. If an Emtron Display is also connected you should start seeing channel data on the
right hand side panel showing with `Telemetry Connected` in the top right hand corner.

If connection fails, the reason will be shown in the `Connection Settings` popup.