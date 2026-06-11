---
title: "Emtron CAN Gauge"
---

**Kit Contents** — When purchasing the Emtron CAN Gauge the following items are included:

- 1 × Emtron CAN Gauge
- 1 × Mounting Bracket
- 2 × Mounting Bracket thumbscrews
- 1 × Unterminated standard flying loom

{{< figure src="/img/can-gauge/kit-contents.jpeg" caption="Emtron CAN Gauge kit contents." >}}

## 1.0 Description

The Emtron CAN Gauge by Gauge ART is a compact 52mm OLED gauge that connects to all Emtron ECUs to display real-time data from CAN broadcasts. It is also compatible with aftermarket and factory ECUs.

The gauge is wirelessly configurable using an Android or Apple iOS mobile device through Wi-Fi. Gauge channels, bar graphs, warning points, and custom gauge labels can be configured using the "Gauge ART CAN Gauge App".

## 2.0 Specification

- 52mm display
- Configurable low and high warnings
- Day / Night dimming
- Wireless Wi-Fi configuration
- Connect more than one unit
- Runtime channel names user definable
- User defined channels can be displayed
- OLED Display
- 1, 2 or 4 channel gauge layouts available
- Up to 10 different pages available

**Inputs:** 1 × CAN bus

**Operating Temperature:** -30 to 85°C (-22 to 185°F)

## 3.0 Requirements

### 3.1 Compatible ECU

All Emtron ECUs are compatible. Most common ECUs are also compatible, including: Adaptronic, AEM EMS 4, AEM EMS Series 2, AEM Infinity, Factory CAN OEM (requires OBD Link), Hondata KPro4 / S300, Link G4+, MaxxECU, Megasquirt MS3, Motec M1 Series, ProEFI, Syvecs S6/S6+/S8, Vipec, Wolf EMS.

### 3.2 Smartphone or Tablet

Smartphone or tablet with Apple iOS or Android v4.4 or later.

### 3.3 ECU Terminals, Connector, & Installation tools

The Emtron CAN Gauge includes an unterminated flying loom that will require connection to a power source and the ECU CAN bus.

## 4.0 Wiring

### 4.1 CAN Gauge Wiring

**Table 4.1 — CAN Gauge Wiring**

| Wire   | Function          |
|--------|-------------------|
| Red    | 14 V Supply       |
| Black  | Ground            |
| Orange | 14 V Illumination |
| White  | CAN Hi            |
| Green  | CAN Lo            |

### 4.2 CAN Bus Wiring

The CAN Gauge includes a user-configurable 120 ohm terminating resistor jumper. The resistor is enabled when the jumper is in place.

**CAN bus wiring precautions**

- CAN Bus High and Low are differential signals, so twisted pair **MUST** be used. Failing to do so will compromise the entire CAN Bus System.
- In some extreme environments, shielded twisted pair may be required to help with reliability and data integrity.
- The fewer connectors in any transmission system the better. Unnecessary connectors are almost guaranteed to present an impedance discontinuity and hence may cause reflections and data loss.
- CAN Bus termination must be done correctly by using a 120 ohm 0.25W resistor at each END of the bus system.
- Maximum stub length to a device from the main Bus is recommended at 0.3m, in accordance with the High-Speed ISO 11898 Standard.

{{< figure src="/img/can-gauge/can-bus-wiring.jpeg" caption="Figure 4.1 — CAN Bus wiring example: ECU and Dash at each end with 120 Ohm termination." >}}

### 4.3 Illumination Signal Wiring

The CAN Gauge can dim illumination at night when the parking lights are on. Using the factory service manual, find a wire in the interior that switches to +12V power when the parking lights are on. Verify with a voltmeter or test light that the wire receives +12V when the parking lights are turned on. Note that many vehicles have an illumination-switched connector in the interior fuse box.

## 5.0 Gauge ART Application

Search "gaugeART" and download the gaugeART CAN Gauge App from your device's app store. If you have two gauges, remove one of the gauges from power — program one gauge at a time.

Turn on your ignition to turn on the CAN Gauge; the welcome screen will be shown. Connect to the gauge via Wi-Fi by tapping **Settings → Wi-Fi**. Tap on **gaugeART** and enter the default password `12345678`. Allow the gauge to connect. If prompted with a message that internet is not available with this device, tap OK. You may now open the gaugeART CAN Gauge App.

### 5.1 Create Configuration

Tap **Create Configuration**. Select ECU type and tap **Next**. The gaugeART CAN Gauge allows you to create up to 10 pages of gauge layouts in 1, 2, or 4 gauge layouts. Tap the centre of the screen for Gauge Screen Setup. On this screen, select a channel, configure graph range, update speed, warnings, and gauge labels (e.g. rename "MAP" to "BOOST"). Tap **Previous Page** to return. Tap the left side to change the configuration between 1, 2, or 4 gauge layout. Tap **Next Page** to add a new page or **Delete** to remove a page.

{{< figure src="/img/can-gauge/app-config.jpeg" caption="Figure 5.1 — gaugeART CAN Gauge App configuration." >}}

### 5.2 Save & Send Configuration

Tap the icon in the top right and tap **Save**. Enter a name under "Enter Save File Name" and tap **Save**. To program, tap **Send Configuration**. The gauge will be programmed and will show your configuration. Programming takes anywhere from 10–60 seconds and will update the gauge's firmware automatically if an update is available.

### 5.3 Load Configuration

Select **"Emtron"**. Previously saved files will be shown in the second drop-down. Click **Load** to open the file. To edit your saved configuration, tap **Edit** once loaded. To program, tap **Send Configuration**.

## 6.0 Emtune Settings

Ensure the ECU firmware Version is 2.17.0. If using earlier firmware versions, the display may still be operational; however, some functionality and channels will not be available.

Make sure the ECU is powered up and is Online in Emtune. Go to **Config View → Communications → CAN Bus 1 → CAN Bus 1 Setup → CAN 1 Baud Rate** and set to 1Mbps.

Open the first available Channel. If there is nothing else already configured on the CAN bus, then CAN 1 Channel 1 would be the first available channel. If this channel is already used, simply select a channel that is free — the CAN 1 channel number selection has no effect on the operation.

{{< figure src="/img/can-gauge/emtune-can-setup.png" caption="Figure 6.2 — CAN 1 Channel 1 setup menu." >}}

Store setting changes permanently in the ECU by pressing **F4**. Switch power OFF and ON to the ECU to ensure the updated CAN bus settings have been initialised. The CAN Gauge should now be receiving and displaying live runtimes.

## 7.0 Ordering Information

| Product          | Part Number |
|------------------|-------------|
| Emtron CAN Gauge | 537-711     |
