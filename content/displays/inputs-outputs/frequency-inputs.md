---
title: "Frequency Inputs"
description: "Configure wheel speed and RPM frequency inputs."
weight: 3
---

**Inputs/Outputs → Frequency Inputs**

Frequency inputs read pulse signals from speed sensors, RPM pickups, and similar sources. Each input converts pulse frequency into a channel value such as wheel speed or engine RPM.

## Configuration

Select a frequency channel from the list, then configure:

| Setting | Description |
|---------|-------------|
| Output Channel | The channel that receives the calculated value |
| Pulses Per Revolution | Number of pulses per wheel or shaft revolution |
| Digital Input | Optional digital input for direction or validity |
| Filter | Signal filtering options |

The hardware type of each input determines which pins on the display connector are used. Refer to the product datasheet for pin assignments.

## Example

Wheel speed sensors on the rear axle might be configured as two frequency inputs — one for left rear and one for right rear. These channels can then feed [Speed Fusion](../functions/speed-fusion), [Math Functions](../functions/maths), or CAN transmit messages.