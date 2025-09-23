---
title: "Emtron GPS Module"
weight: 4
draft: true
---

The Emtron GPS Module that ships with ED Series Displays communicates with the Display via RS232.

## Wiring
| Pin | Function | Notes                                 |
| --- | ---------| ------------------------------------- |
| 1   | GND      | Connect to GND. Eg: The Display's GND |
| 2   | RS232 Tx | Connect to RS232 Rx on the Display    |
| 3   | RS232 Rx | Connect to RS232 Tx on the Display    |
| 4   | +5V      | Connect to 5V supply on the Display   |

{{% badge style="warning" %}}The GPS module requires a 5V power supply. Connecting to an unregulated supply will damage the device.{{% /badge %}}

{{% badge style="info" %}}Connect Tx to Rx and vise versa, it is not a typo.{{% /badge %}}
