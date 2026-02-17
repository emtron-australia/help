---
title: "Overrun Boost (Anti Lag)"
weight: 53
---

The Overrun Boost (ORB) or Anti-Lag System (ALS) can be switched ON using this menu. 

![Image](</img/NewItem36.png>)

Currently Only Mode 1 is available. 

Mode1 allows either:

* The Throttle plate is NOT permanently opened; the plate operates in its normal range. 
* The Throttle plate is partially cracked opened. In this situation the "Cooldown Mode" MUST be set to ALWAYS ON. See tuning help section for more information.  [Cooldown ALWAYS On](<cooldown-always-on.md>)

Additional air is bleed into the engine using the existing Idle Speed Solenoid /Idle Speed Stepper/DBW. If DBW is enabled to ECU will automatically use this to provide addition air by using an Air Bleed Override Table. Otherwise the Idle Speed Mode selected will be used by the ECU to provide the addition air. i.e Solenoid or Stepper. 

There is an option to add extra air using the Output Channel selection from the ORB Menu shown above. This option allows a device/solenoid to be switched ON or controlled using Duty Cycle from a 3D Table in the Tuning view. This table will ONLY be active when the Anti-Lag system is armed and is switched OFF in Cooldown mode.