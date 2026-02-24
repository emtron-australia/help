---
title: "Upshift Rev-Match Enable Table"
weight: 90
---

## Upshift Rev-Match Enable Table

This table controls when the Rev-Match function is started.

0 = OFF

100 = ON 

Any other value = no change

It is important the Rev-match RPM limiting starts AFTER the initial Torque Reduction Cut/Retard. This is because the Upshift Rev-Match RPM limit will be lower than the current  Engine Speed and will most likely take %cut priority,  preventing the initial Torque Reduction Cut/Retard from working as expected.

