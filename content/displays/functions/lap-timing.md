---
title: "Lap Timing"
---

The Lap Timing function outputs lap and timing data based triggered by lap beacon events.

## Input Channels
 - **Speed Channel:** Select the channel to use as the speed input.
 - **Lap Distance Channel:** *Optional* - Select the channel to use as the lap distance input.
 > **Note:** Lap and Race distance can be calculated from the speed input channel.

 ## Input Events
 Two main events are used to control the lap timing function.
 These events can be triggered however you see fit. Typically they're triggered by GPS as configured in [Track Setup](./track-setup.md).

### Lap Beacon
 - Triggers the start of a new lap. 
 - Triggers the update of Best Lap, Previous Lap, and Time Delta related channels.

### Sector Beacon
 - Triggers the start of a new sector within the current lap.
  
## Output Channels
 - Lap
 - Current Lap Time
 - Best Lap Time
 - Optimal Lap Time
 - Time Delta To Best Lap
 - Time Delta To Previous Lap
 - Speed Delta To Previous Lap
 - Speed Delta To Best Lap
