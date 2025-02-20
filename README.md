# BSMRobo25-Code
Code I wrote for the Robot year 24-25. This includes all the proof of concepts and versions. Anything thats non-functional is noted as such.
The read me will contain descriptions of each branch and file.

Proof of Concepts (PoC)
---
These are tests of different libraries and functions before implementing them into the main body of code. This is my method for eliminating 
complications, so I can work out errors with that preticular library or feature before implementing it with other libraies and features.

ExpanderTest_FINAL-FUNCTIONAL_V3_11-18-24.py
----
This where I started, I needed the Pimoroni IO Expander to be functional before I could move on to anything else. I ran into some issues 
with importing the library, I'll talk more about that in my guide to setting up the PI. Chat-GPT struggles with the IO Expander library, it 
doesn't quite know how to define things, you just have to keep inputing errors untill it gets to the correct functions. However occasionally 
it get's itself stuck in a logic loop trying to use the right fuction, it ends up going back to the first thing that didn't work. I 
sometimes just have to start a new request so it doesn't refrence older attempts, I also talk more about this in my Chat-GPT tricks 
document. The only thing required to make this functional is to import sys and give the path to where the IO Expander is.

KeyboardControlledMotor_PoC_V4_1-29-25(Functional-Clean).py
----
This is where I implemented the pynput library to run a motor through the IO expander. This was the last PoC before creating the drive 
system. I did have other PoC's after it but it was to test features to add to the drive system. 

CaptiveWindow_PoC_V1_1-30-25_FUNCTIONAL.py
----
This is a functional script to run a captive window. This is when I had gotten the drive system functional but wanted to avoid the issue of 
when you hold down the keys to move the robot, the key would repeatadly put that letter into the shell or terminal. I wanted a window to pop 
up with a hidden entry text input box when you ran the code so you didn't get the repated letters. The preticular library I used couldn't be 
implemented with the drive code, but it is functional, so I figured I would include it.

tkinerwindow.py
----
This is the solution to the previous PoC not being able to be implemented with the drive code. It uses the tkinter library instead of the os.

backgroundpynput_PoC.py
----
This is a test because I was having issues getting the keyboard listener and the tkinter window to run at the same time. I implented it a 
little differently, but I still used the threads library.

Drive System
----
This is where I started to create the entire control scheme. This first version asinged a function to each unit. You can see more about the control scheme on the pdf of my notes.

V1DriveSystem(Non-Functional).py
----
First version of the drive system. This script never worked, but I used lots of the elements of it for the next verions. Also I spent a bunch of time on it, so felt I had to include it.

V2DriveSys.py
----
This is the point where I took a step back after the previous version to check myself before commiting so much time to something that wouldn't work. This time each key press directly uses the command to run the motors instead of referencing a function to do each action. 
This version only has some of the actions.

V3Drive(Non-Functional).py
----
This version added all the actions and has the tkinter window. The tkinter window is a basic version without the text box or instructions. 
This is the version where I ran into the issue with the keyboard listener and tkinter window not working together, I had a few ideas of how 
to fix it so I made a version save. 

V4Drive.py
----
This is the version where I implemented the fixes from backgroundpynput_PoC.py. This is the only change I made, I made a save because it was 
functioning exacly as I wanted it to.

V5Drive.py
----
This version adds a bit to the message and has the window open in full screen. I had plans to have the terminal update in the 
window, but that was going to be very complicated. Given the time restaints I choose to leave that feature tabled for a later 
date. NEW FEATURE?

FINALS
----
Current final versions

test.py
----
Sanity check if the main code breaks

drive.py
----
Essentailly just V5Drive.py, easier name to type than that. The up/down, true/false values are differnent on the actual pi based 
on polarity of the motors.



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
