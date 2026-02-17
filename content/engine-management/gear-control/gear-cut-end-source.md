---
title: "Gear Cut End Source"
weight: 58
---

Gear Cut End Source 

This setting controls the way the cut is to be ended once triggered.  The following settings are available :

0: Timed Setting uses the Cut Time Table to 

    control the Cut length

1: "Clutch Switch" Status changing to OFF ends 

    the Cut

2:  "Gear Cut Switch" Status changing to OFF ends 

    the Cut

3: If Positive Force Started the cut, the cut End

   will occur when the Force is less than the

   Postive Force Threshold - Gear Cut Force Hysteresis.

   The inverse applies for a Negative Force Start Cut

     

   Example: 

    Force Threshold = 8.0kg

    Gear Cut Force Hysteresis = 3.0kg

    Start Cut at > 8.0 kg

    End Cut at < 5.0 kg

    Force Threshold = -6.0kg

    Gear Cut Force Hysteresis = 3.0kg

    Start Cut at > -6.0 kg

    End Cut at < -3.0 kg

NOTE: "Gear Cut Start Source" MUST be

selected as 2 (Gear Shift Force) for this setting

to work

4: Next Gear Stable will determine the cut time.  Once 

    the next gear is confirmed the ECU will initiate a cut end

