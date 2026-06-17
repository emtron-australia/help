---
title: "Workspaces and Pages"
description: "Organise analysis layouts with workspaces and pages."
weight: 4
---

## Workspaces

A **workspace** is a saved layout of pages, plot panes, and floating gauges. Workspaces let you switch between different analysis setups without reconfiguring plots each time.

### Managing Workspaces

Access workspaces from:

- **Workspace** menu — quick switch between saved workspaces
- **Workspace Explorer** tab in the left drawer (primary window only)
- **Ctrl+W** — workspace search dialog

In the Workspace Explorer:

- **+ New** — create a new workspace
- Click a workspace name to switch to it
- Rename, duplicate, or delete workspaces from the context actions

Each workspace remembers its pane layout, open pages, plot configurations, and floating gauge positions.

## Pages

A **page** is a saved collection of plots within a workspace. Pages are the tabs shown across the top of each plot pane.

### Page Explorer

The **Page Explorer** tab in the left drawer shows all saved page files. Pages are stored as individual files that can be shared between workspaces.

- Click a page to open it in the currently selected pane
- **Ctrl+P** — page search dialog for quick access

### Page Tabs

Each pane shows page tabs along the top:

- Click a tab to switch pages within the pane
- Close a tab with the X button, or **Ctrl+Q** to close the selected page
- **Ctrl+Shift+Q** — close all pages in the pane
- **Page Up / Page Down** — cycle through open page tabs
- **Ctrl+Page Up / Ctrl+Page Down** — switch between plot panes

### Navigator Channel

In layout editing mode, each pane has a **Navigator Channel** selector. This channel drives the preview cursor position when using playback, helping you follow a specific signal as you scroll through the log.

## Pane Layouts

EmVision supports 1 to 4 plot panes arranged in a grid. Cycle pane count with the toolbar button or **Ctrl+1** through **Ctrl+4**.

Each pane is independent — it can show different pages and plot configurations. **Ctrl+Page Up / Ctrl+Page Down** moves focus between panes.

### Auxiliary Page

**Ctrl+`** toggles an auxiliary page area above the main pane grid. This provides an additional full-width plot row, useful for a dedicated track map or lap matrix above your channel plots.

Resize the auxiliary split by dragging the divider. The split ratio is saved per workspace.