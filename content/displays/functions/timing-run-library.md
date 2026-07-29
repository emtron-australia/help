---
title: "Timing Run Library"
description: "Saved circuit, drag, and stage runs — reference for live deltas and review on gauges."
weight: 24
---

**Functions → Timing → Run Library**

The Timing Run Library stores finished (and aborted) runs from [Circuit](lap-timing), [Drag](drag-race-timing), and [Stage](stage-timing) timing on the device. Use it to compare live runs against a past result, or to show a past result on the dash.

Legacy circuit `.trk` files are no longer used. Best laps and trajectories come from this library.

## List and filters

When connected to a device, the page lists runs with discipline, location, time, and duration.

- Filter by discipline (circuit / drag / stage) as needed.  
- Select a run for actions below.  
- Import / export packages for backup or transfer (where available in Studio).

## Reference vs review

| Role | Purpose |
|------|---------|
| **Reference** | Live deltas while you race or stage. Circuit and drag engines load the selected run’s times and trajectory. |
| **Review** | Display-only: show a past run’s times on **Timing Review *** channels without changing live delta behaviour. |

### Set as reference

1. Select a finished run.  
2. **Set as reference**.  
3. Confirm live delta channels start tracking that run (circuit best-lap trajectory, drag splits/trajectory, or stage trajectory).

**Clear reference** removes the ghost so circuit Δ falls back to the current outing’s best lap, and stage/drag live library deltas stop.

You can also step reference on the device with virtual-button events (**Timing Reference Next / Prev / Best / Clear**) if those events are wired on a page.

### Review

**Set as review** (or copy reference → review) fills **Timing Review** channels for gauges that should show a historical result without affecting live deltas.

## What “time” means in the list

| Discipline | Duration / reference time shown |
|------------|----------------------------------|
| **Circuit** | Best lap time of the outing (not total race time). |
| **Drag** | Elapsed strip time (typically 1/4 mile). |
| **Stage** | Total stage time. |

**Timing Reference Time** on the bus matches that representative time for the selected reference run.

## Channels (overview)

**Reference** group (live ghost metadata): run id, label, location, time, distance, mode, plus discipline-specific splits (drag markers, circuit best lap / sectors).

**Review** group: same idea for display-only selection, including stage review time/distance.

**Library count** reflects how many runs match the current filter.

## Tips

- After a good outing, set that run as reference before the next session.  
- For circuit, ensure the reference run has a usable trajectory if you want smooth distance-matched Δt/Δv.  
- For stage, distance-matched Stage Time Delta **requires** a trajectory on the reference run.  
- Drag can use a full library trajectory or fall back to a sparse curve from marker times / manual timeslip.

## Related

- [Circuit Timing](lap-timing) · [Drag Race Timing](drag-race-timing) · [Stage Timing](stage-timing)  
- [Locations & lines](track-setup)
