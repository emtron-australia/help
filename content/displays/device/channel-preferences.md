---
title: "Channel Preferences"
description: "Set display units and formatting for channels."
weight: 1
---

**File → Channel Preferences**

Channel preferences control how channel values are displayed — unit conversions, decimal places, and formatting. Preferences are applied per application or device, not stored in the configuration file.

## How Preferences Work

Channels are stored and logged in their base metric units internally. Preferences only affect display — configuration files and log files remain unit-agnostic. This allows configs and logs to be shared across regions, with each user viewing data in their preferred units.

## Operations

| Button | Description |
|--------|-------------|
| Write to Device | Save preferences to the connected display |
| Read from Device | Load preferences from the connected display |
| Save to File | Export preferences as an `.epref` file |
| Load from File | Import preferences from an `.epref` file |

Configure individual channel display units and precision in the preferences table below the action buttons.