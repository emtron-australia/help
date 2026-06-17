---
title: "Data Grid"
description: "Configure numerical gauge grids for live channel display."
weight: 6
---

The **Grid** view displays channel values in a layout of numerical gauges. Use it for at-a-glance monitoring of key parameters.

## Grid Structure

Grids are organised in three levels:

| Level | Description |
|-------|-------------|
| Groups | Top-level tabs across the grid view |
| Grids | Sub-tabs within each group |
| Cells | Individual gauge positions in a rows × columns layout |

Switch between group and grid tabs at the top of the view.

## Configuring Gauges

Click the **pencil icon** on the grid view to open **Data Grid Setup**.

### Groups

- **Add Group** — create a new group tab
- **Import Group** — load a `.gridgroup` file
- Drag groups to reorder
- **Save Group** / **Delete Group**

### Grids

Within a selected group:

- **Add Grid** — create a new grid tab (defaults to 2×2)
- **Import Grid** — load a `.datagrid` file
- Set **Rows** and **Columns** (up to 9 rows, 6 columns)
- **Save Grid** / **Delete Grid**

### Cell Configuration

Assign a channel to each grid cell by hovering over the gauge and clicking the settings icon. Configure:

| Setting | Description |
|---------|-------------|
| Channel | The telemetry channel to display |

Values update in real time as data arrives from the telemetry stream.

## Import and Export

Grid configurations can be shared between PCs:

| File Type | Contents |
|-----------|----------|
| `.gridgroup` | Entire group with all grids |
| `.datagrid` | Single grid layout |