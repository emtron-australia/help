---
title: "KV16M Data Sheet"
weight: 4
---

# General        

Emtron’s KV16M is a motorsport wire-in ECU with extreme flexibility built on the race proven KV16 ECU platform with additional flexibility and reliability utilising a 136-way Deutsch Autosport connector system.  This ECU will support up to 16 Channels of fuel and 12 Channels fully sequential Ignition.  Every KV16M is housed in a durable billet Aluminium enclosure and includes up to 32MB permanent memory for on board logging, 4-channel oscilloscope function, 24 high resolution analog inputs, DBW control up to 4 channels, dual on-board LSU4.9 Lambda controllers, dual digital Knock control, Ethernet communications and 3 axis G-force sensing to name a few.

Power Supply

* Operating voltage: 6.0 to 22.0 Volts DC (ECU shutdowns at 24.0V)
* Operating current: 450mA at 14.0V (excluding sensor and load currents)
* Reverse battery protection via external fuse
* “Smart” battery transient protection
* “Smart” internal ECU hold power control

Operating Temperature

* Max operating range: -30 to 110°C (-22 to 230°F)
* Recommended operating range: -30 to 85°C (-22 to 185°F)

Physical

* Aluminium 6061 grade CNC billet enclosure
* Enclosure size 134 mm x 162 mm x 27 mm
* Weight: 750g
* Waterproof

- Connector system: 136-way waterproof connectors with gold plated contacts
*  

  *  

    * 1 x 55 Way, shell size 16 Deutsch Autosport (Red) 
    * 1 x 26 Way, shell size 16 Deutsch Autosport (Red)
    * 1 x 55 Way, shell size 16 Deutsch Autosport (Yellow)

Internal

* Dual 100MHz processors
* 500Mb DDR RAM (0.5Gb)
* 32MB ECU logging memory

  * Over 1200 channels available
  * 1Hz to 500Hz logging rate

* Oscilloscope 4-channel function with 32MB storage

  * Sampling at 100k samples/second
  * Includes Crank and Cam sensors inputs
  * Includes Digital Inputs 1-4

* 3-Axis accelerometer

  * 16 Bit resolution
  * +2g/+4g/+8g dynamically selectable full-scale
  * Output data rate 500Hz

***

# 2.0 Outputs

16x Injector Outputs—high or low ohm. 

* Flyback Voltage Clamp 70V
* Independent Saturated or Peak & Hold control per channel
* 8A Peak, 4A hold, 10A Limit Injector Control
* Outputs can be used for ground switching, 6A Continuous, 10A Limit
* All outputs are short circuit and over current protected
* No Flywheel diodes (external diode(s) required for VVT control)

12x Ignition Outputs

* Open collector outputs with Logic Level outputs
* Adjustable Ignition drive current (35mA or 70mA)
* Outputs can be used for Auxiliary ground switching, 1A Continuous, 3A Limit
* All outputs are short circuit and over current protected
* No Flywheel diodes (external diode(s) required for VVT control)
* Ignitor must be used between ECU and coil

16x Auxiliary Outputs

* Variable Valve Timing (VVT) and Variable Valve Timing Electric (VTiE), Drive by Wire(DBW) up to 4 throttle bodies, dual boost control, gearshift solenoids, stepper motor and many more.
* All Outputs have PWM Control, maximum frequency = 15 kHz
* Flywheel diodes integrated into all outputs 

  * Aux 1-8 Flywheel to the “Constant 14V Supply” pin 53 Connector C
  * All other Auxiliaries Flywheel to the “ECU 14V Supply” pins

* All Outputs are short circuit and over current protected

    Low Side Drivers

* Auxiliary 1-4: Low Side 4A continuous, 6A peak modulated, 8A limit 
* Auxiliary 5-8: Low Side 2.5A continuous, 4A peak modulated, 5A limit

High Side Drivers

* Auxiliary 1-8: High Side 4A continuous, 9A limit

Half Bridge Drivers

* Auxiliary 9-12: Half Bridge 5A continuous and 8A limit.  Can be used as Low Side, High Side or together for DC motor control (DBW up to 2x channels)
* Auxiliary 13-16: Half Bridge 7.5A continuous (pin limited).  Can be used as Low Side, High Side or together for DC motor control (DBW up to 2x channels)

(NOTE: Auxiliary 9 -16 can be used to control up to 4x DBW throttle bodies)

1x Analog Output Buffered 

* Voltage range 0 - 5.0V, Output current 100mA

2x Shield Outputs

* Connection for Trigger and Knock shielded cables. Short to battery protection

***

# 3.0 Inputs

24x Analog Voltage/Temperature Inputs. 

* Fully configurable including custom calibrations
* Switchable 1k ohm pull-up resistors on ANV 7-12 (available on 6 channels)
* Accepts a 0.0 - 5.000V analog input range. Resolution is 1.22mV (12-Bit)
* Input Impedance 100k Ohms to ground
* 160Hz Low pass filter
*  

8x Digital/Speed Inputs (DI 1 - 8) 

* Frequency range from 0.0Hz up the 30.0kHz on all 8 channels
* Magnetic and hall/optical effect sensor compatible with programable trigger edge(s)
* Independent programable frequency-based arming threshold control, range 0.0 - 12.0V
* Wheel speed, output shaft speed, turbo speed and other frequency-based signals
* VVT position(s) up to 4 channels available on DI 1- 4.
* Accepts a 0.0 - 20.0V analog input.  Effective resolution is 4.88mV (10-Bit)

- On/Off switched inputs: AC request, launch enable, cruise switch, table control switching etc with programable switch-based arming threshold control, range 0.0 - 20.0V

* Switchable 4k7 ohm pull-up resistors on all 8 channels to 10.0V
* Maximum/Minimum input signal amplitude +/- 80V

6x Digital/Switched Inputs (DI 9 - 14)

* On/Off switched inputs: AC request, Launch enable, cruise switch, table control switching etc with programable switch-based arming threshold control, range 0.0 - 20.0V
* Accepts a 0.0 -20.0 V analog input. Effective resolution is 19.61mV (8-Bit)
* Switchable 4k7 ohm pull-up resistors on all 6 channels to 10.0V

2x Knock Inputs

* 2 Independent knock input channels
* Using Bosch, Digital Knock Integrated Circuit Technology with programmable digital filter coefficients
* Center frequency configurable from 500Hz - 25kHz
* Bandwidth window from 100Hz - 5kHz
* Digital filter window; Hamming or Blackman
* Gain control(x1, x2, x4, x8)
* Cylinder selectable knock input
* Knock control available on ALL Ignition modes (Direct, Wasted, Distributor etc)

## 2x Crank and Cam Inputs

* Magnetic and Hall effect sensor compatible with programable trigger edge(s)
* “True” zero crossing detection on magnetic signals for precise engine position decoding.
* Programmable independent arming threshold control from 0.1V to 12.0V
* Switchable 4k7 ohm pull-up resistor to 5V
* OEM patterns supported 
* Maximum input signal amplitude +/- 80V
* Input Impedance 39k ohms to ground

***

# 4.0 Lambda

2x Lambda channels supporting the Bosch LSU 4.9 sensor

* Using Bosch integrated circuit technology for precise sensor control 
* Nernst cell temperature measurement for dynamic PID closed loop heater control 
* Lambda range: 0.580 La to 10.000 La 
* Diagnostics available for each pin and includes, Short to ground, Short to Vbat, Open Load

***

# 5.0 Voltage and Ground Supplies

4x ECU Supply Inputs

* 7.5A per pin, total 30A
* 6V - 22.0V Range
* Supplies ECU power
* Supplies Auxiliary 1-8 High Side Drivers
* Supplies Auxiliary 9 -16 Half bridge Drivers

3x 5.0V Sensor Supply

* 5V Vref1 output current 400mA
* 5V Vref2 output current 400mA 
* 5V Vref3 output current 400mA
* Accuracy: +/- 1.0% at 25 °C 
* Short circuit, Reverse Battery Protection, Thermal overload protection
* Operating temperature range -40°C  ~ 125°C

1x 8.0V Sensor Supply

* Output current 600mA
* Accuracy: +/- 1.0% at 25 °C
* Short circuit, Reverse battery protection, Thermal overload protection
* Operating temperature range -40°C  ~ 125°C

1x Constant 14V Battery Supply 

* Internal ECU EFI Relay Control (Keep-alive function)
* Flywheel supply for Auxiliary Channels 1-8

6x ECU Main Grounds

* 7.5A per pin, total 45A

4x Analog Sensor 0V Reference 

* Analog Sensor 0V Reference with short to battery protection

**NOTE:** The **Analog Sensor 0V Ref** pin(s) are specialised ground outputs for all analog sensors.  Connect direct to the sensor 0V pin, **DO NOT** connect to the Engine Block or ECU Ground.

# 6.0 Communications

* 1x High Speed Ethernet 100Mbps for tuning software connection
* 2x CAN 2.0B 1Mbps/ 6 Channels per node, total 128 messages
