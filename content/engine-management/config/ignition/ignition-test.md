---
title: "Ignition Test"
weight: 14
---

# Overview

![Image](</img/Ignition17.jpg>)

The Ignition Test function allows each ignition output channel to be manually fired for installation, diagnostics and troubleshooting purposes.

This function can be used to:

- Verify ignition coil wiring.
- Confirm cylinder numbering and firing order.
- Check ignition output operation.
- Verify spark plug and ignition coil functionality.
- Diagnose ignition system faults.

The **Ignition Test Dwell** setting specifies the coil charge time used during the test event and is expressed in units of **milliseconds (ms)**. A test dwell value of **3.0 to 4.0 ms** is suitable for most modern inductive ignition coils.

When an ignition channel test is activated, the ECU charges the selected ignition coil for the configured test dwell period before firing a spark event. The test rate runs at 10Hz

The ignition test function operates at a fixed test rate of **10 Hz** (**10 ignition events per second**).

> **⚠️ Warning**
>
> The Ignition Channel Output must have a cylinder assigned for this function to operate. See See [*Ignition Channel Setup*](<Ignition-Channel-Setup.md>) for help.
>
> Ensure the ignition system is configured correctly before performing an ignition test.
>
> High voltages are generated during ignition testing which may cause injury or damage to ignition components if used incorrectly.
>
> Do not perform ignition tests in the presence of fuel vapour or near flammable materials.

