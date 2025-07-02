---
title: "Turbo Speed"
---

Turbo Speed is available on Channels DI 1- 8 on KV Series and DI1-4 on SL Series.. The units are RPM


See [Speed Settings](<SpeedSettings1.md>) for information on sensor setup.


**Turbo Speed Calculation**&nbsp;


**Turbo Speed(RPM) = Frequency x Scaler (set in Inputs form,&nbsp; Config view) x 10**


Example 2351 Hz, Scaler = 2.56

\
Turbo Speed = (2351 Hz x 2.56) x 10&nbsp; = 60180 RPM


Example 4436 Hz, Scaler = 2.56

\
Turbo Speed = (4436 Hz x 2.56) x 10&nbsp; = 113560 RPM



\*\* Turbo speed sensor electronics divide the raw frequency by 8


Turbo fin count : 14

Electronics divider : 8

Turbo Speed : 100,000

Convert pulse to frequency : /60


(100000/8)\*14/60 = 2916.67hz


Resolution modifier : 10&nbsp;


&#50;916.67 \*10 = 29166.7


Scaler : 10000/29166.7 = 3.43