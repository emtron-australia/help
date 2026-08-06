---
title: "Constants"
description: "Named sections of fixed channel values used by maths, gauges, and logs."
weight: 1
---

**Setup → Constants**

Constants are fixed values published as channels on the display. Use them for car- or session-specific numbers that functions, gauges, and maths need — for example tyre circumference, gear ratios, or driver preferences — without hard-coding those values into each feature.

Constants are part of the configuration file. They are also written into every onboard log so analysis tools can use the same values that were active during the run.

## Sections

Constants are organised into **sections** (for example *Car*, *Driver*, or *Event*).

1. Open **Setup → Constants**.
2. Use **New section** to add a section, and rename it as needed.
3. Select a section, then add channels and set each **value**.
4. Drag sections or entries to reorder them.

Each entry picks a **channel** and an explicit value for that channel. Only one constant should write a given channel.

## Import and export

| Action | Behaviour |
|--------|-----------|
| **Export** | Saves the current constants as YAML (compatible with EmVision session constants). |
| **Import** | **Merges** by section name — you can load several files (e.g. car + driver). Matching section names combine; new sections are added. |
| **Replace…** | Loads one file and discards the current constants set. |

## Tips

- Prefer clear section names so imports from multiple files stay organised.
- Use constants for values that change between cars or events, and leave function-specific calibration on the feature page itself.
- After changing constants, write the configuration to the display so the device and logs match Studio.
