---
title: "Images"
description: "Manage image assets used by gauges."
weight: 5
---

**Display → Images**

The Images page manages PNG image files embedded in the configuration. Gauges such as Dial, Image, Multi Image, and Cropped Image reference files from this library.

## Managing Images

- **Add** — import a PNG file into the configuration.
- **Remove** — delete an unused image from the config.
- **Preview** — view the image and its filename.

Images are referenced by filename in gauge properties (for example, `File Name` on a Dial Gauge). Use PNG format with transparency for best results.

## Recommendations

- Keep image dimensions close to the size they will be displayed at.
- Design dial needle images pointing upward (0°) with the pivot at the intended rotation centre.
- Use consistent resolution across related assets (gauge bezels, backgrounds, needles).