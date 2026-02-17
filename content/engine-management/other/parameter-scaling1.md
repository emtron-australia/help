---
title: "Parameter Scaling"
weight: 1040
---

ALL data/parameters transmitted from the ECU over CAN have units defined by the corresponding parameter calibration table(s). This can be setup and adjusted through the PC tuning software Emtune.

1. All Data is unsigned
1. All Data is 16 bits
1. Low byte of each word (16bit) is transmitted first.

Examples:

* Temperature in degrees Celsius or Fahrenheit
* Pressure in kPa,  PSI,  InHg
* Speed in Kph, mph, m/s

*  
  * Speed in Kph, mph, m/s

| Type        | Units                | Min Value     | Max Value          | Conversion Raw to Displayed Value                                                                                                                                                                                                          |
| ----------- | -------------------- | ------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Position    | %Posn                | -100.0 %     | 100.0 %        | Display = ECU value  x  0.1 - 100                   OR ECU value A:   0000 becomes  -100.0  %    ECU value B:   2000 becomes  100.0 %            |
| Pressure    | kPa/PSI              | 0.0  | 6500.0    | Display = ECU value x  0.1                    OR ECU value A: 0  becomes  0.0  kPa/PSI    ECU value B: 1000 becomes  100.0  kPa/PSI         |
| Temperature | oC / oF    | -50.0   | 250.0     | Display = ECU value x  0.1  - 50                   OR ECU value A: 0  becomes  -50.0 oC/   oF ECU value B: 1500 becomes  100.0 oC  / oF               |
| Lambda      | La                   | 0.000     |   2.000  | Display = ECU value x  0.001                   OR ECU value A    0  becomes  0.000 La     ECU value B    1000  becomes  1.000 La  |

| Type           | Units   | Min Value     | Max Value           | Conversion Raw to Displayed Value                                                                                                                                                                                                                                                                                       |
| -------------- | ------- | ------------- | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Speed          | Kph/mph | 0.0  | 6500.0          | Display = ECU value x  0.1                    OR ECU value A    0     becomes  0.0  kph    ECU value B    1000     becomes  100.0  kph                                                     |
| Ignition Angle | oBTDC   | -100.0 oBTDC |   100.0 oBTDC  | Display = ECU value x  0.1 - 100                   OR ECU value A 1000 becomes  0.0 oBTDC     ECU value B 2000 becomes  100.0 oBTDC                                                                                                     |
| Voltage        | V       | 0.000     |   20.000  | Display = ECU value x  0.001                   OR ECU value A    0  becomes  0.000V     ECU value B    20000  becomes  20.000V                                                                            |
| Percentage1    | %       | 0.0       |   100.0   | Display = ECU value x  0.1                   OR ECU value A    0  becomes  0.0%     ECU value B    1000  becomes  100.0%                                                                                  |
| Percentage2    | %       | -100.00      |   100.00  | Display = ECU value x  0.01 - 100                   OR ECU value A    0  becomes  -100.00%     ECU value B    10000  becomes  0.00%   ECU value C    20000  becomes  +100.00%    |

| Type            | Units   | Min Value     | Max Value        | Conversion Raw to Displayed Value                                                                                                                                                                                                                                                                                                           |
| --------------- | ------- | ------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Rate of Change1 | %/sec   | -100.0  | + 100.0         | Display = ECU value x  0.1 - 100                   OR ECU value A    0     becomes  -100.0 %/sec    ECU value B    1000     becomes  0.0 %/sec Or  ECU value B    2000   becomes  +100.0 %/sec  |
| Rate of Change2 | rpm/sec | -20000  | 20000        | Display = ECU value x   - 20000                   OR ECU value A    0     becomes  - 20000 rpm/sec    ECU value B    20000 becomes  0 rpm /sec Or  ECU value B    40000   becomes +  20000 %/sec          |
| G-Force         | G       | -10.00 G     |   10.00 G   | Display = ECU value x  0.01 - 10                   OR ECU value A 0 becomes  -10.00 G     ECU value B 1000 becomes  0.00 G  or ECU value B 2000 becomes  10.00 G                                                                                       |
| RPM             | RPM     | 0         | 300000       | Display = ECU value x  1                    OR ECU value A 0 becomes  0 RPM    ECU value B 20000 becomes  20000 RPM                                                                                                                                         |
| Pressure Diff   | kPa/PSI | 0.0  | 6500.0  | Display = ECU value x  0.1 - 1000                   OR ECU value A: 10000  becomes  0.0  kPa/PSI    ECU value B: 8000 becomes  - 200.0  kPa/PSI                                                                                                   |
| Counter         |         | 0    | 65535        | Display = ECU value                    OR ECU value A    0     becomes   0    ECU value B    10     becomes  10                                                                                                          |

| VVT Position | Deg | -100.0 | +100.0 | Display = ECU value x  0.1 - 200                   OR ECU value A: 2000  becomes  0.0  Deg    ECU value B: 2304 becomes  30.4 Deg (Cam Advanced) ECU value 3: 1871 becomes  -12.9. Deg (Cam Retarded)  |
| ------------ | --- | ------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

