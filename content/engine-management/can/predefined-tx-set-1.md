---
title: "Predefined CAN Transmit Set 1"
weight: 132
---

All 16 bit values have low byte transmitted first by the ECU. Sequential addressing is used. All parameters are transferred in the units defined inside the ECU. These can be rescaled if required by the receiving device.

Custom Packet 1 contains 10 Message Objects each with a different sequential address. This can be selected on CAN1 or CAN2 and on any of the 6 channels within that CAN node. In total the Custom Packet 1 transmits 40 parameters on one CAN Channel.

> **NOTE:** If all 6 channels were used within one CAN node a total of 240 parameter could be transmitted

## Message 1

**Address:** 1250 (Emtron preferred. User Adjustable)

**Transmits:** 8 bytes/4 parameters.

**Addressing Mode:** Sequential.

| CAN Address | Byte Position | Parameter                | Unit        |
| ----------- | ------------- | ------------------------ | ----------- |
| 1250    | 1-2       | Engine Speed             | rpm         |
| 1250    | 3-4       | Engine Manifold Pressure | Pressure    |
| 1250    | 5-6       | Engine Temperature       | Temperature |
| 1250    | 7-8       | Engine Inlet Temp        | Temperature |

## Message 2

**Address:** 1251 (Sequential based on address in Message 1)

**Transmits:** 8 bytes/4 parameters.

**Addressing Mode:** Sequential.

| CAN Address | Byte Position | Parameter                   | Unit        |
| ----------- | ------------- | --------------------------- | ----------- |
| 1251    | 1-2       | Throttle Position 1         | Position    |
| 1251    | 3-4       | Estimated Charge Temp  | Temperature |
| 1251    | 5-6       | Gear                        | NA          |
| 1251    | 7-8       | Battery Volts               | Voltage     |

## Message 3

**Address:** 1252 (Sequential based on address in Message 2)

**Transmits:** 8 bytes/4 parameters.

**Addressing Mode:** Sequential.

| CAN Address | Byte Position | Parameter        | Unit        |
| ----------- | ------------- | ---------------- | ----------- |
| 1252    | 1-2       | Oil Pressure     | Pressure    |
| 1252    | 3-4       | Oil Temperature  | Temperature |
| 1252    | 5-6       | Fuel Pressure    | Pressure    |
| 1252    | 7-8       | Fuel Temperature | Temperature |

## Message 4

**Address:** 1253 (Sequential based on address in Message 3)

**Transmits:** 8 bytes/4 parameters.

**Addressing Mode:** Sequential.

| CAN Address | Byte Position | Parameter                        | Unit          |
| ----------- | ------------- | -------------------------------- | ------------- |
| 1253    | 1-2       | Exhaust Pressure                 | Pressure      |
| 1253    | 3-4       | Fuel Pressure Differential  | Pressure Diff |
| 1253    | 5-6       | Crankcase Pressure               | Pressure      |
| 1253    | 7-8       | Coolant Pressure                 | Pressure      |

## Message 5

**Address:** 1254 (Sequential based on address in Message 4)

**Transmits:** 8 bytes/4 parameters.

**Addressing Mode:** Sequential.

| CAN Address | Byte Position | Parameter     | Unit  |
| ----------- | ------------- | ------------- | ----- |
| 1254    | 1-2       | Lambda 1      | La    |
| 1254    | 3-4       | Lambda 1      | La    |
| 1254    | 5-6       | Lambda Target | La    |
| 1254    | 7-8       | Drive Speed   | Speed |

## Message 6

**Address:** 1255 (Sequential based on address in Message 5)

**Transmits:** 8 bytes/4 parameters.

**Addressing Mode:** Sequential.

| CAN Address | Byte Position | Parameter      | Unit        |
| ----------- | ------------- | -------------- | ----------- |
| 1255    | 1-2       | Lambda 1 Short | Percentage2 |
| 1255    | 3-4       | Lambda 2 Short | Percentage2 |
| 1255    | 5-6       | Lambda 2 Long  | Percentage2 |
| 1255    | 7-8       | Lambda 2 Long  | Percentage2 |

## Message 7

**Address:** 1256 (Sequential based on address in Message 6)

**Transmits:** 8 bytes/4 parameters.

**Addressing Mode:** Sequential.

| CAN Address | Byte Position | Parameter           | Unit        |
| ----------- | ------------- | ------------------- | ----------- |
| 1256    | 1-2       | Injector Duty Cycle | Percentage1 |
| 1256    | 3-4       | Ignition Angle      | Ign Angle   |
| 1256    | 5-6       | Baro                | Pressure    |
| 1256    | 7-8       | ECU Temp            | Temperature |

## Message 8

**Address:** 1257 (Sequential based on address in Message 7)

**Transmits:** 8 bytes/4 parameters.

**Addressing Mode:** Sequential.

| CAN Address | Byte Position | Parameter          | Unit            |
| ----------- | ------------- | ------------------ | --------------- |
| 1257    | 1-2       | dTPS               | Rate of Change1 |
| 1257    | 3-4       | dRPM               | Rate of Change2 |
| 1257    | 5-6       | Fuel Cut Level     | Percentage1     |
| 1257    | 7-8       | Ignition Cut Level | Percentage1     |

## Message 9

**Address:** 1258 (Sequential based on address in Message 8)

**Transmits:** 8 bytes/4 parameters.

**Addressing Mode:** Sequential.

| CAN Address | Byte Position | Parameter       | Unit        |
| ----------- | ------------- | --------------- | ----------- |
| 1258    | 1-2       | Ethanol Content | Percentage1 |
| 1258    | 3-4       | G-Force Lat     | G-Force     |
| 1258    | 5-6       | G-Force Long    | G-Force     |
| 1258    | 7-8       | G-Force Vert    | G-Force     |

## Message 10

**Address:** 1259 (Sequential based on address in Message 9)

**Transmits:** 8 bytes/4 parameters.

**Addressing Mode:** Sequential.

| CAN Address | Byte Position | Parameter               | Unit        |
| ----------- | ------------- | ----------------------- | ----------- |
| 1259    | 1-2       | Crank/Cam Error Counter | counter     |
| 1259    | 3-4       | Max Engine Speed        | rpm         |
| 1259    | 5-6       | Sync Position           | Percentage1 |
| 1259    | 7-8       | DTC Count               | counter     |
