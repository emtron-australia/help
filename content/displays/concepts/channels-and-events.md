---
title: "Channels and Events"
description: "Explains the fundamental concepts of channels and events."
---

This page outlines the core concepts of channels and events, which are essential for data communication within the system.

## Definitions

### Channels

Channels represent a single piece of dynamic data, serving as the primary communication method within the system. They facilitate data transmission between inputs, functions, and outputs, holding either numerical values or text strings. Channels are ideal for representing sensor readings, user inputs, intermediate values, or other dynamic data that requires processing or display.

The system includes a wide range of built-in channels for common use cases. Using these predefined channels is recommended, as they ensure compatibility across Emtron displays, enabling seamless mapping during configuration imports. If no suitable built-in channel exists, custom channels can be created.

Examples: `Engine Speed`, `Manifold Pressure` and `Engine Temperature`

#### Custom Channels

Custom channels allow you to define named channels tailored to specific use cases. However, when importing or exporting sub-configurations with custom channels, compatibility issues may arise with other base configurations. Reconfiguring or remapping channels is often necessary in such cases.

> TIP: If a commonly used channel is missing from the predefined list, contact Emtron support to request its addition.

#### Units

Channels use predefined metric units wherever applicable. The system operates internally in metric units.

The channel preference system allows you to change display units (e.g., from meters to feet) at the point of display. The system automatically handles conversions between compatible units of the same type.

### Events

Events signal specific occurrences within the system, enabling different components to communicate and respond to changes. Unlike channels, which represent continuous data, events are discrete and occur at a specific point in time.

Examples `Engine Start`, `Lap Beacon` and `Keypad Press 1`

Custom events can be created the same as [custom channels](#custom-channels)

## Concepts

### Coupling

The channel and event system enables communication between various system functions without requiring direct knowledge of each other. This design offers maximum flexibility, allowing functions to interact in any desired configuration.

However, be mindful of the following:

 * Avoid writing to a channel from multiple sources, as this can cause conflicts.
 * Tracking the source of a channel's value can be challenging.

The flexibility provided by this system outweighs these potential drawbacks for a highly configurable product.

### Inputs

Inputs receive channel values or events. For example, a gauge on a display can be an input that reflects a channel's value. Channels and events can be mapped to configurable inputs across various system functions, and a single channel or event can be mapped to multiple input functions as needed.

### Outputs

Outputs write data to channels or events. Key distinctions between channels and events as outputs include:

 * A channel can only be written to by a single function to avoid conflicts, which could lead to erratic behavior. The system cannot detect this error.
 * An event can be triggered by multiple functions without issue, as events are discrete and do not hold continuous values.

### Chaining

Functions can be chained together to perform more complex processing tasks.

It is important a unique channel is used between each function.

{{< mermaid align="center" >}}
graph LR;
  A[Example Input] -- Channel Value A --> B(Math Function)
  B -- Scaled Value A --> C(Table Function)
  C -- Scaled Value B --> D(Table Function)
  D -- Scaled Value C --> E(Example Output)
{{< /mermaid >}}

> Note: Each level of chaining can add between 0 and 10ms of processing delay.

## Examples

The following are contrived examples to demonstrate what is possible.

### Averaging frequency inputs then sending on CAN

This uses the [math function](../functions/maths) to average two channels before spitting them out on the CAN bus.

{{< mermaid align="center" >}}
graph LR;
  A[Frequency Input 1] -- Wheel Speed Left Rear --> C(Math Function)
  B[Frequency Input 2] -- Wheel Speed Right Rear --> C
  C -- Wheel Speed Average Rear --> D(CAN0 Tx)
{{< /mermaid >}}

> Note: As channels can be assigned to multiple inputs, `Wheel Speed Right Rear` could also be assigned to a gauge on the display, or recorded by the data logging system.

### Potentiometer and engine temperature controlled shift point adjustment

Unlikely in real life, but demonstrates combining data from different sources, using a table to scale, then outputting the result.

This uses the [table function](../functions/tables) to combine the potentiometer and engine temperature to select a shift point which is fed into the [shift pattern](../functions/shift-lights).

{{< mermaid align="center" >}}
graph LR;
  A[CAN0 Rx] -- Engine Speed --> C(Table Function)
  A[CAN0 Rx] -- Engine Temperature --> C(Table Function)
  B[Analog Input] -- Shift Adjust --> C(Table Function)
  C(Table Function) -- Shift Level --> D(Shift Light)
{{< /mermaid >}}

By default the shift system uses a gear based calculation. This steps around this and uses a table to combine engine temperature and a user setting.