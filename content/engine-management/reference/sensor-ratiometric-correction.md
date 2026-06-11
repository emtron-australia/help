---
title: "Sensor Ratiometric Correction"
weight: 6
---

## Overview

A sensor's analog output is always proportional (ratiometric) to its supply voltage. The lower the supply voltage, the lower the sensor output voltage. The ECU can correct for this variation in supply voltage and improve sensor performance by applying a ratiometric correction; this is a ratio of the actual sensor supply to the calibrated/ideal sensor supply (5.0V). To do this the ECU must know what supply has been wired to the sensor. There are currently 4 options:

1. **OFF** — ECU applies no sensor ratiometric correction
2. **ECU 5V Ref** — Pin D21 on a KV Series ECU OR Pin B2 on SL series ECU
3. **ECU 5V Ref2** — Pin D22 on a KV Series ECU
4. **5V Ref Ext Supply**

The sensor reference supply can be selected from Emtune by opening the Setup panel of a selected Input Channel.

### 5V Ref Ext Supply

Some sensors may be supplied from an external voltage/supply source. For the ECU to apply ratiometric correction to such a sensor, the ECU needs to know this voltage, so it must be wired into the ECU for measurement. Set up as follows:

1. Connect to the ECU with Emtune. **Config View → Channels → Calculated Runtime → Main**. Select the "5V Ref Ext Supply" setting and pick an input source from the list.

{{< figure src="/img/sensor-ratiometric-correction/5v-ref-ext-supply.png" caption="Calculated Runtime → Main: the \"5V Ref Ext Supply\" is assigned to an input source (here ANV 2)." >}}

2. This runtime can now be viewed from the **Runtime menu (F3) → ECU Internal** tab. This runtime will be used for the "5V Ref Ext Supply" ratiometric correction, so it must accurately represent the sensor supply voltage.

{{< figure src="/img/sensor-ratiometric-correction/runtime-5v-ref-ext.png" caption="ECU Internal runtimes — the measured 5V Ref Ext Supply value used for the ratiometric correction." >}}

## Example

The following test was completed using a 3.0-Bar MAP sensor operating at barometric pressure. A comparison is shown in Table 1.0 between the Ratiometric Correction OFF and ON. With the Ratiometric Correction ON the ECU is able to generate a consistent output for variations in the sensor supply voltage.

**Table 1.0 — MAP Sensor output, Ratiometric OFF/ON Comparison**

| 5V Ref Supply (V) | MAP (Vref Correction OFF) | MAP (Vref Correction ON) |
|-------------------|---------------------------|--------------------------|
| 5.000V            | 99.9 kPa                  | 99.9 kPa                 |
| 4.996V            | 99.8 kPa                  | 99.9 kPa                 |
| 4.975V            | 99.4 kPa                  | 99.9 kPa                 |
| 4.950V            | 98.8 kPa                  | 99.8 kPa                 |
| 4.900V            | 98.0 kPa                  | 99.8 kPa                 |
| 4.850V            | 96.8 kPa                  | 99.8 kPa                 |
| 4.700V            | 93.7 kPa                  | 99.8 kPa                 |
