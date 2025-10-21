---
title: "OBD-II"
description: "User guide for configuring and using the OBD2 scanner module"
---
# OBD2 Scanner User Guide

## Overview

The OBD2 Scanner module provides comprehensive vehicle diagnostics and data acquisition through the On-Board Diagnostics II (OBD2) protocol. This guide covers configuration, operation, and troubleshooting.

## Table of Contents

- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Status Monitoring](#status-monitoring)
- [Supported Services](#supported-services)
- [Advanced Features](#advanced-features)
- [Troubleshooting](#troubleshooting)
- [Examples](#examples)

---

## Quick Start

### Prerequisites

- Vehicle with OBD2 port (1996+ vehicles in most regions)
- CAN bus connection to vehicle OBD2 port
- OBD2 adapter cable or direct CAN connection

### Basic Setup

1. **Enable OBD2 on CAN Bus**
   - Navigate to CAN Bus settings
   - Enable OBD2 scanner on desired CAN bus (typically `can0`)
   - Set request interval (recommended: 100-200ms for standard polling)

2. **Configure Service 0x01 (Current Data)**
   - Enable Service ID: `1` (0x01)
   - Enable PID Discovery for automatic detection
   - Add PIDs you want to monitor (see [Standard PIDs](#standard-pids))

3. **Test Connection**
   - Check **OBD2 Service Status** channel
   - Should show "Connected" when receiving data
   - Check **OBD2 Poll Rate** to verify polling frequency

---

## Configuration

### CAN Bus Settings

```
CAN Bus: can0
├── OBD2 Enabled: Yes
├── Request Interval: 100ms (adjustable 50-1000ms)
└── Services:
    └── Service 0x01 (Show Current Data)
```

### Service Configuration

Each OBD2 service (0x01, 0x09, 0x22, etc.) can be independently configured:

| Setting                | Description                    | Default                               | Notes                                    |
|------------------------|--------------------------------|---------------------------------------|------------------------------------------|
| **Enabled**            | Enable this service            | No                                    | Must be enabled to poll                  |
| **Service ID**         | OBD2 service number            | -                                     | 0x01 = Current Data, 0x09 = Vehicle Info |
| **PID Width**          | Bytes per PID                  | 1 for 0x01<br>2 for others            | Auto-detected                            |
| **Batch PID Requests** | Send multiple PIDs per request | No                                    | Only for Service 0x01                    |
| **PID Discovery**      | Auto-detect supported PIDs     | Yes                                   | Recommended for compatibility            |
| **TX Address**         | CAN transmit ID                | 0x7E0 (physical)<br>0x7DF (broadcast) | Physical for multi-PID                   |
| **RX Address Start**   | Response CAN ID range start    | 0x7E8                                 | Standard OBD2                            |
| **RX Address End**     | Response CAN ID range end      | 0x7EF                                 | Supports multiple ECUs                   |

### PID Configuration

For each PID you want to monitor:

| Setting            | Description                         | Example                |
|--------------------|-------------------------------------|------------------------|
| **Enabled**        | Poll this PID                       | Yes                    |
| **PID**            | Parameter ID                        | 0x0C = Engine RPM      |
| **Channel ID**     | Output channel                      | 60100 (custom channel) |
| **Byte Count**     | Data bytes for this PID             | 2 for RPM              |
| **Description**    | Human-readable name                 | "Engine RPM"           |
| **Decode Formula** | Math expression to convert raw data | `(A*256+B)/4`          |

---

## Status Monitoring

### Status Channels

Monitor OBD2 system health through these channels:

#### Global Status

| Channel                | Description               | Values   |
|------------------------|---------------------------|----------|
| **OBD2 Poll Rate**     | Complete polls per second | 0-100 Hz |
| **OBD2 Response Rate** | Success percentage        | 0-100%   |

#### Per-Service Status (Service 1-8)

| Channel                                     | Description              | Values                                                              |
|---------------------------------------------|--------------------------|---------------------------------------------------------------------|
| **OBD2 Service N Status**                   | Connection status        | Disabled, Connected, No Response, PID Not Supported, Response Error |
| **OBD2 Service N Response Code**            | Last error code          | 0 = OK, 0x11 = Not Supported, 0x12 = Invalid, 0x31 = Out of Range   |
| **OBD2 Service N Supported PIDs 0x00-0xE0** | Bitmap of supported PIDs | Bitfield (32-bit)                                                   |

### Status Values

```
Disabled          = 0  // Service not enabled
Connected         = 1  // Receiving valid data
No Response       = 2  // Not receiving responses (timeout after 5x poll interval)
PID Not Supported = 3  // ECU reports PID not supported
Response Error    = 4  // Other communication error
```

---

## Supported Services

### Service 0x01: Show Current Data

Real-time engine and vehicle parameters.

**Configuration:**
- PID Width: 1 byte
- Supports batch requests (up to 6 PIDs per request)
- Supports PID discovery (recommended)

**Common Use:** Engine RPM, coolant temp, throttle position, vehicle speed

### Service 0x09: Vehicle Information

Static vehicle identification data.

**Configuration:**
- PID Width: 2 bytes
- Single PID per request (no batching)
- Discovery optional

**Common Use:** VIN, calibration IDs, ECU name

### Service 0x22: Read Data By Identifier (UDS)

Manufacturer-specific extended data.

**Configuration:**
- PID Width: 2 bytes
- Single PID per request
- Discovery not typically supported

**Common Use:** Custom manufacturer parameters, advanced diagnostics

---

## Advanced Features

### Multi-PID Polling (Batch Requests)

Request multiple PIDs in a single CAN message for faster polling.

**Benefits:**
- Higher effective poll rate
- Reduced CAN bus traffic
- Lower latency

**Limitations:**
- Only Service 0x01 supports this (per SAE J1979)
- Maximum 6 PIDs per request
- Must use physical addressing (0x7E0) not broadcast (0x7DF)
- Some ECUs may not support this feature

**Configuration:**
```
Service 0x01:
├── Batch PID Requests: Yes
├── TX Address: 0x7E0 (physical addressing required)
└── PIDs: [0x0C, 0x0D, 0x05, 0x0F, 0x10, 0x11]
```

**Expected Poll Rate:**
- 6 PIDs with 100ms interval = ~10 Hz per PID
- Without batching = ~1.6 Hz per PID

### PID Discovery

Automatically detect which PIDs your vehicle supports.

**How It Works:**
1. System queries PID 0x00 (supported PIDs 0x01-0x20)
2. System queries PID 0x20 (supported PIDs 0x21-0x40)
3. Continues for PID ranges: 0x40, 0x60, 0x80, 0xA0, 0xC0
4. Only polls PIDs that are marked as supported
5. Falls back to polling all configured PIDs if discovery fails

**Benefits:**
- Faster polling (skips unsupported PIDs)
- Better compatibility
- Automatic adaptation to vehicle capabilities

**Retry Logic:**
- 3 retry attempts if discovery times out
- 2-second timeout per attempt
- Falls back to polling mode if all retries fail

### Custom Decode Formulas

Convert raw PID data to engineering units using mathematical expressions.

**Formula Variables:**
- `A` = First data byte (0-255)
- `B` = Second data byte (0-255)
- `C` = Third data byte (0-255)
- `D` = Fourth data byte (0-255)
- `E` to `H` = Additional bytes if needed

**Examples:**

```javascript
// Engine RPM (PID 0x0C, 2 bytes)
(A*256 + B) / 4

// Coolant Temperature (PID 0x05, 1 byte)
A - 40

// Throttle Position (PID 0x11, 1 byte)
A * 100 / 255

// Fuel Pressure (PID 0x0A, 1 byte, result in kPa)
A * 3

// Intake Air Temperature (PID 0x0F, 1 byte, result in °C)
A - 40

// MAF Sensor (PID 0x10, 2 bytes, result in g/s)
(A*256 + B) / 100

// O2 Sensor Voltage (PID 0x14, 2 bytes)
A / 200  // Voltage (V)
// B = Short term fuel trim (%)

// Vehicle Speed (PID 0x0D, 1 byte, result in km/h)
A

// Runtime since engine start (PID 0x1F, 2 bytes, result in seconds)
A*256 + B

// Fuel Tank Level (PID 0x2F, 1 byte, result in %)
A * 100 / 255
```

---

## Standard PIDs

### Service 0x01 Common PIDs

| PID  | Description              | Bytes | Formula          | Unit    |
|------|--------------------------|-------|------------------|---------|
| 0x00 | Supported PIDs 01-20     | 4     | -                | Bitmap  |
| 0x04 | Calculated Load          | 1     | `A*100/255`      | %       |
| 0x05 | Coolant Temp             | 1     | `A-40`           | °C      |
| 0x0A | Fuel Pressure            | 1     | `A*3`            | kPa     |
| 0x0B | Intake Manifold Pressure | 1     | `A`              | kPa     |
| 0x0C | Engine RPM               | 2     | `(A*256+B)/4`    | RPM     |
| 0x0D | Vehicle Speed            | 1     | `A`              | km/h    |
| 0x0E | Timing Advance           | 1     | `(A-128)/2`      | °       |
| 0x0F | Intake Air Temp          | 1     | `A-40`           | °C      |
| 0x10 | MAF Air Flow             | 2     | `(A*256+B)/100`  | g/s     |
| 0x11 | Throttle Position        | 1     | `A*100/255`      | %       |
| 0x1F | Runtime Since Start      | 2     | `A*256+B`        | seconds |
| 0x20 | Supported PIDs 21-40     | 4     | -                | Bitmap  |
| 0x2F | Fuel Tank Level          | 1     | `A*100/255`      | %       |
| 0x33 | Barometric Pressure      | 1     | `A`              | kPa     |
| 0x40 | Supported PIDs 41-60     | 4     | -                | Bitmap  |
| 0x42 | Control Module Voltage   | 2     | `(A*256+B)/1000` | V       |
| 0x46 | Ambient Air Temp         | 1     | `A-40`           | °C      |
| 0x5C | Engine Oil Temp          | 1     | `A-40`           | °C      |
| 0x60 | Supported PIDs 61-80     | 4     | -                | Bitmap  |

### Service 0x09 Common PIDs

| PID  | Description                         | Bytes    | Notes        |
|------|-------------------------------------|----------|--------------|
| 0x00 | Supported PIDs                      | 4        | Bitmap       |
| 0x02 | Vehicle Identification Number (VIN) | 17       | ASCII string |
| 0x04 | Calibration ID                      | Variable | ASCII string |
| 0x0A | ECU Name                            | Variable | ASCII string |

---

## Troubleshooting

### Connection Issues

#### "No Response" Status

**Symptoms:** Status shows "No Response" or never connects

**Causes:**
1. Vehicle not in RUN or ENGINE ON mode
2. Incorrect CAN bus connection
3. Wrong CAN bitrate (should be 500 kbps for OBD2)
4. CAN termination issues

**Solutions:**
1. Verify vehicle ignition is ON
2. Check physical CAN bus wiring (CAN-H and CAN-L)
3. Confirm CAN bitrate: `500 kbps` or `1 Mbps`
4. Check CAN termination (120Ω between CAN-H and CAN-L)
5. Try both physical (0x7E0) and broadcast (0x7DF) request addresses

#### "PID Not Supported" Status

**Symptoms:** Status shows "PID Not Supported" with error code 0x11 or 0x12

**Causes:**
1. Vehicle doesn't support the requested PID
2. Service not available on this vehicle/ECU
3. PID configuration error

**Solutions:**
1. Enable **PID Discovery** to auto-detect supported PIDs
2. Check vehicle OBD2 compliance level
3. Try Service 0x01 PIDs first (universal)
4. Verify PID byte count matches specification
5. Some vehicles only support basic PIDs (0x00-0x20)

#### Low Poll Rate

**Symptoms:** OBD2 Poll Rate < 1 Hz, data updates slowly

**Causes:**
1. Too many PIDs configured
2. Request interval too high
3. Multi-PID batching disabled

**Solutions:**
1. Reduce number of active PIDs
2. Decrease request interval (minimum 50ms recommended)
3. Enable **Batch PID Requests** (Service 0x01 only)
4. Use physical addressing (0x7E0) for faster responses
5. Check **OBD2 Response Rate** - should be >80%

#### Low Response Rate

**Symptoms:** OBD2 Response Rate < 80%, intermittent data

**Causes:**
1. CAN bus errors or noise
2. ECU busy with other operations
3. Too short request interval
4. Poor connection quality

**Solutions:**
1. Increase request interval (try 200ms)
2. Check CAN bus wiring quality
3. Verify CAN termination
4. Monitor CAN bus load (should be <70%)
5. Check for CAN errors in bus statistics

### Data Issues

#### Incorrect Values

**Symptoms:** Channel values don't match expected ranges

**Causes:**
1. Wrong decode formula
2. Incorrect byte count
3. Byte order mismatch

**Solutions:**
1. Verify formula against OBD2 specification
2. Check byte count matches PID definition
3. Test with known PIDs first (RPM, Speed)
4. Compare with other scan tools
5. Check formula syntax (use `A`, `B`, `C`, `D` for bytes)

#### Flickering/Unstable Values

**Symptoms:** Values jump erratically between readings

**Causes:**
1. Poll rate too high causing data race
2. Formula error causing invalid calculations
3. CAN bus errors corrupting data

**Solutions:**
1. Increase poll interval
2. Verify formula produces valid output
3. Check CAN bus quality
4. Monitor **OBD2 Response Rate** for drops

### Discovery Issues

#### Discovery Never Completes

**Symptoms:** Service stuck in "Disabled" state, never reaches "Connected"

**Causes:**
1. Discovery timeout (vehicle doesn't respond to PID 0x00)
2. Vehicle doesn't support discovery
3. Wrong service configuration

**Solutions:**
1. Wait for 3 retry attempts (6+ seconds)
2. Disable **PID Discovery** to skip auto-detection
3. Manually configure known PIDs
4. Check logs for timeout messages
5. Some vehicles require specific timing

#### Discovery Detects No PIDs

**Symptoms:** Discovery completes but no PIDs are polled

**Causes:**
1. Vehicle returned empty bitmap
2. No configured PIDs match supported PIDs
3. Discovery misinterpretation

**Solutions:**
1. Manually configure common PIDs (0x0C, 0x0D, 0x05)
2. Disable discovery and poll all configured PIDs
3. Try Service 0x01 PIDs 0x00-0x20 first
4. Check **Supported PIDs** bitmap channels for values

---

## Performance Optimization

### Maximizing Poll Rate

**Goal:** Achieve 10+ Hz poll rate for critical parameters

**Strategy:**
1. Enable **Batch PID Requests** (Service 0x01)
2. Use physical addressing (0x7E0)
3. Request only essential PIDs (6 maximum per batch)
4. Set request interval to 100ms
5. Ensure vehicle supports multi-PID requests

**Expected Results:**
- 6 PIDs @ 100ms interval = ~10 Hz per PID
- Total CAN messages = ~10/second
- Response rate should be >90%

### Minimizing CAN Bus Load

**Goal:** Reduce CAN bandwidth usage

**Strategy:**
1. Increase request interval (200-500ms)
2. Disable unused PIDs
3. Use batch requests to consolidate messages
4. Prioritize essential parameters

**CAN Load Calculation:**
```
Single PID request = 1 frame (~10 bytes @ 500kbps = ~200µs)
Response = 1-8 frames depending on data size
Total per poll = 2-9 frames

Example: 10 PIDs @ 100ms interval
= 10 requests/second × 2 frames avg = 20 frames/sec
= ~4 kbps out of 500 kbps = <1% bus load
```

### Balancing Multiple Services

**Scenario:** Monitor Service 0x01 (current data) and Service 0x09 (VIN)

**Strategy:**
```
Service 0x01:
├── Request Interval: 100ms
├── PIDs: High-frequency data (RPM, Speed, Throttle)
└── Batch Requests: Yes

Service 0x09:
├── Request Interval: 1000ms (slower)
├── PIDs: Static data (VIN, Calibration ID)
└── Batch Requests: No
```

---

## Examples

### Example 1: Basic Engine Monitoring

Monitor essential engine parameters.

**Configuration:**
```
Service 0x01:
  - Enabled: Yes
  - PID Discovery: Yes
  - Batch PID Requests: Yes
  - Request Interval: 100ms
  - TX Address: 0x7E0

PIDs:
  PID 0x0C (Engine RPM):
    - Channel ID: 60100
    - Byte Count: 2
    - Formula: (A*256+B)/4

  PID 0x0D (Vehicle Speed):
    - Channel ID: 60101
    - Byte Count: 1
    - Formula: A

  PID 0x05 (Coolant Temp):
    - Channel ID: 60102
    - Byte Count: 1
    - Formula: A-40

  PID 0x11 (Throttle Position):
    - Channel ID: 60103
    - Byte Count: 1
    - Formula: A*100/255
```

**Expected Results:**
- Poll Rate: ~10 Hz
- Response Rate: >90%
- 4 parameters updated 10 times per second

### Example 2: Performance Logging

High-speed data acquisition for track use.

**Configuration:**
```
Service 0x01:
  - Request Interval: 50ms (20 Hz)
  - Batch PID Requests: Yes
  - TX Address: 0x7E0

PIDs (6 max per batch):
  - 0x0C: Engine RPM
  - 0x0D: Vehicle Speed
  - 0x10: MAF Air Flow
  - 0x11: Throttle Position
  - 0x0F: Intake Air Temp
  - 0x0B: Intake Manifold Pressure
```

**Expected Results:**
- Poll Rate: 20 Hz
- 6 channels @ 20 Hz = 120 samples/second total
- CAN load: ~2%

### Example 3: Diagnostic Scan

Complete vehicle parameter survey.

**Configuration:**
```
Service 0x01:
  - PID Discovery: Yes
  - Request Interval: 200ms
  - Batch PID Requests: No (for maximum compatibility)
  - TX Address: 0x7DF (broadcast)

PIDs: All supported PIDs (auto-detected via discovery)

Service 0x09:
  - Request Interval: 5000ms
  - PIDs: 0x02 (VIN), 0x04 (Calibration ID)
```

**Expected Results:**
- Automatic detection of 20-40 supported PIDs
- Poll rate: 2-5 Hz depending on PID count
- VIN and calibration data refreshed every 5 seconds

### Example 4: Manufacturer-Specific (UDS)

Access extended manufacturer parameters.

**Configuration:**
```
Service 0x22 (UDS):
  - PID Width: 2
  - PID Discovery: No
  - Batch PID Requests: No
  - TX Address: 0x7E0

PIDs (manufacturer-specific examples):
  PID 0xF190:
    - Description: "Boost Pressure"
    - Channel ID: 60200
    - Byte Count: 2
    - Formula: (A*256+B)/100

  PID 0xF191:
    - Description: "Fuel Rail Pressure"
    - Channel ID: 60201
    - Byte Count: 2
    - Formula: (A*256+B)*10
```

**Note:** Manufacturer PIDs vary by make/model. Consult manufacturer documentation.

---

## Technical Reference

### CAN Message Format

**OBD2 Request (Single PID):**
```
ID: 0x7DF (broadcast) or 0x7E0 (physical)
Data: [0x02, 0x01, 0x0C, 0x00, 0x00, 0x00, 0x00, 0x00]
       │     │     │
       │     │     └─ PID (0x0C = RPM)
       │     └─────── Service (0x01)
       └───────────── Length (2 bytes)
```

**OBD2 Request (Multi-PID):**
```
ID: 0x7E0 (physical addressing required)
Data: [0x04, 0x01, 0x0C, 0x0D, 0x05, 0x00, 0x00, 0x00]
       │     │     │     │     │
       │     │     │     │     └─ PID 3 (0x05 = Coolant Temp)
       │     │     │     └─────── PID 2 (0x0D = Speed)
       │     │     └───────────── PID 1 (0x0C = RPM)
       │     └─────────────────── Service (0x01)
       └───────────────────────── Length (4 bytes)
```

**OBD2 Response:**
```
ID: 0x7E8 (or 0x7E9-0x7EF for multiple ECUs)
Data: [0x04, 0x41, 0x0C, 0x1A, 0xF8, 0x00, 0x00, 0x00]
       │     │     │     │     │
       │     │     │     └─────┴─ Data bytes (0x1AF8 = 6904 → RPM = 1726)
       │     │     └───────────── PID echo (0x0C)
       │     └─────────────────── Response mode (0x41 = 0x01 + 0x40)
       └───────────────────────── Length (4 bytes)
```

### ISO-TP Multi-Frame

For responses >7 bytes, ISO-TP (ISO 15765-2) is used:

**First Frame:**
```
[0x10, 0x14, 0x49, 0x02, 0x01, ...]
  │     │     └─────────────────── Start of data
  │     └───────────────────────── Total length (0x14 = 20 bytes)
  └─────────────────────────────── Frame type (0x1 = First Frame)
```

**Consecutive Frames:**
```
[0x21, data, data, data, ...]
  │
  └─ Sequence number (0x21 = frame 1, 0x22 = frame 2, etc.)
```

### Negative Response Codes

| Code | Description                | Meaning                          |
|------|----------------------------|----------------------------------|
| 0x11 | Service Not Supported      | ECU doesn't support this service |
| 0x12 | Sub-Function Not Supported | PID not supported                |
| 0x13 | Incorrect Message Length   | Wrong data size                  |
| 0x31 | Request Out Of Range       | PID out of valid range           |
| 0x33 | Security Access Denied     | Requires authentication          |
| 0x78 | Response Pending           | ECU busy, will respond later     |

---

## Safety and Compliance

### Legal Considerations

- **Regional Compliance:** OBD2 is mandated for vehicles sold in:
  - USA: 1996+
  - EU: 2001+ (gasoline), 2004+ (diesel)
  - Australia: 2006+
  - Other regions vary

- **Emissions Testing:** Tampering with OBD2 data may violate emissions regulations
- **Warranty:** Check vehicle warranty terms regarding aftermarket  scanning

### Best Practices

1. **Non-Intrusive:** Read-only monitoring doesn't affect vehicle operation
2. **Passive Scanning:** This module only reads data, never writes
3. **Standard Compliant:** Follows SAE J1979 and ISO 15765-2 specifications
4. **ECU Protection:** Respects timeouts and retry limits to avoid ECU overload

### Limitations

- **Manufacturer-Specific Data:** Some parameters require proprietary protocols
- **Real-Time Constraints:** Not suitable for safety-critical applications
- **CAN Bus Priority:** OBD2 messages are low priority; critical vehicle systems take precedence
- **ECU Availability:** Some ECUs may be busy and unable to respond immediately

---

## Glossary

| Term                    | Definition                                                             |
|-------------------------|------------------------------------------------------------------------|
| **ECU**                 | Electronic Control Unit - vehicle computer that manages engine/systems |
| **PID**                 | Parameter ID - specific data point (e.g., RPM, temperature)            |
| **ISO-TP**              | ISO 15765-2 Transport Protocol - multi-frame message handling          |
| **SAE J1979**           | Standard defining OBD2 diagnostic protocols                            |
| **UDS**                 | Unified Diagnostic Services (ISO 14229) - extended diagnostics         |
| **DTC**                 | Diagnostic Trouble Code - stored fault code                            |
| **Freeze Frame**        | Snapshot of parameters when fault occurred                             |
| **Bitmap**              | 32-bit field where each bit indicates support for a PID                |
| **Multi-PID**           | Requesting multiple parameters in single message                       |
| **Physical Addressing** | Direct ECU communication (0x7E0) vs broadcast (0x7DF)                  |

---

## Additional Resources

### Standards Documents

- **SAE J1979:** OBD2 Diagnostic Test Modes
- **ISO 15765-2:** Diagnostic communication over CAN
- **ISO 14229-1:** Unified Diagnostic Services (UDS)
- **SAE J2012:** Diagnostic Trouble Code Definitions

### Tools and Validation

- Use OBD2 scan tool to verify vehicle responses
- Compare results with known-good scanner
- Monitor CAN bus with analyzer to debug issues
- Test with multiple vehicles for compatibility

### Support

For additional help:
1. Check system logs for detailed error messages
2. Review CAN bus statistics for communication issues
3. Verify configuration against examples in this guide
4. Test with minimal configuration first (basic PIDs)

---

## Revision History

| Version | Date | Changes         |
|---------|------|-----------------|
| 1.0     | 2025 | Initial release |

---
