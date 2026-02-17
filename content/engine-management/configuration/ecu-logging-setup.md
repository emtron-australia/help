---
title: "ECU Logging Setup"
weight: 16
---

## ECU Logging Setup

## ECU Logger

All Emtron ECUs have ECU logging capabilities.  \
To configure the ECU logger, with the ECU or Cal File open navigate to Logging -> ECU Logger -> Setup 

![Image](</img/NewItem784.png>)

The menu that opens up will allow the user to configure the following options 

## Config

Set the maximum memory size 

Set the Mode 

    Continous = Logging memory will overwrite when full 

    One Shot = Logging will stop once memory is full

## Global Start/Stop Conditions

Set the general conditions for how the ECU logger will start/stop here

## Data Set Configuration

There are 6 data sets that can hold 50 channels each.  

Each data set has select-able "Logging Rate" so the user can manage what channels are being recorded at what speeds.  

![Image](</img/NewItem785.png>)

** EFI Relay control is very important for stable logging recording, this is due to memory transfer from high speed ram in the ECU to permanent memory when the ECU is shut down.  

ECU logging allows ECU Engine and Vehicle data to be transferred into memory and then permanently stored. When required the data can then be downloaded from the ECU using Emtune so it can be analyzed.

The ECU logging uses 2 types of memory for data storage.

1) RAM  (Volatile - ECU requires power to maintain the stored data)

2) Flash Memory (Non-volatile - Data is permanently stored)

## Stage 1

The logging starts by first transferring data into a large high speed DDR RAM buffer. This can store up to 32MB of data.  RAM memory is volatile which means when the power is removed the data is lost. It is fast and has an unlimited number of Write(Store) and Read cycles.

## Stage 2

As the RAM data can be lost when the ECU is powered down, the data must be periodically transfered into Flash Memory where is can be permanently stored. Flash memory has a limited number of write (Store) cycles which is why the data can only be stored periodically. The following condition(s) are used to control this storing:

1. When a logging channel is ON, Data is transferred from RAM into Flash memory at approximately 30sec intervals.
1. When a logging channel switches from ON to OFF all unstored data is transferred into Flash memory.
1. When the ECU is controlling the Main EFI Relay and the ECU receives a request to shut down, the ECU will transfer all unstored data into Flash Memory before switching itself off.

Logging rates can be selected from 1Hz up to 500Hz

Data can from transferred from ECU to PC at approximately 0.5MB/sec. So a 4MB log will take 8 seconds and a 16MB log will take 32 seconds.

Use the **Runtime menu (F3) -> ECU Internal** tab to view the Logging Status

**NOTE: With 500 Hz Rate selected ONLY Dataset 1 is available for logging .**
