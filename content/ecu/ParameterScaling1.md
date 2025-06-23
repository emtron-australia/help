---
title: "Parameter Scaling"
---

ALL data/parameters transmitted from the ECU over CAN have units defined by the corresponding parameter calibration table(s). This can be setup and adjusted through the PC tuning software Emtune.

1. All Data is unsigned
1. All Data is 16 bits
1. Low byte of each word (16bit) is transmitted first.

Examples:

* Temperature in degrees Celsius or Fahrenheit
* Pressure in kPa,&nbsp; PSI,&nbsp; InHg
* Speed in Kph, mph, m/s


* &nbsp;
  * Speed in Kph, mph, m/s

| Type        | Units                | Min Value     | Max Value          | Conversion Raw to Displayed Value                                                                                                                                                                                                          |
| ----------- | -------------------- | ------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Position    | %Posn                | \-100.0 %     | &#49;00.0 %        | Display = ECU value&nbsp; x&nbsp; 0.1 - 100 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; OR ECU value A: &nbsp; 0000 becomes&nbsp; -100.0&nbsp; %&nbsp; &nbsp; ECU value B: &nbsp; 2000 becomes&nbsp; 100.0 %            |
| Pressure    | kPa/PSI              | &#48;.0&nbsp; | &#54;500.0&nbsp;   | Display = ECU value x&nbsp; 0.1&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; OR ECU value A: 0&nbsp; becomes&nbsp; 0.0&nbsp; kPa/PSI&nbsp; &nbsp; ECU value B: 1000 becomes&nbsp; 100.0&nbsp; kPa/PSI&nbsp;        |
| Temperature | oC / oF&nbsp; &nbsp; | \-50.0&nbsp;  | &#50;50.0&nbsp;    | Display = ECU value x&nbsp; 0.1&nbsp; - 50 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; OR ECU value A: 0&nbsp; becomes&nbsp; -50.0 oC/ &nbsp; oF ECU value B: 1500 becomes&nbsp; 100.0 oC&nbsp; / oF &nbsp;             |
| Lambda      | La                   | &#48;.000     | &nbsp; 2.000&nbsp; | Display = ECU value x&nbsp; 0.001 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; OR ECU value A&nbsp; &nbsp; 0&nbsp; becomes&nbsp; 0.000 La &nbsp; &nbsp; ECU value B&nbsp; &nbsp; 1000&nbsp; becomes&nbsp; 1.000 La&nbsp; |



| Type           | Units   | Min Value     | Max Value           | Conversion Raw to Displayed Value                                                                                                                                                                                                                                                                                       |
| -------------- | ------- | ------------- | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Speed          | Kph/mph | &#48;.0&nbsp; | &#54;500.0          | Display = ECU value x&nbsp; 0.1&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; OR ECU value A&nbsp; &nbsp; 0 &nbsp; &nbsp; becomes&nbsp; 0.0&nbsp; kph&nbsp; &nbsp; ECU value B&nbsp; &nbsp; 1000 &nbsp; &nbsp; becomes&nbsp; 100.0&nbsp; kph                                                     |
| Ignition Angle | oBTDC   | \-100.0 oBTDC | &nbsp; 100.0 oBTDC  | Display = ECU value x&nbsp; 0.1 - 100 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; OR ECU value A 1000 becomes&nbsp; 0.0 oBTDC &nbsp; &nbsp; ECU value B 2000 becomes&nbsp; 100.0 oBTDC &nbsp; &nbsp;                                                                                                 |
| Voltage        | V       | &#48;.000     | &nbsp; 20.000&nbsp; | Display = ECU value x&nbsp; 0.001 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; OR ECU value A&nbsp; &nbsp; 0&nbsp; becomes&nbsp; 0.000V &nbsp; &nbsp; ECU value B&nbsp; &nbsp; 20000&nbsp; becomes&nbsp; 20.000V &nbsp; &nbsp;                                                                        |
| Percentage1    | %       | &#48;.0       | &nbsp; 100.0&nbsp;  | Display = ECU value x&nbsp; 0.1 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; OR ECU value A&nbsp; &nbsp; 0&nbsp; becomes&nbsp; 0.0% &nbsp; &nbsp; ECU value B&nbsp; &nbsp; 1000&nbsp; becomes&nbsp; 100.0% &nbsp; &nbsp;                                                                              |
| Percentage2    | %       | \-100.00      | &nbsp; 100.00&nbsp; | Display = ECU value x&nbsp; 0.01 - 100 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; OR ECU value A&nbsp; &nbsp; 0&nbsp; becomes&nbsp; -100.00% &nbsp; &nbsp; ECU value B&nbsp; &nbsp; 10000&nbsp; becomes&nbsp; 0.00% &nbsp; ECU value C&nbsp; &nbsp; 20000&nbsp; becomes&nbsp; +100.00%&nbsp; &nbsp; |



| Type            | Units   | Min Value     | Max Value        | Conversion Raw to Displayed Value                                                                                                                                                                                                                                                                                                           |
| --------------- | ------- | ------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Rate of Change1 | %/sec   | \-100.0&nbsp; | \+ 100.0         | Display = ECU value x&nbsp; 0.1 - 100 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; OR ECU value A&nbsp; &nbsp; 0 &nbsp; &nbsp; becomes&nbsp; -100.0 %/sec&nbsp; &nbsp; ECU value B&nbsp; &nbsp; 1000 &nbsp; &nbsp; becomes&nbsp; 0.0 %/sec Or&nbsp; ECU value B&nbsp; &nbsp; 2000 &nbsp; becomes&nbsp; +100.0 %/sec&nbsp; |
| Rate of Change2 | rpm/sec | \-20000&nbsp; | &#50;0000        | Display = ECU value x &nbsp; - 20000 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; OR ECU value A&nbsp; &nbsp; 0 &nbsp; &nbsp; becomes&nbsp; - 20000 rpm/sec&nbsp; &nbsp; ECU value B&nbsp; &nbsp; 20000 becomes&nbsp; 0 rpm /sec Or&nbsp; ECU value B&nbsp; &nbsp; 40000 &nbsp; becomes +&nbsp; 20000 %/sec&nbsp;         |
| G-Force         | G       | \-10.00 G     | &nbsp; 10.00 G   | Display = ECU value x&nbsp; 0.01 - 10 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; OR ECU value A 0 becomes&nbsp; -10.00 G &nbsp; &nbsp; ECU value B 1000 becomes&nbsp; 0.00 G&nbsp; or ECU value B 2000 becomes&nbsp; 10.00 G&nbsp;                                                                                      |
| RPM             | RPM     | &#48;         | &#51;00000       | Display = ECU value x&nbsp; 1&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; OR ECU value A 0 becomes&nbsp; 0 RPM&nbsp; &nbsp; ECU value B 20000 becomes&nbsp; 20000 RPM&nbsp;                                                                                                                                        |
| Pressure Diff   | kPa/PSI | &#48;.0&nbsp; | &#54;500.0&nbsp; | Display = ECU value x&nbsp; 0.1 - 1000 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; OR ECU value A: 10000&nbsp; becomes&nbsp; 0.0&nbsp; kPa/PSI&nbsp; &nbsp; ECU value B: 8000 becomes&nbsp; - 200.0&nbsp; kPa/PSI &nbsp;                                                                                                 |
| Counter         |         | &#48;&nbsp;   | &#54;5535        | Display = ECU value&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; OR ECU value A&nbsp; &nbsp; 0 &nbsp; &nbsp; becomes &nbsp; 0&nbsp; &nbsp; ECU value B&nbsp; &nbsp; 10 &nbsp; &nbsp; becomes&nbsp; 10&nbsp;                                                                                                         |


| VVT Position | Deg | \-100.0 | \+100.0 | Display = ECU value x&nbsp; 0.1 - 200 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; OR ECU value A: 2000&nbsp; becomes&nbsp; 0.0&nbsp; Deg&nbsp; &nbsp; ECU value B: 2304 becomes&nbsp; 30.4 Deg (Cam Advanced) ECU value 3: 1871 becomes&nbsp; -12.9. Deg (Cam Retarded)&nbsp; |
| ------------ | --- | ------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |


