---
title: Frictional Loss
weight: 3
---

Emtron torque modelling relies on a series of inputs and calculations to achieve accurate output estimates. Frictional loss is a significant factor when estimating engine torque output. If incorrectly calibrated, torque-based functions will not perform as designed and may perform worse than equivalent legacy functions. The ECU provides three frictional loss tables for calibration, as shown in Screenshot 1.

{{< figure src="../../img/frictional-loss/image.png" caption="Screenshot 1: Frictional Loss Tables" >}}

## Frictional Loss Table

The **Frictional Loss Table** is the primary table that must be set. The default values in any Emtron base file will generally be a reasonable starting point, but the better this is calibrated the better torque-based functions will perform. Screenshot 2 shows an example table from a Nissan RB26 six-cylinder engine. As a general rule, higher cylinder counts produce higher frictional losses. Modern engines almost always have significantly lower frictional loss than older counterparts.

{{< figure src="../../img/frictional-loss/image-1.png" caption="Screenshot 2: Frictional Loss Table (Nm)" >}}

## Frictional Loss Offset Tables

Oil temperature also influences frictional loss — cold oil increases friction. The **Frictional Loss Offset 1 Table** is calibrated against engine oil temperature, as shown in Screenshot 3. The table is normalised to zero near the target operating oil temperature (90°C in this example). The **Frictional Loss Offset 2 Table** is available for additional calibration inputs and can be set to zero for most applications.

{{< figure src="../../img/frictional-loss/image-2.png" caption="Screenshot 3: Frictional Loss Offset 1 Table (Nm)" >}}

## Calibration Procedure

Engine mapping must be completed correctly before calibrating the frictional loss tables. Calibration should be performed at the target engine oil temperature.

**Main Frictional Loss Table:**

1. Enable PC logging (F8) and perform a steady engine speed sweep from a low RPM (above idle) up to a safe maximum — avoid the engine speed limit. Screenshot 4 shows a sample sweep from 2000–6000 RPM.
2. Review the **Engine Torque** channel across the tested speed range. Values between −10 Nm and +10 Nm are acceptable; the shape of the curve matters more than the absolute value within this range.
   - Positive values indicate the engine speed should be increasing
   - Negative values indicate the engine speed should be decreasing
3. Adjust the Frictional Loss Table values at each engine speed to achieve this. If Engine Torque is higher than expected, increase the frictional loss value. If lower, reduce it. Frictional loss should increase with increasing engine speed.

Engine speed step-and-hold testing can yield even more accurate readings but is not necessary for most applications.

{{< figure src="../../img/frictional-loss/image-3.png" caption="Screenshot 4: Example Engine Speed Sweep" >}}

**Frictional Loss Offset 1 Table (cold oil):**

1. Allow the engine to cool to ambient temperature.
2. Hold engine speed at a safe RPM for cold oil (e.g., 2000 RPM) until the target oil temperature is reached.
3. Adjust each cell of the Frictional Loss Offset 1 Table to achieve the same −10 Nm to +10 Nm target.

These tables should not require further adjustment unless engine changes affect frictional characteristics.
