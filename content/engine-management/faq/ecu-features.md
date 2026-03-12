---
title: "Emtron ECU Features"
weight: 1
---

![Emtron](/img/emtron-white.svg)

There’s no shortage of engine management platforms on the market today. It’s not much of a leap to say that most of them can achieve similar results when operated by someone familiar with them. So, what makes Emtron different? Extreme flexibility coupled with advanced engine modelling not typically found in aftermarket engine management. This includes the Emtron mathematical torque model, which is a true paradigm shift in the way we approach torque management, motorsport functions, and engine management in general. This is made possible by the Emtron’s advanced air mass modelling.

## Air Mass Modelling
Emtron ECU’s feature a sophisticated air mass model not usually found outside the OE market. The air mass entering the engine is accurately calculated from a variety of sources to allow maximum flexibility of engine tuning.  Numerous air mass calculations can be blended in almost any way, giving the tuner maximum flexibility to account for any situation or edge case. Tuning in terms of air mass instead of raw manifold pressure gives a far greater insight into the dynamic operational conditions of an engine. Tuning in terms of Air Mass Flow can greatly simplify many engine systems, reducing complexity and reducing guess work.

 - Bank or Engine MAP Air Mass
 - Bank or Engine MAF Air Mass
 - Bank or Engine Throttle Air Mass
 - Driver Demand Air Mass
 - 2x Volumetric Efficiency tables, freely configurable, switchable and Z-axis blendable
 - Secondary Load Table
 - Charge Temperature Estimation and offset tables
 - Air Mass Modifier table
 

## Throttle Mass Flow
By measuring the pressure before and after a throttle body, Emtron’s TMF model essentially converts a throttle body into a mass air flow meter, providing a very dynamic and fast air mass calculation that’s perfect for accurately adhering to torque targets without the need for estimate tables or open loop guess work. Throttle Mass Flow modelling also opens up a huge variety of approaches to engine tuning and the ability to easily account for dynamics such as changes in cam timing without compensation tables.

## Expansion Ratio
Emtron’s air mass model can account for changes in engine efficiency based on the engine’s expansion ratio. This means the difference between the inlet manifold pressure and the exhaust manifold pressure. This can be achieved by Installing an Exhaust Manifold Absolute Pressure sensor or using the EMAP Estimation table.

## Fuel Mass Modelling
The primary job of the Air Mass Model is to inform the Emtron Fuel Mass Model. The air mass model, coupled with accurate fuel system and injector data allows the ECU to accurately calculate exactly how to operate the fuel injectors to achieve the desired lambda target, even in the most dynamic environments.

 - Primary and Secondary Injector characterisation with freely customisable 3D Deadtime and Linearisation tables
 - Fuel density modelling, preset based on selected fuel type or custom table
 - Differential fuel pressure correction – Dynamically recalculates the injector flow based on changes in real-time fuel pressure
 - 2x Lambda Target tables
 - 2x Lambda Target Offset tables
 - Fuel Mass Modifier Table
 - Individual Cylinder Trim tables
 - Bank Trim tables
 - Seamless staged injection blending
 - Custom stoichiometric ratio table
 - Z Axis blending on most tables

## Torque Management
Having an accurate picture of air and fuel mass allows the Emtron ECU to accurately calculate real-time engine torque data. There’s no need for lookup tables, torque is mathematically modelled.

Using Throttle Mass Flow, the Emtron ECU can calculate the required air mass for a given torque target, allowing for the kind of advanced torque management required by modern transmissions, as well as a highly refined approach to motorsport functions that are usually achieved with crude cuts and ignition retards.

Emtron torque management uses a priority-based combination of throttle control, ignition retard and cutting to achieve and hold a torque target, all parameters of which can be configured. There’s no need to fill in big tables of cut levels or ignition offsets, the torque model will work out what’s required on the fly.

The result is real torque management that is smoother, faster, and better for engine reliability.

 - Torque based gearshift control for modern transmissions such as the Nissan GR6.
 - Torque based Launch control
 - Torque based Traction control
 - 5x Customisable User Torque Limits

## Features Overview
### Fuel
 - 1 - 16 Injectors
 - Fully fuel mass modelled
 - Sequential, Staged, Group, Non Sequential modes
 - Gasoline Direct Injection (with external driver)
 - GDI/Port Staged
 - Flex fuel fully supported by fuel model
 - Customisable Peak & Hold Injector drivers
 - Primary & secondary injection timing tables
 - Injector Test mode
 - 11x Fuel Model modes
 - 2x Main VE tables
 - Secondary Load table
 - VE Blend Table
 - Fuel Model Blend Table
 - 2x Lambda Target tables, 3x Lambda Target Offset tables
 - Air Mass modifier table, Fuel mass modifier tables
 - MAP, Gear, Engine Temperature, Fuel Temperature, Fuel Pressure, 2x User compensation  - tables
 - Cylinder Trim tables
 - Bank Trim tables
 - Transient compensation tables
 - Starting compensation tables
 - Z Axis blending on most tables

### Ignition
 - 1 – 12 Coils
 - Direct Fire, Wasted Spark, Distributor, Twin Distributor, Direct/Trailing, Wasted/ - Trailing, CDI
 - Powerful 70mA drivers
 - 2x Dwell tables, 1x Dwell offset table
 - Ignition Test mode
 - 2x Main Ignition Tables, switchable, Z-Axis blendable
 - Secondary load table
 - Individual Cylinder Trim tables
 - Advance/Retard Rate tables
 - Starting, Transient, Temperature, MAP, Gear, 2x User compensation tables

### Inputs
 - Input Channels Sources from physical pins or CAN data
 - Configurable fault conditions and DTC’s
 - Limp home limit tables for critical input channels
 - Estimate table fallback for critical channels
 - Ratiometric correction
 - Extensive predefined calibrations
 - Custom user calibrations
 - Arming threshold tables for reluctor speed inputs
 - Configurable digital switch thresholds
 - 4 Channel Trigger Scope
 - 100K samples/second
 - Crank/Sync Inputs
 - Digital Inputs 1-4
 - 32 Mb memory

### General Functions
 - Overrun Fuel Cut
 - Closed Loop Lambda, single or dual bank
 - Cam Switch
 - DBW Control
   - Up to 4 motors
   - Anti-surge air bleed control
   - Throttle body model with %Area/Torque Demand table
 - Idle Speed Control
   - DBW Throttle Mass Flow
   - DBW Position
   - Unipolar Stepper
   - Bipolar Stepper
   - 2 Wire Solenoid
   - 3 Wire Solenoid
   - Idle Ignition Control
 - VVT Cam Control, most types supported.
 - Knock Control
   - Individual cylinder
   - Customisable filtering
   - Cylinder gain and threshold tables
 - Boost Control (Closed Loop)
   - Single Solenoid
   - Dual Solenoid (per Bank control)
   - Push/Pull top port control (CO2)
 - TGV Control
 - Cal Slot Control
 - Closed Loop Stepper Control
 - 3x Engine Speed Limits
   - Torque Control
   - Fuel/Ignition Cut
 - 2x MAP Limits
 - Speed Limit
 - Engine Protection
   - Engine Temperature
   - Oil Pressure
   - Fuel Pressure
   - Exhaust Gas Temperature
 - 2x Fuel Pump Control Functions
 - 2x Fuel Pump Speed Control Functions
 - 2x Cooling Fans
 - 2x AC Fans
 - AC Clutch Control (Basic or Full Control)
 - Tacho Output
 - CE Light Output
 - Purge Solenoid
 - Speedo Output
 - 2x NB Oxy Heater Control
 - Turbo Scavenge Pump
 - Fuel Low Pressure Control (Port)
 - Fuel High Pressure Control (DI)
 - Cruise Control (Torque modelled)
   - Light Output
   - Multiplexed analog switch support
 - Engine Start Control
   - Touch Start/Stop
 - Engine Safety Start Inhibit
 - Engine Immobiliser
 - 6x Shift Solenoids (Liberty / Lenco transmissions)
 - Honda S2000 Temp Gauge Output
 - 5x User Timers
 - 1x Race Timer, 1ms resolution
 - 15x User Functions
   - PWM Duty/Frequency Tables on 1-10
   - Up to 4 Channel combination logic on all

### Motorsport Functions
 - Overrun Boost (Anti Lag)
 - Launch Control
   - Torque Limiting
   - RPM limiting
 - Rolling Launch Control
 - Traction Control
   - Torque (Slip Target)
   - Torque (RPM Target)
   - Drive Slip
   - Output Shaft Slip
 - Gearshift Control
   - Torque OEM Integration
     - Nissan R35 GTR / 370Z
   - Electronic Paddle
   - Manual Sequential
   - Drag – Auto Upshift
   - Basic Gear Cut/Blip Control
 - Differential Control
   - PWM
   - PWM + ACD
   - Yamaha YXZ
 - Trans Brake Control w/ Bump
 - Water Spray
 - Nitrous Control
   - 4 Stages (2x PWM)
   - Fuel mass flow control
 - Flame Control
 - Downshift Rev Matching (Torque based)
 - G-Speed (Accelerometer based speed channel for AWD traction control)

 ### Torque Management
 - 3x Driver Demand Translation tables
 - Driver Demand Translation Clamp table
 - Frictional Loss compensation
 - 5x Independent Torque Control Strategies (used by all torque control functions)
 - Retard Gain
 - Cut Gain
 - Boost Target Margin Offset
 - 5x User Torque Limits
   - Selectable Control Strategy
   - User Channel Enable
   - Main Limit table
   - Limit Offset table

### Communications
 - 2x CAN 2.0B bus nodes
 - 6x Channels per node
 - 4x User Rx data sets
 - 4x User Tx data sets
 - 70x Preset data sets

### Logging
 - 1500+ channels available
 - Up to 500 Hz
 - 32Mb memory, circular or single shot
 - Configurable start/stop conditions
 - Tune and review data in one place. All logging managed and reviewed inside Emtune, no exporting to other software required.