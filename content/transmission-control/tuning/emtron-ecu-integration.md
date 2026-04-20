---
title: "Emtron ECU Integration"
weight: 1
---

This document details the steps required for the TCM and ECU to integrate with each other.

## TM16 to Emtron ECU CAN Protocol
The TM16 CAN protocol uses ID's in the rage of 336 to 345 (0x150 to 0x159). Car must be take to ensure that no other devices are using ID's withing that range.

>[!INFO] Channels controlled by Input Functions (eg: Engine Speed) must have their input source set to CAN.


### Transmission Channels
The following channels are transmitted by the TCM:
 - Gear
 - Gear Request
 - Input Shaft Speed
 - Output Shaft Speed
 - Torque Limit (Slow / Throttle)
 - Torque Limit (Fast / Ignition)
 - Up Shift Switch
 - Down Shift Switch

### Engine Channels
The following channels are transmitted but the ECU:
 - Engine Speed
 - Manifold Absolute Pressure
 - Throttle Area Demand
 - Pedal Position Demand
 - Engine Torque (No Reductions)
 - Engine Torque (Final)
 - Driver Demand Torque
 - Brake Switch
 - Engine Temperature
 - Idle Target
 - CE Light

--- 

## TM16 Setup
1. **Set up the CAN Bus:**
    - Ensure the CAN Node is set to the same bitrate as the ECU (eg: 1 MBps)
    - Ensure the CAN bus is correctly terminated
    - Ensure proper CAN bus topology and wiring
    - Assign a CAN Channel to: "Emtron Transmission Control Rx"
    - Assign a second CAN Channel to: "Emtron Transmission Control Tx"

![Emtron CAN Channels](/img/tm16/tm16_emtron_can.png)

3. **Set the following input function sources to "CAN":**
    - Engine Speed (Main)
    - Throttle Position (Main)
    - Pedal Position (Main)
    - Manifold Absolute Pressure

![ECU Channels](/img/tm16/ecu_channels.png)

4. **Set the Torque Model to CAN:**
    - Torque Model Source
    - Driver Demand Source 
![Torque Model CAN](/img/tm16/tq_model_can.png)

---

## ECU Setup
1. **Set up the CAN Bus:**
    - Ensure the CAN Node is set to the same bitrate as the TCM (eg: 1 MBps)
    - Assign a CAN Channel to "Emtron TM16".

![ECU TM16 CAN Mode](/img/tm16/ecu_tm16_can_mode.png)

2. **Enable Gearshift Control: Emtron TM16**

![Gearshift Control: TM16](/img/tm16/gearshift_tm16.png)

3. **Assign the following inputs to "CAN Bus OEM":**
 - Input Shaft Speed
 - Output Shaft Speed
 - Gear Upshift Switch
 - Gear Downshift Switch

 ![TM16 CAN Channels](/img/tm16/tm16_can_oem.png)

 4. **Assign Gear Detection to "CAN Bus OEM"**

 ![ECU Gear Detection Setup](/img/tm16/ecu_gear_detection.png)

 5. **Fill in the Transmission Gear Ratio Table to match the TCM**
 ![ECU Gear Ratio Table](/img/tm16/ecu_gear_ratio_table.png)

 6. **Setup the Torque Model**
 - Normal Torque Model validation applies. Ensure the torque model is well sorted and frictional loss is validated.
 - Set the CAN Bus Reported Torque Modifier Tables to zero unless you have a specific reason to change it.
 
 ![CAN Bus Reported Torque Modifier Table](/img/tm16/can_reported_tq_mod_table.png)
 
 ![CAN Bus Reported Driver Demand Torque Modifier Table](/img/tm16/can_reported_drver_tq_mod_table.png)

 > [!WARNING] It is critical that the ECU's torque model is well sorted.
 
 - **In the TM16 Menu:**
    - Set TM16 Throttle Torque Gain to Zero
    - Set TM16 Retard Torque Gain to Zero
    - Set TCM WOT Torque Lockout Value to -1000 to disable
    - Setup the Engine Cut Setup to suit your application

![TCM Throttle Torque Gain](/img/tm16/tcm_throttle_tq_gain.png)

![TCM Retard Torque Gain](/img/tm16/tcm_retard_tq_gain.png)

![TM16 Setup Menu](/img/tm16/tm16_setup_menu.png)

![TM16 Engine Cut Setup](/img/tm16/tm16_eng_cut_setup.png)

7. **Up Shift Setup:**
 - In Motorsport > Geashift Control TM16: Configure the upshift to your application.

 ![Upshift Setup](/img/tm16/upshift_setup.png)

8. **Down Shift Setup:**
 - In Motorsport > Gearshift Control TM16, configure Downshift for your application.

![Down Shift Setup](/img/tm16/downshift_setup.png)
> [!INFO] Most applications will use a Base Torque Target of 0 nm. This results in the engine holding itself at the rev match target until the clutch grabs it.

9. **Set up the Downshift Rev-Match Torque Target Margin Table:**

This is the amount of torque applied at the start of the downshift to get the engine to the Rev-Match target.
Engine torque is reduced to the Base Torque Target as the engine speed reaches the Rev-Match Target.

![Downshift Rev-Match Torque Target Margin](/img/tm16/downshift_rev_match_tq.png)

## Important Notes
### Upshift Switch
Upshift Switch is only transmitted when the TCM wants a torque limit during the shift. Otherwise, the Gear Request value will simply change to the next gear and the shift will progress without torque intervention.
 The ECU will abide by the torque limit specified by the TCM during a shit.

### Downshift Switch
Downshift Switch is only transmitted when the TCM wants a Rev-Match. Otherwise, the shift will happen without intervention.

### Rev Match Target
The ECU will calculate its own Rev-Match target RPM based on the Output Shaft Speed and Gear Ratio.
> [!WARNING] It is critical that the gear ratio table is correct.

![Down Shifting Log](/img/tm16/downshift_log.png)


