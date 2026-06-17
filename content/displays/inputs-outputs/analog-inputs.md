---
title: "Analog Inputs"
description: "Configure voltage, resistance, and digital analog inputs."
weight: 4
---

**Inputs/Outputs → Analog Inputs**

Analog inputs read voltage or resistance signals from sensors such as pressure transducers, temperature senders, and potentiometers.

## Input Types

Each analog channel supports one of three types:

| Type | Use Case |
|------|----------|
| Voltage | 0–5 V sensors, MAP sensors, TPS |
| Resistance | NTC temperature sensors, resistance-based senders |
| Digital | Switched inputs read as on/off |

## Hardware Options

Depending on the physical input, additional hardware options may be available:

| Option | Description |
|--------|-------------|
| Internal Pull-up | Enable the onboard pull-up resistor for resistance measurements |
| Extended Range | Use the extended voltage divider for signals above 5 V |

## Calibration

Resistance and voltage inputs support calibration tables to convert the raw reading into engineering units. Configure the calibration curve to match your sensor's characteristics.

Assign each configured input to an **Output Channel** so that functions, gauges, and logging can use the sensor value.