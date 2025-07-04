---
title: "CAN Parameter Scaling"
---

{{% badge style="info" %}}All values are 16 bit unsigned intergers, LSB Byte Order{{% /badge %}} 

{{% badge style="info" %}}Unlisted runtimes are raw{{% /badge %}} 

| **Type**                           | **Multiplier** | **Offset**       | **Unit**     |
| ---------------------------------- | -------------- | ---------------- | ------------ |
| Lambda                             | 0.001          | 0                | Lambda       |
| Lambda Target Error                | 0.001          | -10              | Lambda       |
| STFT/LTFT                          | 0.01           | -100             | %            |
| Cam Position                       | 0.1            | -200             | Degree       |
| MGP                                | 0.1            | -100             | KPA          |
| Fuel/Oil Pressure                  | 0.1            | 0                | KPA          |
| PPS/TPS/Motor Position             | 0.1            | -100             | %            |
| VE                                 | 0.1            | 0                | %            |
| IdleP                              | 0.1            | 0                | %            |
| PP/TP Error                        | 0.1            | 0                | %            |
| DBW Target Error                   | 0.1            | -100             | %            |
| Injector duty                      | 0.1            | 0                | %            |
| Inj PW                             | 0.001          | 0                | ms           |
| F/I Cut                            | 0.1            | 0                | %            |
| Speed KPH                          | 0.1            | 0                | KPH          |
| RPM ROC                            | 1              | -20000           | RPM/second   |
| PP/TP ROC                          | 0.1            | -100             | %/second     |
| ECU G                              | 0.01           | -10              | G            |
| Ignition angle                     | 0.1            | -100             | Degree       |
| Ignition trims                     | 0.1            | -100             | Degree       |
| FP Diff Offset                     | 0.1            | -1000            | KPA          |
| Voltage                            | 0.001          | 0                | Voltage      |
| Drive Slip                         | 0.01           | -100             | %            |
| Temps                              | 0.1            | -50              | Degrees C    |
| Fuel Level                         | 0.1            | 0                | Liters       |
| Fuel used                          | 0.01           | 0                | Liters       |
| Gear                               | 1              | -10              | Gear         |
| Time Milliseconds                  | 0.01           | 0                | Milliseconds |
| Time Seconds                       | 0.1            | 0                | Seconds      |
| Time Min                           | 1              | 0                | Min          |
| Force                              | 0.1            | -100             | KG           |
| Mass flow /Sec                     | 0.1            | 0                | G/s          |
| Mass flow /Cyl                     | 0.001          | 0                | G/cyl        |
| Traction Target                    | 0.1            | 0                | %            |
| Traction Target Error              | 0.1            | -100             | %            |
| Power                              | 1              | 0                | KW           |
| Torque                             | 1              | -1000            | NM           |
| Torque Reduction (Frictional loss) | -1             | 0                | NM           |
| Vehicle Accel (M/S/S)              | 0.01           | -100             | m/s/s        |
| Vehicle Accel (KM/HR/S)            | 0.01           | -100             | km/hr/s      |
