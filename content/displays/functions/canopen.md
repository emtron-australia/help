---
title: "CANopen"
description: "Configure CANopen on a CAN bus: network control, nodes, PDOs, channel packing, and diagnostics"
weight: 15
---

# CANopen

CANopen is an industrial fieldbus protocol that runs on a standard CAN network. Use it when you need to exchange cyclic process data with drives, I/O modules, sensors, or other CANopen devices — for example fan controllers, valve drivers, or third-party modules that speak CANopen PDOs rather than a custom CAN message list.

## Overview

For each CAN bus you can:

1. Turn CANopen on and optionally act as **network master** (NMT).
2. Optionally produce **SYNC** and **heartbeat**.
3. Define **nodes** (devices on the bus by node address).
4. On each node, define **PDOs** (process data objects) that either **transmit** (encode channels onto the bus) or **receive** (decode bus data into channels).
5. **Export / import** the whole CANopen configuration for that bus as a `.canopen` file.

{{% badge style="info" title="Note" %}}
CANopen here is a **master-oriented process-data bridge**: NMT start, cyclic/event/sync PDOs, optional heartbeat and SYNC, and SDO support in firmware for advanced use. It is **not** a full device object dictionary editor or EDS importer.
{{% /badge %}}

### Where to find it

1. Open **Communications**.
2. Select the CAN bus you want to configure.
3. On **Settings**, enable CANopen.
4. Open the **CANOpen** tab (shown when CANopen is enabled).

---

## Bus settings (Settings tab)

These appear under the **CANOpen** heading on the bus **Settings** tab (alongside name, bit rate, and termination).

| Setting | What it does |
|---------|----------------|
| **Enable** | Turns the CANopen stack on for this bus. When off, no CANopen frames are sent or decoded on that bus. |
| **Act as Network Manager** | When on, the device acts as an **NMT master** and sends **Start Remote Node** to each enabled CANopen node after configuration is applied (and again if a heartbeat consumer times out). When off, nodes are assumed already operational (another master on the bus). |
| **SYNC Producer** | When on (and a SYNC interval is set), the device periodically sends a **SYNC** frame (CAN ID `0x080`). Use this when devices expect synchronous PDOs. |
| **SYNC Interval (ms)** | Period between SYNC frames. `0` = do not produce SYNC (even if SYNC Producer is checked). Typical values: 10–100 ms. |
| **HB Producer (ms)** | If non-zero, the device produces its own **heartbeat** at this period (milliseconds). `0` = off. |
| **HB Producer Node ID** | Node address (1–127) used for the heartbeat COB-ID (`0x700` + node ID). Must be a free address on the bus. `0` = invalid / off. |

### CAN bus basics (still required)

CANopen uses the same CAN bus settings as other traffic:

- **Bit rate** — Must match all devices (commonly 250 kbit/s, 500 kbit/s, or 1 Mbit/s).
- **Termination** — Enable bus termination only when this device is at a physical end of the bus (120 Ω).

---

## CANopen tab

With CANopen enabled, the **CANOpen** tab configures nodes and PDOs for that bus.

### Export and import

At the top of the tab:

| Button | Action |
|--------|--------|
| **Export** | Saves this bus’s full CANopen configuration to a **`.canopen`** file (enable flags, SYNC/HB, all nodes and PDOs). |
| **Import** | Loads a **`.canopen`** file into this bus, replacing the current CANopen settings for that bus only. Other CAN buses and non-CANopen settings are unchanged. |

---

## Nodes

A **node** is one CANopen device on the bus, identified by its **node address** (node-ID).

### Node list

- Lists all configured nodes.
- Labels show address and enabled state, e.g. `Node 3 [On]`.
- Drag to reorder (order is for organisation only; the bus address is what matters).
- **Add Node** creates a node with the next free address (1–127) and **Enabled** on.

### Node settings

| Setting | What it does |
|---------|----------------|
| **Enabled** | When off, this node is ignored (no NMT start, no TX/RX PDOs for it). |
| **Address (1–127)** | CANopen node-ID. Must be unique on the bus and match the device (often set by DIP switches or software). Address **0** is not used for devices (reserved for NMT broadcast). |
| **Default TX interval (ms)** | Default period for this node’s **transmit** PDOs when a PDO’s own interval is `0`. `0` here means use the system default (**100 ms**). |
| **Heartbeat consumer (ms)** | If non-zero, expect a **heartbeat** from this node at least this often. After a timeout, the stack records a timeout and, if network manager is on, sends **Start** again to that node. `0` = do not monitor. |
| **RX PDO timeout (ms)** | If non-zero, each **receive** PDO must arrive within this period or a timeout is counted. Starts counting after configuration is applied (no need for a first frame). `0` = do not monitor. |

{{% badge style="tip" title="Tip" %}}
The **CAN ID** of a PDO on the wire is not only the COB base: it is **COB base + node address**. For example, TPDO1 base `0x180` + node `5` → CAN ID **`0x185`**. The UI shows the effective ID when a PDO is selected.
{{% /badge %}}

---

## PDOs (process data objects)

PDOs are the cyclic data packets of CANopen. Each PDO belongs to a node and has a direction:

| Direction in the UI | Meaning |
|---------------------|---------|
| **Transmit (encode)** | **We send** on the bus. Values are read from **input channels**, packed into the frame, and transmitted. Use this to command a device (e.g. enable + target speed). |
| **Receive (decode)** | **We listen** on the bus. Incoming frames are unpacked into **output channels**. Use this to read status, feedback, temperatures, etc. |

### Adding PDOs

- **Add TX PDO** — Creates a transmit PDO with COB base **`0x200`** (standard RPDO1 base when you are the master writing *to* a slave).
- **Add RX PDO** — Creates a receive PDO with COB base **`0x180`** (standard TPDO1 base for data *from* a slave).

These defaults match the common predefined connection set; change the COB base if your device datasheet specifies different IDs.

### PDO settings

| Setting | What it does |
|---------|----------------|
| **COB Base (hex)** | Base COB-ID before adding the node address. Enter hex (with or without `0x`). Effective CAN ID = base + node address (7-bit). |
| **Direction** | Transmit (encode) or Receive (decode). |
| **Interval (ms)** | *(TX only)* How often to send when using **cyclic async**. `0` = use the node’s **Default TX interval**, or **100 ms** if that is also `0`. |
| **Inhibit (ms)** | *(TX only)* Minimum time between two sends of this PDO, even if interval or event would fire sooner. `0` = no extra limit. Useful to avoid flooding the bus. |
| **TX type** | *(TX only)* When the PDO is sent (see below). |

#### Transmit types

| Type in UI | Behaviour |
|------------|-----------|
| **Cyclic async (255)** | Send on a timer (interval). Most common for continuous control. |
| **Event async (254)** | Send when the encoded channel values **change** (and not more often than inhibit allows). First send happens once after enable. |
| **Sync every 1 / 10** | Send after every 1st or 10th **SYNC** frame (when a SYNC producer exists on the bus — this device or another). |

{{% badge style="note" title="Receive PDOs" %}}
Receive PDOs do not use interval / inhibit / TX type. They decode any matching frame as it arrives.
{{% /badge %}}

### Effective CAN ID

Displayed for the selected PDO:

```text
Effective CAN ID = COB Base + (Node Address & 0x7F)
```

Example:

| COB base | Node | CAN ID on the wire |
|----------|------|--------------------|
| `0x200`  | 1    | `0x201`            |
| `0x180`  | 4    | `0x184`            |
| `0x280`  | 10   | `0x28A`            |

---

## Encode (transmit mapping)

For a **TX** PDO, **encode** entries pack channel values into the 8-byte payload.

### Encode list

- One row per field in the frame.
- Label shows channel name and byte index (or “(no channel)” if unassigned).
- **Add Encode** appends a field; the next free byte index is suggested automatically when possible.

### Encode settings

| Setting | What it does |
|---------|----------------|
| **Input Channel** | Channel whose live value is packed into the frame. Leave unassigned until you choose a channel. |
| **Signed** | Treat the packed value as signed (two’s complement) when applying mask/shift. |
| **Mask (hex)** | Bits kept after scaling (e.g. `0xFF` for 8-bit, `0xFFFF` for 16-bit). |
| **Left Shift** | Shift left after mask (for packing bit fields into a byte/word). |
| **Multiplier** | Physical value is multiplied then rounded to an integer raw value. Example: frequency 50.5 with multiplier `10` → raw `505`. Must not be zero. |
| **Byte Index (0–7)** | Starting byte in the 8-byte payload (little-endian multi-byte fields). |
| **Byte Count** | Width: **1**, **2**, or **4** bytes. |

#### How encoding works (simple model)

```text
raw = round(channel_value × multiplier)
raw = (raw & mask) << left_shift
store raw in payload at byte_index for byte_count bytes (little-endian)
```

Multiple encode fields can share a byte (values are **OR**ed into the payload), which is useful for bit-packed flags.

{{% badge style="warning" title="Layout" %}}
Byte index + byte count must fit in 8 bytes (e.g. byte index 7 and count 2 is invalid and will not be written).
{{% /badge %}}

---

## Decode (receive mapping)

For an **RX** PDO, **decode** entries unpack the payload into channels.

### Decode list

Same idea as encode: list of fields with channel + byte position.

### Decode settings

| Setting | What it does |
|---------|----------------|
| **Output Channel** | Channel that receives the decoded physical value. |
| **Signed** | Sign-extend using the highest bit of the **mask**. |
| **Mask (hex)** | Bits kept after right-shift. |
| **Right Shift** | Shift right before mask (extract bit fields). |
| **Multiplier** | Physical value = raw / multiplier. Example: raw `505` with multiplier `10` → `50.5`. Must not be zero. |
| **Byte Index (0–7)** | Starting byte in the payload. |
| **Byte Count** | **1**, **2**, or **4** bytes, little-endian. |

#### How decoding works (simple model)

```text
raw = read little-endian integer at byte_index for byte_count
raw = (raw >> right_shift) & mask
if signed: sign-extend using mask width
channel_value = raw / multiplier
```

---

## Typical setup workflow

### Command a slave (master → device)

1. Enable CANopen on the correct bus; set bit rate and termination as needed.
2. Turn on **Act as Network Manager** if this unit should start the network.
3. **Add Node** with the device’s node address; keep **Enabled** on.
4. **Add TX PDO** (default base `0x200` is often correct for RPDO1).
5. Add **encode** fields for enable, setpoint, etc., matching the device manual (byte layout, scaling).
6. Optionally **Add RX PDO** (base `0x180` for TPDO1) and decode status feedback into channels.
7. Optionally set **heartbeat consumer** on the node if the device produces heartbeats.
8. Apply/send configuration and watch **CANopen Tx/Rx Count** channels and live channel values.

### Example: 16-bit scaled speed at bytes 2–3

Device expects target speed × 10 as unsigned 16-bit little-endian at bytes 2–3:

| Encode field | Value |
|--------------|--------|
| Input channel | Your target speed channel |
| Signed | Off |
| Mask | `0xFFFF` |
| Left shift | `0` |
| Multiplier | `10` |
| Byte index | `2` |
| Byte count | `2` |

---

## Status channels

Per CAN bus index (1–4), the firmware publishes counters you can log or display:

| Channel (pattern) | Meaning |
|-------------------|---------|
| **CANopen *n* Tx Count** | Number of CANopen frames transmitted on that bus instance. |
| **CANopen *n* Rx Count** | Matching CANopen frames received/processed (PDO/HB/EMCY etc., as counted by the stack). |
| **CANopen *n* Rx Timeout Count** | Timeouts: RX PDO silence, heartbeat consumer loss, or receive-queue overload. |

If TX count stays at zero: confirm CANopen **Enable**, node **Enabled**, PDO is **Transmit**, configuration has been applied to the device, and the CAN bus is online.

---

## Quick reference — COB-ID bases (predefined set)

These are industry-standard bases; many devices use them by default:

| Function | Base (hex) | Full ID |
|----------|------------|---------|
| NMT | `0x000` | Always `0x000` |
| SYNC | `0x080` | `0x080` |
| EMCY | `0x080` | `0x080` + node |
| TPDO1 (from device) | `0x180` | `0x180` + node |
| RPDO1 (to device) | `0x200` | `0x200` + node |
| TPDO2 / RPDO2 | `0x280` / `0x300` | + node |
| TPDO3 / RPDO3 | `0x380` / `0x400` | + node |
| TPDO4 / RPDO4 | `0x480` / `0x500` | + node |
| Heartbeat | `0x700` | `0x700` + node |

Always confirm against the **device manual** — some products use custom COB-IDs.

---

## Troubleshooting

| Symptom | Things to check |
|---------|------------------|
| Nothing on the bus | CANopen **Enable**; correct CAN bus and bit rate; termination; config applied to the unit. |
| TX count not increasing | Node **Enabled**; PDO direction **Transmit**; at least one encode entry (payload may still send zeros). |
| RX channels stay stale | COB base + node address match the device; byte layout and multiplier; device is operational (NMT / power). |
| Heartbeat timeouts | Consumer period longer than the device’s heartbeat producer period; correct node address; master not required for HB decode. |
| Wrong values | Multiplier direction (encode ×, decode ÷); signed vs unsigned; little-endian byte order; mask/shift. |
| Import overwrote settings | Import replaces **this bus’s CANopen section only** — re-export a known-good `.canopen` backup before experimenting. |

---

## Related

- [Channels and Events](../concepts/channels-and-events) — how channels are used across the system  
- [OBD-II](obd2) — diagnostics protocol on CAN (different from CANopen)  
- [LIN Bus](lin-bus) — another serial bus configuration page  
