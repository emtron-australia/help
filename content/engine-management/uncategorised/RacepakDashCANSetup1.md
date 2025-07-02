---
title: "Racepak Dash CAN Setup"
---

This section describes how to connect an Racepak IQ3 dash to the Emtron CAN bus.

**Racepak Device Compatibility**&nbsp;




**&#50;50-ds-Iq3s** &nbsp; &nbsp; - Street display

**&#50;50-ds-iq3d** &nbsp; &nbsp; - Drag logger&nbsp;

**&#50;50-ds-iq3ld** &nbsp; &nbsp; - Logger dash&nbsp;

**&#50;50-ds-iq3sl** &nbsp; &nbsp; - Street logger


**&#50;50-ds-iq3** &nbsp; &nbsp; – Display only&nbsp;

These devices require an interfacing module to talk to additional ECU systems/components

\*\* Requires Universal EFI Module **230-vm-efiucan**



**Racepak CAN Wiring colors**


* Green&nbsp; = ground
* Black&nbsp; = CAN Lo
* White = CAN Hi



**ECU Setup**


* Select either CAN1 or CAN2
* Select a Channel with CAN1 or CAN2
* Set Enable to ON
* Set CAN Address = 1250
* Select required DATA Set;&nbsp; Predefined or custom
* Set Direction to transmit
* Set Addressing to sequential
* Set required Transmit Rate. **CAUTION. Do NOT set to high as this will limit the available bandwidth to other devices on the bus**



**Racepak Setup**


A default RacePak Config file has be created to match the Emtron&nbsp; ECU Predefined1 DATA set. This is called Emtron\_Predefined1\_IQ3\_Config.rcg. This should be programmed into the ECU.
