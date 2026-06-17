---
title: "Cameras"
description: "Configure camera inputs for the display."
weight: 6
---

**Inputs/Outputs → Cameras**

ED10M displays support multiple camera inputs for rear-view and auxiliary video feeds. Camera video is displayed using the [Camera Gauge](../functions/gauges#camera-gauge) on a screen.

## Configuration

| Setting | Description |
|---------|-------------|
| Power-On Input | Which camera input is shown when the display starts |

## Switching Inputs

To switch between camera inputs at runtime, trigger one of the built-in camera selection events:

- Select Camera Input 1
- Select Camera Input 2
- Select Camera Input 3
- Select Camera Input 4

These events can be sent from conditional logic, keypad mappings, or the **Test Functions** diagnostics page. The Cameras page includes test buttons to verify each input when a display is connected.

## Display

Add a **Camera Gauge** to a screen in the [Screen Editor](../display-editor/screen-editor). The gauge fills its area with the live feed from the currently selected camera input. Flip options on the gauge correct inverted camera mounting.