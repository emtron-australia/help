---
title: "Launch Control (RPM) Setup"
weight: 65
---

## Launch Control (RPM) Setup

![Image](</img/Launch 3.jpg>)

![Image](</img/Launch 4.jpg>)

## Launch Control modes of operation.

* **Always On**. The Launch Control system is always ON.
* **Clutch Switch Only**

**Arming**: When the Clutch switch is ON the Launch control is armed. 

**Disarming:** When the Clutch is OFF the Launch Control is in standby.

* **Speed Only**. 

**Arming:** When the Speed is less than the " Arming Speed" the Launch Control is armed. 

**Disarming:** When the Speed is greater than the " Disarm Speed" the Launch control is back into standby mode.

* **Clutch and Speed**. 

**Arming:** When the Clutch switch is ON AND the Speed is less than the " Arming Speed" the Launch Control is armed.

**Disarming:** When the Speed is greater than the " Disarm Speed" the Launch control reverts back into standby mode. 

**NOTE**: The Clutch switch is not used during disarming

## Launch Speed Reference Channel

Sets speed channel referenced by launch control function - can be used to arm/disarm the Launch control system. 

0: OFF

1: Drive Speed

2: Ground Speed

3: Drive Speed Front L

4: Drive Speed Front R

5: Drive Speed Rear L

6: Drive Speed Rear R

7: Undriven Speed Front L

8: Undriven Speed Front R

9: Undriven Speed Rear L

10: Undriven Speed Rear R

11: Front Axle Speed

12: Rear  Axle Speed

13: Vehicle Speed

14: Engine Speed

15: Input Shaft Speed

16: Output Shaft Speed

17: GPS Speed

## Launch Enable Switch Lockout

When set to ON, the Launch Enable Switch can be used to enable/disable the Launch control system.

0: OFF

1: ON

The launch enable switch is found in the software: Config >Channels >Input Setup >Motorsport >Launch Enable switch

## ET Lo Lockout

This is an under-temperature or low engine temperature lockout. 

The Launch Control system will be ready for arming when the Engine Temperature is greater than this value.

This lockout references the Engine Temperature sensor

For the Launch System to be ready for arming the following  must be true:

Throttle/Pedal > Launch TP/PP Lockout setting AND

Engine Temperature > ET Lo Lockout setting AND

Engine Temperature < ET Hi Lockout setting AND

User Lockout = ON (if enabled)

## ET Hi Lockout

This is an over-temperature or high engine temperature lockout. 

The Launch Control system will be ready for arming when the Engine Temperature is less than this value.

This lockout references the Engine Temperature sensor

For the Launch System to be ready for arming the following  must be true:

Throttle/Pedal > Launch TP/PP Lockout setting AND

Engine Temperature > ET Lo Lockout setting AND

Engine Temperature < ET Hi Lockout setting AND

User Lockout = ON (if enabled)

## Launch User Lockout

The Launch Control system will be ready for arming when the User Channel (if assigned) is ON.

For the Launch System to be ready for arming the following  must be true:

Throttle/Pedal > Launch TP/PP Lockout setting AND

Engine Temperature > ET Lockout setting AND

User Lockout = ON (if enabled)

0 = Off

## Launch Limit Type

This sets the type of launch limit to be applied to control the engine speed

0: Fuel Cut Only

1: Ign Cut Only

2: Ign Cut + Fuel Cut

## Cut Pattern

Where the cut pattern for engine speed limiting is set.

0: Random Pattern 1

1: Random Pattern 2

2: Sequential Pattern 1

3: Sequential Pattern 2

## Ign Control Range (-/+)

Sets the engine speed range above or below the launch target rpm limit where ignition cut control is applied

Negative values start to the cut the ignition below the launch target rpm limit

Example: -200 RPM

200 rpm before the cut target the minimum cut clamped value is applied

The ignition cut percentage increases to the maximum cut clamp value at the launch rpm limit

Positive values are above the launch target rpm limit

Example: +200 RPM

At the Launch target rpm limit, the minimum cut clamp percentage value is applied

The ignition cut percentage increases to the maximum cut clamp value at 200 rpm above the Launch target rpm limit.

## Ign Minimum %Cut Clamp

Sets the minimum ignition cut clamp percentage applied at the start of the control range

## Ign Maximum %Cut Clamp

Sets the maximum ignition cut clamp percentage applied at the end of the control range.

## Fuel Control Range (-/+)

Sets the engine speed range above or below the launch target rpm limit where fuel cut control is applied

Negative values start to the cut the fuel below the launch target rpm limit

Example: -200 RPM

200 rpm before the cut target the minimum cut clamped value is applied

The fuel cut percentage increases to the maximum cut clamp value at the launch rpm limit

Positive values are above the launch target rpm limit

Example: +200 RPM

At the Launch target rpm limit, the minimum cut clamp percentage value is applied

The fuel cut percentage increases to the maximum cut clamp value at 200 rpm above the Launch target rpm limit.

## Fuel Minimum %Cut Clamp

Sets the minimum fuel cut clamp percentage applied at the start of the control range

## Fuel Maximum %Cut Clamp

Sets the maximum fuel cut clamp percentage applied at the end of the control range.
