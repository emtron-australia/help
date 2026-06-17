---
title: "Live Plots"
description: "Configure scrolling time plots for live telemetry data."
weight: 7
---

The **Plots** view displays scrolling time-history plots of selected channels. Data is buffered locally by the [Data Logger](data-logger) and plotted in real time.

## Plot Structure

Plots are organised in three levels:

| Level | Description |
|-------|-------------|
| Groups | Top-level tabs (up to 7 groups) |
| Pages | Sub-tabs within each group (up to 8 pages) |
| Plots | Up to 4 time plots stacked vertically on each page |

## Configuring Plots

Click the **pencil icon** on the plots view to open **Live Data Setup**.

### Groups

- **Add Group** — create a new group (creates a default page with 3 time plots)
- **Import Group** — load a `.logginggroup` file
- Drag groups to reorder
- **Save Group** / **Delete Group**

### Pages

Within a selected group:

- **Add Page** — create a new page tab
- **Import Page** — load a `.loggingpage` file
- Set **Plot Count** (0–4 plots per page)
- **Save Page** / **Delete Page**

### Time Plot Configuration

Each plot cell supports up to 8 channels. Configure channels directly on the plot:

- Click the plot to open channel selection
- Assign channels to plot traces
- Set Y-axis minimum and maximum, or enable auto-scale per channel
- Use **quick add mode** to rapidly add channels from the live data list

Plots scroll automatically as new data arrives. When logging is **paused**, use the toolbar controls to scroll back through buffered history.

## Split Layouts

When using **Plot + Plot** or **Plot + Grid** view types, each side has independent group and page tabs. The secondary plot area uses a separate tab index, so you can show different channel sets side by side.

## Import and Export

| File Type | Contents |
|-----------|----------|
| `.logginggroup` | Entire group with all pages |
| `.loggingpage` | Single page with plot configuration |