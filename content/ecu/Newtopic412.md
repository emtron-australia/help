---
title: "Secondary Balance Table"
---

**Secondary Balance Table**&nbsp;


![Image](</img/Z Axis50.jpg>)


The Secondary Balance Table describes the ratio for the volume of fuel delivered by each injector to make the total amount of fuel for the injection event.&nbsp;

* &#48;% means all fuel is supplied from the primary injectors
* &#49;00% means all fuel is supplied from the secondary injectors
* &#53;0% being equal volumes of fuel out both primary and secondary injectors.&nbsp;

If the injector settings are correct,&nbsp; table adjustment should have minimal affect on the tune.\

**Example 1:**


Primary Injector = 1000 cc/min

Secondary Injector = 1000 cc/min

Required Total Injector Flow = 20.000 ms


&#49;) Balance Table = 50.0%(Equal flow from both injectors):

Primary Injector Flow = 10.000ms

Secondary Injector Flow = 10.000ms


&#50;) Balance Table = 25.0%( 25% of the flow supplied from Sec Injectors)

Primary Injector Flow = 15.000ms

Secondary Injector Flow = 5.000ms


&#51;) Balance Table = 75.0%( 75% of the flow supplied from Sec Injectors)

Primary Injector Flow =&nbsp; 5.000ms

Secondary Injector Flow = 15.000ms


**Example 2:**


Primary Injector = 1000 cc/min

Secondary Injector = 2000 cc/min

Required Total Injector Flow = 20.000 ms


&#49;) Balance Table = 50.0%(Equal flow from both injectors):

Primary Injector Flow = 10.000ms

Secondary Injector Flow = 5.000ms


&#50;) Balance Table = 25.0%( 25% of the flow supplied from Sec Injectors)

Primary Injector Flow = 15.000ms

Secondary Injector Flow = 2.500ms


&#51;) Balance Table = 75.0%( 75% of the flow supplied from Sec Injectors)

Primary Injector Flow =&nbsp; 5.000ms

Secondary Injector Flow = 7.500ms


Ideally you want to adjust the the Balance Table so the pulse width and hence duty cycle is the same for both Primary and Secondly Injectors. To calculate the Balance value use the following formula:


**Secondary Balance (to achieve equal Prim/Sec Pulse Widths)** **=&nbsp; (Sec/Prim Ratio x 100)**&nbsp;

**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; (1 + Sec/Prim Ratio)**


&nbsp;where ..


**&nbsp;Sec/Prim Ratio = (Num Sec Injectors x Inj Size Sec)**&nbsp;

**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; (Num Prim Injectors x Inj Size Prim).**


Using the data&nbsp; from the above Example 2:


**Sec/Prim Ratio = 4 x 2000 cc/min &nbsp; = 2.00**&nbsp;

**&nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 4 x 1000 cc/min**


**Secondary Balance (to achieve equal Prim/Sec Pulse Widths) = &nbsp; &nbsp; (2.00 x 100)&nbsp; = 66.6%**

**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; (1 + 2.00)** &nbsp;


![Image](</img/Secondary Balance Table.jpg>)

The above example is from a Mitsubishi EVO IX with staged injectors


**Getting creative...**

In the case where 2 separate fuel systems are utilized with 2 different fuel types. Example: Gasoline and Methanol

The secondary balance table becomes the runtime the fuel density change is spanned across in the main fuel configuration

See Gasoline to Methanol examples below

![Image](</img/Duel fuel balance.jpg>)

The Stoichiometric custom table should also be spanned across the secondary blend runtime in this application.

![Image](</img/Duel fuel balance 2.jpg>)





