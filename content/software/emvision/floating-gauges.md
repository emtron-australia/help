---
title: "Floating Gauges"
description: "Overlay gauges on top of the analysis view."
weight: 10
---

**Workspace → Add Floating Gauge**

Floating gauges are draggable, resizable gauge overlays that sit above all plot content. They show a channel value at the current cursor position and persist within the workspace.

## Gauge Types

| Type | Display |
|------|---------|
| Bar | Horizontal or vertical bar fill |
| Radial | Circular arc gauge |
| Steering Wheel | Rotating wheel indicator |
| Force | Force vector display |

## Configuration

Double-click a floating gauge to open its setup dialog:

| Setting | Description |
|---------|-------------|
| Channel | Source channel to display |
| Gauge Type | Bar, radial, steering wheel, or force |
| Direction | Fill direction (left-to-right, top-to-bottom, etc.) |
| Min / Max | Value range for the gauge scale |
| Color Bands | Threshold bands with custom colours |

## Managing Gauges

- **Drag** to reposition a gauge anywhere on screen
- **Resize** using the corner handle
- **Delete** from the setup dialog
- Gauges are saved with the workspace and restored when switching back

Floating gauges are useful for keeping a speed, RPM, or pressure readout visible while working with detailed line plots.