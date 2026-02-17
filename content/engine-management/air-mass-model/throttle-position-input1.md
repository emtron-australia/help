---
title: "Throttle Position 1"
weight: 99
---

Used primarily by the ECU for Transient Accel and Decel fueling. It can be used in 4D/5D mapping and also controls the lockout conditions for many ECU functions. 

## Clamp Settings

The available range is from -100.0 % to 100.0%, however after calibration the range should show 0.0%(closed throttle) to 100.0%(open throttle).

NOTE: The ECU does not clamp the minimum TP to 0.0% nor the maximum to 100.0%. These settings are adjustable from the Input Setup Form.

## Clamp Lo

Recommended value = -10.0%. 

## Clamp Hi

Recommended value = 105.0%. 

## Filter Settings

FIlter Setting Minimum = 0  (OFF)

FIlter Setting Maximum = 50

Recommended Filter Range = 2 - 5

## Specs

Minimum Value = -100.0 %

Maximum Value = 100.0 %

Resolution  = 0.1 %

Accuracy = +/-0.1 % 

In DBW Applications also refer to DBW Input Setup
