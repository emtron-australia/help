---
title: "Transbrake"
---

>[!WARNING] 
>Transbrake is a motorsport orientated function can lead to transmission and/or other driveline component damage if not used correctly.

The Transbrake function locks up the transmission so that engine load can be applied against the torque converter for staging and launching. It works by applying additional clutches along with the clutches required for the current forward gear. Typically this is achieved by engaging Reverse and First gear at the same time, effectively binding the transmission.

---

## Transbrake Mode
There are two modes of operation:
 - **Forward + Reverse**: Engages the clutches for reverse AND the current forward gear (eg: 1st).
  - **Clutch Select Table**: User definable clutch selection to be applied in combination with the current forward gear's clutches.

---

## Activation
The Tranbrake is activated by the `Transbrake Switch` input. The switch input is configured separately in Input Config.

---

## Lockouts
**Any** of the following lockout conditions will result in the Transbrake being disabled:
 - **Output Shaft Speed Max**: If the output shaft speed exceeds this value, the Transbrake is disabled.
 - **Gear Max**: The transbrake will be disabled above this gear.
 - **User Enable**: A User Function can be selected to act as a lockout. The selected User Function must be ON or the Transbrake will be disabled.

---

## Bump
During a bump, the Transbrake is momentarily released to allow the car to increment forward for staging.
Bump is activated by the `Transbrake Bump Switch` input. The switch input is configured separately in Input Config.

 - **Bump Time**: The Transbrake is released for this amount of time, regardless of the Bump Switch being held for longer.
 - **Bump Cooldown Time**: After a bump, another one cannot be requested until this time has elapsed. 
 
>[!INFO] Repeated Bumps
>To request subsequent bumps, the `Transbrake Bump Switch` switch must be released and re-pressed. Holding the bump switch will not result in repeated bumps.

---

## Interaction with Other Systems
>[!CAUTION]
>Care should be taken to ensure other system lockouts are configured, in particular: **Takeup**.

- **Takeup**: If Takeup's own `Transbrake Lockout` option is set, Takeup control locks itself out whenever the Transbrake is active, so the two won't fight over clutch pressure.
- **Clutch-By-Wire (CBW)**: An active CBW request blocks the Transbrake from ever activating.