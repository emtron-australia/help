---
title: "Speed Fusion"
---

# Speed Fusion

## Overview

**Speed Fusion** combines data from multiple sensors to produce a single, accurate speed measurement that is more reliable than any individual source. It draws on GPS speed, drive speed (from the ECU or CAN bus), wheel speed sensors, and IMU data (accelerometer and gyroscope) to deliver a smooth, low-latency fused speed output.

Speed Fusion continuously monitors for wheel slip and automatically reduces the influence of any sensor that appears unreliable, such as a spinning driven wheel under hard acceleration.

### Key Features

- Combines GPS, drive speed, wheel speeds, and IMU data into a single reliable output
- Automatically detects and discounts wheel slip
- Compensates for sensor drift over time
- Works with partial sensor sets — unused inputs can be left unconfigured

---

## Configuration

### Enable / Disable

| Setting     | Description                                                              |
|-------------|--------------------------------------------------------------------------|
| **Enabled** | Turns Speed Fusion on or off. When disabled, no fused speed is produced. |

---

### Sensor Inputs

Assign each input to the channel that provides that sensor's data. Leave a channel unassigned if that sensor is not available — Speed Fusion will simply use whichever sources are connected.

| Input                         | Description                              | Units |
|-------------------------------|------------------------------------------|-------|
| **Drive Speed**               | Speed from the vehicle ECU or CAN bus    | kph   |
| **GPS Speed**                 | Speed from the GPS receiver              | kph   |
| **Front-Left Wheel Speed**    | Individual wheel speed sensor            | kph   |
| **Front-Right Wheel Speed**   | Individual wheel speed sensor            | kph   |
| **Rear-Left Wheel Speed**     | Individual wheel speed sensor            | kph   |
| **Rear-Right Wheel Speed**    | Individual wheel speed sensor            | kph   |
| **Longitudinal Acceleration** | Forward/backward acceleration from IMU   | m/s²  |
| **Vertical Acceleration**     | Up/down acceleration from IMU            | m/s²  |
| **Pitch Rate**                | Nose-up/nose-down rotation rate from IMU | °/s   |

---

### Wheel Drive Configuration

Indicate which wheels are driven (powered) by the motor. Speed Fusion prefers non-driven wheels for speed estimation because driven wheels are more likely to slip under acceleration.

| Setting                | Description                    |
|------------------------|--------------------------------|
| **Front-Left Driven**  | Enable if this wheel is driven |
| **Front-Right Driven** | Enable if this wheel is driven |
| **Rear-Left Driven**   | Enable if this wheel is driven |
| **Rear-Right Driven**  | Enable if this wheel is driven |

**Examples:**
- Front-wheel drive: enable Front-Left and Front-Right
- Rear-wheel drive: enable Rear-Left and Rear-Right
- All-wheel drive: enable all four

> When all wheels are driven, Speed Fusion still uses wheel speeds but treats them as less reliable and relies more heavily on GPS and drive speed.

---

## Tuning Parameters

These settings control how much Speed Fusion trusts each sensor source, and how aggressively it detects wheel slip. The defaults are appropriate for most vehicles — only adjust these if you observe specific problems.

### Sensor Trust

Lower values mean *more trust* in that source; higher values mean *less trust*. Think of these as a confidence level for each sensor's accuracy.

| Parameter                | Default  | Description                                                                                                             |
|--------------------------|----------|-------------------------------------------------------------------------------------------------------------------------|
| **GPS Speed Trust**      | 1.0 kph  | How much variation is expected in the GPS speed reading                                                                 |
| **Drive Speed Trust**    | 0.5 kph  | How much variation is expected in the drive speed from the ECU/CAN                                                      |
| **Wheel Speed Trust**    | 0.3 kph  | How much variation is expected in wheel speed readings                                                                  |
| **Speed Responsiveness** | 1.0 kph  | How freely the fused speed estimate can change between updates — increase if output lags, decrease if output is jittery |
| **Vertical Accel Trust** | 3.0 m/s² | How closely vertical acceleration tracks expected gravity — higher values allow more pitch angle variation              |

### Slip Detection

| Parameter                       | Default  | Description                                                                                                                                                                                                                                       |
|---------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Slip Gate**                   | 10.0 kph | Maximum allowable difference between a sensor reading and the current speed estimate before that reading is rejected. Increase if valid readings are being discarded during hard acceleration; decrease if bad readings are affecting the output. |
| **Acceleration Slip Threshold** | 3.0 m/s² | How large an acceleration mismatch between wheel sensors and the IMU must be before wheel slip is declared. Lower values detect slip earlier; higher values only flag severe slip.                                                                |

---

## Tuning Guide

### Starting Point

The defaults work well for most vehicles. Before adjusting anything, verify that all configured channels are receiving valid data and that sensor units are correct (speeds in kph, acceleration in m/s²).

### Common Adjustments

| Symptom                                                 | Adjustment                                                                             |
|---------------------------------------------------------|----------------------------------------------------------------------------------------|
| Fused speed lags behind actual speed                    | Increase **Speed Responsiveness**                                                      |
| Fused speed is jittery or noisy                         | Decrease **Speed Responsiveness**, or increase the trust value for the noisiest sensor |
| Wheel slip not being detected                           | Decrease **Acceleration Slip Threshold**                                               |
| Valid readings incorrectly rejected during acceleration | Increase **Slip Gate**                                                                 |
| GPS signal is unreliable (tunnels, urban areas)         | Increase **GPS Speed Trust** to reduce GPS influence                                   |
| Drive speed source has noticeable latency               | Increase **Drive Speed Trust** to reduce its influence                                 |

### Driving Style Adjustments

- **Street or steady-state driving** — use lower (default) responsiveness values for a smooth output
- **Motorsport / high-dynamics driving** — increase **Speed Responsiveness** to allow the estimate to change more quickly
- **Off-road or rough terrain** — increase sensor trust values to tolerate higher sensor noise

---

## Troubleshooting

| Problem                       | Likely Cause                                                   | Solution                                                                   |
|-------------------------------|----------------------------------------------------------------|----------------------------------------------------------------------------|
| No fused speed output         | Speed Fusion is disabled, or no sensor channels are configured | Enable Speed Fusion and verify at least one speed input is assigned        |
| Fused speed lags actual speed | Speed Responsiveness is too low                                | Increase **Speed Responsiveness**                                          |
| Fused speed is jittery        | Sensor trust values are too low (over-trusting noisy sensors)  | Increase trust values for noisy sources                                    |
| Wheel slip not detected       | Acceleration Slip Threshold is too high                        | Decrease **Acceleration Slip Threshold**                                   |
| Valid measurements rejected   | Slip Gate is too tight                                         | Increase **Slip Gate**                                                     |
| Pitch angle appears incorrect | IMU sensor orientation or calibration issue                    | Verify accelerometer and gyroscope channel assignments and sensor mounting |

