---
title: "Odometer"
description: "Track total distance and trip meters."
weight: 4
---

**Functions → Odometer**

The odometer function integrates a speed input to track total vehicle distance and up to four independent trip meters.

## Configuration

| Setting | Description |
|---------|-------------|
| Speed Input (km/h) | Channel providing vehicle speed in km/h |
| Trip 1–4 Reset Event | Event that resets each trip meter to zero |

The main **Odometer** channel holds total distance in km. Trip channels hold distance since their last reset event.

## Resetting the Odometer

The total odometer value can only be decreased with a one-time code from Emtron support:

1. Connect to the display.
2. Open **Functions → Odometer**.
3. Note the **challenge code** displayed on the page.
4. Contact Emtron support with the code to receive a reset password.
5. Enter the new odometer value. If the new value is higher than the current reading, no password is required.

Increasing the odometer (for example, after an instrument cluster replacement) does not require a support code.