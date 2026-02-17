---
title: "Ethernet Connection"
weight: 2
---

## Connecting the ECU

### Communication Cable

The Emtron proprietary communication cable translates standard high speed Ethernet to a Lemo connector that feeds directly into the ECU header.

![Image](</img/NewItem163.png>)![Image](</img/NewItem162.png>)

The pin configuration for the Lemo receiver is as follows.

### SL series

![Image](</img/SL B Plug.jpg>)

| Wire         | SL Pin    |
|--------------|-----------|
| Green/White  | B31 (TX+) |
| Green        | B32 (TX-) |
| Orange/White | B33 (RX+) |
| Orange       | B34 (RX-) |

### KV series

![Image](</img/KV D Plug.jpg>)

| Wire         | SL Pin    |
|--------------|-----------|
| Green/White  | D23 (TX+) |
| Green        | D24 (TX-) |
| Orange/White | D25 (RX+) |
| Orange       | D26 (RX-) |


## IP Config
The Emtune software will communicate to the ECU over a static IP address.

Set your IP and subnet to the following on the Ethernet port you will be using on your PC.

**IP:** 192.168.1.50
**Subnet:** 255.255.255.0

![Image](</img/NewItem159.png>)

With successful connection, the Emtune Welcome screen will display “ECU DETECTED” in blue in the bottom left corner as can be observed in the background in the above example.

### Windows 11
1. Right click on the `Network Connection` icon in the system tray. It may appear as a wired connection or a wifi icon.
![Image](/img/win11_1.png)

2. Click on `Ethernet`
![Image](/img/win11_2.png)

3. Expand the settings for your ethernet adapter and click on the Edit button for `IP Assignment`.
![Image](/img/win11_3.png)

4. Set it to `Manual`, turn on `IPv4`, and enter the emtron `IP Address` and `Subnet mask`.
![Image](/img/win11_4.png)

5. Click `Save`.
6. Done. Connect the Emtron Ethernet cable.

### Windows 10
To setup the Ethernet on Windows 10 ready for the ECU connection use the following steps.

![Image](</img/W10 Eth 1.jpg>)

* Left Click Windows Icon - Bottom Left corner

![Image](</img/W10 Eth 2.jpg>)

* Left Click Settings Icon -  2nd from bottom on Left

![Image](</img/W10 Eth 3.jpg>)

* Left Click "Network & Internet" - Top Right

![Image](</img/W10 Eth 4.jpg>)

* Left Click "Ethernet" - 4th from Top on the Left

![Image](</img/W10 Eth 5.jpg>)

* Left Click "Change Adapter Options" - Top Right

![Image](</img/W10 Eth 6.jpg>)

* Right Click "Ethernet"

![Image](</img/W10 Eth 7.jpg>)

* Left Click "Properties"

![Image](</img/W10 Eth 8.jpg>)

* Select "Internet Protocol Version 4 (TCP/IPv4) and Left Click "Properties"

![Image](</img/W10 Eth 9.jpg>)

* Use the following IP address

![Image](</img/W10 Eth 10.jpg>)

* Left Click "OK" and exit, the process is complete
* Done. Connect the Emtron Ethernet cable.

### Windows 8.1
To setup the Ethernet on Windows 8.1 ready for the ECU connection use the following steps.

* Type "View Network Connections" into the search window, accessed from the start menu. Windows should provide a list of results. Select View Network Connections.

![Image](</img/AAAA30.jpg>)

Or alternatively if the search function doesn't provide this:

Start > Control Panel > Network and Sharing Center.
Once in this menu select "Change Adapter Settings"

![Image](</img/AAAA31.jpg>)

* Once in this menu select "Change Adapter Settings"

![Image](</img/AAAA32.jpg>)

* The below menu should be visible. Select "Ethernet"

![Image](</img/AAAA28.jpg>)

* Right click to Access Properties

![Image](</img/AAAA33.jpg>)

* Select TCP/IPv4 then click Properties

![Image](</img/AAAA34.jpg>)

* Select "Use the following IP address" and enter in the address 192.168.1.50. The Subnet should automatically default to 255.255.255.0. Click OK.

![Image](</img/AAAA35.jpg>)

* Done. Connect the Emtron Ethernet cable.

### Windows 7
To setup the Ethernet on Windows 7 ready for the ECU connection use the following steps.

* Type "View Network Connections" into the search window, accessed from the start menu. Windows should provide a list of results. Select View Network Connections.

![Image](</img/NewItem28.jpg>)

or alternatively if the search function doesn't provide this:

Start > Control Panel > Network and Internet > Network and Sharing Center.
Once in this menu select "Change Adapter Settings"

![Image](</img/NewItem29.png>)

* The below menu should be visible. Select "Local Area Connection"

![Image](</img/NewItem31.png>)

* Select TCP/IPv4 then click Properties

![Image](</img/NewItem33.png>)

* Select "Use the following IP address" and enter in the address 192.168.1.50. The Subnet should automatically default to 255.255.255.0. Click OK.

![Image](</img/NewItem32.png>)

* Done. Connect the Emtron Ethernet cable.

### Windows XP
{{% badge style="warning" %}}Emtune is no longer developed to offer Windows XP compatibility.{{% /badge %}}