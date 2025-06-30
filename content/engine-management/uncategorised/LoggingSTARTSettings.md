---
title: "Logging START Settings"
---

For ECU logging to START for a selected Dataset the following must occur :


\- RPM is greater than RPM Start **AND**

\- TPS is greater than TPS Start **AND**

\- MAP is greater than MAP Start **AND**

\- Selected User Channel is **ON** *(if Enabled)* **AND**

\- Logging Switch Status is **ON** *(if Enabled)* **AND**

\- Start Delay time has been reached.


* Entering a 0 into any of the Start Parameters means it will not be used to control the start of logging.
* If ALL Start conditions are zero, the logging will never start.
* If ONLY the logging switch is required then assign this to an input using the Inputs Pins Setup menu (F10), switches Tab and then set ALL the Start parameters to zero.



Use the **Runtime Menu** **-\> ECU Internal** Tab to view ECU logging status.
