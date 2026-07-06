---
title: "Deceleration Fuel Compensation"
weight: 23
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

## Decel Sensitivity Table

The Decel Sensitivity Table is the multiplication factor, expressed as a percentage, that determines the amount of transient fuel removed based on the rate of change of the selected Accel/Decel Mode.

### Example:
**Operating Conditions**

- TPS Rate of Change (dTPS1) = **10 %/sec**
- Decel Sensitivity = **10%**
- Base Pulse Width = **5.0 ms**

**Calculation**

```text
Decel Fuel = dTPS1 × Accel Sensitivity
           = 10 × 0.10
           = 1.0 ms

Final Injection Pulse Width
= Base Pulse Width - Accel Fuel
= 5.0 ms - 1.0 ms
= 4.0 ms
```

![Image](</img/Z Axis46.jpg>)

---

## Decel Clamp Table

The decel Clamp Table limits the maximum amount of  fuel that can be remvoved during transient deceleration event. It defines the maximum allowable decrease in injector pulse width (PW), expressed as a percentage of the calculated base fuel pulse width. This prevents excessive transient enleanment during rapid throttle changes, helping to maintain stable air-fuel ratio control and avoiding under-fuelling.


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
- Max Decel Enleanment = 2.0 ms 
- Total Maximum PW = 2.0 ms
```

![Image](</img/Z Axis43.jpg>)

---

## Decel Decay Table


The Decel Decay Table controls the rate of decay or how quickly the removed decel fuel is returned as a percentage of an engine cycle

Example:

Decel fuel start value = 10ms
Decel decay = 10%
Decel fuel will decay back to zero 10% per engine cycle


![Image](</img/Z Axis48.jpg>)
