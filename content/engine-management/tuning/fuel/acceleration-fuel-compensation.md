---
title: "Acceleration Fuel Compensation"
weight: 22
---

During rapid changes in throttle position and engine load, fuel delivery does not immediately track the change in airflow. This is due to a portion of the injected fuel temporarily adhering to the intake port walls and intake valves as a liquid film before it evaporates and is drawn into the combustion chamber.

When airflow increases rapidly, additional fuel is temporarily required to establish the larger fuel film while maintaining the correct air-fuel ratio. Without this compensation, the engine will momentarily operate lean, resulting in hesitation, poor throttle response or engine stumble.

Conversely, when airflow decreases rapidly, the existing fuel film continues to evaporate even though less fuel is being injected. This can temporarily enrich the mixture, requiring fuel to be removed to maintain the commanded air-fuel ratio.

Transient Fuel Compensation automatically adds or subtracts fuel during rapid changes in engine airflow to maintain the commanded air-fuel ratio, improve throttle response and ensure smooth engine drivability. During operation, the ECU continuously calculates the following transient fuel runtimes. These values are applied to the **Final Injection Pulse Width** to compensate for transient fuel film dynamics.

| Runtime | Description |
|---------|-------------|
| **Accel Fuel** | Additional injector pulse width calculated during acceleration and added to the Final Injection Pulse Width. |
| **Accel Clamp** | Maximum transient fuel that may be added under the current operating conditions. |
| **Decel Fuel** | Injector pulse width removed during deceleration and subtracted from the Final Injection Pulse Width. |
| **Decel Clamp** | Maximum transient fuel that may be removed under the current operating conditions. |
| **Fuel Accel/Decel Scaler** | Engine Temperature compensation multiplier applied to the calculated Accel Fuel and Decel Fuel corrections. |

---

## Transient Setup

**Accel Enable**  
Enables or disables Transient Acceleration Fuel Compensation.

**Decel Enable**  
Enables or disables Transient Deceleration Fuel Compensation.

**Accel/Decel Mode**  
Selects the runtime input used to initiate the transient fuel compensation function.

| Value | Input |
|--------:|-------|
| **0** | **TPS 1** – Throttle Position Sensor 1 or Drive-By-Wire Servo Position Sensor 1(when enabled) |
| **1** | **MAP** – Manifold Absolute Pressure |
| **2** | **PP 1** – Pedal Position Sensor 1 |

**Accel/Decel Threshold (+/-)**  
Defines the minimum rate of change required to activate the transient fuel compensation function. The threshold is expressed as the rate of change per second.

- Lower values increase sensitivity, causing the function to activate more readily.
- Higher values reduce sensitivity and help prevent unnecessary transient fuel corrections.
- A typical starting value is **1.0 units/second** of the selected input.
  
A typical value is 1.0 %/sec.

---

## Accel Sensitivity Table

The Accel Sensitivity Table is the multiplication factor, expressed as a percentage, that determines the amount of transient fuel added based on the rate of change of the selected Accel/Decel Mode.

### Example:
**Operating Conditions**

- TPS Rate of Change (dTPS1) = **20 %/sec**
- Accel Sensitivity = **10%**
- Base Pulse Width = **5.0 ms**

**Calculation**
```text
Accel Fuel = dTPS1 × Accel Sensitivity
           = 20 × 0.10
           = 2.0 ms

Final Injection Pulse Width
= Base Pulse Width + Accel Fuel
= 5.0 ms + 2.0 ms
= 7.0 ms
```

![Image](</img/Z Axis36.jpg>)

---

## Accel Clamp Table

The Accel Clamp Table limits the maximum amount of additional fuel that can be applied during transient acceleration enrichment events. It defines the maximum allowable increase in injector pulse width (PW), expressed as a percentage of the calculated base fuel pulse width. This prevents excessive transient enrichment during rapid throttle changes, helping to maintain stable air-fuel ratio control and avoiding over-fuelling.

### Example:

**Calculation**
```text
Accel Clamp = 50% 
Base Fuel Pulse Width = 4.0 ms 

Maximum additional fuel allowed: 
= 50% of 4.0 ms 
= 0.5 × 4.0 ms 
= 2.0 ms 

Therefore: 
- Base PW = 4.0 ms 
- Max Accel Enrichment = 2.0 ms 
- Total Maximum PW = 6.0 ms
```

![Image](</img/Z Axis34.jpg>)

---

## Accel Engine Temperature Comp Table

The Accel Engine Temperature Compensation Table introduces a multiplier of the calculated accel fuel value against engine temperature

### Example:
  
**Calculation**
```text
Accel fuel = 10ms
Engine Temperature Comp = 1.5 

Total Accel fuel = 10 * 1.5 = 15.0ms
```


![Image](</img/Z Axis40.jpg>)

---

## Accel Decay Table

The Accel Decay Table defines the rate at which transient acceleration fuel is removed from the fueling calculation. This value determines how quickly the additional enrichment decays over successive engine cycles, expressed as a percentage reduction per cycle.

### Example:
  
**Calculation**
```text

Accel decay = 10%
Accel fuel will decay back 10% every cycle
```

![Image](</img/Z Axis38.jpg>)
