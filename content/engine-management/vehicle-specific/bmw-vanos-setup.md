---
title: "BMW Vanos Setup"
weight: 0
---

## BMW VANOS Support

Early BMW Motorsport VANOS systems were unique.  It uses an auxiliary oil pump that boosts operating oil pressure to a constantly regulated 100bar of pressure.  The high pressure is used to hydraulically lock the cam position to target during all operating conditions.  The design of the system requires two channels per camshaft as there is no default position (ie – Intake retarded position, exhaust advanced position).  This means there are separate channels for each camshaft for retard and advance.  If the control system is at target, the cams remained hydraulically locked by switching the control system off.  Because of the unique mechanical nature of the system, ECU control must be very specific.  Emtron has developed a special strategy that mimics the OE function, but allows complete flexibility to enable even more precise control. 

BMW Engines that use high pressure BMW Motorsport VANOS 

* BMW S50B30     -     Single VANOS intake cam
* BMW S50B32    -     Double VANOS intake and exhaust cam
* BMW S54         -     Double VANOS intake and exhaust cam
* BMW S62         -     Double VANOS intake and exhaust cam (two banks)

******* USA versions BMW S50B30 (and BMW S52B32) do NOT use BMW Motorsport VANOS.  ***

******* Later Motorsport models updated VANOS to more conventional control.   BMW S65 and BMW S85 use only one output per camshaft like conventional systems.***

When selecting these function types, there will be additional options available for choosing the specific channels for retard or advance channels.  

![Image](</img/NewItem115.png>)

******* BMW Motorsport VANOS is driven high side.  If the installer chooses to drive low side, the solenoids MUST be modified as the flyback diodes will now allow them to be driven low. Diodes must be reversed or removed.***
