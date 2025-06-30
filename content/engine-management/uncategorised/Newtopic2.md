---
title: "OBD II J1979"
---

[](<https://www.digitaltrends.com/cars/everything-you-need-to-know-about-obd-obdii/>)

[Onboard Diagnostics 2 or OBD2](<https://www.digitaltrends.com/cars/everything-you-need-to-know-about-obd-obdii/>) is supported by the ECU using the SAE J1979 standard. The ECU supports the following service requests:


* Show current data
* Mil Status
* Show stored Diagnostic Trouble Codes (DTCs)
* Clear Diagnostic Trouble Codes (DTC)&nbsp; and stored values
* Request vehicle information




**OBD II Service Mode 01 - Show Current Data**


The ECU supports the following PIDs when the "Show Current Data" serviced is requested.&nbsp; &nbsp;


| **PID** **(hex)** | **PID** **(Dec)** | **Data bytes returned** | **Description**                                                                                           | **Min value** | **Max value** | **Units**                                                                   | **Notes**                                                                                        |
| :---------------: | :---------------: | :---------------------: | --------------------------------------------------------------------------------------------------------- | ------------- | ------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
|      &#48;1       |       &#49;       |          &#52;          | Monitor status since DTCs cleared. (Includes malfunction indicator lamp (MIL) status and number of DTCs.) |               |               |                                                                             |                                                                                                  |
|      &#48;3       |       &#51;       |          &#50;          | Fuel system status                                                                                        |               |               |                                                                             | Only displayed when Closed Loop Fuel enabled. [See Below](<Newtopic2.md#PID0x03\_Supplementary>) |
|      &#48;4       |       &#52;       |          &#49;          | Calculated engine load                                                                                    | &#48;         | &#49;00       | %                                                                           |                                                                                                  |
|      &#48;5       |       &#53;       |          &#49;          | Engine coolant temperature                                                                                | \-40          | &#50;15       | °C                                                                          |                                                                                                  |
|      &#48;6       |       &#54;       |          &#49;          | Short term fuel trim—Bank 1                                                                               | \-100&nbsp;   | &#57;9.2      | %                                                                           | Only displayed when Closed Loop Fuel enabled                                                     |
|      &#48;7       |       &#55;       |          &#49;          | Long term fuel trim—Bank 1                                                                                |               |               |                                                                             |                                                                                                  |
|      &#48;8       |       &#56;       |          &#49;          | Short term fuel trim—Bank 2                                                                               |               |               |                                                                             |                                                                                                  |
|      &#48;9       |       &#57;       |          &#49;          | Long term fuel trim—Bank 2                                                                                |               |               |                                                                             |                                                                                                  |
|      &#48;A       |      &#49;0       |          &#49;          | Fuel pressure ([gauge pressure](<https://en.wikipedia.org/wiki/Pressure\_measurement#Absolute>))          | &#48;         | &#55;65       | kPa                                                                         | Only displayed when Fuel Pressure input enabled                                                  |
|      &#48;B       |      &#49;1       |          &#49;          | Manifold absolute pressure                                                                                | &#48;         | &#50;55       | kPa                                                                         |                                                                                                  |
|      &#48;C       |      &#49;2       |          &#50;          | Engine RPM                                                                                                | &#48;         | &#49;6,383    | rpm                                                                         |                                                                                                  |
|      &#48;D       |      &#49;3       |          &#49;          | Vehicle speed                                                                                             | &#48;         | &#50;55       | km/h                                                                        |                                                                                                  |
|      &#48;E       |      &#49;4       |          &#49;          | Timing advance                                                                                            | \-64          | &#54;3.5      | ° before [TDC](<https://en.wikipedia.org/wiki/Dead\_centre\_(engineering)>) |                                                                                                  |
|      &#48;F       |      &#49;5       |          &#49;          | Inlet Air Temperature                                                                                     | \-40          | &#50;15       | °C                                                                          |                                                                                                  |
|      &#49;0       |      &#49;6       |          &#49;          | Final Mass Flow Rate                                                                                      | &#48;         | &#54;55.35    | g/s                                                                         | Note. This is Final flow rate, not MAF flow rate                                                 |
|      &#49;1       |      &#49;7       |          &#49;          | Throttle Position/Servo Main (for DBW Application)                                                        | &#48;         | &#49;00       | %                                                                           |                                                                                                  |
|      &#49;4       |      &#50;0       |          &#49;          | Narrow Band Oxygen Sensor 1                                                                               | &#48;         | &#49;.275     | V                                                                           | Only displayed when Narrow-band input enabled                                                    |
|      &#49;5       |      &#50;1       |          &#49;          | Narrow Band Oxygen Sensor 2                                                                               | &#48;         | &#49;.275     | V                                                                           | Only displayed when Narrow-band input enabled                                                    |
|      &#49;C       |      &#50;8       |          &#49;          | OBD standards this vehicle conforms to                                                                    |               |               |                                                                             | [See Below](<Newtopic2.md#PID0x1C\_Supplementary>)                                               |
|      &#49;F       |      &#51;1       |          &#50;          | Run time since engine start                                                                               | &#48;         | &#54;5535     | seconds                                                                     |                                                                                                  |




**Supplementary Information**&nbsp;


**PID 0x03 - Fuel System Closed Loop Status**&nbsp;

| **CAN Value** | **Suffix**  | **Description**                                                                                    |
| :-----------: | :---------: | -------------------------------------------------------------------------------------------------- |
|     &#49;     |    OPEN     | Open loop due to insufficient engine temperature                                                   |
|     &#50;     |    CLSD     | Closed loop, using oxygen sensor feedback to determine fuel mix                                    |
|     &#52;     |    OPEN1    | Open loop due to lockout condition or OFF (fuel cut due to deceleration, limiting, post start etc) |
|     &#56;     |   OPEN 2    | Open loop due to system failure                                                                    |
|    &#49;6     | CLSD1&nbsp; | Closed loop, using at least one oxygen sensor but there is a fault in the feedback system          |


**PID 0x04 - Calculated Engine Load**&nbsp;

There are 2 types of load defined by the SAE J1979, one is Calculated engine load the other Absolute engine load. The Calculated Load is referenced to engine speed, so its the %Engine Load at that RPM.

As defined by ODB II regulations Calculated load =&nbsp; (Current airflow / peak airflow @sea level)&nbsp; x (Baro @sea level / Baro) x 100%


**PID 0x1C - OBD standards this vehicle conforms to**

A request for this PID returns a single byte of data which describes which OBD standards this ECU was designed to comply with. Emtron replies with a value of 6

| **Value** | **Description**                                                                                                |
| :-------: | -------------------------------------------------------------------------------------------------------------- |
|   &#49;   | OBD-II as defined by the [CARB](<https://en.wikipedia.org/wiki/California\_Air\_Resources\_Board>)             |
|   &#50;   | OBD as defined by the [EPA](<https://en.wikipedia.org/wiki/United\_States\_Environmental\_Protection\_Agency>) |
|   &#51;   | OBD and OBD-II                                                                                                 |
|   &#52;   | OBD-I                                                                                                          |
|   &#53;   | Not OBD compliant                                                                                              |
|   &#54;   | EOBD (Europe)                                                                                                  |
|   &#55;   | EOBD and OBD-II                                                                                                |
|   &#56;   | EOBD and OBD                                                                                                   |
|   &#57;   | EOBD, OBD and OBD II                                                                                           |
|  &#49;0   | JOBD (Japan)                                                                                                   |
|  &#49;1   | JOBD and OBD II                                                                                                |
|  &#49;2   | JOBD and EOBD                                                                                                  |
|  &#49;3   | JOBD, EOBD, and OBD II                                                                                         |
|  &#49;4   | Reserved                                                                                                       |
|  &#49;5   | Reserved                                                                                                       |
|  &#49;6   | Reserved                                                                                                       |


