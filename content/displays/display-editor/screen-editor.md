---
title: "Screen Editor"
description: "Create and edit dash screens with gauges and widgets."
weight: 1
---

**Display → Screen Editor**

The Screen Editor is the primary layout tool. Each tab represents one screen (page) on the dash. Screens contain gauges positioned at specific coordinates on the display.

## Working with Screens

- **Add Screen** — create a new dash page.
- **Rename** — double-click the tab name to edit.
- **Reorder** — use the move-left and move-right buttons on each tab.
- **Export / Import** — save individual screens as `.edscreen` files to share between configs.

Toggle **Edit Statics** to switch between dynamic screens (updated every frame) and static screens (rendered once for performance).

## Adding Gauges

1. Select a screen tab.
2. Click **Add Gauge** and choose a gauge type.
3. Position and size the gauge on the preview canvas.
4. Configure properties in the panel on the right — channel assignment, colours, fonts, and type-specific settings.

Use the zoom slider to adjust the editor zoom level. The preview shows a live render when a device is connected.

## Gauge Types

All gauge types are documented in the [Gauges](../functions/gauges) reference. Common choices:

| Gauge | Purpose |
|-------|---------|
| Value | Numeric channel display |
| Dial | Rotating needle on an image |
| Bar | Horizontal or vertical fill indicator |
| Text | Static labels and titles |
| Status | Text with coloured background per value |
| Layer Group | Container that switches between sub-layers |
| Camera | Live video feed |

## Testing

Set **Test Value** on a gauge to preview how it looks with a specific channel value without needing live data. When connected, the preview updates with real channel values automatically.