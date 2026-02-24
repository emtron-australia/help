---
title: "Racepak Dash CAN Setup"
weight: 102
---

This section describes how to connect an Racepak IQ3 dash to the Emtron CAN bus.

## Racepak Device Compatibility

**250-ds-Iq3s**     - Street display

**250-ds-iq3d**     - Drag logger 

**250-ds-iq3ld**     - Logger dash 

**250-ds-iq3sl**     - Street logger

**250-ds-iq3**     – Display only 

These devices require an interfacing module to talk to additional ECU systems/components

** Requires Universal EFI Module **230-vm-efiucan**

## Racepak CAN Wiring colors

* Green  = ground
* Black  = CAN Lo
* White = CAN Hi

## ECU Setup

* Select either CAN1 or CAN2
* Select a Channel with CAN1 or CAN2
* Set Enable to ON
* Set CAN Address = 1250
* Select required DATA Set;  Predefined or custom
* Set Direction to transmit
* Set Addressing to sequential
* Set required Transmit Rate. **CAUTION. Do NOT set to high as this will limit the available bandwidth to other devices on the bus**

## Racepak Setup

A default RacePak Config file has be created to match the Emtron  ECU Predefined1 DATA set. This is called Emtron_Predefined1_IQ3_Config.rcg. This should be programmed into the ECU.
