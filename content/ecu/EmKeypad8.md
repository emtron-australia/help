---
title: "Emtron 8 Way Keypad Configuration"
---

Configure Emtron CAN as follows to use Emtron 8 Way Keypad&nbsp;


Set CAN Baud Rate to 1Mbps&nbsp;


&nbsp; &nbsp; Config -\> Communications -\> CAN Bus 1/2 -\> CAN Bus 1/2 Setup


![Image](</lib/NewItem441.png>)



Set CAN Channel Settings as follows :&nbsp;


&nbsp; &nbsp; Config -\> Communications -\> CAN Bus 1/2 - Channel 1-6 - &nbsp; &nbsp; 40 : Emtron 8 - way Keypad


![Image](</lib/NewItem442.png>)


Configure the Keypad behavior as follows :&nbsp;


&nbsp; &nbsp; Config -\> Communications -\> Emtron CAN Devices -\> Emtron Keypad&nbsp;


![Image](</lib/NewItem443.png>)


Keypad button behavior has multiple modes of configuration


&#48;: Toggle (2 Position)

&#49;: Sequential (3 Position)

&#50;: Sequential (4 Position)

&#51;: Binary (8 Position)

&#52;: Momentary


Keypad Button1 Mode


Toggle: x2 Position

OFF - No LED

ON - Green LED


Sequential: x3 Positions

OFF - No LED

Position 1 - Green LED

Position 2 - Orange LED


Sequential: x4 Positions

OFF - No LED

Position 1 - Green LED

Position 2 - Orange LED

Position 3 - Red LED


Binary: x8 Positions

OFF - No LED

Position 1 - Green LED

Position 2 - Orange LED

Position 3 - Green \& Orange LED

Position 4 - Red LED

Position 5 - Red \& Green LED

Position 6 - Red \& OrangeLED

Position 7 - Red \& Green \& Orange LED


Momentary: Green light ON while button is pressed


Assign Keypad inputs as follows :&nbsp;


&nbsp; &nbsp; Config -\> Channels -\> Input Setup -\>&nbsp;


![Image](</lib/NewItem444.png>)




![Image](</lib/NewItem445.png>)



\*\* When using Keypad input in multiple positions (sequential or binary), the keypad position runtime can be used in tables as in above example &nbsp;



