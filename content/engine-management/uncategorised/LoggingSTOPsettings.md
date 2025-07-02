---
title: "Logging STOP settings"
---

For ECU logging to STOP for a selected Dataset the following must occur :


\- RPM is less than RPM Stop **AND**

\- TPS is less than TPS Stop **AND**

\- MAP is less than MAP Stop **AND**

\- Selected User Channel is **OFF** *(if Enabled)* **AND**

\- Logging Switch Status is **OFF** *(if Enabled)* **AND**

\- Stop Delay time has been reached.


* Entering a 0 into any of the Stop Parameters means it will not be used to Stop the logging.
* If ALL Stop conditions are zero, the logging will never stop. This should be avoided. Make sure the Stop conditions are set correctly.&nbsp;
* If ONLY the logging switch is required then assign this to an input using the Inputs Pins Setup menu (F10), switches Tab and then set ALL the Stop parameters to zero.



Use the **Runtime Menu** -**\> ECU Internal** Tab to view ECU logging status.
