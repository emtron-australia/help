---
title: "Drive Slip Calculation"
weight: 0
---

## Drive Slip

Given as a percentage of the difference between the speed of the driven wheel compared to the speed of an  undriven wheel. The Drive Slip can be both positive and negative.

Drive Slip = Speed Channel 1 - Speed Channel 2

            Speed Channel 2

which is normally expressed as:

Drive Slip = Driven wheel speed - undriven wheel speed

            undriven wheel speed

0.0%      = The driven and undriven wheels are at the same speed.

+10.0%  = The driven wheels are turning 10% faster than the non driven wheels.

-10.0%      = The driven wheels are turning 10% slower than the non driven wheels .

**Example 1 - Drive Slip settings**. Front wheel drive, 4 wheel speed inputs connected.

Drive Speed Front L  = DI 1

Drive Speed Front R  = DI 2

Undriven Speed Rear L  = DI 3

Undriven Speed Rear R  = DI 4

The ECU will average the front wheel speed and load this value into the runtime " Front Axle Speed"

The ECU will average the rear wheel speed and load this value into the runtime " Rear Axle Speed"

Driven Speed Channel =  Front Axle Speed

Undriven Speed Channel =  Rear Axle Speed

**Example 2 - Drive Slip Settings**. Rear wheel drive, 4 wheel speed inputs connected.

Undriven Speed Front L  = DI 1

Undriven Speed Front R  = DI 2

Drive Speed Rear L  = DI 3

Drive Speed Rear R  = DI 4

The ECU will average the front wheel speed and load this value into the runtime " Front Axle Speed"

The ECU will average the rear wheel speed and load this value into the runtime " Rear Axle Speed"

Driven Speed Channel =  Rear Axle Speed

Undriven Speed Channel =   Front Axle Speed

## Turning Slip

The difference between the wheel speeds on the left side of the vehicle and the wheel speeds on the right side of the vehicle. The ECU uses "Front Axle Speed" and "Rear Axle Speed" to calculate this. 

**ECU calculated values**: If sufficient Input Speed channels are selected the ECU can calculate the following addition data.

***Front Axle Speed.*** 

The average of either:

1.  
   1.     The Drive Speed Front L and R or
   1.     The Undriven Speed Front L and R

***Rear Axle Speed.*** 

The average of either:

1.  
   1.     The Drive Speed Rear L and R or
   1.     The Undriven Speed Rear L and R

***Cornering Speed L.*** 

The average of the Speed Front L (driven or undriven) and Speed Rear L (driven or undriven)

***Cornering Speed R.*** 

The average of the Speed Front R (driven or undriven) and Speed Rear R (driven or undriven)

**NOTE:** The ECU will check which speed channels are assigned and use this information to calculate the data. For this to work correctly for example the Speed Front L Driven and Undriven channels can never both be selected.
