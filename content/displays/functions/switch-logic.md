---
title: "Switch Logic"
description: "How to configure the switching input logic on the device"
---

Switch Inputs allow any input channel to be used for binary switch logic. The output is either 0 when inactive/off or 1 when active/on.

### Input Channel:
The channel used as the input value source.

### Output Channel:
The channel that contains the final result of the switch logic.

### Detection Mode:
Determines the switches behaviour.
 - **Active Low:** Transitions to ON when the input is less than or equal to `Low Threshold`. Does not transition back to OFF until the input is greater than or equal to `High Threshold`. *Typical use: Low side switch.*
 - **Active High:** Transitions to ON when the input is greater or equal to than `High Threshold`. Does not transition back to OFF until the input is less than or equal to `Low Threshold`. *Typical use: High side switch.*
 - **Active Inside Range:** Transitions to ON while the input is greater than or equal to `Low Threshold` AND the input is less than or equal to `High Threshold`. *Typical use: Voltage ladder switches such cruise control buttons or other steering wheel controls.*
 - **Active Outside Range:** Transitions to ON while the input is less than or equal to `Low Threshold` AND the input is greater than or equal to `High Threshold`. *Typical use: Inverse voltage ladder. Can determine when single position is not pressed.*

> Note: `Toggle` mode will alter the behaviour described here. See below...*


### High Threshold
Input comparison high value. Used by all `Detection Modes`.
*Must be greater than `Low Threshold`.*

### Low Threshold
Input comparison low value. Used by all `Detection Modes`.
*Must be less than `High Threshold`.*

### Range Hysteresis
Hysteresis value used on both the `Low Threshold` and `High Threshold` boundaries.
Only applies to Detection Modes `Active Inside Range` and `Active Outside Range`.

**Active Inside Range:** The switch will turn ON when the input is inside the threshold boundaries. In order to turn off, the input must be less than `Low Threshold` - `Range Hysteresis` OR greater than `High Threshold` + `Range Hysteresis`. The activation window is effectively widend when in the ON state.

**Active Inside Range:** The switch will turn ON when the input is outside the threshold boundaries. In order to turn off, the input must be greater than `Low Threshold` + `Range Hysteresis` AND less than `High Threshold` - `Range Hysteresis`. The activation windows are effectively widend when in the ON state.

### Toggle
Alters the behaviour of the output. When the input detection is determined to be in the ON state, rather than following that state, the output value will toggle from OFF to ON and ON to OFF with each successive transition. This allows a momentary switch or keypad button to toggle (latch) each time it is pressed.

### Invert
Inverts the output result. OFF becomes ON and ON becomes OFF.
