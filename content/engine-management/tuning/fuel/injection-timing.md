---
title: "Injection Timing"
weight: 8
---


## ⚙️ Injection Timing Table

The Injection Timing table defines the desired injection event angle as a function of engine operating conditions.

Table values are expressed in crankshaft degrees Before Top Dead Centre (BTDC) and are referenced to Cylinder 1 Compression TDC (i.e 400  = 400 degrees before TDC Cylinder 1 compression).  The table is configured as an advance-style table, therefore larger values schedule the injection event earlier in the engine cycle.

The interpretation of the table values depends on the selected Injection Timing Reference mode:

Start of Injection – Table values define when the injector begins delivering fuel.<br>
End of Injection – Table values define when the injector finishes delivering fuel.

Table Size: 22 columns x 12 rows

Resolution: 0.1 Deg<br>
Range: 0.0 - 720.0 Degs

## ⚠️ Notes
When Staged Injection is enabled, a secondary Injection Timng Table can be used which operates independently of the Primary Injectors.  The Sec Injectors can be advanced up during the initial transition into staged mode to help improve the overall smoothness during this event

## ⚙️ Injection Timing Reference

The Injection Timing Reference setting determines whether the Injection Timing table values specify the Start of Injection (SOI) or End of Injection (EOI) event.

Injection Timing determines when fuel is delivered into the engine cycle relative to **Cylinder 1 Compression Top Dead Centre (TDC)**.

Injection Timing values are expressed in **crankshaft degrees Before Top Dead Centre (BTDC)** . Larger values schedule the injection event earlier in the engine cycle.


## Timing Reference Examples

| Value | Description |
|---------|---------|
| 400° BTDC | 400° before Cylinder 1 Compression TDC |
| 360° BTDC | TDC between the exhaust and intake strokes (valve overlap period) |
| 300° BTDC | Approximately 60° after intake valve opening on a typical 4-stroke engine |

## Options

| Value | Mode |
|---------|---------|
| 0 | Start of Injection |
| 1 | End of Injection |

## Start of Injection (SOI)

The Injection Timing table value defines when the injector begins delivering fuel.

The ECU calculates the corresponding End of Injection based on the injector pulse width and operating conditions.

This mode is typically used when the desired fuel delivery strategy is based on the opening point of the injection event.

## End of Injection (EOI)

The Injection Timing table value defines when the injector finishes delivering fuel.

The ECU automatically calculates the corresponding Start of Injection based on the injector pulse width and operating conditions.

This mode is commonly used when precise control of fuel delivery relative to intake valve events is required.

For sequential injection systems, End of Injection mode is often preferred because the completion of fuel delivery can be aligned with intake valve events. This can reduce fuel wall wetting, improve fuel preparation and promote more consistent cylinder-to-cylinder fuel distribution.

## ⚠️ Notes

- Injection timing values are referenced to Cylinder 1 Compression TDC regardless of the cylinder being fuelled.
- Higher values move the injection event earlier in the engine cycle.
- Whether the value represents the Start or End of Injection depends on the selected Injection Timing Reference mode.
- The actual injector opening and closing points will vary with pulse width, engine speed and operating conditions.

##  ⚙️ Setting

To locate setting Injection Timing Reference see:  
Config -> Fuel -> Fuel Main -> Injection Timing Reference (Prim) <br>
Config -> Fuel -> Fuel Secondary Setup -> Injection Timing Reference (Sec) <br>

To locate Injection Timing Table see:  Tuning  View -> Fuel -> Injection Timing Tables

Example for Primary Injection.

![Image](</img/Z Axis24.jpg>)

Example for Staged Injection with the angle spanned across intake camshaft target angle & fuel mass final (g/cyl).

![Image](</img/Secondary inj timing.jpg>)




