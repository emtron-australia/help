---
title: "Math Channels"
description: "Create derived channels using formulas and the emexpr language."
weight: 8
---

**File → Maths** (or **F6**)

Math channels compute new channel values from existing log data. EmVision uses the same **emexpr** expression language as Display Studio. Expressions are re-evaluated over the open log when you apply changes in the maths dialog.

## Expression language (emexpr)

Full syntax, operators, built-in functions, filters, and examples are documented here:

> **[Math Functions (Display Studio)](/displays/functions/maths)** — expression syntax, `math.*` / `filter.*` / `calc.*` / `gen.*` libraries, literals (`0x`, `0b`), and stateful evaluation.

That page is written for real-time evaluation on the display (100 Hz continuous or on-event). In EmVision the same expression language is applied offline to logged samples. Prefer the **syntax and function reference** there; evaluation timing and display-only setup fields (Continuous / On Event, reset events) apply on the vehicle, not when analysing a log.

## Using maths in EmVision

1. Open **File → Maths** (or press **F6**).
2. Organise work into **groups** and **expressions** (the shared maths config UI).
3. Name each expression and write an expression that references log channels by name.
4. Use enum lookup on status-style inputs to insert a named state’s numeric value into the expression when available.
5. Math channels can reference **other math channels** as inputs.
6. Close the dialog or leave it so changes push to the worker — channels update for plots and the measurements panel.

A warning indicator appears on groups or expressions that fail to compile. Fix the expression text and re-apply.

## What you can do

- Scale, offset, and blend channels
- Filters and derivatives (via `filter.*` / related functions — see the [syntax reference](/displays/functions/maths))
- Boolean and conditional logic (`? :`, comparisons)
- Intermediate values with `let`
- Binary and hex integer literals (`0b`, `0x`)

## Import and export

Math configuration can be shared between projects using the import/export controls in the maths dialog (formula/function files such as `.elform` / `.elfunc` where offered by the UI).

## Applying and storage

- Math results are **not** written back into the original log file.
- Definitions live in the client configuration and are available in later sessions; use them with [user channels](user-channels) when you need custom channel identity (name, units, colour).
- Recalculation runs against the currently open reference (and related) log data.

## Related

- [User Channels](user-channels) — custom channel names for analysis
- [Math Functions](/displays/functions/maths) — full emexpr reference (Display Studio docs)
- [Export Log](export-log) — export native log channels (math may not be included)
