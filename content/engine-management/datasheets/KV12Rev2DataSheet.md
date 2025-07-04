---
title: "KV12 Rev2 Data Sheet"
weight: 2
---

# General &nbsp; &nbsp; &nbsp; &nbsp;


Emtron’s KV12 is a wire in ECU with extreme flexibility.&nbsp; Industry leading I/O count will ensure you do not have to make any sacrifices when configuring your engine and vehicle.&nbsp; This ECU will support up to 12 Channels of fuel and 12 Channels fully sequential Ignition.&nbsp; Every KV12 is housed in a durable billet Aluminium enclosure and includes up to 32MB permanent memory for on board logging, 4-channel oscilloscope function, DBW control up to 2 channels, dual on-board LSU4.9 Lambda controllers, dual digital Knock control, Ethernet communications and 3 axis G-force sensing to name a few.



**Power Supply**

* Operating voltage: 6.0 to 22.0 Volts DC (ECU shutdowns at 24.0V)
* Operating current: 390mA at 14.0V (excluding sensor and load currents)
* Reverse battery protection via external fuse
* “Smart” battery transient protection


**Operating Temperature**

* Max operating range: -30 to 110°C (-22 to 230°F)
* Recommended operating range: -30 to 85°C (-22 to 185°F)


**Physical**

* Aluminium 6061 grade CNC billet enclosure
* Enclosure size 134 mm x 162 mm x 27 mm
* Weight: 730g
* Connector system: 120-way Super Seal waterproof connectors with gold plated contacts

- Pin diameter: 1 mm
- Current rating: maximum 15A per pin (wire gauge dependant)&nbsp;

* Connector A: 26 pin Key 2 Super Seal
* Connector B: 34 pin Key 2 Super Seal
* Connector C: 34 pin Key 1 Super Seal
* Connector D: 26 pin Key 1 Super Seal


**Internal**

* Dual 100MHz processors
* &#53;00Mb DDR RAM (0.5Gb)
* &#51;2MB ECU logging memory

  * Over 1200 channels available
  * &#49;Hz to 500Hz logging rate

* Oscilloscope 4-channel function with 32MB storage

  * Sampling at 100k samples/second
  * Includes Crank and Cam sensor inputs
  * Includes Digital inputs 1-4

* On-Board barometric pressure sensor

  * Range 40 - 115.0 kPa

* &#51;-Axis accelerometer

  * &#49;6-Bit resolution
  * \+2g/+4g/+8g dynamically selectable full-scale
  * Output data rate 500Hz &nbsp;


***

# Outputs


**&#49;2x Port Injector Outputs—high or low ohm**

* Flyback Voltage Clamp 70V
* Independent Saturated or Peak \& Hold control per channel
* &#56;A Peak, 4A hold, 10A Limit Injector Control
* Outputs can be used for ground switching, 6A Continuous, 10A Limit
* All outputs are short circuit and over current protected
* No Flywheel diodes (external diode(s) required for VVT control)


**&#49;2x Ignition Outputs**

* Open collector outputs with Logic Level outputs
* Adjustable Ignition drive current (35mA or 70mA)
* Outputs can be used for Auxiliary ground switching, 1A Continuous, 3A Limit
* All outputs are short circuit and over current protected
* No Flywheel diodes (external diode(s) required for VVT control)
* Ignitor must be used between ECU and coil


**&#49;6x Auxiliary Outputs**

* Variable Valve Timing (VVT) and Variable Valve Timing Electric (VTiE), Drive by Wire (DBW) up to 2 throttle bodies, dual boost control, gearshift solenoids, stepper motor and many more.
* All outputs have PWM control, maximum frequency = 15 kHz
* Flywheel diodes integrated into all outputs&nbsp;

  * Auxiliary 1-8 Flywheel to the “ECU Supply” pin D1 connector D
  * Auxiliary 9-12 Flywheel to the “ECU 9-12 Supply” pin D20 connector D
  * Auxiliary 13-16 Flywheel to the “ECU 13-16 Supply” pin D2 connector D

* All outputs are short circuit and over current protected

&nbsp; &nbsp; **Low Side Drivers**

* Auxiliary 1-4: Low Side 4A continuous, 6A peak modulated, 8A limit&nbsp;
* Auxiliary 5-8: Low Side 2.5A continuous, 4A peak modulated, 5A limit

**High Side Drivers**

* Auxiliary 1-8: High Side 4A continuous, 9A limit

**Half Bridge Drivers**

* Auxiliary 9-12: Half Bridge 5A continuous and 8A limit.&nbsp; Can be used as Low Side, High Side or together for DC motor control (DBW up to 2x channels)
* Auxiliary 13-16: Half Bridge 15.0A continuous (pin limited).&nbsp; Can be used as Low Side, High Side or together for DC motor control (DBW up to 2x channels)

(**NOTE**: Auxiliary 9 -16 can be used to control up to 4x DBW throttle bodies)



**&#49;x EFI Relay Output**

* Low Side Driver for relay control. Current limited to 200mA (Output will switch ON when Ignition Switch Input (D15) is greater than 4V).


**&#49;x Analog Output Buffered**&nbsp;

* Voltage range 0.0 - 5.0V, output current 100mA


**&#49;x Shield Output**

* Connection for Trigger and Knock shielded cables. Short to battery protection&nbsp;


***

# Inputs


**&#49;6x Analog Voltage/Temperature Inputs.**&nbsp;

* Fully configurable including custom calibrations
* Switchable 1k ohm pull-up resistors on ANV 7-12 (available on 6 channels)
* Accepts a 0.0 - 5.000V analog input range. Resolution is 1.22mV (12-Bit)
* Input Impedance 100k Ohms to ground
* &#49;60Hz Low pass filter


**&#56;x Digital/Speed Inputs (DI 1 - 8)**&nbsp;

* Frequency range from 0.0Hz up the 30.0kHz on all 8 channels
* Magnetic and hall/optical effect sensor compatible with programmable trigger edge(s)
* Independent programmable frequency-based arming threshold control, range 0.0 - 12.0V
* Wheel speed, output shaft speed, turbo speed and other frequency-based signals
* VVT position(s) up to 4 channels available on DI 1- 4.
* Accepts a 0.0 - 20.0V analog input.&nbsp; Effective resolution is 4.88mV (10-Bit)

- On/Off switched inputs: AC request, launch enable, cruise switch, table control switching etc with programable switch-based arming threshold control, range 0.0 - 20.0V

* Switchable 4k7 ohm pull-up resistors on all 8 channels to 10.0V
* Maximum/Minimum input signal amplitude +/- 80V


**&#54;x Digital/Switched Inputs (DI 9 - 14)**

* On/Off switched inputs: AC request, Launch enable, cruise switch, table control switching etc with programable switch-based arming threshold control, range 0.0 - 20.0V
* Accepts a 0.0 -20.0 V analog input. Effective resolution is 19.61mV (8-Bit)
* Switchable 4k7 ohm pull-up resistors on all 6 channels to 10.0V


**&#50;x Knock Inputs**

* &#50; Independent knock input channels
* Using Bosch, Digital Knock Integrated Circuit Technology with programmable digital filter coefficients
* Center frequency configurable from 500Hz - 25kHz
* Bandwidth window from 100Hz - 5kHz
* Digital filter window; Hamming or Blackman
* Gain control(x1, x2, x4, x8)
* Cylinder selectable knock input
* Knock control available on ALL Ignition modes (Direct, Wasted, Distributor etc)


**&#49;x Dedicated Ignition Switch Input**

* &#54;.0 - 20.0V input used for EFI Relay Control. (With input \> 4V the EFI Relay output (D9) will switch ON)


**&#50;x Crank Index and Sync Engine Decoding Inputs**

* Magnetic and Hall effect sensor compatible with programable trigger edge(s)
* “True” zero crossing detection on magnetic signals for precise engine position decoding.
* Programmable independent arming threshold control from 0.1V to 12.0V
* Switchable 4k7 ohm pull-up resistor to 5V
* OEM patterns supported&nbsp;
* Maximum input signal amplitude +/- 80V
* Input Impedance 39k ohms to ground


***

# Lambda


**Two Lambda channels supporting the Bosch LSU 4.9 sensor**


* Using Bosch integrated circuit technology for precise sensor control&nbsp;
* Nernst cell temperature measurement for dynamic PID closed loop heater control&nbsp;
* Lambda range: 0.580 La to 10.000 La&nbsp;
* Diagnostics available for each pin and includes, Short to ground, Short to Vbat, Open Load


***

# Voltage and Ground Supplies


**&#49;x ECU Supply Input**

* &#49;5.0A Max (pin limited)
* &#54;V - 22.0V Range
* Supplies ECU power
* Supplies Auxiliary 1-8 High Side Drivers


**&#49;x Auxiliary 9-12 Supply Input**&nbsp;

* &#49;5.0A Max (pin limited)
* Power supply for Auxiliary channels 9 -12. (See KV Series Power Distribution Wiring - A10.pdf for more information on how this should be wired)


**&#49;x Auxiliary 13-16 Supply Input**&nbsp;

* &#49;5.0A Max (pin limited)
* Power supply for Auxiliary channels 13 -16. See KV Series Power Distribution Wiring - A10.pdf for more information on how this should be wired)


**&#50;x 5.0V Sensor Supply**

* &#53;V Vref1 output current 400mA
* &#53;V Vref2 output current 400mA&nbsp;
* Accuracy: +/- 1.0% at 25 °C&nbsp;
* Short circuit, Reverse Battery Protection, Thermal overload protection
* Operating temperature range -40°C&nbsp; ~ 125°C


**&#49;x 8.0V Sensor Supply**

* Output current 600mA
* Accuracy: +/- 1.0% at 25 °C
* Short circuit, Reverse battery protection, Thermal overload protection
* Operating temperature range -40°C&nbsp; ~ 125°C


**&#53;x ECU Main Grounds**

* &#49;5.0A per pin, total 60A


**&#50;x Sensor 0V Reference**&nbsp;

* Analog Sensor 0V Reference with short to battery protection


**NOTE:** The **Sensor 0V Reference** pin(s) are specialised ground outputs for all analog sensors.&nbsp; Connect direct to the sensor 0V pin, **DO NOT** connect to the Engine Block or ECU Ground.


***

# Communications


* &#49;x High Speed Ethernet 100Mbps for tuning software connection
* &#50;x CAN 2.0B 1Mbps/ 6 Channels per node, total 128 messages
