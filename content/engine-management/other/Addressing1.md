---
title: "Addressing"
weight: 1001
---

0: Single (11-BIT)

1: Sequential (11-BIT)

2: Single (29-BIT)

3: Sequential 29-BIT)

---

Addressing

Single: Only the single "CAN Address" is active

** This means data can only be TX/RX **on that single CAN Base Address**

Sequential:  The CAN address starts at the "CAN Address"  defined then sequentially 

increments that address until all the data has been transmitted

** Once the data (TX/RX) on the CAN Base Address is full, the ECU will poll the next address *sequentially* for additional data

    IE 1250, 1251, 1252, ...

