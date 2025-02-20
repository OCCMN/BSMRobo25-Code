# Import Libraries
import sys
sys.path.append('/home/robo24/myenv/lib/python3.11/site-packages')
import ioexpander
from pynput import keyboard
import time
import threading
import tkinter as tk

# Initialize the IO Expander
expander = ioexpander.IOE(i2c_addr=0x19)  # Default I2C address of the IO Expander

# Define Variabes
speedvar = 0.1 #sets speed variable
speeddis = speedvar * 100 #used to dispay speed variable as a percent not a decimal
print(f"Speed: {speeddis}%")#intial speed displayed

#Pin assign multiple motors
MOTORS = [
    {"pwm_pin": 1, "dir_pin": 7}, #Motor ID: 0 Left Drive
    {"pwm_pin": 2, "dir_pin": 8}, #Motor ID: 1 Right Dive
    {"pwm_pin": 3, "dir_pin": 9}, #Motor ID: 2 Left Front Flip
    {"pwm_pin": 4, "dir_pin": 10}, #Motor ID: 3 Right Front Flip
    {"pwm_pin": 5, "dir_pin": 11}, #Motor ID: 4 Left Rear Flip
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
    
# Start the listener in a separate thread
def start_listener():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
        
# Function Capture input sans displaying it
def on_key(event):
    return "break"
    
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
#Forward Drive            
        elif key.char == 'w':
            print("Forward")
            run_motor(0, speedvar, True) #M0 fwd @speedvar
            run_motor(1, speedvar, True) #M1 fwd @speedvar
#Backward Drive
        elif key.char == 's':
            print("Backward")
            run_motor(0, speedvar, False) #M0 bwd @ speedvar
            run_motor(1, speedvar, False) #M1 bwd @ speedvar
#Left Turn
        elif key.char == 'a':
            print("Left Turn")
            run_motor(0, 0.2, False) #M0 bwd @ 20%
            run_motor(1, 0.3, True) #M1 fwd @ 30%
#Right Turn
        elif key.char == 'd':
            print("Right Turn")
            run_motor(0, 0.3, True) #M0 fwd @ 30%
            run_motor(1, 0.2, False) #M1 bwd @ 20%
#LF Flip Up
        elif key.char == 'u':
            print("LF Up")
            run_motor(2, 0.4, True) #M2 up @ 40% 
#LF Flip Down
        elif key.char == 'j':
            print("LF Down")
            run_motor(2, 0.4, False) #M2 dwn @ 40% 
#RF Flip Up
        elif key.char == 'i':
            print("RF Up")
            run_motor(3, 0.4, True) #M3 up @ 40%
#RF Flip Down
        elif key.char == 'k':
            print("RF Down")
            run_motor(3, 0.4, False) # M3 dwn @ 40%
#LR Flip Up
        elif key.char == 'y':
            print("LR Up")
            run_motor(4, 0.4, True) # M4 up @40%
#LR Flip Down
        elif key.char == 'h':
            print("LR Down")
            run_motor(4, 0.4, False) #M4 dwn @40%
#RR Flip Up
        elif key.char == 'o':
            print("RR Up")
            run_motor(5, 0.4, True) #M5 up @40%
#RR Flip Down
        elif key.char == 'l':
            print("RR Down")
            run_motor(5, 0.4, False) #M5 dwn @40%
            
    except AttributeError:
        pass

def on_release(key):
    try:
#Forward Stop
        if key.char == 'w':
            run_motor(0, 0, False)#stop motor 0 on release
            run_motor(1, 0, False)#stop motor 1 on release
#Backward Stop
        elif key.char == 's':
            run_motor(0, 0, False)#stop motor 0 on release
            run_motor(1, 0, False)#stop motor 1 on release
#Left Turn Stop
        elif key.char == 'a':
            run_motor(0, 0, False) #stop motor 0 on release
            run_motor(1, 0, False) #stop motor 1 on release
#Right Turn Stop
        elif key.char == 'd':
            run_motor(0, 0, False) #stop motor 0 on release
            run_motor(1, 0, False) #stop motor 1 on release    
#LF Flip Up Halt
        elif key.char == 'u':
            run_motor(2, 0, False) #M2 Halt
#LF Flip Down Halt
        elif key.char == 'j':
            run_motor(2, 0, False) #M2 Halt 
#RF Flip Up Halt
        elif key.char == 'i':
            run_motor(3, 0, False) #M3 Halt
#RF Flip Down Halt
        elif key.char == 'k':
            run_motor(3, 0, False) # M3 Halt
#LR Flip Up Halt
        elif key.char == 'y':
            run_motor(4, 0, False) # M4 Halt
#LR Flip Down Halt
        elif key.char == 'h':
            run_motor(4, 0, False) #M4 halt
#RR Flip Up Halt
        elif key.char == 'o':
            run_motor(5, 0, False) #M5 halt
#RR Flip Down Halt
        elif key.char == 'l':
            run_motor(5, 0, False) #M5 halt
            
    except AttributeError:
        # Handle other keys
        pass
    
    # Stop the listener when 'Esc' is released
    if key == keyboard.Key.esc:
        print("Stopping Motors...")
        run_motor(MOTOR.index(motor), 0, False) #Stop all motors
        print("All Motors Halted")
        print("Safe to Stop Program")
        return False  # Returning False stops the listener
    


# Function to launch the Tkinter window
def open_window():
    # Create a simple Tkinter window
    root = tk.Tk()
    root.title("Input Window")

     
    # Add a StringVar to update the message dynamically
    message_var = tk.StringVar()

    # Define the message with the variable from the script
    def update_message():
        message_var.set(f"Welcome to the Robot Drive System.\nSpeed is set to: {speeddis:.0f}%")

    update_message()

    # Add a multi-line message label that updates dynamically
    message_label = tk.Label(root, textvariable=message_var, font=("Arial", 12), justify="center", wraplength=250)
    message_label.pack(pady=10)

    entry = tk.Entry(root)
    entry.pack(pady=10)

    entry.bind("<Key>", on_key)
        
    # Start the Tkinter event loop
    root.mainloop()
    

# Create and start the listener thread
listener_thread = threading.Thread(target=start_listener, daemon=True)
listener_thread.start()

# Open the Tkinter window
open_window()

