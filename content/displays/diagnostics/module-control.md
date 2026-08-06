---
title: "Module Control"
description: "Enable or disable display backend modules at runtime."
weight: 3
---

**Diagnostics → Module Control**

Module Control lists backend modules running on the connected display. You can enable or disable non-critical modules at runtime to isolate problems or free resources while testing.

## Using Module Control

1. Connect to the display.
2. Open **Diagnostics → Module Control**.
3. Optionally filter the list with the search box.
4. Click **Refresh** to reload the module list from the device.
5. Use **Enable** / **Disable** on a module.

## Always-on modules

Some modules are marked **Always on**. They cannot be disabled at runtime because the display needs them for basic operation.

## Notes

- Disabled modules stay off until you re-enable them or the device restarts (then the normal startup set applies).
- Prefer this page for temporary diagnostics. Permanent feature configuration belongs in the normal Setup / Functions menus.
