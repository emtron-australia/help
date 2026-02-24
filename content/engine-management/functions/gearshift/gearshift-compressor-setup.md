---
title: "Gearshift Compressor Setup"
weight: 77
---

## Gearshift Compressor Setup

## Gearshift Comp Pressure Target

Pressure Target for Compressor. The Output will be switch off when the pressure is reached.\

## Gearshift Comp Pressure Hysteresis

This value is subtracted from the Pressure Target and determines when the Output will be switched  back ON.

Pressure Target = 150.0 PSI

Pressure Hysteresis = 10.0 PSI

The Pump will stay ON until 150.0 PSI is reached. The Pump will then turn OFF. When the pressure drops to 140 PSI to pump will switch back ON\

## Gearshift Comp Voltage Lockout

The Gearshift Compressor Output will be switched OFF below this Voltage.  Used normally to switch OFF the Compressor to prevent battery drain in Low Voltage situations.

0 = OFF\

## Gearshift Comp RPM Lockout

The Gearshift Compressor Output will be switched OFF below this Engine Speed.  Used normally to switch OFF the Pump during low RPM and cranking.

0 = OFF

Typical Value = 400 RPM

## Gearshift User Lockout

The Gearshift Compressor Output will be switched OFF when the User Channel is ON/Active.

0: OFF

1: User Channel 1

2: User Channel 2

3: User Channel 3

4: User Channel 4

5: User Channel 5

6: User Channel 6

7: User Channel 7

8: User Channel 8

9: User Channel 9

10: User Channel 10

## Gearshift Comp Timeout

With the Compressor ON, if the Target pressure cannot be reached within this timeout value the Output will be switched OFF. The timer will only be reset when the Lockouts become active OR the Re-try Interval is reached/used.

0 = OFF

Typical Value = 30secs

## Gearshift Comp Re-try Interval

In the event the Timeout is reach and the output is switched OFF the system will switch the ouput back ON at this interval in an attempt to keep system pressure.  This event normally occurs when the feedback input fails.

0 = OFF
