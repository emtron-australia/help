---
title: "Track Setup"
---

Track Setup determines how GPS based [Lap Timing](./lap-timing.md) functions.

Lap Timing and Track Setup are separated so that other systems can also generate the lap and sector beacons. This allows the use of other timing systems such as laser beacons.

## Location Detection
Each track has a central GPS position. This allows the device to select the track as the active track when it detects itself inside the detection radius of a particular track.
> **Note:** To use automatic track location detection, `Startup Track Selection` needs to be set to `Auto Select Using GPS`.

Alternatively, tracks can be selected manually by assigning events to the `Select Previous Track Event` and/or `Select Next Track Event` options.

## Tracks
Tracks are essentially a collection of GPS coordinate lines that allow the device to output sector and lap beacons.
The track's `Latitude` and `Longitude` values are used to set the position of the map window as well as automatic location detection.
To quickly adjust the position, click the `Pick Position` button and click the new postion in the map window.

## Sectors
Sectors are made up of two position coordinates to create an imaginary line. When the device detects that it has crossed this line, it can output an event.

To create a new sector line: 
 1. Click `Add Line`. 
 2. Update the line type and name as needed.
 3. Click the `Pick Position` button for Lat A / Long A.
 4. Click the position in the map window for the lines A position.
 5. Click the `Pick Position` button for Lat B / Long B.
 6. Click the position in the map window for the lines A position.
 7. Select the output event. Typically this is either `Lap Beacon` or `Sector Beacon`.

There are two important events used by the [Lap Timing](./lap-timing.md) function. Appropriate use of these beacon events will result in accurate lap timing data.

### Lap Beacon
When the `Lap Beacon` event is triggered, the [Lap Timing](./lap-timing.md) function will initiate the start of a new lap.

### Sector Beacon
When the `Sector Beacon` event is triggered, the [Lap Timing](./lap-timing.md) function will initiate the start of a new sector within the current lap.