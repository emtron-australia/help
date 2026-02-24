---
title: "Cam Position Offsets"
weight: 0
---

## Cam Position Offsets

![Image](</img/VVT 3.jpg>)

Like Crank Position Offset, the ECU must know the offset position of each Camshaft used for Cam Control as well.  

The offset allows the target look up table to either add or subtract desired position based on this entry.  

![Image](</img/VVT 4.jpg>)

To program the Position Offset, the ECU must put the engine into a special mode to return the camshafts to default positions (intake retarded, exhaust advanced).  

Generally, this forces the ECU to stop attempting to regulate the camshafts (VVT solenoids OFF).  

There are 2 methods to achieve the same goal.

## Method 1

Start engine (warm engine)

Set VVT Offset(s) = 1 (ON)

Display VVT Abs Position = choose camshaft to display 

![Image](</img/VVT 5.jpg>)

Under Runtimes (F3, VVT/VVL)

Use absolute position runtimes to populate the offset.  

**Each position represents either a rising or falling edge per cycle (dependent on edge selection under inputs).  **Choose the lowest number**. 

![Image](</img/VVT 6.jpg>)

## Method 2

![Image](</img/VVT 7.jpg>)

Whilst on the Cam Position Offset page

Start engine (warm engine)

Set VVT Offset(s) = 1 (ON)

Open ECU Runtimes (F3) go to VVT/VVL

Use the VVT target Error to validate the position offset number.

This can be do by simply increasing or decreasing the value until as close to zero error is achived

Once completed for each cam, set VVT Offset(s) to = 0 (Off)

![Image](</img/VVT 8.jpg>)

## BMW VANOS Support

Because BMW Motorsport VANOS systems to not return to default positions when the VVT solenoids are OFF, Emtron has a specialized function that will automatically apply a constant duty to the intake retard channels and exhaust advance channels when the Set VVT Offset(s) mode = 1.  This allows the user to program the Position Offsets for each camshaft as normal.  

