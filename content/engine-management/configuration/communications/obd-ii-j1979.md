---
title: "OBD II J1979"
weight: 100
---

[](<https://www.digitaltrends.com/cars/everything-you-need-to-know-about-obd-obdii/>)

[Onboard Diagnostics 2 or OBD2](<https://www.digitaltrends.com/cars/everything-you-need-to-know-about-obd-obdii/>) is supported by the ECU using the SAE J1979 standard. The ECU supports the following service requests:

* Show current data
* Mil Status
* Show stored Diagnostic Trouble Codes (DTCs)
* Clear Diagnostic Trouble Codes (DTC)  and stored values
* Request vehicle information

## OBD II Service Mode 01 - Show Current Data

The ECU supports the following PIDs when the "Show Current Data" serviced is requested.   

| **PID** **(hex)** | **PID** **(Dec)** | **Data bytes returned** | **Description**                                                                                           | **Min value** | **Max value** | **Units**                                                                   | **Notes**                                                                                        |
| :---------------: | :---------------: | :---------------------: | --------------------------------------------------------------------------------------------------------- | ------------- | ------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
|      01       |       1       |          4          | Monitor status since DTCs cleared. (Includes malfunction indicator lamp (MIL) status and number of DTCs.) |               |               |                                                                             |                                                                                                  |
|      03       |       3       |          2          | Fuel system status                                                                                        |               |               |                                                                             | Only displayed when Closed Loop Fuel enabled. [See Below](<Newtopic2.md#PID0x03_Supplementary>) |
|      04       |       4       |          1          | Calculated engine load                                                                                    | 0         | 100       | %                                                                           |                                                                                                  |
|      05       |       5       |          1          | Engine coolant temperature                                                                                | -40          | 215       | °C                                                                          |                                                                                                  |
|      06       |       6       |          1          | Short term fuel trim—Bank 1                                                                               | -100    | 99.2      | %                                                                           | Only displayed when Closed Loop Fuel enabled                                                     |
|      07       |       7       |          1          | Long term fuel trim—Bank 1                                                                                |               |               |                                                                             |                                                                                                  |
|      08       |       8       |          1          | Short term fuel trim—Bank 2                                                                               |               |               |                                                                             |                                                                                                  |
|      09       |       9       |          1          | Long term fuel trim—Bank 2                                                                                |               |               |                                                                             |                                                                                                  |
|      0A       |      10       |          1          | Fuel pressure ([gauge pressure](<https://en.wikipedia.org/wiki/Pressure_measurement#Absolute>))          | 0         | 765       | kPa                                                                         | Only displayed when Fuel Pressure input enabled                                                  |
|      0B       |      11       |          1          | Manifold absolute pressure                                                                                | 0         | 255       | kPa                                                                         |                                                                                                  |
|      0C       |      12       |          2          | Engine RPM                                                                                                | 0         | 16,383    | rpm                                                                         |                                                                                                  |
|      0D       |      13       |          1          | Vehicle speed                                                                                             | 0         | 255       | km/h                                                                        |                                                                                                  |
|      0E       |      14       |          1          | Timing advance                                                                                            | -64          | 63.5      | ° before [TDC](<https://en.wikipedia.org/wiki/Dead_centre_(engineering)>) |                                                                                                  |
|      0F       |      15       |          1          | Inlet Air Temperature                                                                                     | -40          | 215       | °C                                                                          |                                                                                                  |
|      10       |      16       |          1          | Final Mass Flow Rate                                                                                      | 0         | 655.35    | g/s                                                                         | Note. This is Final flow rate, not MAF flow rate                                                 |
|      11       |      17       |          1          | Throttle Position/Servo Main (for DBW Application)                                                        | 0         | 100       | %                                                                           |                                                                                                  |
|      14       |      20       |          1          | Narrow Band Oxygen Sensor 1                                                                               | 0         | 1.275     | V                                                                           | Only displayed when Narrow-band input enabled                                                    |
|      15       |      21       |          1          | Narrow Band Oxygen Sensor 2                                                                               | 0         | 1.275     | V                                                                           | Only displayed when Narrow-band input enabled                                                    |
|      1C       |      28       |          1          | OBD standards this vehicle conforms to                                                                    |               |               |                                                                             | [See Below](<Newtopic2.md#PID0x1C_Supplementary>)                                               |
|      1F       |      31       |          2          | Run time since engine start                                                                               | 0         | 65535     | seconds                                                                     |                                                                                                  |

## Supplementary Information

## PID 0x03 - Fuel System Closed Loop Status

| **CAN Value** | **Suffix**  | **Description**                                                                                    |
| :-----------: | :---------: | -------------------------------------------------------------------------------------------------- |
|     1     |    OPEN     | Open loop due to insufficient engine temperature                                                   |
|     2     |    CLSD     | Closed loop, using oxygen sensor feedback to determine fuel mix                                    |
|     4     |    OPEN1    | Open loop due to lockout condition or OFF (fuel cut due to deceleration, limiting, post start etc) |
|     8     |   OPEN 2    | Open loop due to system failure                                                                    |
|    16     | CLSD1  | Closed loop, using at least one oxygen sensor but there is a fault in the feedback system          |

## PID 0x04 - Calculated Engine Load

There are 2 types of load defined by the SAE J1979, one is Calculated engine load the other Absolute engine load. The Calculated Load is referenced to engine speed, so its the %Engine Load at that RPM.

As defined by ODB II regulations Calculated load =  (Current airflow / peak airflow @sea level)  x (Baro @sea level / Baro) x 100%

## PID 0x1C - OBD standards this vehicle conforms to

A request for this PID returns a single byte of data which describes which OBD standards this ECU was designed to comply with. Emtron replies with a value of 6

| **Value** | **Description**                                                                                                |
| :-------: | -------------------------------------------------------------------------------------------------------------- |
|   1   | OBD-II as defined by the [CARB](<https://en.wikipedia.org/wiki/California_Air_Resources_Board>)             |
---
|   3   | OBD and OBD-II                                                                                                 |
|   4   | OBD-I                                                                                                          |
|   5   | Not OBD compliant                                                                                              |
|   6   | EOBD (Europe)                                                                                                  |
|   7   | EOBD and OBD-II                                                                                                |
|   8   | EOBD and OBD                                                                                                   |
|   9   | EOBD, OBD and OBD II                                                                                           |
|  10   | JOBD (Japan)                                                                                                   |
|  11   | JOBD and OBD II                                                                                                |
|  12   | JOBD and EOBD                                                                                                  |
|  13   | JOBD, EOBD, and OBD II                                                                                         |
|  14   | Reserved                                                                                                       |
|  15   | Reserved                                                                                                       |
|  16   | Reserved                                                                                                       |

