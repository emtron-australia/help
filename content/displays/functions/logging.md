---
title: "Logging"
description: "Configure on-board data logging on the display."
weight: 2
---

**Functions → Logging**

The logging function records channel values and events to files on the display's internal storage. Logged data can be downloaded from the **Home** view when a device is connected.

## Logging Groups

Logging is organised into groups. Each group defines what to log, when to start, and when to stop.

### Creating a Group

1. Open **Functions → Logging**.
2. On the **Groups** tab, click **Add Group**.
3. Name the group and configure its settings.

Groups can be exported and imported as `.lgrp` files to share logging setups between configs.

## Group Configuration

Each group has four main areas:

### Start Conditions

Define when logging begins. Use [condition sets](conditions) to trigger on channel values, events, or combinations — for example, when engine RPM exceeds idle speed.

### Stop Conditions

Define when logging ends. Common choices include ignition off, a manual stop event, or a timer expiry.

### Logged Channels

Add channels to record and set each channel's **Log Rate**. Higher rates capture more detail but produce larger files.

### Logged Events

Add events to record. Event timestamps are stored when the event fires.

## Settings Tab

The **Settings** tab configures global logging parameters such as file naming, storage limits, and post-trigger behaviour. Adjust these to match how much storage the display has available and how long you need logs retained.