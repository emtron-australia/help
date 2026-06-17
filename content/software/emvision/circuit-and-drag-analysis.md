---
title: "Circuit and Drag Analysis"
description: "Circuit lap analysis and drag strip distance markers."
weight: 9
---

## Circuit / Drag Mode

The mode button in the title bar controls how EmVision interprets race milestones and distance markers:

| Mode | Description |
|------|-------------|
| Auto (Circuit) | Automatically detected circuit racing — lap and sector markers from GPS |
| Auto (Drag) | Automatically detected drag racing — distance-based markers |
| Forced (Circuit) | Override auto-detection; treat as circuit |
| Forced (Drag) | Override auto-detection; treat as drag |
| Auto (None) | No automatic milestone detection |

Click the button to cycle through modes. Use forced modes when auto-detection picks the wrong type for your log.

## Speed Channels

Configure the speed channels used for distance integration in [Settings](settings):

| Setting | Purpose |
|---------|---------|
| Circuit Speed Channel | Speed source for circuit distance calculation |
| Drag Speed Channel | Speed source for drag distance markers |
| Drag Event Trigger Channel | Channel that triggers drag event generation |

## Drag Distance Markers

The **Tools** menu provides drag strip analysis functions. These place distance markers (60 ft, 330 ft, 660 ft, 1320 ft, etc.) on the log timeline.

### Generate from Cursor

**Tools → Generate drag distance markers from cursor**

Places markers at standard drag strip distances, calculated forward from the current cursor position using the drag speed channel.

### Generate from Trigger Channel

**Tools → Generate drag distance markers from trigger channel**

Automatically places markers when the configured trigger channel meets its threshold — useful for batch-processing multiple runs in a single log.

### Clear Markers

**Tools → Clear drag distance markers on selected section**

Removes all drag distance markers from the currently selected log section (reference or overlay).

> **Note:** Drag tools require distance data in the log. If the log has no distance channel, the Tools menu items are disabled.