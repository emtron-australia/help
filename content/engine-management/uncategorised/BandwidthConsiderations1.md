---
title: "Bandwidth Considerations"
---

Bus bandwidth needs to be considered when data is transmitted over CAN. The ECU has Transmit rates from 10Hz up to 1000Hz.&nbsp;


Example 1:


The following uses the Predefined 1 Tx&nbsp; DATA set. This uses 10 sequential addresses and it total transmits the value of 40 parameters.&nbsp; CAN Baud rate at 1Mbps


| Tx Rate    | Number of Messages | Bandwidth Used (%) | Available Bandwidth for other devices |
| ---------- | ------------------ | ------------------ | ------------------------------------- |
| &#49;0Hz   | &#49;0             | &#49;.2%           | &#57;8.8%                             |
| &#53;0Hz   | &#49;0             | &#54;.1%           | &#57;3.9%                             |
| &#49;00Hz  | &#49;0             | &#49;2.2%          | &#56;7.8%                             |
| &#53;00Hz  | &#49;0             | &#54;1%            | &#51;9%                               |
| &#49;000Hz | &#49;0             | Cannot be achieved |                                       |



Example 2:


The following uses the Custom 1 Tx&nbsp; DATA set. This uses 5 sequential addresses and it total transmits the value of 20 parameters.&nbsp; CAN Baud rate at 1Mbps


| Tx Rate    | Number of Messages | Bandwidth Used (%) | Available Bandwidth for other devices |
| ---------- | ------------------ | ------------------ | ------------------------------------- |
| &#49;0Hz   | &#53;              | &#48;.6%           | &#57;9.4%                             |
| &#53;0Hz   | &#53;              | &#51;.05%          | &#57;6.95%                            |
| &#49;00Hz  | &#53;              | &#54;.1%           | &#57;3.9%                             |
| &#53;00Hz  | &#53;              | &#51;0.5%          | &#54;9.5%                             |
| &#49;000Hz | &#53;              | &#54;1%            | &#51;9%                               |





