---
title: "Connection Troubleshooting"
description: "Steps to resolve connection issues between your PC and Emtron displays."
weight: 1
---

If you are unable to connect to an Emtron display from your PC, the most common cause is security software blocking the connection. Work through the steps below in order.

## 1. Temporarily Disable Antivirus Software

Some antivirus programs actively block network connections to unknown devices, even on a local network. Temporarily disabling your antivirus is the quickest way to determine whether it is the cause.

1. Locate your antivirus icon in the Windows system tray (bottom-right of the taskbar).
2. Right-click the icon and look for an option such as **Disable**, **Pause Protection**, or **Turn off**.
3. Choose a short disable period (e.g. 10–15 minutes) if prompted.
4. Attempt to connect to the display again.
5. If the connection succeeds, re-enable your antivirus and proceed to [add a firewall exception](#add-a-windows-firewall-exception) rather than leaving protection disabled.

> **Note:** The exact steps vary by antivirus product. Refer to your software's documentation if you cannot find the disable option.

## 2. Add a Windows Firewall Exception

Windows Firewall may block incoming or outgoing traffic to the display. Adding an exception allows the connection while keeping the firewall active.

### Allow an App Through the Firewall

1. Open the **Start** menu and search for **Windows Defender Firewall**.
2. Click **Allow an app or feature through Windows Defender Firewall**.
3. Click **Change settings** (administrator rights required).
4. Click **Allow another app…** and browse to the EMtune or display configuration executable.
5. Ensure both **Private** and **Public** checkboxes are ticked for the application.
6. Click **OK** to save.

## 3. Check Network Adapter Settings

If the display is connected over Wi-Fi or a dedicated Ethernet adapter, ensure the adapter is set to a **Private** network profile. Windows restricts some traffic on Public networks.

1. Open **Settings → Network & Internet**.
2. Click on the active network connection.
3. Under **Network profile type**, select **Private**.

## 4. Still Having Issues?

If none of the above steps resolve the connection problem, please contact [Emtron support](../../support/support).
