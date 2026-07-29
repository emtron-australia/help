---
title: "Stage Timing"
description: "Single-segment stage, rally, or hill-climb timing (arm → start → finish)."
weight: 23
---

**Functions → Timing → Stage**

Stage Timing measures one continuous segment from start to finish — stage rally, hill climb, or any point-to-point run. It does not count laps. Runs save to the [Timing Run Library](timing-run-library).

## Enabling

Check **Enable** and set the **speed channel** (km/h). Distance can be integrated from speed or read from a distance channel.

## Arm, start, finish, abort

| Stage | Typical use |
|-------|-------------|
| **Arm** | Staging before the clock (switch, edge/level conditions, event, or Auto). |
| **Start** | Clock starts (start line event, green light, or conditions). |
| **Finish** | Clock stops. Prefer **Event** mapped to a **Finish Beacon** from a geo finish line under [Locations & lines](track-setup), or a dedicated finish event. |
| **Abort** | Condition, event, or speed-drop while running. |

Unlike circuit timing, stage **does** use **Finish Beacon** for the finish line. Circuit S/F uses **Lap Beacon** only.

## Live delta

**Stage Time Delta** is distance-matched against the stage run set as **reference** in the Run Library (current time − reference time at the same distance). Negative means ahead of the reference.

- Requires a saved **trajectory** on the reference run.  
- There is no fixed “manual reference time” in stage config — use the library.  
- Without a usable reference trajectory, Stage Time Delta stays invalid (blank/NaN).

## Output channels

| Channel | Description |
|---------|-------------|
| Stage State | Disabled / Idle / Armed / Running / Finished / Aborted |
| Stage Time | Elapsed stage time |
| Stage Distance | Distance covered |
| Stage Time Delta | Live distance-matched Δ vs library reference |

Events: Stage Start, Stage Finish, Stage Abort (when those transitions occur).

## Related

- [Locations & lines](track-setup) — map finish line to Finish Beacon  
- [Timing Run Library](timing-run-library)  
- [Circuit Timing](lap-timing) · [Drag Race Timing](drag-race-timing)
