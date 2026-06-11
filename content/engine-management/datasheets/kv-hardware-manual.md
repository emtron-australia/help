---
title: "KV Series Hardware Manual"
subtitle: "KV8 / KV12 / KV16 / KV16M"
weight: 5
---

**Rev 1.0** &nbsp;•&nbsp; Supported models: **KV8 / KV12 / KV16 / KV16M**

{{< figure src="/img/kv-hardware-manual/page01_img10.jpeg" caption="Emtron KV8 ECU" >}}
{{< figure src="/img/kv-hardware-manual/page01_img11.jpeg" caption="Emtron KV12 ECU" >}}

---

## 1.0 Analog Inputs

The KV series supports up to 24, 12-bit high resolution analog input channels.

| KV ECU | Analog Inputs |
|--------|---------------|
| KV8    | 16            |
| KV12   | 16            |
| KV16   | 16            |
| KV16M  | 24            |

### 1.1 Analog Input Channels 1-16/24

All analog input channels are sampled using high resolution 12-bit analog to digital converters with a 0.0 - 5.000V input range. The ECU uses a high precision internal voltage reference giving high-performance signal conversion. Analog channels 7-12 have configurable 1k ohm pullups so temperature sensors can be connected to these channels when required. All analog inputs can also be used as switched inputs with arming levels programmable from 0.0 – 5.0V.

**Analog Voltage Input 1-24 Summary**

- 16x/24x Analog Inputs with 6 channels available for temperature measurement with switchable pullup resistors
- Fully configurable including custom calibrations
- Switchable 1k ohm pull-up resistors on ANV 7-12 making these inputs suitable for temperature measurement. Pullup supply is to 5.0V Vref1.
- Every input accepts a 0.0 - 5.000V analog input range. Resolution is 1.22mV using a 12-bit analog to digital converter.
- Input Impedance 100k Ohms to ground
- 1st order 160Hz Low pass filter
- All inputs support ratiometric and absolute 3-wire based sensors such as MAP, Throttle position(s) and pressures etc
- AN7-12 support thermistor 2-wire sensors such as engine temperature, inlet air temperature with the pullup resistor switched ON when required.

{{< figure src="/img/kv-hardware-manual/page04_img01.jpeg" caption="Simplified analog input channel — ANV In, 100 kΩ to ground, 0 V Ref." >}}

### 1.2 Analog Temperature Input Channels 7-12

As mentioned in 1.1 these channels have switchable 1k pullup resistors. This allows these channels to support ratiometric and absolute sensors (Pullup switch OFF) or thermistors 2-wire sensors with the pullup(s) switched ON. When the pullup is enabled the ECU applies a ratiometric correction which maintains a very stable output independent of pullup supply variations.

**Analog Voltage Input 7-12 Summary**

- Switchable 1k ohm pull-up resistors, pullup supply to 5.0V Vref1.
- Every input accepts a 0.0 - 5.000V analog input range. Resolution is 1.22mV using a 12-bit analog to digital converter.
- Input Impedance 100k Ohms to ground
- 1st order 160Hz Low pass filter
- Supports either ratiometric and absolute 3-wire based sensors (pullup Off) or thermistor 2-wire sensors with pullup ON when required.

{{< figure src="/img/kv-hardware-manual/page05_img01.jpeg" caption="Analog input 7-12 with switchable 1 kΩ pull-up to 5.0 V Vref1 (for thermistors), or ratiometric mode with the pull-up OFF." >}}

### 1.3 Digital Inputs 1-14 used as analog input(s)

Digital Input channels 1-14 are primarily used to measure frequency based signal and as switched inputs. However, the analog voltage on each digital input is also measured so all digital inputs can support ratiometric and absolute 3-wire based sensors. The input range is extended to 0-20V, which means the effective resolution is 4 times less than Analog Inputs 1-16. For this reason, don't connect engine critical sensors to these channels e.g. Manifold Pressure, Throttle Position, Pedal Position etc. Digital Input channels 1-14 should be used to measure an analog signal once all the dedicated Analog Inputs 1-16/24 have been allocated.

**Digital Analog Inputs 1-8 Summary**

- Accepts a 0.0 - 20.0V analog input. Resolution is 4.88mV (10-Bit)
- Switchable 4k7 pull-up resistor to 8.8V on all 8 channels
- Input Impedance 39k Ohms to ground
- Over and under voltage protection

**Digital Analog Inputs 9-14 Summary**

- Accepts a 0.0 - 20.0V analog input. Resolution is 19.61mV (8-Bit)
- Switchable 4k7 pull-up resistor to 9.4V on all 6 channels
- Input Impedance 70k Ohms to ground

### 1.4 Sensor 0V Reference Pin(s)

These pins are NOT ECU grounds. Although a multi-meter test will show continuity to the ECU ground, these pins are designed as a low current 0V reference for pressure, position and temperature sensors. The following rules **MUST** always be observed:

- **DO NOT** connect these pins to the ECU main ground location(s). This is a specialised ground reference for all analog sensors and should be connected directly to the sensor 0V (ground) pin.
- **DO NOT** connect frequency-based sensor grounds to the 0V Reference pin; for example, an Ethanol content sensor. Use the main ECU ground.

{{< figure src="/img/kv-hardware-manual/page06_img01.png" caption="Incorrect — the 0V Reference must not be branched or shared with another ground point." >}}
{{< figure src="/img/kv-hardware-manual/page06_img02.jpeg" caption="Incorrect — do not daisy-chain the 0V Reference or tie it to the main ECU/engine ground." >}}
{{< figure src="/img/kv-hardware-manual/page06_img03.png" caption="Correct — the 0V Reference is wired directly to the sensor's 0V pin only." >}}

### 1.5 Analog Input configuration example

Table 1.0 shows a typical analog input assignment on a Drive by Wire (DBW) application.

**Table 1.0. Analog Channel 1-16 assignment example.**

| Channel                  | Input Pin                           |
|--------------------------|-------------------------------------|
| Manifold Pressure        | Analog Voltage 1                    |
| Boost Pressure           | Analog Voltage 2                    |
| DBW1 Servo Position Main | Analog Voltage 3                    |
| DBW1 Servo Position Sub  | Analog Voltage 4                    |
| Mass Air Flow Meter 1    | Analog Voltage 5                    |
| Engine Temperature       | Analog Voltage 7 (Pull-up Channel)  |
| Inlet Temperature        | Analog Voltage 8 (Pull-up Channel)  |
| Engine Oil Temperature   | Analog Voltage 9 (Pull-up Channel)  |
| Gearbox Oil Temperature  | Analog Voltage 10 (Pull-up Channel) |
| Fuel Temperature         | Analog Voltage 11 (Pull-up Channel) |
| Engine Oil Pressure      | Analog Voltage 12 (Pull-up Channel) |
| Fuel Pressure            | Analog Voltage 13                   |
| Gear Detection Voltage   | Analog Voltage 14                   |
| Pedal Position Sensor 1  | Analog Voltage 15                   |
| Pedal Position Sensor 2  | Analog Voltage 16                   |

---

## 2.0 Digital Inputs

Digital Inputs 1-14 provide frequency and switched based inputs into the ECU. These inputs have a high level of configurability allowing easy interface to all sensor types. Digital Inputs 1-8 can be used to measure frequency, while all channels can accept a switched input. The analog voltage on all 14 channels is measured and can be used for diagnostics or ratiometric sensor interface.

### 2.1 Digital Input Channels 1-8 – Frequency

- Frequency range from 0.0Hz up to 30.0kHz on all 8 channels
- Magnetic and hall/optical effect sensor compatible with programmable trigger edge(s); rising, falling and both.
- Independent programmable frequency-based arming threshold control, range 0.0 - 12.0V
- Wheel speed, output shaft speed, turbo speed and other frequency-based signals
- VVT position(s) up to 4 channels available on DI 1-4.
- Switchable 4k7 ohm pull-up resistors on all 8 channels to 8.8V
- Filter time constant = 20us
- Maximum/Minimum input signal amplitude +/- 80V
- Input Impedance 39k Ohms to ground.
- Switch Input: Switch to 0V, Switch to VBatt, logic signal

{{< figure src="/img/kv-hardware-manual/page08_img01.jpeg" caption="Digital frequency input — switchable 4k7 pull-up, protection clamp and zero-crossing comparator stage." >}}

**NOTE**

1. ONLY Digital Inputs 1-4 can be used to measure Cam Position(s) for VVT control.
2. The ECU uses "True" zero crossing detection on magnetic based signals. This gives precise 0V crossing detection, critical on magnetic sensors used in VVT control.
3. Emtron Scope function is available on Digital Inputs 1-4.

### 2.11 Arming Threshold Control – Magnetic Sensors

Arming threshold control is primarily used in zero crossing detection of magnetic based signals. The zero crossing circuitry cannot be triggered until the input signal has crossed an "arming" threshold on the positive-going (rising edge) portion of the waveform. Until this happens the zero crossing circuitry is OFF and all zero crossings will be ignored. Once the input signal has exceeded the arming threshold, the zero crossing circuitry is now ready (armed) and waiting for the zero crossing.

The arming threshold values will need adjusting as the signal frequency increases. i.e. signal amplitude is proportional to frequency until the sensor reaches saturation. For this reason, frequency-based signal should use a 2D tables for arming threshold control.

Below is a scope trace showing a signal over one cycle, scaled at 2V/Div. A conventional oscilloscope or the Emtron scope can be used to view a signal to best determine the correct arming thresholds. The preferred method is to find the lowest amplitude during one cycle (highlighted by the red circle below) and make the arming threshold 60% of that value. In this example the lowest value is 1.9V. Taking 60% gives an arming threshold of 1.1V.

{{< figure src="/img/kv-hardware-manual/page09_img01.jpeg" caption="Oscilloscope capture of a magnetic sensor signal (2 V/Div). The red circle marks the lowest amplitude point used to calculate the arming threshold (60% of 1.9 V = 1.1 V)." >}}

In summary when the positive-going input exceeds 1.1V, the zero crossing circuitry becomes armed and is ready to detect the zero crossing on the next falling edge.

### 2.2 Digital Input Channels 1-14 – Switched Input

Digital Input channels 9-14 are for non-frequency based signal such as switched inputs, while Digital Inputs 1-8 are available for both. The status of a switched input (On/Off) is controlled by measuring the analog input voltage and comparing against user defined On threshold and user defined Off threshold. A switched input can supply either a ground or voltage into the ECU.

- Accepts a 0.0 - 20.0V analog input.
- Effective resolution DI 1-8 is 4.88mV (10-Bit)
- Effective resolution DI 9-14 is 19.61mV (8-Bit)
- Switch to 0V, Switch to VBatt, logic signal
- On/Off switched inputs: AC request, launch enable, cruise switch, table control switching etc with programmable switch-based arming threshold control, range 0.0 - 20.0V
- Switchable 4k7 ohm pull-up resistors on all 14 channels.
- Over and under voltage protection.
- Input Impedance DI1-8, 39k ohms to ground
- Input Impedance DI9-14, 70k ohms to ground

{{< figure src="/img/kv-hardware-manual/page10_img01.jpeg" caption="Switched input stage with switchable 4k7 pull-up and comparator." >}}

#### Switch to Ground

In the case of a switch supplying a ground, the pullup resistor needs to be turned ON. With the switch in the OFF position, the ECU input will read the voltage supplied by the pullup resistor. With the switch in the ON position, the pullup resistor voltage is pulled to ground and the ECU input will read close to 0V.

**NOTE:** The current is limited by the 4k7 resistor so pulling the input to ground using the switch will not damage the ECU.

The current can be worked out using Ohms Law: V = I x R. Measure the voltage at the pin with the switch OFF, typically around 9V. Resistor = 4700 Ohm. Current (I) = 9V / 4700 = 1.9mA

{{< figure src="/img/kv-hardware-manual/page10_img02.jpeg" caption="Switch to Ground — pull-up switched ON; the switch pulls the input to 0V." >}}

#### Switch to Power

In the case of a switch supplying power, the pullup resistor needs to be turned OFF. With the switch in the OFF position, the ECU input will read the 0V through the internal pulldown resistor network. With the switch in the ON position, the switch voltage is fed into the ECU input.

**NOTE:** The ECU input is protected against high voltage up to +80V. Feeding the battery voltage into an input will not damage the ECU.

{{< figure src="/img/kv-hardware-manual/page11_img01.jpeg" caption="Switch to Power — pull-up switched OFF; the switch feeds voltage into the protected input." >}}

### 2.3 Digital Input Channels 1-14 – Analog Input

When not used as frequency or switched inputs these channels can be used to measure analog signals for ratiometric and absolute 3-wire based sensors. Refer back to Section 1.3.

### 2.4 Digital Input configuration example

Table 2.0 shows a Digital Input engine configuration example for both Non-VVT and VVT applications.

**Table 2.0. Digital Input engine configuration example**

| DI Input Pin     | Channel (non VVT)      | Channel (VVT)           |
|------------------|------------------------|-------------------------|
| Digital Input 1  | Speed Rear LH          | Intake LH Cam Position  |
| Digital Input 2  | Speed Rear RH          | Intake RH Cam Position  |
| Digital Input 3  | Power Steer switch     | Exhaust LH Cam Position |
| Digital Input 4  | Start Switch           | Exhaust RH Cam Position |
| Digital Input 5  | Clutch Switch          | Speed Front LH          |
| Digital Input 6  | Turbo Speed            | Speed Front RH          |
| Digital Input 7  | Launch Enable Switch   | Speed Rear LH           |
| Digital Input 8  | Fuel Used Reset Switch | Speed Rear RH           |
| Digital Input 9  | Rotary Switch          | Clutch Switch           |
| Digital Input 10 | AC switch              | Start Switch            |
| Digital Input 11 |                        | Launch Enable Switch    |
| Digital Input 12 |                        | Fuel Used Reset Switch  |
| Digital Input 13 |                        | AC switch               |
| Digital Input 14 |                        | Rotary Switch           |

---

## 3.0 Auxiliary Outputs

The ECU has 16 Auxiliary Outputs with a wide variety of driver types to suit all applications. These drives are suitable for controlling relays, resistive and inductive loads, stepper motors, DC servo motors and electronic throttles. All outputs are short circuit and over current protected.

### 3.1 Auxiliary Output 1-8 – Low side or High side

Auxiliary 1-8 drivers can be configured as Off, Low side or High side driving. Low side refers to an open collector output that switches to ground. A High side driver refers to an output that switches to the ECU Supply voltage.

- Auxiliary 1-8 drivers can be configured for Low side or High side driving
- Maximum frequency 15kHz
- Flywheel diode integrated into all outputs with recirculation current to the ECU Supply pin D1
- Pin voltage monitored for diagnostics
- Over current / Short to Battery / Thermal overload protection
- Electrostatic discharge (ESD) protection
- Reverse battery protection

**Low Side Drivers**

- Auxiliary 1-4: Low side 4A continuous, 8A limit
- Auxiliary 5-8: Low side 2.5A continuous, 5A limit

**High Side Drivers**

- Power sourced from the ECU Supply pin
- Auxiliary 1-8: High side 4A continuous, 9A limit

**Suitable applications**

- High frequency solenoids used in Variable Valve Timing (VVT), Variable Valve Timing Electric (VTiE), Idle Speed Control
- Low frequency solenoids used in boost control, gearshift solenoids, stepper motor and many more
- Solenoid and relay switching used in cam switching (VTEC), runner length control and basic fuel pump, fan and AC relay control.

{{< figure src="/img/kv-hardware-manual/page12_img01.jpeg" caption="Auxiliary 1-8 output stage — selectable high-side / low-side driver with integrated flywheel diode to the ECU Supply." >}}

### 3.2 Auxiliary Output 9-12 – Half Bridge

Half bridge drivers supply either a ground or battery voltage i.e. there is no "off" state. Auxiliary outputs 9-12 are medium power half bridge drivers, primarily used for DBW control. Auxiliary 9/10 can be paired into H-bridge configuration for DBW 1 control and Auxiliary 11/12 can be paired into H-bridge configuration for DBW 2 control.

- Driver IC for Aux9-12 needs power using "Aux 9-12 Supply" pin D20. In non-DBW applications the ECU Supply power source can be used. In DBW applications power to this pin **MUST** come from an ECU controlled DBW Relay.
- Maximum frequency 15 kHz
- Flywheel diode integrated into all outputs with recirculation current to the Aux 9-12 Supply pin D20
- Over current / Short to Battery / Thermal overload protection
- Electrostatic discharge (ESD) protection
- Reverse battery protection
- Half Bridge 5A continuous and 8A limit. Can be used as Low Side, High Side or paired with another channel for DC motor control (DBW)

{{< figure src="/img/kv-hardware-manual/page13_img01.jpeg" caption="Auxiliary 9-12 medium-power half-bridge driver (high-side / low-side), powered from the Aux 9-12 Supply." >}}

### 3.3 Auxiliary Output 13-16 – Half Bridge

Half bridge drivers supply either a ground or battery voltage i.e. there is no "off" state. These are high power half bridge drivers used to switch high current inductive loads. In a KV12 and KV16 they can also be paired for DBW control giving a total of 4 DBW channels.

- Driver ICs for Aux13-16 needs power using "Aux 13-16 Supply" pin D2. In non-DBW applications the ECU Supply power source can be used. In DBW applications power to this pin **MUST** come from an ECU controlled DBW Relay.
- Maximum frequency 15 kHz
- Flywheel diode integrated into all outputs with recirculation current to the Aux 13-16 Supply pin D2
- Over current / Short to Battery / Thermal overload protection
- Electrostatic discharge (ESD) protection
- Reverse battery protection
- Half Bridge 15.0A continuous (pin limited). Can be used as Low Side, High Side or paired with another channel for DC motor control (DBW)

{{< figure src="/img/kv-hardware-manual/page13_img02.jpeg" caption="Auxiliary 13-16 high-power half-bridge driver, powered from the Aux 13-16 Supply." >}}

### 3.4 Auxiliary Outputs – Full Bridge Configuration (DBW)

By connecting 2x half bridge outputs together a full bridge can be configured. This is used for DC motor direction and braking control required for applications like DBW control. The below schematic shows Aux 9 and 10 paired to form a full bridge configuration for DBW control.

{{< figure src="/img/kv-hardware-manual/page14_img01.jpeg" caption="Full bridge (H-bridge) formed by pairing Aux 9 and Aux 10 for DBW motor direction and braking control." >}}

The following table 3.0 explains the operation for the full bridge.

**Table 3.0. Full Bridge operation**

| Transistor Q1 | Transistor Q2 | Transistor Q3 | Transistor Q4 | DBW/Motor Direction    | Aux 9 Output | Aux 10 Output |
|:-------------:|:-------------:|:-------------:|:-------------:|------------------------|:------------:|:-------------:|
|      ON       |      OFF      |      OFF      |      ON       | Forward                |      H       |       L       |
|      OFF      |      ON       |      ON       |      OFF      | Reverse                |      L       |       H       |
|      ON       |      OFF      |      ON       |      OFF      | High side Freewheeling |      H       |       H       |
|      OFF      |      ON       |      ON       |      OFF      | Low Side Freewheeling  |      L       |       L       |

For 1 or 2 channels DBW applications the following output pairing is required:

- DBW1, it is recommended to pair Auxiliary 9 and Auxiliary 10 outputs.
- DBW2, it is recommended to pair Auxiliary 11 and Auxiliary 12 outputs.

For KV12 and KV16, 4 channel DBW applications the following output pairing is required:

- DBW3, it is recommended to pair Auxiliary 13 and Auxiliary 14 outputs.
- DBW4, it is recommended to pair Auxiliary 15 and Auxiliary 16 outputs.

### 3.5 Auxiliary Output – Flywheel diodes

Flywheel diodes are used to eliminate the voltage spike or flyback voltage when an inductive load is switched off. The diode recirculates the inductive energy at switch off, so it can be dissipated by the internal resistance of the load. This schematic shows the Low side driver switching off; the red arrows indicate how the current recirculates through the flywheel diode and back through the load. The current will decay until it's insufficient to keep the load On or solenoid open, at which point the load will turn Off.

**Note:** The ECU and load share the same power supply allowing the flywheeling to operate.

{{< figure src="/img/kv-hardware-manual/page15_img01.jpeg" caption="Low-side driver with integrated flywheel diode. The red arrows show the current recirculation path when the driver turns off." >}}

**Important points**

- Flywheel diodes allow inductive energy to be dissipated back into the load
- Flywheel diodes will increase the time it takes for the load to switch off
- Flywheel diodes minimize EMI by removing the inductive voltage spike and forcing the current to recirculate. The higher the frequency the more important this is.

#### 3.51 VVT and Idle Solenoids – why we need flywheel diodes

When controlling VVT solenoids flywheel diodes are required for the solenoid to operate correctly. At frequencies between 200Hz - 300Hz, the flywheel diode prevents the solenoid switching fully On or fully Off. The flywheel diode allows the current to recirculate and find an "average" value during the switch On and switch Off times (duty cycle). Instead of the solenoid switching fully On or fully Off we can control its position between these 2 points. By controlling the duty cycle, the solenoid average position can be controlled.

For this reason, Auxiliary channel 1-16 are recommended for VVT/Idle solenoid control. If however a Fuel or Ignition channel is used an external flywheel **MUST** be fitted.

#### 3.52 Boost Control Solenoid

These solenoids require a fast reduction in current when switched off. As all Auxiliary channels have integrated flywheel diodes this recirculation circuitry slows the switch off time at higher frequencies and will cause solenoid control issues. For this reason, the boost control modulation frequency should be kept below 30Hz. Typical values are 15 – 20Hz.

#### 3.53 Transmission Brake Solenoid

Some Transmission Brake solenoids produce a large amount of energy when released. Auxiliary channels 13-16 are the only outputs with enough current to power such solenoids. It is strongly recommended to run an external flywheel diode to prevent long term ECU damage. If the output is modulated a flywheel diode **MUST** be installed (See Emtron www for details).

**NOTE:** Maximum Trans-brake frequency is 100Hz

### 3.6 Permanently Powered Loads

Auxiliary outputs 1-8 are not suitable for permanently powered loads. The integrated flywheel diode will cause back-feeding onto the flywheel recirculation pin (ECU Power pin) and keep the ECU powered up. This can be viewed using the schematic below. With the Low and High side drivers off, current will flow through the solenoid, through the flywheel diode and back onto the ECU supply. To avoid this issue, move the load to a non-flywheel output such as an unused Fuel or Ignition channel or re-configure the solenoid supply feed.

{{< figure src="/img/kv-hardware-manual/page16_img01.jpeg" caption="A permanently powered load on an Aux 1-8 output back-feeds through the flywheel diode onto the ECU supply, keeping the ECU powered up." >}}

### 3.7 Auxiliary Output configuration example

Table 3.1 shows an Auxiliary output engine configuration example for both Non-VVT and VVT applications.

**Table 3.1. Auxiliary Output engine configuration example**

| Aux Output Pin | Channel (non VVT) | Channel (VVT)           |
|----------------|-------------------|-------------------------|
| Auxiliary 1    | Idle Solenoid     | VVT Intake LH Solenoid  |
| Auxiliary 2    | Boost Solenoid    | VVT Intake RH Solenoid  |
| Auxiliary 3    | Tacho             | VVT Exhaust LH Solenoid |
| Auxiliary 4    | Fuel Pump         | VVT Exhaust RH Solenoid |
| Auxiliary 5    | Fuel Pump Speed   | Cooling Fan             |
| Auxiliary 6    | AC Clutch         | Boost Solenoid          |
| Auxiliary 7    | Cooling Fan       | Tacho                   |
| Auxiliary 8    | Cam Switch        | Fuel Pump               |
| Auxiliary 9    | AC Fan            | DBW 1+                  |
| Auxiliary 10   | CEL               | DBW 1-                  |
| Auxiliary 11   |                   | Downshift Solenoid      |
| Auxiliary 12   |                   | Upshift Solenoid        |
| Auxiliary 13   |                   | AC Fan                  |
| Auxiliary 14   |                   | CEL                     |
| Auxiliary 15   |                   | AC Clutch               |
| Auxiliary 16   |                   | DBW Relay               |

---

## 4.0 Injector Outputs

The KV series supports from 8 up to 16 injector outputs and will control both modes of injection; Saturated and Peak and Hold.

| KV ECU | Injector Outputs |
|--------|------------------|
| KV8    | 8                |
| KV12   | 12               |
| KV16   | 16               |
| KV16M  | 16               |

### 4.1 Injector Control

Precise and consistent control is also gained with a high 70V flyback voltage, allowing for rapid current reduction at switch Off time.

- Flyback Voltage Clamp 70V
- Total current limited to 10A
- Outputs can be used for ground switching, 6A Continuous, 10A Limit
- All outputs are short circuit and over current protected
- Pin voltage monitored for diagnostics
- No Flywheel diodes (external diode(s) required for VVT and Idle Speed control)
- Suitable to connect loads that are permanently powered

#### 4.11 Peak and Hold Injector Control

When using low impedance injectors (< 5 Ohms) the ECU uses a switch mode current limiting technique to minimise heat dissipation in the Injector. This gives better injector control and helps maximize injector life by lowering its operating temperature. Switched Flywheel circuitry is used to recirculate injector current back to the ECU supply during the "Hold" phase. This is ONLY active in Peak and Hold mode.

- Independently configurable Peak and Hold currents up to 16 cylinders
- Flyback Voltage Clamp 70V
- Max Peak current 8A
- Max Hold current 4A
- Total current limited to 10A
- Flywheel recirculation current to the ECU Supply pin D1 during "Hold" phase.

{{< figure src="/img/kv-hardware-manual/page18_img01.jpeg" caption="Peak and Hold injector driver with switched flywheel recirculation to the ECU Supply during the Hold phase." >}}

### 4.2 Saturated Injector Control

Required when injector resistance is greater than 5 Ohms

- Flyback Voltage Clamp 70V
- Total current limited to 10A

{{< figure src="/img/kv-hardware-manual/page19_img01.jpeg" caption="Saturated injector driver with 70 V flyback voltage clamp." >}}

### 4.3 Auxiliary Load Switching on Injector Outputs

When the Injector output is not configured to drive an injector, it can be used to switch or modulate a resistive or inductive load. i.e. relay, waterspray solenoid, Boost solenoid etc.

- Flyback Voltage Clamp 70V
- Total current limited to 10A
- Maximum Frequency 5kHz
- No internal flywheel diodes. VVT and Idle solenoids require external flywheel diodes

### 4.4 Protection

- Over current / Short to Battery protection
- Electrostatic discharge (ESD) protection
- Flyback Voltage Clamp 70V

---

## 5.0 Ignition Outputs

The KV series supports from 8 up to 12 Ignition channels with logic level outputs.

| KV ECU | Ignition Outputs |
|--------|------------------|
| KV8    | 8                |
| KV12   | 12               |
| KV16   | 12               |
| KV16M  | 12               |

### 5.1 Ignition Control

When configured for ignition, these outputs are logic level drivers, capable of sourcing current in the range of 35 - 70mA. **DO NOT** connect directly to a coil and attempt to drive it. An ignitor **MUST** be used between the ECU and coil.

- Open collector output (low side) with active current source control to produce a logic level signal for Ignitor control.
- Adjustable Ignition drive current (35mA or 70mA global control). For example, more current is required when 1 output is driving 2 ignitors.

{{< figure src="/img/kv-hardware-manual/page20_img01.jpeg" caption="Logic-level ignition output driver — open collector with active current source for ignitor control." >}}

### 5.2 Auxiliary Load Switching on Ignition Outputs

When the Ignition output is not configured to drive an ignitor, it can be used to switch or modulate a resistive or inductive load. i.e. relay, waterspray solenoid, Boost solenoid etc.

- Open collector outputs (low side) with current source is OFF.
- Flyback Voltage Clamp 40V
- Continuous current limited to 1A
- Total current limited to 3A
- Maximum Frequency 5kHz
- No internal flywheel diodes. VVT and Idle solenoids require external flywheel diodes

{{< figure src="/img/kv-hardware-manual/page20_img02.jpeg" caption="Ignition output used for auxiliary load switching (current source OFF, 40 V flyback clamp)." >}}

### 5.3 Protection

- Over current / Short to Battery protection
- Electrostatic discharge (ESD) protection
- Flyback Voltage Clamp 40V

---

## 6.0 Crank Index and Sync Sensor Inputs

The KV series supports a Crank Index and Sync position inputs.

- Magnetic and hall/optical effect sensor compatible with programmable trigger edge(s); rising, falling and both.
- "True" zero crossing detection on magnetic signals for precise engine position decoding
- Independent programmable arming threshold control, range 0.0 - 12.0V
- Switchable 4k7 ohm pull-up to 5.0V
- Maximum/Minimum input signal amplitude +/- 80V
- Input Impedance 39k Ohms to ground
- OEM patterns supported

{{< figure src="/img/kv-hardware-manual/page22_img01.jpeg" caption="Crank Index / Sync magnetic input with switchable pull-up and true zero-crossing detection." >}}

For the maximum noise immunity and best possible signal to noise ratio both positive ("+") and negative ("-") inputs should be connected directly to the sensor. **DO NOT** connect a Crank or Cam sensor negative to the ECU ground or engine block, instead use the dedicated negative inputs supplied by the ECU.

**NOTE**

1. Emtron Scope function is available on both Crank Index and Sync inputs.
2. For more information on Arming Thresholds, refer back to section 2.11.

---

## 7.0 Knock Control

- 2x Independent knock input channels
- Fully differential inputs for each channel
- Bosch knock integrated circuit technology using advanced digital signal processing
- Programmable FIR-filter
  - Selectable center frequency from 500Hz - 25kHz
  - Selectable bandwidth from 100Hz - 5kHz
- Selectable Digital Filter Window; Hamming or Blackman
- Gain Control (1x, 2x, 4x, 8x)
- Input anti-aliasing Low pass filter
- Cylinder selectable Knock input
- Individual cylinder Knock control available on ALL Ignition modes with a 720 sync (Direct, Wasted, Distributor etc)
- Diagnostics available for each pin (includes shorted inputs)

---

## 8.0 Lambda Control

The ECU supports on-board dual Lambda controllers using the Bosch LSU4.9 wide band oxygen sensor. The ECU uses Bosch integrated and amplifier control circuitry to give precise sensor control and performs three primary functions:

- Measurement of oxygen concentration
- Sensor temperature for heater control.
- Diagnostics of sensor wiring.

The stability of the LSU4.9 Sensor temperature is critical because measurement of oxygen concentration is temperature sensitive. The ECU uses an advanced control system to measure the internal resistance of the Nernst cell and generate dynamic PID heater and temperature control.

**Lambda LSU4.9 Summary**

- 2x Independent on-board lambda channels supporting the Bosch LSU 4.9 sensor
- Using Bosch integrated circuit technology for precise sensor control
- Nernst cell temperature measurement for dynamic PID closed loop heater and temperature control
- Lambda range: 0.580 La to 10.000 La
- Diagnostics available for each pin includes, Short to ground, Short to Vbatt, Open Load.

---

## 9.0 Supply Voltage Inputs

### 9.1 ECU Supply

The ECUs use a "smart" transient protection system to protect itself from damage against high voltage transients. It constantly monitors the ECU supply voltage and if it exceeds 24V a transient protection system activates and begins limiting/regulating the internal ECU supply at 24V. This effectively clamps the ECU supply protecting it in the short term. Due to the large currents involved, the transient protection system cannot clamp the voltage at 24V indefinitely. After 1 second, if the ECU supply has not returned to less than 24V the transient protection system shuts the power down and the ECU will switch off. The figure below illustrates the operation of the transient protection system by showing the input 300ms transient event vs output characteristics.

{{< figure src="/img/kv-hardware-manual/page24_img01.jpeg" caption="\"Smart\" transient protection behaviour — input voltage surge (80 V) vs the clamped 24 V internal output during a 300 ms event." >}}

- Operating voltage: 6.0 to 22.0 Volts DC (ECU shutdowns at 24.0V)
- Typical operating current: 390mA at 14.0V (excluding sensor and load currents)
- Reverse battery protection via external fuse
- "Smart" battery transient protection
- 15.0A Max (pin limited)
- Power supply for Auxiliary Channels 1-8 High Side Drivers
- Flywheel supply for Injector channels when Peak & Hold mode is active
- Flywheel supply for Auxiliary channels 1-8

### 9.2 Aux 9-12 Supply

This is a dedicated power supply for Auxiliary Channels 9-12 half bridge drivers. Power must be supplied to this pin for these channels to operate correctly. In non-DBW (Drive by Wire) applications the ECU Supply power can be shared, assuming the wire gauge has a sufficient rating for the current demand. In DBW applications power to this pin **MUST** come from an ECU controlled DBW Relay. See the KV Series Power Distribution Wiring for more information on how this should be wired.

- 15.0A Max (pin limited)

### 9.3 Aux 13-16 Supply

This is a dedicated power supply for Auxiliary Channels 13-16. Power must be supplied to this pin for these Auxiliary channels to operate correctly. In non-DBW (Drive by Wire) applications the ECU Supply power can be shared, assuming the wire gauge has a sufficient rating for the current demand. In 4 channel DBW applications power to this pin **MUST** come from an ECU controlled DBW Relay.

- 15.0A Max (pin limited)

---

## 10.0 Regulated Voltage Outputs

The KV series regulated supplies are designed for the harsh automotive environment. They include protection from reverse battery, jump starting transient voltage surges and automatic shutdown when the output is shorted to ground.

**5.0V VRef1**

- Main sensor 5.0V supply
- Continuous current 0.4 Amps
- Accuracy: +/- 1.0% at 25 °C (10mV/V)
- Short circuit, Reverse battery protection, Thermal overload protection
- Operating temperature range -40°C ~ 125°C

**5.0V VRef2**

- Secondary sensor 5.0V supply
- Continuous current 0.4 Amps
- Accuracy: +/- 1.0% at 25 °C (10mV/V)
- Short circuit, Reverse battery protection, Thermal overload protection
- Operating temperature range -40°C ~ 125°C

**8V VCAS**

- Continuous current: 0.6 Amps
- Accuracy: +/- 1.0% at 25 °C
- Short circuit, Reverse battery protection, Thermal overload protection
- Operating temperature range -40°C ~ 125°C

---

## 11.0 EFI Relay Control

The ECU can control an EFI relay, allowing for management of its own power supply. To achieve this a dedicated Ignition Switch Input and EFI Relay Output are used. When 14V is applied to the Ignition Switch input, the ECU internal circuitry switches the EFI relay output On. This will provide a ground, turning the relay On and supplying power to the ECU. Once powered up the ECU takes control on this output. When the Ignition Switch turns Off the ECU can complete critical tasks before shutting itself down (for example, DBW Self calibration and ECU Logging data storage).

{{< figure src="/img/kv-hardware-manual/page26_img01.jpeg" caption="Dedicated EFI relay control circuit — the Ignition Switch input drives the EFI Relay Output (relay ground, 200 mA)." >}}

**Dedicated EFI Relay Control**

- Provides a relay ground, 200mA Limit
- Short circuit, thermal overload protection, reverse battery

**Dedicated Ignition Switch**

- Used to control Main EFI Relay circuit at key-on
- Input Analog Voltage Range: 0 - 20.0V
- Input Impedance 100k Ohms to ground
- Adjustable On/Off software thresholds. Resolution = 0.1V

