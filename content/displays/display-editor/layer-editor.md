---
title: "Layer Editor"
description: "Create reusable gauge layers for layer group gauges."
weight: 2
---

**Display → Layer Editor**

Layers are self-contained gauge layouts that can be embedded in a screen via the [Layer Group Gauge](../functions/gauges#layer-group-gauge). Each layer is an independent set of gauges rendered to an off-screen texture.

## Working with Layers

- **Add Layer** — create a new layer definition.
- **Duplicate Layer** — copy an existing layer as a starting point.
- **Export / Import** — save layers as `.edlayer` files.

Layers are edited the same way as screens — add gauges, position them, and configure properties. The layer dimensions define the render area.

## Using Layers on a Screen

1. Create one or more layers in the Layer Editor.
2. In the Screen Editor, add a **Layer Group Gauge**.
3. Assign which layers the group can display.
4. Configure events for **Next Layer**, **Previous Layer**, and direct **Show** events per layer.

Layer switching is event-driven, making layers suitable for multi-page dashboards, context-sensitive views, and menu systems.