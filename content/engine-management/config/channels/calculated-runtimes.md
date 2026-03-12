---
title: "Calculated Runtimes"
---

## Main

![Image](</img/Config Fuel29.jpg>)

![Image](</img/Config Fuel30.jpg>)

The Calculated runtimes Main is where the Efficiency Calculation and Load Calculation runtimes are defined.

The runtime is defined by nominating the air mass calculation and or blend to used to arrive at the runtime result

This permits the user to quickly utilize more complex forms of efficiency & load calculation

Both the efficiency & load calculation runtimes are labeled with a specific task in mind and also available as a selectable runtime for any table

Example: 

In the KV sample file; note the main VE table load axis (Y axis) is configured as “Efficiency Calculation”, and the main ignition map is configured as “Load Calculation”

## Efficiency Calculation

** Efficiency Calculation is used for Fuel Tables

Select how the runtime calculates Efficiency Calculation

0: MAP

    Manifold Pressure converted to Efficiency Calculation %

    MAP = 55.7kpa

Efficiency Calculation = 55.7%

1: TPS

    Throttle Position converted to Efficiency Calculation %

    TPS = 98.5%

Efficiency Calculation = 98.5% 

2: BAP

    Barometric Pressure converted to Efficiency Calculation %

    BAP = 93.4kpa

Efficiency Calculation = 93.4%

3: MAP/BAP %

    Manifold Pressure divided by Barometric Pressure converted to Efficiency Calculation %

    

MAP = 85kpa

BAP = 87kpa

Efficiency Calculation = (85/87)*100 = 97.70%

4: MAP/EMAP %

Manifold Pressure divided by Barometric Pressure converted to Efficiency Calculation %

    

MAP = 220kpa

EMAP = 240kpa

Efficiency Calculation = (220/240)*100 = 91.66%

5: TPS/BAP %

    Throttle Position divided by Barometric pressure converted to Efficiency Calculation  %

TPS = 98%

BAP = 85kpa

Efficiency Calculation = (98/85)*100 = 115.29%

6: Air Mas Final (mg/cyl)

    Air Mass milligrams per cycle converted to Efficiency Calculation %

    

    Air Mass = 0.121g/cyl

    Efficiency Calculation = 0.121*1000 = 121%

    

    Air Mass = 1.373g/cyl

    Efficiency Calculation = 1.373*1000 = 1373%

7: MAP Bank 1 & 2 Avg

    Manifold Pressure Bank 1 and 2 averaged together converted to Efficiency Calculation %

    MAP Bank 1 = 224kpa

    MAP Bank 2 = 236kpa

    Efficiency Calculation = 224+236/2 = 230%

8: MAP Modelled

    Manifold Pressure Modelled converted to Efficiency Calculation %

    Manifold Pressure Modelled = 155kpa

    Efficiency Calculation = 155%

9: MAP Modelled Bank 1 & 2 Avg

    Manifold Pressure Modelled Bank 1 and 2 averaged together converted to Efficiency Calculation %

    MAP Modelled Bank 1 = 224kpa

    MAP Modelled Bank 2 = 236kpa

    Efficiency Calculation = 224+236/2 = 230%

10 : MAP Modelled/BAP %

Manifold Pressure Modelled divided by Barometric Pressure converted to Efficiency Calculation %

    

MAP Modelled = 85kpa

BAP = 98kpa

Efficiency Calculation = (85/98)*100 = 86.73%

11: MAP Modelled Bank 1 & 2 Avg/BAP %

Manifold Pressure Modelled Bank 1 and 2 averaged together, divided by Barometric Pressure, and converted to Efficiency Calculation %

    MAP Modelled Bank 1 = 75kpa

    MAP Modelled Bank 2 = 78kpa

    BAP = 90kpa

    Efficiency Calculation = ((75+78/2)/90)*100 = 85%


## Load Calculation

** Load Calculation is used for Ignition Tables

Select how the runtime calculates Load Calculation

0: MAP

    Manifold Pressure converted to Load Calculation %

    MAP = 55.7kpa

Load Calculation = 55.7%

1: TPS

    Throttle Position converted to Load Calculation %

    TPS = 98.5%

Load Calculation = 98.5% 

2: BAP

    Barometric Pressure converted to Load Calculation %

    BAP = 93.4kpa

Load Calculation = 93.4%

3: MAP/BAP %

    Manifold Pressure divided by Barometric Pressure converted to Load Calculation %

    

MAP = 85kpa

BAP = 87kpa

Load Calculation = (85/87)*100 = 97.70%

4: MAP/EMAP %

Manifold Pressure divided by Barometric Pressure converted to Load Calculation %

    

MAP = 220kpa

EMAP = 240kpa

Load Calculation = (220/240)*100 = 91.66%

5: TPS/BAP %

    Throttle Position divided by Barometric pressure converted to Load Calculation %

TPS = 98%

BAP = 85kpa

Load Calculation = (98/85)*100 = 115.29%

6: Air Mas Final (mg/cyl)

    Air Mass milligrams per cycle converted to Load Calculation %

    

    Air Mass = 0.121g/cyl

    Load Calculation = 0.121*1000 = 121%

    

    Air Mass = 1.373g/cyl

    Load Calculation = 1.373*1000 = 1373%

7: MAP Bank 1 & 2 Avg

    Load Pressure Bank 1 and 2 averaged together converted to Load Calculation %

    MAP Bank 1 = 224kpa

    MAP Bank 2 = 236kpa

    Load Calculation = 224+236/2 = 230%

8: MAP Modelled

    Manifold Pressure Modelled converted to Load Calculation %

    Manifold Pressure Modelled = 155kpa

    Load Calculation = 155%

9: MAP Modelled Bank 1 & 2 Avg

    Manifold Pressure Modelled Bank 1 and 2 averaged together converted to Load Calculation %

    MAP Modelled Bank 1 = 224kpa

    MAP Modelled Bank 2 = 236kpa

    Load Calculation = 224+236/2 = 230%

10 : MAP Modelled/BAP %

Manifold Pressure Modelled divided by Barometric Pressure converted to Load Calculation %

    

MAP Modelled = 85kpa

BAP = 98kpa

Load Calculation = (85/98)*100 = 86.73%

    

11: MAP Modelled Bank 1 & 2 Avg/BAP %

Manifold Pressure Modelled Bank 1 and 2 averaged together, divided by Barometric Pressure, and converted to Load Calculation %

    MAP Modelled Bank 1 = 75kpa

    MAP Modelled Bank 2 = 78kpa

    BAP = 90kpa

    Load Calculation = ((75+78/2)/90)*100 = 85%
