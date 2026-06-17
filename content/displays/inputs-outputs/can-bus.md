---
title: "CAN Bus"
description: "Configure CAN bus ports, termination, and message mapping."
weight: 1
---

**Inputs/Outputs → CAN**

The ED7 and ED10 displays support multiple CAN bus ports. Each bus can be configured independently for baud rate, termination, and message routing.

## Bus Configuration

Each CAN tab (CAN 1, CAN 2, etc.) provides:

| Setting | Description |
|---------|-------------|
| Baud Rate | Bus speed — typically 500 kbit/s or 1 Mbit/s |
| Termination | Enable the onboard 120 Ω termination resistor when this device is at the end of the bus |
| Mode | Normal operation or diagnostic listen mode |

Use the **Comms Options** panel to enable CAN diagnostic streaming, which shows raw bus traffic when a device is connected.

## Receive Messages

CAN receive entries map incoming CAN frames to channels or events:

1. Select a bus tab.
2. Add a **Receive** message definition.
3. Set the CAN ID, byte layout, and scaling.
4. Assign the output **Channel** or **Event**.

Multiple receive definitions can exist on each bus. Emtron ECUs typically transmit on standard Emtron CAN IDs — the display ships with default receive templates for Emtron Display Tx Set 1 and Set 2.

## Transmit Messages

CAN transmit entries send channel values on the bus at a configured rate:

1. Add a **Transmit** message definition.
2. Configure the CAN ID and byte packing.
3. Select the source **Channel** for each signal.

## OBD-II

OBD-II scanning is configured as a CAN client on one of the bus ports. See the [OBD-II](../functions/obd2) guide for full setup and PID configuration.

## Wiring Notes

- Use twisted pair for CAN High and Low.
- Terminate the bus with 120 Ω at each end only.
- Maximum recommended stub length is 0.3 m.

Refer to the [ED10M](datasheet-ed10m) or [ED7M](datasheet-ed7m) datasheet pinout for CAN wiring connections.