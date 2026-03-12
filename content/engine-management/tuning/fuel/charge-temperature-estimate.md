---
title: "Charge Temperature Estimate Table"
---

Used to provide the ECU an inlet air charge temperature estimate using air temp sensor and engine temp sensor inputs.

 - 0%: Charge Temp = Air Temp 
 - 50%: Charge Temp = Half way between Air Temp and Engine Temp
 - 100%: Charge Temp = Engine Temp 

![Image](</img/AAAA118.jpg>)

## Charge Temperature Offset Table
Charge Temp Offset allows the user to offset the calculated Charge Temperature in a table

** Often used when using different fuel types with higher evaporate properties (Ethanol/Methanol), and flex fuel setup (see Sample File)

![Image](</img/AAAA119.jpg>)

![Image](</img/AAAA120.jpg>)

## Charge Temperature Comp Table 1
![Image](</img/AAAA121.jpg>)

![Image](</img/AAAA122.jpg>)

## Charge Temperature Z-Axis Setup
![Image](</img/Z Axis17.jpg>)

The Z-Axis activates a user definable X-Axis to swap or blend between Charge Temperature Compensation tables based on the selected runtime 

![Image](</img/Z Axis27.jpg>)

Charge Temperature Compensation ZAxis spanned across ethanol content example shown above.