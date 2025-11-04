---
title: "Emtune Release Notes"
weight: 2
---

## Emtune V1.22
*4 November 2025*

`Includes ECU Firmware v2.20.20`
### New Features
 - Added support for Shadow logging download. *NOT currently available on from welcome screen. Open ECU first.*
 - Added notes about Half Bridge Drivers to Output Setup form.
 - Increased max idle area demand.
 - Updated Dyno Comms.
 - Updated help browser to use docs.emtronaustralia.com.au
 - Added Home button to built in help browser.

### Bug Fixes
 - CAN Voltage visibility on Digital Input Setup form - Fixed.
 - Calibration not working on Shadow DI 7+ on Input Setup form - Fixed.
 - CAN Rx Parameters showing on R35 Launch control settings - Fixed.
 - Torque Traction Z axis table not showing - Fixed.
 - DI 7&8 not available as input voltage on SL Series - Fixed.
 - Frictional Loss min/max clamps - Fixed.
 - License check shutting down current version - Fixed.

---

## Emtune V1.21
*6 January 2025*

`Includes ECU Firmware v2.20.0`

### New Features
 - Added Math Expression parser engine to Emtune.
   - Added Math Expression based Calculated Channels mode for use in the logger.
   - Added Math Expressions to tables for user definable fast editing via 'Q' key.
   - Emtune will remember user expressions for each table.
 - Added right click menu to logging tabs.
 - Cal File Upgrade Wizard added to Utilites menu so it can be run at any time. Disabled on firmware below 2.19.0.
 - Added LSU ADV Notes inside lambda form.
 - Separated Air Mass and Fuel Mass model setup in menu system.
 - Added searchable Live Runtimes panel to Tuning and Config screens, toggle with Ctrl+R key.
 - Display of opposing cylinder in ignition channel assignment when in waste spark modes.
 - Loading of default Lambda EMAP Correction tables now done via a user prompt.
 - Significant improvment to gauge tab switching performance.
 - Significant improvment to logging group switching performance.
 - Lambda Pressure Compensation now promts user to load comp tables.
 - Added Support for Shadow 8 ECU
   - USB Communications
   - USB Bootloader
   - Shadow 8 knock detection hardware config
 - Emtune options now available from welcome screen.
 - Updated Default Logger layout.
 - Updated TMF Outflow channel names to be more descriptive.
 - Autosaved log files now append ECU serial number to the file name by default.
 - VE Table 1 and VE Table 2 edits can be linked when banked VE modes are active.
 - Added Labels to user fuel comp tables.
 - Firmware upgrade wizard can now load previous version cal file for improved migration.
 - Added Mainline ProHub Dyno controller support (newly released model) for data and direct dyno control. 
 - New app icon.
 - Added live data to Inputs Setup form to make calibrating sensors easier.
 - Increased continuous logger memory to approximately 10 minutes (up from 30 seconds).

### Bug Fixes
 - Emtune disappears off taskbar during page change - Fixed.
 - "Index position out of range" message when setting up a new logging chart - Fixed.
 - EEFFACE exception when logger tries to open a very large log file - Fixed.
 - Settings not displaying correctly when runtimes paused via 'P' key - Fixed.
 - LSU 4.9 or LSU ADV not displaying correctly - Fixed.
 - Occasional incorrect behaviour of Axis Setup Insert and Delete cell functions - Fixed.
 - Lambda Setup not updating when pressure compensations in use - Fixed.
 - Logging tabs not loading when changing with < > keys - Fixed.
 - Main tabs leaving menus in disabled state when changing with rapid [ or ] key double taps - Fixed.
 - Escape key having no default menu entry point before any menu item has ever been clicked - Fixed.
 - Numerous visibility control bugs - Fixed.
 - Logging layout not updating when a page is loaded from a file - Fixed.

---

## Emtune Update V1.20
*1 August 2023*

`Includes ECU Firmware v2.19.0`

### New Features
 - MAJOR UPDATE - New unified application theme throughout. 
 - Updated Splash screen.
 - Updated Welcome screen.
 - Tidy-up and layout audit of all forms and windows.
 - Customisable User Menu System adds ability for tuning and configuration menu items and labels to be layed out in any way.
 - Notification of paused runtime values (P Key) to status bar.
 - Improved backwards compatibility with dynamic menu structure loading depending on loaded or connected ECU firmware version.
 - Firmware Upgrade Wizard to help generate default values for new ECU functions after a firmware update.
 - Manual Calibration Offset value added to Manifold Pressure and Boost Pressure Input setup.
 - Added Apply button to Input Setup window so calibrations can be performed on the fly.
 - Option to have Emtune track the current Cal file path for the duration of the session.
 - Custom Labels added to Custom CAN Tx & Rx Data sets.
 - Custom Labels added to Timers.
 - Custom Labels added to User Temp/Pressure/Position Inputs.
 - User Labels editable from Setup windows as well as Function Configuration windows.
 - User Labels now displayed throughout Emtune in Axis Setup, F3 Runtimes window, Logger, Menus, and Gauges.
 - Logged parameters list now has sizeable Value and Units columns.
 - Option to Invert all Table Y axis’ by default.
 - Ethernet Configuration helper tool added to welcome screen. Tool requires Microsoft .NET6, which will be installed for you if not already on your system.
 - Preset Sensor Calibrations added for Emtron sensors.
 - Preset Sensor Calibrations added for common Bosch and SRS sensors.
 - Table Help view (H key) now has scalable height control.
 - Help descriptions added to CAN Data Set windows.
 - ECU Logging setup now calculates the logging time available based on dataset structure and logging rates.
 - ECU Logging setup can now multi-select channels for removal.
 - Confirmation message before erasing ECU Logging memory.
 - Option to view single axis table surface plot as a slim 3D line.
 - Wheel Speed Input filtering tables added.
 - New User Outputs setup window greatly improves the readability of the logic structure.
 - Timers now use new setup window.
 - Race Timer now use new setup window.
 - Cal Slot Setup window updated.
 - Inputs Setup and Function Setup lists scrollable with mouse wheel.
 - More Injector Characterization Tables added to included files.
 - More sample Cal files added to included files.
 - Message added to ECU Logging Setup when 500Hz is used to warn of disabling other data sets.
 - Updates to contextual help.
 - Updated log selection highlight to improve visibility.
 - Changed Gearbox Oil Temp channel to Transmission Oil Temp.
 - Changed Gearbox Ratio channel to Gear Ratio.
 - Firmware release notes now displayed before confirmation of a firmware update.
 - Scaler Calculator tool for Wheel Speeds, Input/Output Shaft Speeds, and Turbo Speed input channels.
 - Status input type mode added to Digital Inputs for more intuitive use of User Functions and Keypad buttons as input source.
 - Soft rate limiter added to Auto Lambda (L Key) function to stop repeated updates before the last change has been sent to the ECU.
	
### Bug Fixes
 - MAP Calibration being reloaded with previous values on connection recovery - Fixed.
 - R, P, and V key shortcuts interfering with logged parameter search - Fixed.
 - Null reference when selecting custom logged parameter range display – Fixed.
 - User Output Function Labels displaying in Timer Setup windows – Fixed.
 - Deletion of last table axis cell not working – Fixed.
 - Axis setup Insert key inserting value of zero regardless of position or adjacent cell values – Fixed.
 - Importing of tables from locked Cal files – Fixed.
 - Table Surface Plot not rendering correctly when table set to single axis only – Fixed.
 - Cal file name not updating if edited outside Emtune – Fixed.
 - Threading issue encountered sometimes when sending cal file to ECU – Fixed.
 - Numerous spelling mistakes fixed.
 - Emtune erroneously downloading zeros from an unbooted ECU when serial number reported as 0 – Fixed.
 - Table Difference View not always displaying correct values - Fixed.
 - Log position cursor not showing on some 2D Tables - Fixed.

---

## Emtune Update V1.19
*1 September 2020*

`Includes ECU Firmware v2.18.0`

### New Features
 - MAJOR UPDATE - An expansion of the Emtron web server now adds the ability of Emtune auto updates and allows the latest version to operate in a backwards compatibility mode.  Emtune will detect the version of firmware in the connected ECU or desired ECU cal file opened in offline mode and will apply the correct menu settings.  This ensures calibration settings such as tables and menu items in Emtune will sync with the corresponding major firmware build version.  
 - Calculated Channel feature added to Emtune.  UI level functions added.  Ability to code custom channels with C language.  Calculated channels available in Emtune logging and Emtune gauges in realtime 
 - Emtune Help is served online from the Emtron web server. 
 - Optimalisation of vertical viewing space in the Logging View  
 - Logging plot splitters made narrower for improved viewing space and cleaner look.
 - Logging Screen Runtime list has been rebuilt with a splitter added to allow user width control.  "R" Button hotkey to toggle viewability functionality has been maintained. 
 - DTC Code form sorting feature.  Sorts by current and then by non active with error count codes
 - www.emtron.world hyperlink added to Emtune Welcome screen
 - Cruise Control Command Switch voltage table added to allow user configuration of any single input cruise command switch.
 - Added support for temperature input channel units to be in represented in Ohms
 - Auto conversion of predefined input channels in Kilohms if selected
 - Manual Lambda correction target minimum lowered to 0.3
 - Added a message box to confirm deleting logging pages or logging page groups to prevent accidental user deleting
 - Installer Paths added for Sensor Calibrations 
 - Lambda trim "L" Button hotkey now limits the amount of instantaneous lambda trimming per button press. This will also limit the lambda trim from correcting when the lambda sensor is not ready due to an abnormal lambda error
 - Lambda trim "L" Button hotkey command now clears the current short term and current long term fuel trims with each key press.  The currently used trims are also accounted for in the lambda correction calculation to prevent closed loop lambda control windup during VE table calibration 
 - Minor logo colour theme change in Emtune 
 - Improve Emtune application bootup time by 25 percent and show splash screen longer during the bootup process
 - Search feature speed improved
 - Shift Left and Shift left hotkey added to logging to allow shifting the log plot left and right
 - Bosch Windarab export feature added
  
### Bug Fixes
 - Nitrous Visibility control issue fixed.
 - Filter setting now visible when input channel set to sync sensor.
 - Charge Temperature Offset now reads read correctly when configured to Imperial Units 
 - Lambda correction hotkey functions during Pause (P button hotkey) mode now apply correctly.
 - Ctrl Z function not updating local single zone menu item settings until there is a user navigation.  It now updates with no user navigation as expected.
 - ECU Overview summary "Trailing Spark" channels displaying even when this ignition mode was not selected fixed.  
 - Track Map not plotting fixed.  
 - Changing view into logging page or from runtimes list would cause navigation bar toggle tabs.  Focus now goes to the currently opened tab navigation. 
 - Status bit based data no updating when in pause mode

---

## Emtune Update V1.18
*20 September 2019*
### New Features
 - MAJOR UPDATE - Imperial Units Support Globally - Selectable groups
 - Parameter Search Feature has units added to the ID
 - Gauge Plot Zoom function added when in pause mode
 - Gauge Layout lock to prevent accidental dragging of windows
 - 2D Plots added yellow box border when in focus
 - Pause Key P changes focus from the main table to the 2D Plot
 - Window panning added to the 2D Plot when in pause mode
 - Yamaha YXZ1000R Manifold Pressure Sensor Calibration added 
 - Bosch 2.5ar Sensor calibration added
 - Axis Setup Auto Sort numerical order
 - Axis Setup blanking unused cells 
 - License Server auto comms enable for unapproved public users
 - 32Bit runtime ID's added for GPS support 
 - Inputs channel selection changed to a search window for fast selection
 - ID1050 Injector Deadtime and Linearisation Tables added 
 - Added Emtron Display Tx Set 1 and 2

---

## Emtune Update V1.17
*25 February 2019*
### New Features
 - Major Update for Emtune Help 
 - Added ECU Overview Button to the ECU Password Protection Screen
 - Added new Hotkey Ctrl + A for highlighting all cells in a table
 - A Password Protected ECU can now have an unlocked Cal File loaded into the ECU by any user.  NOTE: The Password Protected ECU Cal File will be overwritten and lost
 - Charge Temp Estimate Offset example tables added to a new Tables folder
 - 82mm Bosch ETC Cal Module added
 - Subaru Sti ETC Cal Module added 
 - 8 Way Emtron Keypad features now available 
 - Table Interpolation and extrapolate functions now consider cell values in the calculation
	
---

## Emtune Update V1.16
*4th December 2018*
### New Features
 - Tables and the surface plot now have a five colour gradient. There are 3 main colour groups:
 - Fuel related tables
 - Ignition related tables
 - All other tables
 - 'Builds Features' can now be enabled and disabled from Emtune. Enabled Builds will be displayed in the welcome screen.
 - Offline Cal files can now be locked 
 - A new warning when attempting to exceed the maximum password length.
 - New table smoothing feature (S button) . Can be pressed once or held until desired smoothing effect reached.
### Bug Fixes
 - Fixed issues with occasional incorrect menu visibility.
 - Keyboard events causing help search issues.

---

## Emtune Update V1.15
*24th April 2018*
### New Features
 - R35 GT-R Plugin ECU base calibration added to the Cal files directory.
 - Emtune controls EFI relay when there is a key OFF event to allow online editing while the PC is connected.
 - Improved drawing in the Emtune logger.
 - Paddle Shift example Cal Module updated. 
### Bug Fixes
 - Fix cursor issue causing different values to be displayed in logger.
 - Fix cursor appearing stuck when in dual mode in logger.

---

## Emtune Update V1.14
*26th Feb 2018*
### New Features
 - ECU online lockout when attempting to connect to a newer firmware than the current version of Emtune supports
 - Active Cell Crosshair feature that tracks the current logger cursor position - O key toggles a yellow box in the tuning view. 
 - Manifold Pressure channel imperial units is now an option.   

### Bug Fixes
·	Q key uses active cell now.
·	Table group paste works when inverted.
·	Fix log file name not updating when saving the log.
·	Fix Load Page in the logger causing another group to be created.

---

## Emtune Update V1.13
*23th November 2017*
### New Features
 - New layout system for logging
 - Logging video playback
 - Logging track map (beta)
 - 'Q' key loads a configurable runtime value into the active cell
 - Active cell available on all tables
 - Logs can be viewed without opening a calibration file
### Bug Fixes
 - Removed interpolation of status values in logs
 - Fixed issue where occasionally a "firmware does not support this feature" was incorrectly shown.
 - Fixed issue where occasionally the table crosshair would hide when on the top row of a table.

## Emtune Update V1.12
*11th August 2017*
### New Features
 - Added logging page groups
 - Added Lambda Table conversion for AFR option 
 - 2D Plot auto-scale feature
 - Improved ECU logging runtime selector form for fast selection
### Bug Fixes
	PC logging runtimes that are not in ECU

---

## Emtune Update V1.11
*1st May 2017*
### New Features
 - Adding undo to Import Table
 - Auto License server user level update 
 - Global font update
 - Inputs and Output channels have row in bold when enabled
 - Adding erase logs to the Welcome Screen
 - PC Logging performance optimised including large log loading speed 
 - R Hotkey in Logging View to hide RHS runtimes parameter list
 - PC Logging navigation smoothness improvements
 - Progress bar cycle when waiting for command progress
 - PC Log Autosaving
 - Invert function added for multi-channel function outputs 
### Bug Fixes
 - Incorrect fault value scaling in Inputs Setup Form
 - "Format Error" with user login 
 - Crash when closing overlaid log file
 - Auto Lambda correct using current lambda value and not the paused lambda value for correction
 - Plot spin getting limited
 - General Visibility control issue
 - Zoom getting stuck in PC logging
 - Error due to multiple PC logs being open
 - Panning double press 
 - Error when you press F8 twice fast
 - Lambda target F6 shortcut not working
 - PC Logging crashing with large logs
	
---

## Emtune Update V1.10
*27th September 2016*
### New Features
 - Adding license server support.
 - Usability improvements to the custom tx dataset form.
 - Live data screen can be configured when in the offline file editing mode.
 - Logging plot navigation speed improvements.
 - F10 to download ECU logs.
 - Adjustable table font size.
 - Gauge files for multiple screen resolutions.
 - Input and output functions that are disabled are shown in grey.
 - Restyling the progress bars.
### Bug Fixes
 - Opening saved scope files automatically assigns channels.
 - Scope form now takes navigation key presses immediately after a download.
## Emtune Update V1.9
*3rd June 2016*
### New Features
 - New colour theme.
 - Critical events can be acknowledged without opening the event log form.
 - New default gauge layouts.
 - Adjustable hysteresis on parameter event generation conditions.
 - Partial cal files can be loaded into the current file or ECU.
 - Logging elapsed time parameter is fixed at the top of the right hand side parameter list.
 - Logging parameter list is sortable and searchable.
 - Quick reconnect when the communications cable is temporarily disconnected.
 - Help text in ECU logging setup form.
### Bug Fixes
 - Fixed issue with up and down buttons on the scope form not working correctly.
 - Fixed issue when using the keyboard to select the logging screen and losing focus.
 - Fixed issue when connecting to an ECU with unsupported firmware.
 - Fixed issue where there was a gap at the start of a recorded PC log.
 - Fixed issue where event log notification was flashing in the welcome screen.
 - Fixed flicker on logging view when settings were changed.
 - Fixed issue where exporting tab gauge layouts would sometimes output the wrong layout.

---

## Emtune Update V1.8
*25th March 2016*
### New Features
 - Custom CAN Rx form.
 - Global dash configuration load/save form.
 - Logging view zooms to fit overlay log if larger than main log.
 - Keyboard navigation for scope view.
 - Event log system that detects parameter changes and error conditions.
 - ECU logging downloads are faster.
 - ECU logs can be downloaded while connected.
 - Runtime value menu (F3) how has a search function.
 - Gear detection voltage tolerance table.
 - Live data mode for telemetry applications.
 - Adjustable gauge 'speed' in live data mode.
 - Adjustable communication timeout values.
 - Increased amount of history available in the pause function.
 - Runtime value list gauge.
### Bug Fixes
 - Fixed the table crosshair appearing on the table offline under some conditions.
 - Pressing F12 multiple times while connecting now doesn't cause error message, instead it is ignored. 
 - Fixed hard to read text in knock control setup form.
 - Dash tab group not deleting.
	
---

## Emtune Update V1.7
*29th January 2016*
### New Features
 - Inputs and functions grids are now searchable.
 - Table invert is now based on individual tables.
 - Double click the calibration file in windows explorer now opens EMtune with the clicked on file.
 - Added text value to gauges for status parameters.
 - Parameter move up and down options in the time plot configuration form.
### Bug Fixes
 - Key off then key on recovery speed improved.
 - Tab change speed improved.

---

## Emtune Update V1.6
*18th January 2016*
> To take advantage of new gauge layouts, you may need to reset the gauge layouts to their default setting. To do this, select 'Dash Setup' from the 'File' menu, and then click the 'Reset to Default' button down the bottom right. Warning: This will erase all dash customisations that have been made - only do this if you are not concerned with losing customisations.

### New Features
 - Adding search to user output function parameter selection.
 - Added the maths input popup to the input custom calibration table.
 - Improved the software startup time.
 - Text relating to parameter status values now shows in logging.
 - New 3D table plot. Now has correct axis scaling, and the current position is displayed at the top left.
 - Gauges available on the tuning, configuration and diagnostics view.
 - Splitters are now on all gauge panels allowing the screen ratio to be adjusted.
 - Modern themed main menu, and improved general styling.
 - Full screen mode (F11) and full screen table (CTRL + F11).
 - Added gauge layout import and export.
 - Added gauge align to grid function.
 - Removed old plot tab. Newer gauges can be used instead.
 - New logging navigator.
 - Adding release notes form.
 - Prompt user when in recovery mode and an ECU with a different serial number is plugged in.
 - Table Y axis can now be inverted.
 - Gauge configurations can be imported and exported.
 - Gauge font size is now adjustable.
 - Better support for high DPI screens.
	
### Bug Fixes
 - Fixed falling back to the welcome screen occasionally during connection.
 - Fixed falling back to the welcome screen occasionally during recovery.
 - Fixed table crosshair drawing issues.
 - Fixed runtime popup form not updating after a connection recovery.
