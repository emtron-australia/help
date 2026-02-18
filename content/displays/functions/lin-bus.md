---
title: "LIN Bus"
description: "How to configure the LIN Bus"
---

# LIN Bus Configuration

## Overview

The LIN (Local Interconnect Network) Bus configuration allows you to define frames and signals for LIN communication. LIN is a serial communication bus commonly used in automotive systems for low-speed, cost-effective data exchange.

**Note**: Currently, master mode only is supported. The system acts as the LIN master, controlling communication with slave devices on the bus.

## Settings Tab

### Bus Configuration

- **Enabled**: Turn the LIN bus on or off
- **Baud Rate**: Set the communication speed in bits per second (e.g., 9600, 19200). Typical values are 9600 or 19200 bps

## Frames

Frames are the fundamental units of LIN communication. Each frame contains a PID (Protocol ID) and carries signals.

### Frame List

Displays all configured frames with their names and period (update interval in milliseconds). Use **Add Frame** to create a new frame, or **Import Frame** to load a previously saved frame.

### Frame Settings

Configure the following for each frame:

- **PID** (0-63): Unique identifier for the frame on the bus
- **Name**: Descriptive name for the frame (optional, helps identify frames in the list)
- **Direction**:
  - **Publish**: Master transmits, slaves receive
  - **Read**: Master receives from slaves
- **Length**: Data payload size in bytes (1-8)
- **Period**: How often the frame is transmitted (milliseconds)
- **Checksum Type**:
  - **Classic**: Standard LIN checksum
  - **Enhanced**: Extended checksum format

### Frame Diagram

Visual representation of your frame layout showing how signals are distributed across the data bytes. Each colored line represents a signal, with a legend showing signal names below the diagram.

## Signals

Each frame can contain multiple signals carrying data values.

### Signal Configuration

- **Bit Offset**: Starting bit position within the frame
- **Channel**: Which data channel this signal maps to (or "NO CHANNEL" for unused signals)
- **Type**: Data format (Integer, Float32, Float64)
- **Endianness**: Byte order
  - **Little Endian**: LSB first
  - **Big Endian**: MSB first
- **Factor**: Scaling multiplier for the raw value
- **Offset**: Value offset to apply
- **Length**: Signal width in bits

Use **Add Signal** to add signals to a frame. The **Export Frame** button at the bottom saves the current frame configuration for reuse.
