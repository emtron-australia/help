---
title: "Emtron CDI4 — 4 Channel"
weight: 1
---

**Emtron4 — 4 Channel Capacitor Discharge Ignition** (© M&W Ignitions)

{{% badge style="warning" %}}HIGH VOLTAGE{{% /badge %}} It is important to fully read and understand these instructions and have a good knowledge of automotive electrical systems before commencing installation.

## Installation Notes

### Mounting

Do not mount the unit where it will be exposed to water or other liquids; ensure the bottom condensation slots are unobstructed and oriented to permit gravity drain. Select a location away from intense heat and, if required, provide a source of cooling air to remove internally generated heat.

{{% badge style="warning" %}}WARNING{{% /badge %}} Do not mount using Velcro — failure to use the supplied rubber mounts will void warranty!

### Ignition Leads

Do not use plain metal wire or carbon core ignition leads. Use spiral wound inductively suppressed metal core ignition leads such as those available from Magnecor (www.magnecor.com).

### Spark Plugs

The use of non-resistor spark plugs (where possible) will greatly enhance ignition performance. In some installations the use of resistor spark plugs may be unavoidable. During regular maintenance, measure internal resistance to ensure damage has not occurred — open circuit or high resistance may cause failure of spark plug wires, ignition coils and damage to the CDI.

Surface discharge and semi-surface discharge spark plugs should only be used with CDI ignition in naturally aspirated or low boost applications. Do not set a spark gap greater than 0.025" (0.65mm) in high power/boost installations.

### Insulation Precautions

Degrease spark plug insulators and coil/plug boots after handling to prevent spark tracking or insulation breakdown. Use the supplied dielectric grease on spark plug insulators and coil/plug boots to increase insulation properties and ease installation/removal. Use of dielectric grease in the main connector may reduce water ingress.

### Wiring & Power Supply

Emtron CDI systems are designed to blow the external fuse under conditions of over voltage or reverse polarity. Faults such as loose battery terminals, poor wiring or a defective alternator/regulator may also cause this to occur. Fitting a higher current fuse won't disable this feature, will void warranty and may cause irreparable damage to the unit. **Fit the recommended size fuse!**

Main connector pins are designed to be roll crimped. Squeeze crimping or soldering may cause damage/distortion resulting in misfiring or incorrect CDI operation.

Connect the ignition system directly to the battery. If required wire length exceeds recommendations, use paired battery cable (power and ground) to make up the distance. Do not rely on the vehicle chassis to provide a ground path. If connected to a high impedance supply shared with the ECU or its sensors, erratic operation may be experienced.

Do not use voltage boosters as they are unable to provide the instantaneous current required for correct CDI operation.

When using a total loss electrical system, install either a 16V or 18V battery to ensure adequate supply voltage, and isolate during charging to prevent excessive voltage damaging the CDI or ECU.

Use twisted pair wire for all power supply and coil connections. For improved noise suppression and compliance with Australian EMC standards, use twisted shielded pair wire for coils. Keep coil wires one continuous length from the CDI and do not fit intermediate connectors into the harness. All coil negative wires must be joined at or in the CDI connector. Keep coil primary (CDI) wires away from HT leads, the coil HV outlet and the coil body to prevent flashovers.

### Triggering

Trigger input & coil output numbers (letters) indicate CDI ignition **sequence**, not cylinder number. Emtron CDI systems default to falling edge ignition. To select rising edge ignition, ground the Trigger Edge pin.

{{% badge style="warning" %}}WARNING{{% /badge %}} If the CDI trigger edge and ECU ignition edge do not match, timing will be erratic!

### Tuning

CDI systems are 'edge triggered' and not affected by dwell settings. Emtron CDI systems may reduce combustion delay requiring a reduction in ignition timing. Resulting changes in combustion characteristics may also require alterations to fuel flow. **Always re-tune fuel and timing curves after installing CDI ignition!**

### Tacho Output

The tacho output provides a 50% duty cycle square wave signal at battery supply voltage. This will work with most aftermarket digital tachos; however, early designs and those previously connected to the coil negative side may require a tacho adaptor to read correctly.

### LED Indicator

After applying power to the switch wire, the LED will illuminate for 1 second and extinguish. The LED will then flash briefly with each consecutive trigger event received (it may be necessary to view the LED directly on axis). A repeated double flash of the LED may indicate a possible faulty ignition coil, faulty wiring, low supply voltage or damage to the CDI.

### Testing

The CDI may be tested by momentarily grounding the trigger inputs, causing the LED to flash and the corresponding ignition coil to spark. **Do not conduct this test without grounded spark plugs installed!**

## Ignition Coils

### Coil Selection

Most inductive ignition coils will work reasonably well with CDI systems; however, for ultimate ignition energy and efficiency use a coil specifically designed for CDI use, such as the M&W #COI006.

### COP Coils

COP (coil on plug) coils with inbuilt drivers are not suitable for use with CDI ignition. COP coils designed for inductive ignition may contain a blocking diode in the secondary winding which must be considered during wiring (see coil polarity note below). Use resistive spark plugs with all COP coils. Keep plug gap < 0.025" (0.6mm) to prevent coil damage. **DO NOT use AEM pencil coils under any circumstances!**

### Ferrite CDI Coils

Ferrite core CDI coils provide a lightweight solution for direct fire applications and give high secondary current; however, they may not be suitable for all applications due to their extremely short arc duration. The high level of EMI emitted by these coils may also require additional shielding to prevent electrical interference with the ECU or CDI. Do not use ferrite coils in parallel wired pairs!

### Coil Polarity

All diagrams are shown for CDI style coils. For correct operation with inductive ignition coils, wire the primary connections in reverse to maintain correct spark plug polarity.

{{% badge style="warning" %}}CAUTION{{% /badge %}} Ignition coil damage may occur if operated with an excessive spark gap.

## Mounting Dimensions

{{< figure src="/img/cdi/cdi4/mounting-dimensions.png" caption="Emtron CDI4 mounting dimensions (slot dimensions 5mm × 10mm)." >}}

## Connections and Specifications

{{< figure src="/img/cdi/cdi4/connections-specifications.png" caption="Emtron CDI4 18-pin connector pinout (viewed from back of connector) and specifications." >}}

**Specifications**

| Parameter                     | Value                                        |
|-------------------------------|----------------------------------------------|
| Supply voltage                | 13V - 18V DC negative ground                 |
| Startup voltage               | 6V                                           |
| Maximum supply current        | 7.0A                                         |
| Power off current             | < 700µA                                      |
| Maximum ignition frequency    | 1,200Hz                                       |
| Maximum energy limit          | 700/550 Hz                                    |
| Coil primary voltage          | 460V/540V (paired triggers)                  |
| Spark energy                  | 115/150 millijoules (paired triggers)        |
| Trigger                       | 10mA adjustable edge                         |
| Tacho                         | 12V, 100mA square wave                       |
| Maximum allowable case temperature | 105°C                                  |
| Dimensions                    | 112L × 110W × 40H mm                          |
| Weight                        | 570g                                         |

## 4 Cylinder Direct Fire Ignition

{{< figure src="/img/cdi/cdi4/sequential-ignition-wiring.png" caption="Four-coil sequential ignition wiring. Use 18-20 gauge wire, twist 1 turn in 20mm, with junction < 100mm from the connector joined to 14 gauge for the run to the battery (max length 2.5M)." >}}

## Shielding & EMC Compliance

{{< figure src="/img/cdi/cdi4/shielding-emc.png" caption="Shielding for Australian EMC compliance — shielded power cables required; use twisted shielded cable grounded at one end only." >}}
