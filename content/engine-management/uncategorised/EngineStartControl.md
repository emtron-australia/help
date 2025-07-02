---
title: "Engine Start Control"
---

**Overview**


This function controls both Engine Starter Function output and Immobiliser Function.


The Engine Start Function will switch an Output ON to start the engine cranking. The ECU Output would normally be connected to the Starter Relay. Once the ECU determines the engine is running the relay will be switched OFF.

**NOTE: Both an Input and Output Channel MUST be selected for the Engine Start function to work.**


The Immobiliser Function prevents Fuel and Ignition occurring while the Immobiliser Function is active. An Output can also be configured to further enhance this function. For example you might want to inhibit the starter relay operating.




**Engine Start Function**&nbsp;



**Input Channel**


One of two Inputs can be configured to control this function:


* **Start/Stop Switch**. (See Config View -\> Input Pins Setup -\> Switches Tab).&nbsp; With this Input the Switch can Start and Stop the Engine
* **Start Position Switch**. (See Config View -\> Input Pins Setup -\> Switches Tab). This Switch will ONLY Start the engine.


**Output Channel**


**&#49;. Starter Relay Output**&nbsp; - **Input Switch Configured as "Start/Stop Switch":**&nbsp;


* When the engine speed is zero and the button is pressed the ECUs interprets this as a request to START the engine. At this point the ECU will switch ON the Starter Relay.&nbsp; During the "Cranking Timeout" period the ECU will monitor Engine Speed and when it exceeds the "Engine Started RPM" the Starter Relay will be switched OFF. If the "Cranking Timeout" period is reached and the engine has not started the Starter Relay will be switched OFF.&nbsp;
* When the engine is running and the button is pressed the ECUs interprets this as a request to STOP the engine. The ECU will switch OFF Fuel and Ignition until the Engine Speed has reached zero.



**&#50;. Starter Relay Output**&nbsp; - **Input Switch Configured as "Start Position Switch":**&nbsp;


* When the engine speed is zero and the button is pressed the ECUs interprets this as a request to START the engine. At this point the ECU will switch ON the Starter Relay.&nbsp; During the "Cranking Timeout" period the ECU will monitor Engine Speed and when it exceeds the "Engine Started RPM" the Starter Relay will be switched OFF. If the "Cranking Timeout" period is reached and the engine has not started the Starter Relay will be switched OFF.&nbsp;


This mode is more used in Motorsport applications. The Start Button starts the engine and the Main kill switch is used to shut the engine down and disconnect power from all systems.


**NOTE:** In this Mode the Switch CANNOT be used to STOP the engine when it is running. It is a Start ONLY function. However, there is a safety feature build; when the engine is cranking if engine needs to be stopped, pressing the Start button again will stop the engine cranking.



**Immobiliser Function**&nbsp;



