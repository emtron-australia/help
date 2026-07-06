---
title: "Secondary Balance Table"
---

## Overview

The Secondary Balance Table defines how the total fuel required for each injection event is divided between the **Primary** and **Secondary** injectors.

Table values are expressed as a **percentage (%)** and represent the proportion of the total fuel volume delivered by the Secondary injectors. The remaining fuel is automatically delivered by the Primary injectors.

## Table Values

| Value | Fuel Distribution |
|--------:|-------------------|
| **0%** | 0% Secondary injectors, 100% Primary injectors |
| **50%** | Equal fuel volume delivered by the Primary and Secondary injectors |
| **100%** | 100% Secondary injectors, 0% Primary injectors |

Intermediate values proportionally divide the required fuel between the Primary and Secondary injectors.

> **ℹ️ Note**
>
> The Secondary Balance Table controls the **fuel volume distribution** between the Primary and Secondary injectors. The ECU automatically calculates the individual injector pulse widths based on the injector flow rates and the configured Secondary Balance value to achieve the required total fuel delivery.
>
>When the Primary and Secondary injector flow rates are correctly configured and calibrated, changing the **Secondary Balance** value should have little or no effect on the overall engine air-fuel ratio
> 


![Image](</img/Z Axis50.jpg>)

### Example 1:

**Operating Conditions**

- Primary Injector = 1000 cc/min 
- Secondary Injector = 1000 cc/min 
- Required Total Injector Flow = 20.000 ms 

1) Balance Table = 50.0%(Equal flow from both injectors):<br>
Primary Injector Flow = 10.000ms
Secondary Injector Flow = 10.000ms

2) Balance Table = 25.0%( 25% of the flow supplied from Sec Injectors):<br>
Primary Injector Flow = 15.000ms
Secondary Injector Flow = 5.000ms

3) Balance Table = 75.0%( 75% of the flow supplied from Sec Injectors):<br>
Primary Injector Flow =  5.000ms
Secondary Injector Flow = 15.000ms


### Example 2:

**Operating Conditions**

- Primary Injector = 1000 cc/min
- Secondary Injector = 2000 cc/min
- Required Total Injector Flow = 20.000 ms

1) Balance Table = 50.0%(Equal flow from both injectors):<br>
Primary Injector Flow = 10.000ms
Secondary Injector Flow = 5.000ms

2) Balance Table = 25.0%( 25% of the flow supplied from Sec Injectors):<br>
Primary Injector Flow = 15.000ms
Secondary Injector Flow = 2.500ms

3) Balance Table = 75.0%( 75% of the flow supplied from Sec Injectors):<br>
Primary Injector Flow =  5.000ms
Secondary Injector Flow = 7.500ms

### ⚠️ Note

**Ideally you want to adjust the the Balance Table so the pulse width and hence duty cycle is the same for both Primary and Secondly Injectors. To calculate the Balance value use the following formula:**

### Secondary Balance (to achieve equal Prim/Sec Pulse Widths)

```text
                    (Sec/Prim Ratio × 100)
Secondary Balance = ──────────────────────
                     (1 + Sec/Prim Ratio)
```
Where:

```text
                    (Num Sec Injectors × Inj Size Sec)
Sec/Prim Ratio  = ─────────────────────────────────────
                    (Num Prim Injectors × Inj Size Prim)
```

### Example

Using the data  from the above Example 2:


```text
                    (4 × 2000cc/min)
Sec/Prim Ratio  =  ──────────────────  = 2.00
                    (4 x  1000cc/min)
```

 Secondary Balance (to achieve equal Prim/Sec Pulse Widths): 
```text
                    (2.00× 100)
Secondary Balance = ──────────── = 66.6%
                     (1 + 2.00)
```


![Image](</img/Secondary Balance Table.jpg>)

The above example is from a Mitsubishi EVO IX with staged injectors

---

## Getting creative...

In the case where 2 separate fuel systems are utilized with 2 different fuel types. Example: Gasoline and Methanol

The secondary balance table becomes the runtime the fuel density change is spanned across in the main fuel configuration

See Gasoline to Methanol examples below

![Image](</img/Duel fuel balance.jpg>)

The Stoichiometric custom table should also be spanned across the secondary blend runtime in this application.

![Image](</img/Duel fuel balance 2.jpg>)

