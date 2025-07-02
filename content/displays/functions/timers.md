---
title: "Timers"
---

Generates a timer with customisable start, stop, and reset logic.

![Timers](/img/ed_timers.png)
> Pictured example: Hide the camera view 10 seconds after reverse gear is deselected.

---

### Output Channel
The channel that contains the output time in seconds.

---

### On Expired Event
This event will be triggered when the timer reaches `Max Time`.

---

### Max Time
The maximum time (in seconds) that the timer can reach.
*0 = No time limit.*

---

### Reset Mode:
Determines the reset behaviour.
 - **Never:** The timer never resets.
 - **On Timer Start:** When the timer starts, the time will be reset to 0.
 - **On Timer Stop:** When the timer stops, the time will be reset to 0.
 - **On Condition:** When the `Reset Condition` result is true, the timer will be reset to 0.

---

### Start Condition
When the result of the `Start Condition` logic is true AND the result of the `Stop Condition` is false, the timer will be started. \n
*`Stop Condition` takes precedence over `Start Condition`.*

---

### Stop Condition
When the result of the `Stop Condition` logic is true, the timer will be started. \n
If there are no conditions set, the result will always be false. \n
*`Stop Condition` takes precedence over `Start Condition`.*

---

### Reset Condition:
When the result of the `Reset Condition` logic is true, the timer will be reset to 0. \n
If there are no conditions set, the result will always be false. \n
*Only used when `Reset Mode` is `On Condition`.*

---