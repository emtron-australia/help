---
title: "Fonts"
description: "Manage custom fonts for text and value gauges."
weight: 6
---

**Display → Fonts**

Custom fonts can be embedded in the configuration for use by Text, Value, Time, and Status gauges.

## Managing Fonts

- **Add** — import a font file into the configuration.
- **Remove** — delete an unused font.

Assign a font to a gauge via its **Font** property. Leave empty to use the default system font.

## Recommendations

- Prefer compact, readable fonts designed for small pixel sizes.
- The font atlas system provides fast rendering for numeric value gauges — custom fonts work but may have slightly different performance characteristics.