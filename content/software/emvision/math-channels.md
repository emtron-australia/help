---
title: "Math Channels"
description: "Create derived channels using formulas and functions."
weight: 8
---

**File → Math Channels** (or **F6**)

Math channels compute new channel values from existing log data. They are recalculated when the dialog is closed and applied to the current log session.

## Formulas

The **Formulas** tab defines expression-based math channels. Each formula:

- Has a **name** that appears in the channel list
- Uses an **expression** referencing existing channels by name
- Supports standard arithmetic operators and functions

Formulas are evaluated across the entire log, producing a new channel that can be added to any plot.

### Import and Export

Formulas can be saved and loaded as `.elform` files to share between projects.

## Functions

The **Functions** tab defines multi-step function pipelines. Each function:

- Has a **name** and **description**
- Chains operations (filters, scaling, integration, etc.) on input channels
- Produces an output channel

Functions support more complex processing than single-line formulas — for example, smoothing a signal before calculating a derivative.

### Import and Export

Functions can be saved and loaded as `.elfunc` files.

## Applying Changes

Math channels are not written back to the log file. They exist only in the current EmVision session (and are saved with the workspace). Close the Math Channels dialog to trigger recalculation — a warning icon appears on tabs with configuration errors.