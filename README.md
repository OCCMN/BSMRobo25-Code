# BSMRobo25-Code
Code I wrote for the Robot year 24-25. This includes all the proof of concepts and versions. Anything thats non-functional is noted as such.
The read me will contain descriptions of each branch and file.



Brushless/Arm Control
----

BrushlessMotorController_PWMControl.ino
----
Arduino script using the servo library to run the REV Neos w/ a Spark Max Controller. Had to do a lot to get it running, the 
motor contoroller didn't like a straight PWM signal for some reason. The timing makes it a single pulse after time=0 (best I can 
do explaining it in words).

Yellow = PWM
Green = Ground

SerialLED.ino + SerialKeyboardLED.py
----
These 2 pieces of code work together to turn on an LED with a keyboard press. The SerialKeyboardLED.py script is a python script that uses the pynput library to monitor keyboard inputs on a PC(this reuires you to install python and nessicary libs to your PC). 
On the press/release of a key the script sends a command over serial to the arduino. The arduino, runing the SerialLED.ino script, listens to the serial connection for incomming commands (these "commands" are almost like the name of a defintion, they don't do anything 
unless you set them up to do something) depending on the comand it either turns on or off the LED. I have one command registered to the key press to turn on the LED, and another one set on the release of the key to turn off the LED. This makes the key act like a momentary 
push button for the LED; it's only on when the key is held down. The commands are just letter and the program can distinguish between upper and lowercase letters. So for keyboard inputs I just use the uppercase as the command for pressing the key and the lowercase for the 
release of the key (thats not in this program but it is in future versions based off this). This script was a great visual representation of if the code was working I left it in for the rest of the programs as a sanity check.

SerialMotor.ino + SerialMotorKeyboard.py
----
Same setup as the LED scripts but the commands in this one control the various arm movements(arm control scheme jpg). It mixes the brushless control and the Serial communication. Pretty simple process after the other ones work, repetiton. 

ArduinoBrushedMotor.ino
----
There is one brushed motor for the arm that I needed to control with the arduino so this was just a test script for that. But this worked so well with serial as well that I want to look into using only an ardino and serial to control the robot(after qualies). It would 
remove the hassle of having to run through the pi and the IO expander. Also removes the latency with VNC. I think this would also make integrating easier as I would just have to figure out how to use the same keys to do different thing at different times. An Arm Mode and a 
Drive mode. NEW FEATURE?

Next Steps
----
1. Integrate w/bottom drive (After Qualies?)
   - Potential Issue w/ keyboard listener not ignoring inputs meant for pi
   - Issue w/ running out of usb ports? Can we use the hub ports? 

Future Docs/Files (Reminder List)
----
- REV Resources
- Brushed Motor Resources
- Brushed Motor Controller Resources
- How to set up pi for this code
- Image of Pi disk
- REV Hardware client motor controller settings
- Coding w/ ChatGPT Tricks and Tips
- Arm Schemeatic Notes
