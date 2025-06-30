---
title: "Predefined CAN Transmit Packet 1"
---

**Predefined Dataset 1**


All 16 bit values have low byte transmitted first by the ECU. Sequential addressing is used. All parameters are transferred in the units defined inside the ECU. These can be rescaled if required by the receiving device.&nbsp;

Custom Packet 1 contains 10 Message Objects each with a different sequential address. This can be selected on CAN1 or CAN2 and on any of the 6 channels within that CAN node. In total the Custom Packet 1 transmits 40 parameters on one CAN Channel.


**NOTE: If all 6 channels were used within one CAN node a total of 240 parameter could be transmitted**


**Message 1:**

Address: 1250 (Emtron preferred. User Adjustable)

Transmits 8 bytes/4 parameters.

Addressing Mode = Sequential.

| CAN Address | Byte Position | Parameter                | Unit        |
| ----------- | ------------- | ------------------------ | ----------- |
| &#49;250    | &#49;-2       | Engine Speed             | rpm         |
| &#49;250    | &#51;-4       | Engine Manifold Pressure | Pressure    |
| &#49;250    | &#53;-6       | Engine Temperature       | Temperature |
| &#49;250    | &#55;-8       | Engine Inlet Temp        | Temperature |



**Message 2:**

Address: 1251 (Sequential based on address in Message 1)

Transmits 8 bytes/4 parameters.

Addressing Mode = Sequential.

| CAN Address | Byte Position | Parameter                   | Unit        |
| ----------- | ------------- | --------------------------- | ----------- |
| &#49;251    | &#49;-2       | Throttle Position 1         | Position    |
| &#49;251    | &#51;-4       | Estimated Charge Temp&nbsp; | Temperature |
| &#49;251    | &#53;-6       | Gear                        | NA          |
| &#49;251    | &#55;-8       | Battery Volts               | Voltage     |



**Message 3:**

Address: 1252 (Sequential based on address in Message 2)

Transmits 8 bytes/4 parameters.

Addressing Mode = Sequential.


| CAN Address | Byte Position | Parameter        | Unit        |
| ----------- | ------------- | ---------------- | ----------- |
| &#49;252    | &#49;-2       | Oil Pressure     | Pressure    |
| &#49;252    | &#51;-4       | Oil Temperature  | Temperature |
| &#49;252    | &#53;-6       | Fuel Pressure    | Pressure    |
| &#49;252    | &#55;-8       | Fuel Temperature | Temperature |



**Message 4:**

Address: 1253 (Sequential based on address in Message 3)

Transmits 8 bytes/4 parameters.

Addressing Mode = Sequential.

| CAN Address | Byte Position | Parameter                        | Unit          |
| ----------- | ------------- | -------------------------------- | ------------- |
| &#49;253    | &#49;-2       | Exhaust Pressure                 | Pressure      |
| &#49;253    | &#51;-4       | Fuel Pressure Differential&nbsp; | Pressure Diff |
| &#49;253    | &#53;-6       | Crankcase Pressure               | Pressure      |
| &#49;253    | &#55;-8       | Coolant Pressure                 | Pressure      |



**Message 5:**

Address: 1254 (Sequential based on address in Message 4)

Transmits 8 bytes/4 parameters.

Addressing Mode = Sequential.

| CAN Address | Byte Position | Parameter     | Unit  |
| ----------- | ------------- | ------------- | ----- |
| &#49;254    | &#49;-2       | Lambda 1      | La    |
| &#49;254    | &#51;-4       | Lambda 1      | La    |
| &#49;254    | &#53;-6       | Lambda Target | La    |
| &#49;254    | &#55;-8       | Drive Speed   | Speed |



**Message 6:**

Address: 1255 (Sequential based on address in Message 5)

Transmits 8 bytes/4 parameters.

Addressing Mode = Sequential.

| CAN Address | Byte Position | Parameter      | Unit        |
| ----------- | ------------- | -------------- | ----------- |
| &#49;255    | &#49;-2       | Lambda 1 Short | Percentage2 |
| &#49;255    | &#51;-4       | Lambda 2 Short | Percentage2 |
| &#49;255    | &#53;-6       | Lambda 2 Long  | Percentage2 |
| &#49;255    | &#55;-8       | Lambda 2 Long  | Percentage2 |



**Message 7:**

Address: 1256 (Sequential based on address in Message 6)

Transmits 8 bytes/4 parameters.

Addressing Mode = Sequential.

| CAN Address | Byte Position | Parameter           | Unit        |
| ----------- | ------------- | ------------------- | ----------- |
| &#49;256    | &#49;-2       | Injector Duty Cycle | Percentage1 |
| &#49;256    | &#51;-4       | Ignition Angle      | Ign Angle   |
| &#49;256    | &#53;-6       | Baro                | Pressure    |
| &#49;256    | &#55;-8       | ECU Temp            | Temperature |





**Message 8:**

Address: 1257 (Sequential based on address in Message 7)

Transmits 8 bytes/4 parameters.

Addressing Mode = Sequential.

| CAN Address | Byte Position | Parameter          | Unit            |
| ----------- | ------------- | ------------------ | --------------- |
| &#49;257    | &#49;-2       | dTPS               | Rate of Change1 |
| &#49;257    | &#51;-4       | dRPM               | Rate of Change2 |
| &#49;257    | &#53;-6       | Fuel Cut Level     | Percentage1     |
| &#49;257    | &#55;-8       | Ignition Cut Level | Percentage1     |



**Message 9:**

Address: 1258 (Sequential based on address in Message 8)

Transmits 8 bytes/4 parameters.

Addressing Mode = Sequential.

| CAN Address | Byte Position | Parameter       | Unit        |
| ----------- | ------------- | --------------- | ----------- |
| &#49;258    | &#49;-2       | Ethanol Content | Percentage1 |
| &#49;258    | &#51;-4       | G-Force Lat     | G-Force     |
| &#49;258    | &#53;-6       | G-Force Long    | G-Force     |
| &#49;258    | &#55;-8       | G-Force Vert    | G-Force     |



**Message 10:**

Address: 1259 (Sequential based on address in Message 9)

Transmits 8 bytes/4 parameters.

Addressing Mode = Sequential.

| CAN Address | Byte Position | Parameter               | Unit        |
| ----------- | ------------- | ----------------------- | ----------- |
| &#49;259    | &#49;-2       | Crank/Cam Error Counter | counter     |
| &#49;259    | &#51;-4       | Max Engine Speed        | rpm         |
| &#49;259    | &#53;-6       | Sync Position           | Percentage1 |
| &#49;259    | &#55;-8       | DTC Count               | counter     |


#