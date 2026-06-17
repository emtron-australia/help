---
title: "Vehicle Details"
description: "Configure constant vehicle parameters used by display functions."
weight: 1
---

**Setup → Details → Vehicle**

Vehicle Details stores constant values that other functions reference — wheel sizes, gear ratios, engine parameters, and similar fixed data. These are written to dedicated channels and remain available throughout the configuration.

## Tabs

The vehicle details page is organised into tabs:

| Tab | Typical Parameters |
|-----|-------------------|
| Engine | Displacement, cylinders, idle speed |
| Transmission | Gear ratios, final drive |
| Differential | Diff ratio |
| Wheels/Tyres | Tyre rolling radius, wheel circumference |
| Geometry | Wheelbase, track width |
| Camber / Caster / Toe | Suspension geometry |
| Aero | Aerodynamic constants |
| Vehicle | General vehicle identification |

Each field maps to a built-in channel. When a function needs a vehicle constant (for example, wheel circumference for speed calculations), select the corresponding channel from the channel picker.

## All Tab

**Setup → Details → All**

The **All** tab provides a searchable list of every configurable item in the configuration, including persistent channels and function settings. Use it to quickly locate a channel assignment or setting without navigating through individual function pages.

Filter the list by name to find channels, events, or configuration paths across the entire config.