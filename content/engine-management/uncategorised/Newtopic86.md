---
title: "EFI Relay Control"
---


The ECU can control an EFI relay, allowing for management of its own power supply. To achieve this a dedicated Ignition Switch Input and EFI Relay Output are used. When 14V is applied to the Ignition Switch input, the ECU internal circuity switches the EFI relay output On. This will provide a ground, turning the main relay On and suppling power to the ECU. Once powered up the ECU takes control on this output. When the Ignition Switch turns OFF the ECU can complete critical tasks before shutting itself down (for example, DBW Self calibration and ECU Logging data storage).&nbsp;


The below image shows the internal operation of the EFI Relay system. The control on the EFI Relay output (Low side driver) is managed by a diode OR gate i.e if the Ignition Switch input is ON OR the ECU Control is ON, the EFI Relay output will be ON and providing a ground.&nbsp;


![Image](</img/Untitled224.png>)



**Dedicated EFI Relay Output**

**&nbsp;**

• Provides a relay ground, 200mA Limit&nbsp;

• Short circuit, thermal overload protection, reverse battery&nbsp;


**Dedicated Ignition Switch**&nbsp;


• Used to control Main EFI Relay circuit at key-on&nbsp;

• Input Analog Voltage Range: 0 - 20.0V&nbsp;

• Input Impedance 100k Ohms to ground&nbsp;

• Adjustable On/Off software thresholds. Resolution = 0.1V&nbsp;

