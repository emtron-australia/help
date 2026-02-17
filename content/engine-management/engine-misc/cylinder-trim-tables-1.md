---
title: "Cylinder Trim Tables"
weight: 85
---

Emtune has multiple tables for many engine functions.  The table behavior is based on comprehensive selections in Tuning under the respective function (IE, Fuel, Ignition, DBW, Cam control).  Some functions have many tables that can be enabled such as Fuel and Ignition tabs.  These main functions allow you to enable a variety of compensations, modifiers, individual trims, and more.  

For main table controls, the selections are mostly universal.  

(Fuel example shown)

![Image](</img/NewItem117.png>)

Not all of the above example will be available for every function, but generally most functions are the same.  

**ON – Table *** enable those respective tables always. 

**Cal Slot** enables which table is currently being commanded by the Cal Slot Control (see Cal Slot Control)

**Z-Axis** uses a separate X axis lookup that can allow the blending of all the available tables.  

![Image](</img/NewItem116.png>)

Any runtime can be used, and the units equal which table to run in this case.  You can see in the above example the ECU will switch (and interpolate in between) the three different tables available based on TP1 position.  

*** Blend** tables allow switching between two tables only.  

