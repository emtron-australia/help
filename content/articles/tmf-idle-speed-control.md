---
title: TMF Idle Speed Control
weight: 4
---

For idle speed control, users often try to manage engine speed by manipulating throttle position to control airflow. This works reasonably well with solenoid systems (ICV), where position has a more proportional effect on airflow.

With DBW — especially on larger throttles — small changes in throttle position have a disproportionately large effect on airflow, making fine control difficult. Emtron addresses this with a purpose-built approach.

**TMF (Throttle Mass Flow) Idle Speed Control** is a specialised function that provides superior airflow control at idle by working directly in mass flow terms rather than raw position.

## Initial Position

The concept is straightforward: the airflow required to idle the engine is mapped and controlled directly. The Initial Position table defines target airflow (g/s) based on XY parameters.

{{< figure src="../../img/tmf-idle-speed-control/image.png" caption="Screenshot 1: Initial Position (g/s) – Airflow-based idle target table" >}}

A PID loop can be enabled for adaptation, just as with traditional idle systems. Because the PID output is airflow rather than raw position, it has greater authority and precision.

## Throttle Body Model

The target air mass is translated to a DBW servo position via the **Throttle Body Model**, which should be validated before relying on TMF idle control.

{{< figure src="../../img/tmf-idle-speed-control/image-1.png" caption="Screenshot 2a: Throttle Body Model Setup" >}}
{{< figure src="../../img/tmf-idle-speed-control/image-2.png" caption="Screenshot 2b: Throttle Body Area Table" >}}

Regardless of whether the Throttle Body Model is used as part of the engine's airflow model, TMF Idle Speed Control uses the TMF calculation to determine DBW position.

## Idle Ignition Control

TMF Idle Speed Control should be treated as the **base air delivery** system. **Idle Ignition Control** handles fine idle speed corrections, as ignition timing has a fast and predictable effect on engine torque at low RPM.

{{< figure src="../../img/tmf-idle-speed-control/image-3.png" caption="Screenshot 3: TMF Idle with Idle Ignition Control" >}}
{{< figure src="../../img/tmf-idle-speed-control/image-4.png" caption="Screenshot 4: Example Base Idle Initial Position (airflow) and corresponding Base Idle Ignition Table" >}}

The Emtron Idle Ignition Control is a comprehensive system with full PID controls. When used together with TMF Idle Speed Control, it delivers OEM-level idle quality on virtually any application.

{{< figure src="../../img/tmf-idle-speed-control/image-5.png" caption="Screenshot 5: Idle target adjusted live – engine following correctly" >}}
{{< figure src="../../img/tmf-idle-speed-control/image-6.png" caption="Screenshot 6: Log showing throttle position and ignition control working together" >}}
