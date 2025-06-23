---
title: "Gearshift - Paddle"
---

**Gearshift without “shift position” – Tolerance Voltage**

![Image](</lib/NewItem917.png>)

Larger tolerance voltage number will achieve next gear stable sooner.&nbsp; Consider volt change per gear, to determine tolerance volt. &nbsp;

Gear volt spread is 0.60x volt.&nbsp; 0.225 tolerance will achieve “gear change” 63% of the way through the barrel turn. &nbsp;

This is a way control the shift timing if using “Next Gear Stable” function

![Image](</lib/NewItem916.png>)

Above example is vehicle using a static cut value (75%). &nbsp;

Next Gear % Cut Level and Ignition Retard Recovery Time are being leveraged to phase back in engine power. &nbsp;

**Pre-loading Gearbox**

Necessary to achieve swift ratchet action, similar to a “stick” setup where you’d deny cut until a specific force on the shifter. &nbsp;

Mechanical lag of linakge, air lines, etc – all contribute to needing pre-loading. &nbsp;

Cars with high forward momentum will need pre-loading to ensure the middle phase of the gearshift happens at the right time, when the dogs are fully dis-engaged.&nbsp;

![Image](</lib/NewItem915.png>)

Observe engine in full cut off, engine speed decelerating, but speed still increasing.&nbsp; The barrel has not turned at the right time (when the engine speed decelerated) and caught the previous gear deceleration side of the dog hanging the upshift up. &nbsp;

Pre-loading can be done with Torque Reduction Delay table, or if Shift Position is available, in full closed loop -\>

![Image](</lib/NewItem914.png>)


**Torque Reduction and Re-Introduction**

Reduction in torque can be achieved many ways with fuel, ignition, or both cut tables.&nbsp; Retard tables.&nbsp; Rev matching cut functions, and even DBW target hijacking. &nbsp;

Different scenarios will call for different methods of reduction types. &nbsp;

On turbocharged engines, using too much cut may reduce exhaust energy affecting turbine speed. &nbsp;

Too much retard may increase exhaust energy

A global boost control comp for “Ignition Trims Total” is suggested


Re-Introduction of torque is critical to prevent drivetrain from clashing, bouncing on dogs (drive/decel), and creating excessive ringing in the driveline. &nbsp;

* Plotting/observing Engine Torque (requires tuned torque model) runtimes can help what the engine is doing during the shift quickly
* Using Shift Position channels in cut tables

  * Cut Recovery Time table functions off values in the cut table – if last value is “0” then recovery time has nothing to recover from
  * Tolerance Voltage in the Gear Volt input setup should be considered.&nbsp; Suggest using a lower tolerance voltage to control the ECU through the shift


