---
title: "TM16-R35 Adapter Datasheet"
---

The TM16-R35 Adapter allows Plug-n-Play control of the Nissan GR6 DCT transmission in the 2007+ R35 GTR.

## Pinout

![Nissan GR6 TCM Pinout](/img/gr6/gr6_tcm_pins.png)

### Connector A (Black)
| OEM Pin | Function            | TM16 Pin |
| ------- | ------------------- | -------- |
| 1       | +14V (TCM Relay)    | C2, C3, C4, C5 |
| 2       | -                   |          |
| 3       | GND                 | B9, B34, C7, C26 |
| 4       | GND                 | B9, B34, C7, C26 |
| 5       | +14V (TCM Relay)    | C2, C3, C4, C5 |
| 6       | -                   |          |
| 7       | GND                 | B9, B34, C7, C26 |
| 8       | GND                 | B9, B34, C7, C26 |
| 9       | Batt +14V           | C1      |
| 10      | Reverse Light Output | Sol 15 (B24) |
| 11      | CAN 1 H             | C8       |
| 12      | -                   |          |
| 13      | -                   |          |
| 14      | TCM Power Relay     | Sol 16 (B25) |
| 15      | CAN 1 L             | C14      |
| 16      | Brake Switch 1      | DI 10 (A27) |
| 17      | Ignition Switch     | C6       |
| 18      | -                   |          |
| 19      | Starter Relay Enable | Aux 8 (B8) |
| 20      | -                   |          |
| 21      | -                   |          |
| 22      | -                   |          |
| 23      | Manual Switch 1     | DI 7 (A27) |
| 24      | -                   |          |
| 25      | 5V Ref 2            | C17      |
| 26      | 5V Ref 2            | C17      |
| 27      | Shifter Pos Switch 1 | ANV 9 (A10) |
| 28      | Manual Switch 2     | DI 8 (A28) |
| 29      | -                   |          |
| 30      | -                   |          |
| 31      | Engine Speed (Tracking) | DI 4 (A21) |
| 32      | -                   |          |
| 33      | Shifter Pos Switch 2 | ANV 10 (A11) |
| 34      | Snow Mode Switch    | DI 13 (A30) |
| 35      | Shifter Pos Switch 4 | ANV 12 (A13) |
| 36      | -                   |          |
| 37      | R Mode Switch       | DI 12 (A29)         |
| 38      | Shifter Pos Switch 3 | ANV 11 (A12) |
| 39      | Up Shift Switch     | DI 5 (A22) |
| 40      | -                   |          |
| 41      | -                   |          |
| 42      | Down Shift Switch   | DI 6 (A23) |
| 43      | Shifter Pos Switch 5 | ANV 13 (A14) |
| 44      | Shifter Pos Switch 6 | ANV 14 (A15) |
| 45      | R Mode Lamp         | Sol 13 (B22) |
| 46      | Shift Lock Solenoid | Aux 6 (B6) |
| 47      | Snow Mode Lamp      | Sol 14 (B23) |
| 48      | -                   |          |

### Connector B (Brown)
| OEM Pin | Function            | TM16 Pin |
| ------- | ------------------- | -------- |
| 49      | Shift Solenoid 1    | Aux 1 (B1) |
| 50      | -                   |          |
| 51      | Shift Solenoid 3    | Aux 3 (B3) |
| 52      | -                   |          |
| 53      | Shift Solenoid 5    | Aux 5 (B5) |
| 54      | Shift Solenoid 2    | Aux 2 (B2) |
| 55      | -                   |          |
| 56      | Shift Solenoid 4    | Aux 4 (B4) |
| 57      | Solenoid Supply     | Sol 1-4 +V (B30) |
| 58      | -                   |          |
| 59      | Solenoid Supply     | Sol 5-8 +V (B31) |
| 60      | -                   |          |
| 61      | -                   |          |
| 62      | Axis A Solenoid     | Sol 3 (B12) |
| 63      | -                   |          |
| 64      | Axis B Solenoid     | Sol 7 (B16) |
| 65      | -                   |          |
| 66      | Sensor GND          | A9, A34, C19 |
| 67      | Shift Fork 1 Pos (Main) | ANV 4 (A4) |
| 68      | Sensor GND          | A9, A34, C19 |
| 69      | Sensor GND          | A9, A34, C19 |
| 70      | Shift Fork 4 Pos (Main) | ANV 8 (A8) |
| 71      | 5V Ref 1            | C16      |
| 72      | Clutch A Speed      | DI 1 (A18) |
| 73      | 5V Ref 1            | C16      |
| 74      | 5V Ref 1            | C16      |
| 75      | 5V Ref 1            | C16      |
| 76      | Speed Sensor +      | *(From TCM Relay)* |
| 77      | Line Pressure Sensor | ANV 1 (A1) |
| 78      | Speed Sensor +      | *(From TCM Relay)* |
| 79      | Shift Fork 1 Pos (Tracking) | ANV 5 (A5) |
| 80      | Sensor GND          | A9, A34, C19 |
| 81      | 5V Ref 1            | C16      |
| 82      | Clutch B Speed      | DI 2 (A19) |
| 83      | Sensor GND          | A9, A34, C19 |
| 84      | Sensor GND          | A9, A34, C19 |
| 85      | Shift Fork 2 Pos (Main) | ANV 6 (A6) |
| 86      | Sensor GND          | A9, A34, C19 |
| 87      | Trans Fluid Temp    | ANV 15 (A16) |
| 88      | 5V Ref 1            | C16      |
| 89      | Park Switch         | DI 14 (A31) |
| 90      | -                   |          |
| 91      | Sensor GND          | A9, A34, C19 |
| 92      | Shift Fork 3 Pos (Main) | ANV 7 (A7) |
| 93      | -                   |          |
| 94      | Sensor GND          | A9, A34, C19 |
| 95      | -                   |          |
| 96      | -                   |          |

### Connector C (Grey)
| OEM Pin | Function            | TM16 Pin |
| ------- | ------------------- | -------- |
| 97      | 5V Ref 1            | C16      |
| 98      | Clutch A Pressure   | ANV 2 (A2) |
| 99      | Sensor GND          | A9, A34, C19 |
| 100     | -                   |          |
| 101     | -                   |          |
| 102     | 5V Ref 1            | C16      |
| 103     | Clutch B Pressure   | ANV 3 (A3) |
| 104     | Sensor GND          | A9, A34, C19 |
| 105     | Speed Sensor +      | *(From TCM Relay)* |
| 106     | Output Shaft Speed  | DI 3 (A20) |
| 107     | Sensor GND          | A9, A34, C19 |
| 108     | -                   |          |
| 109     | -                   |          |
| 110     | -                   |          |
| 111     | -                   |          |
| 112     | -                   |          |
| 113     | Line Pressure Solenoid | Sol 9 (B18) |
| 114     | -                   |          |
| 115     | Lubrication Flow Solenoid | Sol 11 (B20) |
| 116     | -                   |          |
| 117     | -                   |          |
| 118     | Solenoid Supply     | Sol 9-12 +V (B32) |
| 119     | -                   |          |
| 120     | Solenoid Supply     | Sol 9-12 +V (B32) |
| 121     | Solenoid Supply     | Sol 1-4 +V (B30) |
| 122     | -                   |          |
| 123     | Solenoid Supply     | Sol 5-8 +V (B31) |
| 124     | -                   |          |
| 125     | -                   |          |
| 126     | Clutch A Solenoid   | Sol 1 (B10) |
| 127     | -                   |          |
| 128     | Clutch B Solenoid   | Sol 5 (B14) |
