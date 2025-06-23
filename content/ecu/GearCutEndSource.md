---
title: "Gear Cut End Source"
---

Gear Cut End Source&nbsp;


This setting controls the way the cut is to be ended once triggered.&nbsp; The following settings are available :


&#48;: Timed Setting uses the Cut Time Table to&nbsp;

&nbsp; &nbsp; control the Cut length

&#49;: "Clutch Switch" Status changing to OFF ends&nbsp;

&nbsp; &nbsp; the Cut

&#50;:&nbsp; "Gear Cut Switch" Status changing to OFF ends&nbsp;

&nbsp; &nbsp; the Cut

&#51;: If Positive Force Started the cut, the cut End

&nbsp;&nbsp; will occur when the Force is less than the

&nbsp;&nbsp; Postive Force Threshold - Gear Cut Force Hysteresis.

&nbsp;&nbsp; The inverse applies for a Negative Force Start Cut

&nbsp; &nbsp; &nbsp;

&nbsp;&nbsp; Example:&nbsp;

&nbsp; &nbsp; Force Threshold = 8.0kg

&nbsp; &nbsp; Gear Cut Force Hysteresis = 3.0kg

&nbsp; &nbsp; Start Cut at \> 8.0 kg

&nbsp; &nbsp; End Cut at \< 5.0 kg


&nbsp; &nbsp; Force Threshold = -6.0kg

&nbsp; &nbsp; Gear Cut Force Hysteresis = 3.0kg

&nbsp; &nbsp; Start Cut at \> -6.0 kg

&nbsp; &nbsp; End Cut at \< -3.0 kg


NOTE: "Gear Cut Start Source" MUST be

selected as 2 (Gear Shift Force) for this setting

to work


&#52;: Next Gear Stable will determine the cut time.&nbsp; Once&nbsp;

&nbsp; &nbsp; the next gear is confirmed the ECU will initiate a cut end




