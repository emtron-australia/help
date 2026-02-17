---
title: "Air Mass Modelled (Parameter Blend)"
weight: 72
---

## Air Mass Modelled (Parameter Blend)

![Image](</img/Untitled263.png>)

This mode generates new calculated runtime called "Air Mass Modelled (g/cyl)"  which is a blend of two different air mass parameters. The "Blend Table"

determines the blend ratio between both parameters.

The configuration takes place in: Config -> Channels -> Calculated Runtimes -> Air Mass Modelled Setup. See [Air Mass Modelled Setup](<air-mass-modelled-setup.md>)

![Image](</img/Untitled265.jpg>)

## Air Mass Modelled Blend Parameter 1

Select the method of air mass calculation for Parameter 1

## Air Mass Modelled Blend Parameter 2

Select the method of air mass calculation for Parameter 2

This Fuel mode is most commonly used when bending between Manifold Pressure Sensor and Manifold Pressure Estimate as shown above.  (see further help on MAP Estimate).  

If Air Mass Modelling is not being used, select the same runtime for both parameters or set Air Mass Modelled Blend Table to point towards the appropriate runtime.  

## Air Mass Modelled Blend Table

![Image](</img/NewItem181.png>)

0% = Parameter 1 

100% = Parameter 2

