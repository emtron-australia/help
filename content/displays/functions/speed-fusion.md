---
title: "Speed Fusion"
hidden: true
---

# SpeedFusion Module User Manual

## Overview

The **SpeedFusion** module provides accurate, low-latency speed estimation by fusing multiple sensor inputs using an Extended Kalman Filter (EKF). It combines GPS speed, CAN bus drive speed, wheel speed sensors, accelerometers, and gyroscope data to produce a robust fused speed output that is more reliable than any single sensor.

### Key Features

- **Multi-sensor fusion** combining GPS, CAN, wheel speeds, and IMU data
- **Extended Kalman Filter** for optimal state estimation
- **Slip detection** to identify and reject unreliable wheel speed measurements
- **Automatic bias compensation** for accelerometer and gyroscope biases
- **Configurable noise parameters** for fine-tuning fusion behavior
- **Real-time processing** with minimal latency

---

## Configuration Parameters

All SpeedFusion configuration is provided through the `SpeedFusionConfig` protocol buffer message. Below is a detailed explanation of each parameter.

### 1. Sensor Input Channels

These parameters specify which channels in the system provide sensor data. Channel IDs are system-wide unique identifiers for data sources.

#### `driveSpeedChannelId` (uint32)
- **Description**: Channel ID for CAN bus drive speed measurement
- **Units**: kilometers per hour (kph)
- **Usage**: Typically sourced from the vehicle's OBD/CAN bus or custom drive controller
- **Default**: Must be specified by the user
- **Example**: Channel containing speed from vehicle ECU

#### `gpsSpeedChannelId` (uint32)
- **Description**: Channel ID for GPS-derived speed measurement
- **Units**: kilometers per hour (kph)
- **Usage**: High accuracy but potentially slower update rate (typically 1-5 Hz)
- **Default**: Must be specified by the user
- **Example**: Channel from GPS receiver module

#### `flSpeedChannelId` (uint32)
- **Description**: Channel ID for front-left wheel speed
- **Units**: kilometers per hour (kph)
- **Usage**: Used for slip detection and direct speed measurement
- **Default**: Must be specified by the user

#### `frSpeedChannelId` (uint32)
- **Description**: Channel ID for front-right wheel speed
- **Units**: kilometers per hour (kph)

#### `rlSpeedChannelId` (uint32)
- **Description**: Channel ID for rear-left wheel speed
- **Units**: kilometers per hour (kph)

#### `rrSpeedChannelId` (uint32)
- **Description**: Channel ID for rear-right wheel speed
- **Units**: kilometers per hour (kph)

### 2. Wheel Configuration

These boolean flags indicate which wheels are driven (powered) by the vehicle's motor.

#### `flDriven`, `frDriven`, `rlDriven`, `rrDriven` (bool)
- **Description**: Indicates whether each wheel is driven/powered by the motor
- **Default**: `false`
- **Impact**: The algorithm preferentially uses non-driven wheel speeds for speed estimation, as driven wheels may slip during acceleration. If all wheels are marked as driven, all wheels are used but with higher measurement noise (100x multiplier).
- **Example Configuration**:
  - Front-wheel drive vehicle: `flDriven=true, frDriven=true, rlDriven=false, rrDriven=false`
  - Rear-wheel drive vehicle: `flDriven=false, frDriven=false, rlDriven=true, rrDriven=true`

### 3. IMU Sensor Channels

These channels provide inertial measurement unit (accelerometer and gyroscope) data for attitude estimation and vertical constraint checks.

#### `longitudinalAccelChannelId` (uint32)
- **Description**: Channel ID for longitudinal (forward/backward) acceleration
- **Units**: meters per second squared (m/s²)
- **Usage**: Used to model horizontal acceleration and as a constraint in the Kalman filter
- **Range**: Typically -20 to +20 m/s²
- **Note**: This is fused with wheel speed to estimate and correct accelerometer bias

#### `verticalAccelChannelId` (uint32)
- **Description**: Channel ID for vertical (up/down) acceleration
- **Units**: meters per second squared (m/s²)
- **Usage**: Used to estimate vehicle pitch angle and as a pseudo-measurement constraint
- **Range**: Typically 8 to 12 m/s² (9.81 is gravity at rest)

#### `pitchAngularRateChannelId` (uint32)
- **Description**: Channel ID for pitch angular rate (rotation around lateral axis)
- **Units**: degrees per second (°/s)
- **Usage**: Directly updates pitch angle state in the Kalman filter
- **Conversion**: Internally converted to radians per second for processing

---

## Noise and Uncertainty Parameters

The Extended Kalman Filter uses these parameters to weight different measurements and model system uncertainties. Lower values indicate greater confidence in a measurement or process model.

### Process Noise Parameters

Process noise describes the algorithm's belief in how accurately it can predict state evolution between measurements.

#### `sigmaV` (double)
- **Description**: Process noise standard deviation for horizontal speed
- **Units**: kilometers per hour (kph)
- **Default**: 1.0 kph
- **Range**: 0.1 - 5.0 kph (typical)
- **Impact**: Higher values allow the estimated speed to change more freely between measurements
- **Tuning**: Increase if the filter lags behind actual speed changes; decrease if the estimate is too noisy

#### `sigmaTheta` (double)
- **Description**: Process noise standard deviation for pitch angle
- **Units**: radians
- **Default**: 0.05 rad (≈ 2.9°)
- **Range**: 0.01 - 0.2 rad
- **Impact**: Controls how quickly the estimated pitch angle can change
- **Tuning**: Adjust based on vehicle suspension characteristics and gyro reliability

#### `sigmaBa` (double)
- **Description**: Process noise standard deviation for accelerometer bias
- **Units**: meters per second squared (m/s²)
- **Default**: 0.1 m/s²
- **Range**: 0.01 - 0.5 m/s²
- **Impact**: Controls how quickly the algorithm can adapt to accelerometer drift
- **Tuning**: Higher values if accelerometer bias changes rapidly; lower for stable accelerometers

#### `sigmaBg` (double)
- **Description**: Process noise standard deviation for gyroscope bias
- **Units**: radians per second (rad/s)
- **Default**: 0.001 rad/s
- **Range**: 0.0001 - 0.01 rad/s
- **Impact**: Controls adaptation to gyroscope drift
- **Tuning**: Adjust based on gyroscope quality and thermal drift characteristics

### Measurement Noise Parameters

Measurement noise describes the algorithm's belief in the accuracy of each measurement source.

#### `sigmaGps` (double)
- **Description**: Measurement noise standard deviation for GPS speed
- **Units**: kilometers per hour (kph)
- **Default**: 1.0 kph
- **Range**: 0.5 - 5.0 kph
- **Impact**: Lower values give GPS measurements more influence on the fused speed
- **Tuning**:
  - Increase if GPS jumps around or has poor signal (urban canyon)
  - Decrease if GPS is the most reliable source available

#### `sigmaCan` (double)
- **Description**: Measurement noise standard deviation for CAN bus drive speed
- **Units**: kilometers per hour (kph)
- **Default**: 0.5 kph
- **Range**: 0.1 - 2.0 kph
- **Impact**: Controls the influence of CAN drive speed on the fused estimate
- **Note**: Dynamically increased by 100x if the innovation (error) exceeds `slipGate`
- **Tuning**: Adjust based on how much the drive speed measurement drifts at constant speed

#### `sigmaWheel` (double)
- **Description**: Measurement noise standard deviation for wheel speeds
- **Units**: kilometers per hour (kph)
- **Default**: 0.3 kph
- **Range**: 0.1 - 1.0 kph
- **Impact**: Controls the influence of wheel speed measurements
- **Tuning**: Lower values trust wheel speeds more; increase if wheels slip frequently

#### `sigmaVert` (double)
- **Description**: Measurement noise standard deviation for the vertical pseudo-measurement
- **Units**: meters per second squared (m/s²)
- **Default**: 3.0 m/s²
- **Range**: 1.0 - 10.0 m/s²
- **Impact**: Controls how strongly the constraint from vertical acceleration influences pitch angle estimation
- **Technical**: Uses gravity (9.81 m/s²) as a reference to constrain pitch angle
- **Tuning**: Higher values = looser constraint; lower values = tighter constraint to gravity

---

## Slip Detection and Gating Parameters

These parameters control how the algorithm detects and rejects unreliable measurements caused by wheel slip.

#### `slipGate` (double)
- **Description**: Innovation gate for slip rejection (threshold for all speed measurements)
- **Units**: kilometers per hour (kph)
- **Default**: 10.0 kph
- **Range**: 3.0 - 20.0 kph
- **Impact**: If the difference between measured speed and estimated speed exceeds this threshold, the measurement is rejected
- **Use Cases**:
  - Tighter gate (3-5 kph) for accurate speed sources with low noise
  - Looser gate (15-20 kph) for noisy sensors or high-dynamics scenarios
- **Tuning Guide**:
  - Increase if valid measurements are being rejected during hard acceleration
  - Decrease if erroneous measurements are affecting the estimate

#### `accelSlipThresh` (double)
- **Description**: Acceleration mismatch threshold for wheel slip detection
- **Units**: meters per second squared (m/s²)
- **Default**: 3.0 m/s²
- **Range**: 1.0 - 10.0 m/s²
- **Impact**: Detects wheel slip by comparing acceleration derived from wheel speeds to acceleration from IMU
- **Algorithm**: If $|\text{wheel\_accel} - \text{imu\_accel}| > \text{accelSlipThresh}$, wheel slip is detected
- **Consequence of Detection**: When slip is detected, the measurement noise for wheel speeds is multiplied by 100, effectively deweighting them
- **Tuning Guide**:
  - Lower values = more sensitive to slip detection
  - Higher values = only detect severe slip; useful if sensor calibration is poor

---

## Enable/Disable

#### `enabled` (bool)
- **Description**: Master enable/disable flag for the SpeedFusion module
- **Default**: `false`
- **Effect**:
  - When `enabled=false`: Module outputs NaN for fused speed
  - When `enabled=true`: Module processes measurements and produces fused speed estimate
- **Usage**: Use to turn off fusion during system startup, testing, or when reliability is uncertain

---

## Configuration Examples

### Example 1: Street Car with GPS and CAN Speed

```protobuf
SpeedFusionConfig {
  enabled: true

  // Sensor channels
  driveSpeedChannelId: 1001           // From vehicle CAN bus
  gpsSpeedChannelId: 1002             // From GPS module
  flSpeedChannelId: 1003
  frSpeedChannelId: 1004
  rlSpeedChannelId: 1005
  rrSpeedChannelId: 1006

  // IMU channels
  longitudinalAccelChannelId: 1007
  verticalAccelChannelId: 1008
  pitchAngularRateChannelId: 1009

  // Wheel drive configuration (front-wheel drive)
  flDriven: true
  frDriven: true
  rlDriven: false
  rrDriven: false

  // Moderate noise settings for typical automotive environment
  sigmaV: 0.5            // Trust speed estimates well
  sigmaTheta: 0.05       // Moderate pitch dynamics
  sigmaBa: 0.1
  sigmaBg: 0.001
  sigmaGps: 1.0          // GPS may have some noise
  sigmaCan: 0.3          // CAN is fairly reliable
  sigmaWheel: 0.5        // Wheel speeds can slip
  sigmaVert: 3.0

  slipGate: 8.0          // Moderate slip tolerance
  accelSlipThresh: 3.0
}
```

### Example 2: Track Testing with High Dynamics

```protobuf
SpeedFusionConfig {
  enabled: true

  // Same sensor channels as above
  driveSpeedChannelId: 1001
  gpsSpeedChannelId: 1002
  flSpeedChannelId: 1003
  frSpeedChannelId: 1004
  rlSpeedChannelId: 1005
  rrSpeedChannelId: 1006
  longitudinalAccelChannelId: 1007
  verticalAccelChannelId: 1008
  pitchAngularRateChannelId: 1009

  // Rear-wheel drive, both rear wheels driven
  flDriven: false
  frDriven: false
  rlDriven: true
  rrDriven: true

  // Aggressive tuning for high-dynamics
  sigmaV: 2.0            // Allow speed to change quickly
  sigmaTheta: 0.1        // More aggressive pitch dynamics
  sigmaBa: 0.2           // Accelerometer bias changes faster
  sigmaBg: 0.002
  sigmaGps: 2.0          // GPS less trusted at high speeds
  sigmaCan: 1.0          // CAN may be noisy at extremes
  sigmaWheel: 2.0        // Expect significant slip
  sigmaVert: 5.0         // Looser vertical constraint

  slipGate: 15.0         // More permissive slip tolerance
  accelSlipThresh: 5.0   // Only reject obvious slip
}
```

### Example 3: Low-Latency Wheel-Speed-Only System

```protobuf
SpeedFusionConfig {
  enabled: true

  // Focus on wheel speeds
  driveSpeedChannelId: 0              // Not used
  gpsSpeedChannelId: 0                // Not used
  flSpeedChannelId: 1003
  frSpeedChannelId: 1004
  rlSpeedChannelId: 1005
  rrSpeedChannelId: 1006
  longitudinalAccelChannelId: 1007
  verticalAccelChannelId: 1008
  pitchAngularRateChannelId: 1009

  // AWD configuration
  flDriven: true
  frDriven: true
  rlDriven: true
  rrDriven: true

  // Conservative tuning for wheel-speed only
  sigmaV: 0.5
  sigmaTheta: 0.05
  sigmaBa: 0.1
  sigmaBg: 0.001
  sigmaGps: 10.0         // GPS ignored (high noise)
  sigmaCan: 10.0         // CAN ignored (high noise)
  sigmaWheel: 0.2        // Wheel speeds are primary source
  sigmaVert: 3.0

  slipGate: 5.0
  accelSlipThresh: 2.0   // Sensitive slip detection
}
```

---

## Tuning Guide

### Step 1: Verify Channel Configuration

Ensure all channel IDs point to valid, active data sources:
- Use monitoring tools to confirm channels are receiving data
- Check units match the algorithm's expectations (kph for speeds, m/s² for acceleration)
- Verify IMU data ranges are reasonable (vertical accel ~9.81 m/s² at rest)

### Step 2: Start with Defaults

The default parameters in `ConfigUpdated()` are conservative and should work for most vehicles:
- `sigmaV=1.0, sigmaTheta=0.05, sigmaBa=0.1, sigmaBg=0.001`
- `sigmaGps=1.0, sigmaCan=0.5, sigmaWheel=0.3, sigmaVert=3.0`
- `slipGate=10.0, accelSlipThresh=3.0`

### Step 3: Monitor Fusion Performance

Key metrics to observe:
- **Fused Speed Lag**: Is the output lagging behind actual speed changes? → Increase `sigmaV`
- **Fused Speed Noise**: Is the output too jittery? → Decrease `sigmaV` or increase measurement noise
- **Pitch Angle Accuracy**: Does the pitch estimate match expected vehicle dynamics? → Tune `sigmaTheta`
- **Slip Rejection**: Are valid measurements rejected? → Increase `slipGate`; Are invalid measurements accepted? → Decrease `slipGate`

### Step 4: Sensor-Specific Tuning

- **More confident in GPS**: Decrease `sigmaGps` (e.g., 0.5)
- **GPS unreliable**: Increase `sigmaGps` (e.g., 2.0-3.0)
- **Wheel speeds drift**: Increase `sigmaWheel` or `accelSlipThresh`
- **CAN speed has latency**: Increase `sigmaCan` to give it less influence
- **Accelerometer drift**: Increase `sigmaBa` to allow faster bias correction

### Step 5: Dynamics-Specific Tuning

- **Steady-state driving**: Use conservative (small) process noise values
- **High-performance driving**: Increase process noise values to allow faster state changes
- **Off-road/rough terrain**: Increase all measurement noise values to handle sensor noise

---

## Algorithm Overview

### State Vector

The SpeedFusion algorithm maintains a 5-element state vector:

$$\mathbf{x} = \begin{bmatrix} v_h \\ \theta \\ b_{a,x} \\ b_{a,z} \\ b_g \end{bmatrix}$$

Where:
- $v_h$: Horizontal speed (kph)
- $\theta$: Pitch angle (radians)
- $b_{a,x}$: Longitudinal accelerometer bias (m/s²)
- $b_{a,z}$: Vertical accelerometer bias (m/s²)
- $b_g$: Gyroscope bias (rad/s)

### Kalman Filter Cycle

1. **Prediction**: Uses IMU data to predict state and covariance
   - Speed prediction: $v_h \leftarrow v_h + \Delta t \cdot a_h \cdot 3.6$
   - Pitch prediction: $\theta \leftarrow \theta + \Delta t \cdot (\omega - b_g)$

2. **Correction**: Updates estimates using available measurements
   - Speed measurements (GPS, CAN, Wheels) applied via linear measurement model
   - Vertical acceleration as pseudo-measurement to constrain pitch

3. **Slip Detection**: Rejects measurements inconsistent with IMU acceleration

### Output

The algorithm outputs the estimated horizontal speed to `IdFusedSpeed` channel, clamped to non-negative values.

---

## Troubleshooting

| Problem                       | Cause                                     | Solution                                                  |
|-------------------------------|-------------------------------------------|-----------------------------------------------------------|
| Fused speed is NaN            | Module disabled or invalid channel data   | Enable module; verify all channels have valid data        |
| Fused speed lags actual speed | Too much confidence in smooth estimates   | Increase `sigmaV` and/or `sigmaWheel`                     |
| Fused speed is jittery        | Too little confidence in estimates        | Decrease `sigmaV`; increase measurement noise values      |
| Wheel slip not detected       | `accelSlipThresh` too high                | Decrease threshold or improve accelerometer calibration   |
| Valid measurements rejected   | `slipGate` too tight                      | Increase `slipGate`; check measurement noise calibration  |
| Pitch angle incorrect         | Poor IMU calibration or wrong orientation | Verify accelerometer/gyroscope alignment and zero offsets |

---

## Integration Notes

- The module processes measurements at the call rate of `Update()` (typically 50-100 Hz)
- All sensor channels are read once per update cycle; missing data is handled gracefully
- Initial covariance is set to high values to allow rapid convergence to correct state
- The algorithm is designed to be robust to sensor delays and missing measurements

---

## References

- Extended Kalman Filter theory
- Vehicle dynamics and pitch angle estimation
- GPS/INS integrated navigation
- Wheel slip detection algorithms

