# py-face-turret
A turret that follows your face.

This idea is stolen from Michael Reeves' laser turret which you can find here https://www.youtube.com/watch?v=Q8zC3-ZQFJI.

It's very likely that I made the whole thing way harder than it needed to be, since:

`src/face.py` sends commands to the Raspberry;

`src/server.py` hosts a server on the Raspberry, receives the commands from the previous script and sends the commands to the Arduino;

`src/servos.py` makes the Arduino able to receive commands from the Raspberry through a serial port, parses commands and sends them to the two servos that work as X and Y axis.

# Requisites
-Pythonn 3.x

-Raspberry (I used a Raspberry Pi 3 B+)

-Arduino (I used an Arduino Mega 2560)
