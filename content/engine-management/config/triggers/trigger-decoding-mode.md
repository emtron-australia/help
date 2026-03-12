---
title: "Engine Decoding Mode"
weight: 2
---

Engine decoding Mode configures the engine trigger type read by the ECU.  

![Image](</img/AA main12.jpg>)

When selecting modes 3+ the ECU will initialize both the Crank Index and Sync Sensor channels to the correct settings. This includes:
 - Sensor Type
 - Sensor Edge
 - Sensor Pull-up
 - Arming Threshold Tables (TBC)

This is considered Pre-Defined Decoding.  All settings for Tooth Count, Index Tooth, Crank Index Offset, are all dictated by the ECU firmware and cannot be customized.  

>[!INFO] If you have a custom setup that is using a type of one of these triggers that has been customized, please contact Emtron support directly for assistance.  

After this is completed the ECU will be automatically restarted. If required the user can then adjust these settings.

>[!WARNING] Any setting change in the Crank Index or Sync Sensor menu that differ from the default values may cause permanent engine damage.