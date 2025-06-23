---
title: "Connecting the ECU"
---

**Connecting the ECU**


**Communication Cable**


The Emtron proprietary communication cable translates standard high speed Ethernet to a Lemo connector that feeds directly into the ECU header. &nbsp;


![Image](</lib/NewItem163.png>)![Image](</lib/NewItem162.png>)


The pin configuration for the Lemo receiver is as follows. &nbsp;


**SL series**&nbsp;


![Image](</lib/SL B Plug.jpg>)


Green/White &nbsp; &nbsp; – &nbsp; &nbsp; B31 (TX+)

Green &nbsp; &nbsp; &nbsp; &nbsp; – &nbsp; &nbsp; B32 (TX-)

Orange/White&nbsp; &nbsp; – &nbsp; &nbsp; B33 (RX+)

Orange&nbsp; &nbsp; – &nbsp; &nbsp; B34 (RX-)



**KV series**&nbsp;


![Image](</lib/KV D Plug.jpg>)



Green/White &nbsp; &nbsp; – &nbsp; &nbsp; D23 (TX+)

Green &nbsp; &nbsp; &nbsp; – &nbsp; &nbsp; D24 (TX-)

Orange/White&nbsp; &nbsp; – &nbsp; &nbsp; D25 (RX+)

Orange &nbsp; &nbsp; –&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; D26 (RX-)


**IP Config**


The Emtune software will communicate to the ECU over a static IP address. &nbsp;

Set your IP and subnet to the following on the Ethernet port you will be using on your PC.&nbsp;


IP &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; : 192.168.1.50

Subnet &nbsp; &nbsp; &nbsp; &nbsp; : 255.255.255.0

![Image](</lib/NewItem159.png>)


With successful connection, the Emtune Welcome screen will display “ECU DETECTED” in blue in the bottom left corner as can be observed in the background in the above example.