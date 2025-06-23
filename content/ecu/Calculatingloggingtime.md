---
title: "Calculating logging time"
---


Time to 100% full the ECU logging Memory =&nbsp; &nbsp; &nbsp; &nbsp; ( Memory Size (MB)&nbsp; / 2 )&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Logging Rate x Number of Parameter&nbsp;


**NOTE**: When the logging mode is set to "Circular" this is the time to complete one logging cycle


**Example1** : Dataset 1 Logging Rate = 100Hz. Logging 20 parameters. Memory Size at 4MB



Time for ECU logging memory to reach 100% capacity =&nbsp; &nbsp; &nbsp; &nbsp; 4MB /2&nbsp; &nbsp; &nbsp; = 1000 secs = 16.6 minutes

&nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 100 x 20


**Example2** : Dataset 1 Logging Rate = 100Hz. Logging 20 parameters. Dataset 2 Logging Rate = 5Hz. Logging 20 parametersMemory Size at 4MB



Time for ECU logging memory to reach 100% capacity =&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 4MB /2 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; = 952 secs = 15.87 minutes

&nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; (100 x 20) + (5 x 20)


**Example3** : Dataset 1 Logging Rate = 100Hz. Logging 50 parameters. Memory Size at 32MB



Time for ECU logging memory to reach 100% capacity =&nbsp; &nbsp; &nbsp; &nbsp; 32MB /2&nbsp; &nbsp; &nbsp; = 3200 secs = 53.3 minutes

&nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 100 x 50


