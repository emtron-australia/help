---
title: "Knock Control"
---

**Knock Control Introduction**


All Emtron ECU’s have Knock control, using inputs from a piezoelectric sensor. The ECU monitions the knock level for individual cylinders over a user defined crank angle window.&nbsp;


Each knock input is fully differential, giving superior common-mode noise rejection in the harsh automotive environment.&nbsp; The ECU starts by passing the analog signal from the knock sensor (piezoelectric) through an anti-aliasing signal conditioning filter before using Bosch integrated circuit technology for advanced digital signal processing.&nbsp; The digital filter is a fully programmable  finite impulse response (FIR) filter allowing the user to adjust both the centre frequency and bandwidth. This is extremely powerful and very flexible, allowing the user to customise the filter design to suit the application.&nbsp;



**Hardware Specification**&nbsp;


* SL4 &nbsp; &nbsp; &nbsp; &nbsp; - &nbsp; &nbsp; Single knock input
* SL8/KV8/12/16 &nbsp; &nbsp; - &nbsp; &nbsp; Dual knock input


**Knock Control Function Enable**


Config -\>Functions -\> Function Output Setup -\> Engine Functions -\> Knock Control&nbsp;

Or

Utilities -\>Knock Studio -\>Knock Control&nbsp;


Disabled = Function is switched off&nbsp;

Enabled = Function is switched on


**Filter Window Type**


The effects of Filter Window can be visually seen when the different options are selected. It is a complicated topic, but basically a Window function is used to limit the signal in time and generate a different frequency response.&nbsp; The Hamming window provides tighter bandwidth control, requiring the centre frequency to be more accurate. The Blackman has a slightly more relaxed bandwidth by comparison and therefore the centre frequency is not as critical.&nbsp;


* None = Using raw Digital Filtering with no windowing
* Hamming&nbsp;
* Blackman &nbsp;


**Centre Frequency** = Central frequency the knock control will operate at. This is the dominant frequency the engine is expected to knock at.


An estimation or initial guess of the knock frequency can be done using this basic equation. This is ONLY a starting point and should be verified on the vehicle.&nbsp;


Knock Frequency(Hz) =&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 1800 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; x 1000 &nbsp; = &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 1800&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; x 1000&nbsp;

&nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Piston Circumference(mm)&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 3.14 x Piston Diameter (mm)


Example . Piston Diameter 85mm.&nbsp; Knock Frequency&nbsp; = 1800 / (3.14 x 85mm)&nbsp; x 1000 = 6744 Hz


**Bandwidth** = Defines the frequency range (higher = wider) over which the knock control will operate. Outside that range all knock signals will be ignored. The engine will never knock at exactly the same frequency every time due to changes in combustion pressure and temperature, so the correct bandwidth is important. Too small and important knock events might be missed, too big and normal engine noise may contaminate the knock data.&nbsp; Typical values are recommend at 200 - 400Hz.


The below example shows the setup for a Centre frequency of 7000Hz and Bandwidth if 200Hz.


![Image](</img/NewItem300.png>)



**Knock Control using the 2nd harmonic**


Sometimes an engines noise profile at the base frequency or 1st harmonics shows an indistinguishable difference between a knock event and normal engine noise. In this situation the 2nd harmonics (double the base frequency) can be used to achieve a better signal to noise ratio on a true knock event.


For example a Subaru engine has a knock frequency (1st harmonic) of approximately 6.0Khz. The second Harmonics would therefore be 12.0khz. If the engine noise profile at 6.0Khz showed an indistinguishable difference between a knock event and engine noise, the centre frequency off 12.0Khz could be used.&nbsp;


**NOTE:**&nbsp;

* There are 2 types of knock sensors, "wide-band" and "tuned".&nbsp; Wide-band sensor will work over a range of 0 -20Khz, whereas a "tuned" sensor is designed to have a resonant frequency, producing a larger output level at the one frequency.&nbsp;
* Tuned knock sensors usual operate at the 2nd harmonic&nbsp;





