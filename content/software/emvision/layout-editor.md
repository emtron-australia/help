---
title: "Layout Editor"
description: "Configure plot types and split panes within a page."
weight: 6
---

## Entering Layout Edit Mode

Click the **pencil icon** in the title bar toolbar to enter full layout editing. While editing:

- A semi-transparent overlay appears on each plot
- The plot type selector and split controls are visible
- Other plots in the pane are dimmed while one is being configured

Click the pencil icon again to finish editing.

### Quick layout from the plot menu

You can also **right-click** a plot panel and change its type, split it, or delete it without entering full layout edit mode. Use **Settings** on that menu for channel/setup dialogs on line and scatter plots (same as the plot pencil control).

## Changing Plot Type

Each plot cell has a dropdown (or context menu) to select its type:

1. Line Plot
2. Scatter Plot
3. Track Map
4. Lap Timing
5. Gauge Area
6. Lap Matrix

Changing the type replaces the current plot content. Channel assignments from the previous type are not carried over.

## Splitting Panes

The layout editor overlay shows directional buttons around a central circle:

| Button | Action |
|--------|--------|
| Up | Split the cell horizontally, adding a plot above |
| Down | Split the cell horizontally, adding a plot below |
| Left | Split the cell vertically, adding a plot to the left |
| Right | Split the cell vertically, adding a plot to the right |

Splits can be nested to create complex multi-plot layouts within a single page. Drag the split dividers to adjust relative sizes — split ratios are saved with the page.

## Navigator Channel

The **Navigator Channel** is set once under **[Settings](settings) → General**. It drives the bottom navigator strip and cursor preview during playback — it is not configured per page.

## Maximising Plots

Each plot has a maximise button in its corner to expand it to fill the entire pane. Click again to restore the multi-plot layout.