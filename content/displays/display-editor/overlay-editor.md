---
title: "Overlay Editor"
description: "Configure gauges that appear above all screens."
weight: 3
---

**Display → Overlay Editor**

Overlays are gauge layouts rendered on top of every screen. They are useful for elements that should always be visible — shift lights, warning indicators, alarm banners, or a persistent speed readout.

## Configuration

Overlays are edited like screens and layers:

1. Add gauges to the overlay canvas.
2. Position them in screen coordinates.
3. Assign channels and styling.

Because overlays render above the active screen, use a high **Z Layer** value on overlay gauges to ensure they appear in front of screen content.

## Typical Uses

- Shift light LEDs across the top of the display
- Alarm/warning icons that persist across page changes
- A compact status bar with time, lap count, or connection indicator