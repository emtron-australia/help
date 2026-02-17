---
title: "Ethanol Sensor - Flex Fuel"
weight: 24
---

## Flex Fuel configuration example:

KV and SL series ECU both support the GM (Continental) and Ford style flex fuel sensors. 

## Step 1

Wire in the Ethanol Sensor to the ECU using one of the available digital inputs that can read frequency (DI 1-8) and configure the DI as follows:

Go to **Config -> Inputs -> Input Pins Setup** then select the **Vehicle** tab

![Image](</img/NewItem138.png>)

The **Input Source** should match the Digital Input channel the sensor is wired to. In this example Digital Input 6 (DI 6) is used.

Edit the input sensor settings to be as follows:

Active Edge = **Falling** \
[Arming thresholds] -> Threshold Mode = **Table**

“Edit Table” values Set to 2.0 Volts

![Image](</img/NewItem137.png>)

Configure the type of Ethanol sensor used within Emtune software, **Tuning -> Engine Functions -> Ethanol Sensor -> Setup**

![Image](</img/NewItem136.png>)

0: GM / Continental 

1: FORD

Verify the operation of the Ethanol sensor by pulling up the run time variables by pressing the shortcut key **F3** and selecting the **Fuel 2** tab.

![Image](</img/NewItem135.png>)

## Step 2

Configure the VE fuel model to load the Ethanol % compensation tables:  (Fuel Density Table and Stoichiometric Custom Table)

Preconfigured templates/copies of these tables are included within the Emtune installation package and can be found in the folder   **C:\\Emtron\\Table Files** 

To load these preconfigured tables simply right click within the current table you wish to change and select “**Load Table**” and browse to the file location listed above.

The below tables allows the ECU  to accurately make adjustments injector pulse widths based on the characteristics of ethanol based fuel and its different % blends with Gasoline.

To configure this table to go **Config-> Fuel -> Fuel Density Table**

![Image](</img/NewItem134.png>)       

Configure the custom stoichiometric table which also is based on the Ethanol % of the fuel 

To configure this table to go **Config-> Fuel -> Stoichiometric Custom Table**

![Image](</img/NewItem133.png>)

## Step 3

Next we go onto configuring the Z-Axis control on the Main Ignition Tables. 

This allows the tuner to have the ability to manipulate the tune based on the Ethanol Content % value provided by the flex fuel sensor. This Z-Axis (ethanol %) is used to determine the % blend between the two Main Ignition tables.

## Tuning -> Ignition -> Ignition Table Control -> Main Ignition Tables

![Image](</img/NewItem132.png>)

Set the **Ignition table control** to **6:  ON –Z-Axis**. 

![Image](</img/NewItem131.png>)

This will activate the **Main Ignition Tables** **1-3** as well as the **Ign Main Table Z-Axis Setup** table.

## Step 4

Go to **Tuning -> Ignition -> Z-Axis Setup -> Ign Main Table ZAxis Setup**

![Image](</img/NewItem130.png>)

Configure the **Ign Main Table Z-Axis setup** table such that the X-Axis parameter is **Ethanol Content %**.  (Shortcut key **A** to access axis setup)

![Image](</img/NewItem129.png>)

This table controls the percentage of blend used by the ECU between the Main Ignition tables. 

A value of 1.0 = use 100% **Main Ignition Table1** (Gasoline / pump gas Ignition Table)

A value of 1.5 = use the average value of **Main Ignition Table 1** and **Main Ignition Table 2**

A value of 2.0 = use 100 % percent of **Main Ignition Table 2** (E85% tune Ignition table)

The engine should be tuned on 100 % Gasoline (pump gas) and E85 separately and the appropriate Ignition tables populated before attempting to tune any Z-Axis setup tables.

Steps 2 -4 can and should be repeated for other aspects of a Flex Fuel tune. These include:

* Starting Enrichment compensation tables
* Boost Target Table Control 
* Map Limit Table Control
* Lambda Target Tables
* Any table within the ECU that can be spanned against Ethanol Content %

## NB:

The VE fuel table should not need any compensation based on Ethanol Content as the Fuel Model accounts for this.  

Should you need to make corrections Ethanol % then the Fuel Mass Modifiers table could be used to correct for any inaccuracies in the fuel model.   Such causes of error could be attributed to incorrect injector data, inaccuracies in the Flex Sensor and any other sensors in the system the ECU relies on to create an accurate model.

To enable the Fuel Mass Modifier table to go **Tuning -> Fuel -> Fuel Table Control -> Fuel Modifier Tables**

![Image](</img/NewItem128.png>)

Enable **the Fuel Mass Modifer Table Control**  set value to **1**

![Image](</img/NewItem127.png>)

Configure Fuel Mass Modifier Table such that Ethanol Content % on the X-axis and Efficiency Calculation % on the Y-axis   Shortcut key (**A**) to configure table axis. Eg below shows Fuel Mass Modifier Table with percentage trims being applied to the Main VE Fuel Fable

![Image](</img/NewItem126.png>)

