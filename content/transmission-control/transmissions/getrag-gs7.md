---
title: "Getrag GS7"
draft: true
---

## Wiring
The OEM Mechatronic unit must be removed so that the transmission can be run directly by the TCM. 

>[!INFO] The example below uses the DomiWorks Install Board.
>  The pullup resistors supplied on the board **should be removed** as pullup control is available on all TCM inputs.

![GS7 Mech Pads](/img/getrag-gs7/gs7_mech_pads.png)

| OEM Pad | Function | TCM Pin |
| ------- | -------- | ------- |
| PA1     | SGND     | SGND |
| PA2     | Clutch A Pressure | An 3 |
| PA3     | +5V      | 5V Out 1 |
| PB1     | SGND     | SGND |
| PB2     | Clutch B Pressure | An 1 |
| PB3     | +5V      | 5V Out 1 |
| PC1     |          |   |
| PC2     | Clutch A Speed | Hall 1 |
| PC3     | Clutch B Speed | Hall 2 |
| PC4     | Fork 4/6 Position | An 2 |
| PC5     | SGND     | SGND |
| PC6     | Fork 5/7 Position | An 4 |
| PC7     | +5V      | 5V Out 1 |
| PC8     | Clutch A Temp ? | An 5 |
| PC9     | +5V      | 5V Out 1 |
| PC10    | Clutch B Temp | 5B Out 1 |
| PC11    | Fork 2/R Position | An 8 |
| PC12    | Fork 1/3 Position | An 7 |
| PC13    | +5V      | 5V Out 1 |
| PD1     | Shift Solenoid 1 | Sol 13 |
| PD2     | Solenoid +12V | Sol +V Out (B33) |
| PD3     | Shift Solenoid 2 | Sol 14 |
| PD4     | Solenoid +12V | Sol  +V Out (B33) |
| PD5     | Shift Solenoid 3 | Sol 15 |
| PD6     | Solenoid +12V | Sol +V Out (B33) |
| PD7     | Shift Solenoid 4 | Sol 16 |
| PD8     | Solenoid +12V | Sol +V Out (B33) |
| PE1     |          |   |
| PE2     |          |   |
| PE3     | SGND     | SGND |
| PE4     |          |   |
| PE5     |          |   |
| PE6     | Trans Fluid Temp | An 9  |
| PE7     | Input Shaft Speed | Hall 3 |
| PE8     |          |   |
| PE9     |          |   |
| PE10    |          |   |
| PE12    |          |   |
| PE13    |          |   |
| PE14    |          |   |
| PE15    |          |   |
| PF1     | Axis A Safety | Sol 2 |
| PF2     | Solenoid + 12V | Sol +V Out (B30) |
| PF3     | Clutch A | Sol Pair 1&4 |
| PF4     | Solenoid + 12V | Sol +V Out (B30) |
| PF5     | Axis B Safety | Sol 6 |
| PF6     | Solenoid + 12V | Sol +V Out (B30) |
| PF7     | Clutch B | Sol Pair 5&8 |
| PF8     | Solenoid + 12V | Sol +V Out (B30) |
| PF9     | Line Pressure Solenoid | Sol 9 |
| PF10    | Solenoid + 12V | Sol +V Out (B30) |
| PF11    | Cooling Flow Solenoid | Sol 10 |
| PF12    | Solenoid + 12V | Sol +V Out (B30) |

## Clutch Geometry
| Clutch    | Plates (S/D) | Friction ID/OD (mm) | Piston ID/OD (mm) |
| --------  | :----------: | :-----------------: | :---------------: |
| Clutch A  | 2(S) + 4(D)  | 190.0 / 218.0       | 190.0 / 209.0 *   |
| Clutch B  | 2(S) + 4(D)  | 121.5 / 162.0       | 96.0 / 142.0 *    |

> \* Piston diameters are close approximations only
