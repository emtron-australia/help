---
title: "Multi-Clutch Shifting"
---

Shifting on multi-clutch transmissions happens over 4 phase:
 1. Fill
 2. Torque Transfer
 3. Inertial Sync
 4. Lock

![Shift Pressure Phases](/img/tm16/shift_pressure_phases.png)
> A simplified representation of the clutch pressures during the 4 shift phases.

The TCM will calculate all required clutch pressures based on supplied and available engine torque. As long as the clutch geometry is configured reasonably and the torque data from the engine is accurate, there's very little tuning required.

>[!WARNING] It is absolutely critical that the engine torque data is accurate.

---

## Line Pressure
>[!CAUTION] 
>DO NOT try to tune the shifting on a multi-clutch transmission by manipulating the Line Pressure.

Line Pressure should be sufficient to supply all the pressure the clutches need during a shift, but the clutches should control their own pressures. 

Clutch pressure can be considered a minimum value for the Line Pressure Target.

Some transmissions will require the Line Pressure to be set very high for the duration of a shift, giving maximum flow control to the clutch solenoids. 

> Depending on the transmission in question, setting the Line Pressure to "Downstream Pressure Offset" mode can simplify this process.

---

## Fill Phase
Any clutch that is disengaged will have it's pressure fully bled off. The job of the fill phase is simply to ensure that the oncoming clutch pressure chamber is filled with fluid so that it can operate as fast as possible once the shift actually starts.

Generally, the clutch pressure at the end of the Fill phase will be the clutch's touch point pressure. The Fill phase is not intended to apply any meaningful clutch pressure.

>[!INFO] Unlike the rest of the shift phases, the fill phase doesn't use torque, it is purely pressure based.

The Fill phase is broken into 3 sub phases:
 1. Pre-Fill
 2. Fast Fill
 3. Stable Fill

The amount of time spent in each phase is limited by the `Total Fill Time` table and the phase order.
```
Stable Fill time = Total Fill Time - (Pre-fill + Fast Fill)
```
**Example:**
 - Pre-fill = 20ms
 - Fast fill = 40ms
 - Total fill time = 100ms

Stable fill = 100 - (20 + 40) = 40ms

Setting a fill phase time to zero will result in that phase being skipped. It's perfectly valid in many cases to skip the Pre-fill or the Fast Fill phase.
It's also common for high torque, high speed shifts to consist of only the Fast-Fill phase. In this case, the Pre-fill Time would be 0 and the Fast Fill Time would take up the entire Total Fill Time. 

> [!INFO] Regardless of the Pre-fill and Fast Fill times, the Fill phase will always exit once the Total Fill Time has elapsed.


### Pre-Fill
The Pre-fill phase simply opens the clutch pressure solenoid at the very start of the shift. The specified pressure is absolute and disregards the touch point.

Pre-fill pressure does not usually exceed the touch point pressure.

**Typical Pressure:** 0.5 - 1.5 Bar
**Typical Time:** 0-100ms

> Setting the `Pre-Fill Time` to 0 will skip the Pre-fill phase.

### Fast Fill
![alt text](/img/tm16/fast_fill.png)

During Fast Fill, the clutch pressure solenoid is driven very high for a short period. The intention is to allow a fast in-rush of fluid to fill the clutch chamber as fast as possible.

>[!CAUTION] 
>A correctly configured combination of Fast Fill Pressure and Fast Fill Time should result in the actual pressure ramping up very quickly to, but never in excess of the touch point.

**Typical Pressure:** 3.0 - 5.0 Bar
**Typical Time:** 20-50ms

### Stable Fill
After the Pre-fill and Fast Fill phases are complete, any remaining Fill Time will be spent in the Stable Fill phase.

The pressure specified during Stable Fill is an **offset** of the clutch's touch point pressure. 

**Example:**
 - Touch Point = 1.3 Bar.
 - Stable Fill Pressure Offset = -0.1 Bar.

Stable Fill Pressure = 1.3 + -0.1 = 1.2 Bar.

**Typical Pressure Offset:** 0.0 Bar (Settle on the Touch Point)

---

## Torque Transfer Phase
The Torque transfer phase begins the process of transferring supplied engine torque over to the oncoming clutch. In most cases, the oncoming clutch will still be fully slipping by the end of the phase, but it will be holding most of if not all the torque.

### Up Shift & Overrun Down Shift
Torque is transferred to the oncoming clutch while the offgoing clutch is mostly released. By the end of the phase, the oncoming clutch will be carrying all the torque, but it will still be fully slipping at the offgoing gear speed.
It's the Inertial Sync phase's job to reduce the slip to zero.

![Up Shift Transfer Torque](/img/tm16/transfer_torque.png)
> Note the engine speed is still matching Clutch A (offgoing) at the end of the transfer phase.

### Driven Down Shift
During a driven down shift, the offgoing clutch's torque capacity is reduced to deliberately introduce a controlled amount of slip that will bring the Input Shaft Speed up to the ongoing gear speed. 
As the clutch slip approaches zero, the oncoming clutch is ramped in to catch the input load, while the offgoing clutch is tapered out. 

By the end of the Transfer phase the oncoming clutch slip should be near zero. 

![Driven Down Shift](/img/tm16/driven_down_shift.png)
> Driven Down Shift with ideal speed synchronization.

### Down Shift Rev Match
During a rev match, both the offgoing and oncoming clutch are reduced to zero torque capacity. They will both settle on their touch points, allowing the engine to freely rev.

As the oncoming slip approaches zero, the oncoming clutch is ramped in to catch the input torque load.

---

## Inertial Sync Phase
During this phase, clutch slip is reduced to near zero and the Input Shaft Speed is synced to the oncoming gear speed. Additional Torque capacity is applied to the oncoming clutch to achieve this.

The engine's inertia and torque is considered when calculating how much torque to apply to control the slip.

At high input torque, prolonged sync times will result in increased clutch heat and wear.

>[!INFO] The main "Gear" runtime will change to the next gear at the start of the Inertial Sync phase.

![Inertial Phase Torque](/img/tm16/inertial_torque.png)
>The Engine Speed is now matching Clutch B (oncoming) at the end of the Inertial Sync phase.

### Torque Reductions
Any torque reduction that is enabled by the user is applied now to aid in syncing the Input Shaft Speed. Using torque reductions mean less clutch capacity is needed to achieve synchronization.

![Up Shift Torque Limit](/img/tm16/up_shift_torque_limit.png)
> Up shift torque limit gets applied at the start of the Inertial Sync phase and is removed as slip approaches zero.

>[!TIP] 
>If the engine continues to limit torque after the clutch is synced and locked, the shift will feel harsh.

There are 3 tables that control the up shift torque limit:
 - **Up Shift Torque Limit Enable**: determines if a torque limit is allowed or not.
 - **Up Shift Torque Limit**: Absolute explicit torque limit value.
 - **Up Shift Torque Reduction**: Torque reduction as a percentage of Engine Torque (Available).

The lowest torque limit output from the tables will be used.

**For Example:**
```
Engine Torque (Available): 800 Nm
Up Shift Torque Limit Enable: ON
Up Shift Torque Limit: 500 Nm
Up Shift Torque Reduction: 40%
```
```
Up Shift Torque Reduction = 800 - (40% of 800) = 800 - 320 = 480 Nm.
```
Because 480 Nm is less than the 500 Nm absolute limit, 480 Nm will be used.

---

## Lock Phase
The Lock phase is used to eliminate any remaining clutch slip. A user definable amount of additional torque capacity is applied to the clutch during the lock phase. 

---

## Shift Tuning
The torque modelled approach to shifting dramatically reduces the tuning complexity of gear shifts for the end user, provided the input torque is accurate and the Clutch Configuration is accurate.

The goal when tuning a shift is simply to achieve the slip target throughout the shift. If the slip is on target then the only thing left to do is dial in the feel by manipulating the shift target times.

The runtimes to watch are `Oncoming Clutch Slip Target` and `Oncoming Clutch Slip`. Ideally they should lay over each other.

If a shift feels harsh, check the slip curve. If the slip is on target, extend the shift times before looking for a way to alter the clutch pressure or clutch torque capacity.

**Tuning Considerations:**
 - The [Clutches Geometry Model](./clutch-model.md) has the most influence over clutch torque calculations during a shift.
 - The amount of torque to added to sync engine speed during the [Inertial Sync Phase](#inertial-sync-phase) is determined by the [Engine's Inertia](./engine-torque.md#engine-inertia) setting. Incorrect engine inertia will result in poor synchronization.

![Ideal Shift Slip Example](/img/tm16/shift_slip_ideal.png)
> Ideal clutch slip curve during an upshift.

### Shift Runtimes
When looking to see what's happening during a shift there are several important runtime channels to watch:

 - **Shift Phase**: Shows which phase the shift is currently in.
 - **Clutch Input Torque**: This is the torque that all the clutch pressure calculations use as their input reference. Most of the time this is the same as `Engine Torque (Supplied)`.
 - **Clutch # Input Torque**: Each clutch may have a different input torque depending on it's current Gear Load Factor Table value. ```Clutch # Input Torque = Clutch Input Torque x Clutch # Gear Load Factor```
 - **Oncoming Clutch Torque Split**: During a shift, this is the calculated torque that the oncoming clutch is required to hold. The value seen here is before any closed loop intervention. It's the raw output of the shift modelling and inertia factors.
 - **Offgoing Clutch Torque Split**: During a shift, this is the calculated torque that the offgoing clutch is required to hold. The value seen here is before any closed loop intervention. It's the raw output of the shift modelling and inertia factors.
 - **Oncoming Clutch Slip Target**: How much slip the oncoming clutch should have for an ideal shift, to meet the user's shift time targets.
 - **Oncoming Clutch Slip**: The actual slip of the oncoming clutch. During ideal shift conditions, this will usually lay over the top of the target value. It's very possible and expected that under some conditions this will not be the case, for example: During a rev-matched downshift where the synchronization of the engine speed is not controlled by the TCM.
 - **Shift P Gain**: Shift closed loop control proportional output.
 - **Shift I Gain**: Shift closed loop control integral output.
 - **Shift D Gain**: Shift closed loop control derivative output.
 - **Clutch # Torque Capacity**: The actual calculated torque capacity of the clutch derived from it's currently applied pressure. This value is after all closed loop control and rate limiting has been applied.

---

## Touch Points
>[!IMPORTANT]
>It is critical that the Clutch Touch Points are setup at the outset. Poorly configured touch points will always lead to bad shifting and drivability.

For detailed information on setting touch points see [here](./touch-points.md).

---

## Clutch Capacity Learning
The [Clutches Geometry Model](./clutch-geometry.md) and engine inertia value will control the majority of the clutch torque applied during a shift. During a shift, the closed loop PID algorithm will make adjustments to the final clutch torque to try and keep the slip curve on target. After a shift, as long as the conditions are met, the [Clutch Capacity Adaption](./clutch-capacity-learning.md) system will look at the previous shift's closed loop output and make small adjustments to the relevant clutch's Learned Capacity Scaler.