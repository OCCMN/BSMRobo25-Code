# BSMRobo25-Code
Code I wrote for the Robot year 24-25. This includes all the proof of concepts and versions. Anything thats non-functional is noted as such.

The read me will contain descriptions of each branch and file.

Proof of Concepts (PoC)

These are tests of different libraries and functions before implementing them into the main body of code. This is my method for eliminating complications, so I can work out errors with that preticular library or feature before implementing it with other libraies and features.

ExpanderTest_FINAL-FUNCTIONAL_V3_11-18-24.py

This where I started, I needed the Pimoroni IO Expander to be functional before I could move on to anything else. I ran into some issues with importing the library, I'll talk more about that in my guide to setting up the PI. Chat-GPT struggles with the IO Expander library, it doesn't quite know how to define things, you just have to keep inputing errors untill   it gets to the correct functions. However occasionally it get's itself stuck in a logic loop trying to use the right fuction, it ends up going back to the first thing that didn't work. I sometimes just have to start a new request so it doesn't refrence older attempts, I also talk more about this in my Chat-GPT tricks document. The only thing required to make this functional is to import sys and give the path to where the IO Expander is.

KeyboardControlledMotor_PoC_V4_1-29-25(Functional-Clean).py

This is where I implemented the pynput library to run a motor through the IO expander. This was the last PoC before creating the drive system. I did have other PoC's after it but it was to test features to add to the drive system. 
