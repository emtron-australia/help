---
title: "Addressing"
---

&#48;: Single (11-BIT)

&#49;: Sequential (11-BIT)

&#50;: Single (29-BIT)

&#51;: Sequential 29-BIT)


\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_


Addressing


Single: Only the single "CAN Address" is active


\*\* This means data can only be TX/RX **on that single CAN Base Address**


Sequential:&nbsp; The CAN address starts at the "CAN Address"&nbsp; defined then sequentially&nbsp;

increments that address until all the data has been transmitted


\*\* Once the data (TX/RX) on the CAN Base Address is full, the ECU will poll the next address *sequentially* for additional data

&nbsp; &nbsp; IE 1250, 1251, 1252, ...

