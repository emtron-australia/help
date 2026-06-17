---
title: "User Channels"
description: "Create custom channels for project-specific data."
weight: 2
---

**Setup → User Channels**

User channels let you define custom named channels for data that is not covered by the built-in channel list. They behave like any other channel — functions can read and write them, gauges can display them, and they can be logged.

## Creating a Channel

1. Open **Setup → User Channels**.
2. Click **Add** to create a new channel.
3. Set the **Name** and select a **Unit** type.
4. Optionally assign an **Enum** to display human-readable text instead of numeric values.

## Import and Export

User channel definitions can be exported and imported between configurations using the toolbar buttons. This is useful when sharing a common set of custom channels across multiple vehicle configs.

> **TIP:** Prefer built-in channels where they exist. Built-in channels ensure compatibility when importing sub-configurations from other projects. Contact Emtron support to request addition of commonly needed channels.

See [Channels and Events](../concepts/channels-and-events#custom-channels) for guidance on when to use custom channels.