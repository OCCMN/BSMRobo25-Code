# Import Libraries
import sys
sys.path.append('/home/robo24/myenv/lib/python3.11/site-packages')
import ioexpander
from pynput import keyboard
import time

# Initialize the IO Expander
expander = ioexpander.IOE(i2c_addr=0x18)  # Default I2C address of the IO Expander

# Define Variabes
speedvar = 0.1 #sets speed variable
speeddis = speedvar * 100 #used to dispay speed variable as a percent not a decimal
print(f"Speed: {speeddis}%")#intial speed displayed

#Pin assign multiple motors
MOTORS = [
    {"pwm_pin": 1, "dir_pin": 7}, #Motor ID: 0 Left Drive
    {"pwm_pin": 2, "dir_pin": 8}, #Motor ID: 1 Right Dive
    {"pwm_pin": 3, "dir_pin": 9}, #Motor ID: 2 Left Front Flip
    {"pwm_pin": 4, "dir_pin": 10}, #Motor ID: 3 Left Rear Flip
    {"pwm_pin": 5, "dir_pin": 11}, #Motor ID: 4 Right Front Flip
    {"pwm_pin": 6, "dir_pin": 12}, #Motor ID: 5 Right Rear Flip
]

# Set up the pins for all motors
for motor in MOTORS:
    expander.set_mode(motor["pwm_pin"], ioexpander.PWM) 
    expander.set_mode(motor["dir_pin"], ioexpander.OUT) 

#Dictionary to track state of key
#key_states = {}

#set PWM freq
expander.set_pwm_frequency(1000) #Frequency in Hz (ajust to motor)

#define PWM resolution
PWM_MAX = 65535

#Function for motor control
def run_motor(motor_index, speed, direction):
    """
    Controls the motor speed and direction.
    
    :param motor_index: Index of the motor in the MOTORS list
    :param speed: Motor speed (0.0 to 1.0 for 0% to 100% duty cycle).
    :param direction: Motor direction (True for forward, False for reverse).
    """
    
    motor = MOTORS[motor_index]
    
    # Set the direction
    expander.output(motor["dir_pin"], direction)
    
    # Set the PWM duty cycle
    speed = int(max(0.0, min(1.0, speed)) * PWM_MAX) # Clamp speed to range [0.0, 1.0]
    expander.output(motor["pwm_pin"], speed)
    
    
def on_press(key):
    global speedvar
    try:
        if key.char == '=':  # = is presed increase speed by 5%
            speedvar += 0.05
            speeddis = speedvar * 100
            print(f"Speed: {speeddis}%")
        elif key.char == '-':  # - is presed decrease speed by 5%
            speedvar -= 0.05
            speeddis = speedvar * 100
            print(f"Speed: {speeddis}%")
        elif key.char == '1': #If 1 is pressed set speed to 25%
            speedvar = 0.25
            speeddis = speedvar * 100
            print(f"Speed: {speeddis}%")
        elif key.char == '2': #If 2 is pressed set speed to 50%
            speedvar = 0.50
            speeddis = speedvar * 100
            print(f"Speed: {speeddis}%")
        elif key.char == '3': #If 3 is pressed set speed to 75%
            speedvar = 0.75
            speeddis = speedvar * 100
            print(f"Speed: {speeddis}%")
        elif key.char == 'w':
            run_motor(0, speedvar, True) #run motor 0 forward
            run_motor(1, speedvar, True) #run motor 1 forward
        elif key.char == 's':
            run_motor(0, speedvar, False) #run motor 0 backward
            run_motor(1, speedvar, False) #run motor 0 backward
            
    except AttributeError:
        pass

def on_release(key):
    try:
        if key.char == 'w':
            run_motor(0, 0, True)#stop motor 0 on release
            run_motor(1, 0, True)#stop motor 1 on release
        elif key.char == 's':
            run_motor(0, 0, False)#stop motor 0 on release
            run_motor(1, 0, False)#stop motor 1 on release
    except AttributeError:
        # Handle other keys
        pass
    
    # Stop the listener when 'Esc' is released
    if key == keyboard.Key.esc:
        print("Exiting program...")
        return False  # Returning False stops the listener


# Start listening to key events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    
