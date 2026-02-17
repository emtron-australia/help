---
title: "User 1 Setup"
weight: 39
---

User outputs are configured from this menu item.  Once the function has been enabled in the Functions setup menu the following form may be configured to control the output or status  :

![Image](</img/useroutputform1.png>)

There are up to 4 channels which can produce a result.  When the channel conditions and operations are met the result becomes "TRUE".

Once the result is true the output will perform depending on the how the function has been setup.  1 of 3 options can be configured :

1) Switched. In this mode when the Result is "TRUE" the output simply turns ON

![Image](</img/NewItem14.jpg>)

2) Switch Table.  When the Result is TRUE the Table becomes active .0 = Output = off, 100.0 = ON.  Any other setting does nothing to the output.

![Image](</img/NewItem13.jpg>)

**3**) PWM.  When the Result is TRUE the Table becomes active . The value in the table is the %DC of the output.

