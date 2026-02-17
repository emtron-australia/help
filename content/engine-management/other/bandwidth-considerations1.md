---
title: "Bandwidth Considerations"
weight: 1004
---

Bus bandwidth needs to be considered when data is transmitted over CAN. The ECU has Transmit rates from 10Hz up to 1000Hz. 

Example 1:

The following uses the Predefined 1 Tx  DATA set. This uses 10 sequential addresses and it total transmits the value of 40 parameters.  CAN Baud rate at 1Mbps

| Tx Rate    | Number of Messages | Bandwidth Used (%) | Available Bandwidth for other devices |
| ---------- | ------------------ | ------------------ | ------------------------------------- |
| 10Hz   | 10             | 1.2%           | 98.8%                             |
| 50Hz   | 10             | 6.1%           | 93.9%                             |
| 100Hz  | 10             | 12.2%          | 87.8%                             |
| 500Hz  | 10             | 61%            | 39%                               |
| 1000Hz | 10             | Cannot be achieved |                                       |

Example 2:

The following uses the Custom 1 Tx  DATA set. This uses 5 sequential addresses and it total transmits the value of 20 parameters.  CAN Baud rate at 1Mbps

| Tx Rate    | Number of Messages | Bandwidth Used (%) | Available Bandwidth for other devices |
| ---------- | ------------------ | ------------------ | ------------------------------------- |
| 10Hz   | 5              | 0.6%           | 99.4%                             |
| 50Hz   | 5              | 3.05%          | 96.95%                            |
| 100Hz  | 5              | 6.1%           | 93.9%                             |
| 500Hz  | 5              | 30.5%          | 69.5%                             |
| 1000Hz | 5              | 61%            | 39%                               |

