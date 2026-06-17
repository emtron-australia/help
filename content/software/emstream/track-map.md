---
title: "Track Map"
description: "GPS track map with live vehicle position."
weight: 8
---

The **Track** view shows the vehicle's GPS position on a map in real time. It is useful for monitoring on-track position during a session.

## Live Data

The track map reads GPS and vehicle channels from the telemetry stream:

- GPS latitude and longitude for vehicle position
- Drive speed, steering angle, accelerator, brake pressure
- Gear, engine power, and torque (when transmitted)

Vehicle position updates as GPS data arrives. The map auto-scales to fit the track or follows the vehicle depending on zoom mode.

## Track Outline

Load a track background from **View → Set Track File**:

| Format | Description |
|--------|-------------|
| `.geojson` | Track outline from Emtron track maps or custom GeoJSON |

GPX and GeoJSON are mutually exclusive — loading one clears the other.

## GPX Routes

Load a route or waypoint file from **View → Set GPX File**:

| Format | Description |
|--------|-------------|
| `.gpx` | Waypoints and routes from GPS devices or mapping tools |

Toggle **View → Connect Waypoints** to draw lines between GPX waypoints.

## Combined Layouts

**Track + Grid** shows the track map alongside a data grid. Drag the split divider to adjust the relative sizes. The divider position is saved between sessions.