# Import Libraries
import sys
sys.path.append('/home/robo24/myenv/lib/python3.11/site-packages')
import ioexpander
from pynput import keyboard
import time
import threading
import tkinter as tk

# Initialize the IO Expander
expander = ioexpander.IOE(i2c_addr=0x18)  # Default I2C address of the IO Expander

# Define Variabes
speedvar = 0.8  # Speed variable (0.0 to 1.0)
speeddis = speedvar * 100  # Convert to percentage for display
print(f"Speed: {speeddis}%")  # Initial speed display

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
expander.set_pwm_frequency(400) #Frequency in Hz (ajust to motor)

#define PWM resolution
PWM_MAX = 65535 #65535 (16-bit max value

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
    ##global speedvar
    try:
#Sets Speed
##        if key.char == '=':  # = is presed increase speed by 5%
##            speedvar += 0.01
##            speeddis = speedvar * 100
##            print(f"Speed:{speeddis}%")
##        elif key.char == '-':  # - is presed decrease speed by 5%
##            speedvar -= 0.01
##            speeddis = speedvar * 100
##            print(f"Speed:{speeddis}%")
##        elif key.char == '1': #If 1 is pressed set speed to 25%
##            speedvar = 0.25
##            speeddis = speedvar * 100
##            print(f"Speed:{speeddis}%")
##        elif key.char == '2': #If 2 is pressed set speed to 50%
##            speedvar = 0.50
##            speeddis = speedvar * 100
##            print(f"Speed:{speeddis}%")
##        elif key.char == '3': #If 3 is pressed set speed to 75%
##            speedvar = 0.75
##            speeddis = speedvar * 100
##            print(f"Speed:{speeddis}%")
#Forward Drive            
        if key.char == 'w':
            run_motor(0, 0.34, False) #M0 fwd @speedvar
            run_motor(1, 1, True) #M1 fwd @speedvar
            time.sleep(0.01)
#Backward Drive
        elif key.char == 's':
            run_motor(0, 0.34, True) #M0 bwd @ speedvar
            run_motor(1, 1, False) #M1 bwd @ speedvar
            time.sleep(0.01)
#Left Turn
        elif key.char == 'a':
            run_motor(0, 0.34, True) #M0 bwd @ 20%
            run_motor(1, 1, True) #M1 fwd @ 30%
            time.sleep(0.01)
#Right Turn
        elif key.char == 'd':
            run_motor(0, 0.34, False) #M0 fwd @ 30%
            run_motor(1, 1, False) #M1 bwd @ 20%
            time.sleep(0.01)
#LF Flip Up
        elif key.char == 'u':
            run_motor(2, 0.6, False) #M2 up @ 40%
            time.sleep(0.01)
#LF Flip Down
        elif key.char == 'j':
            run_motor(2, 0.6, True) #M2 dwn @ 40%
            time.sleep(0.01)
#RF Flip Up
        elif key.char == 'i':
            run_motor(3, 0.6, True) #M3 up @ 40%
            time.sleep(0.01)
#RF Flip Down
        elif key.char == 'k':
            run_motor(3, 0.6, False) # M3 dwn @ 40%
            time.sleep(0.01)
#LR Flip Up
        elif key.char == 'y':
            run_motor(4, 0.6, True) # M4 up @40%
            time.sleep(0.01)
#LR Flip Down
        elif key.char == 'h':
            run_motor(4, 0.6, False) #M4 dwn @40%
            time.sleep(0.01)
#RR Flip Up
        elif key.char == 'o':
            run_motor(5, 0.6, False) #M5 up @40%
            time.sleep(0.01)
#RR Flip Down
        elif key.char == 'l':
            run_motor(5, 0.6, True) #M5 dwn @40%
            time.sleep(0.01)

        ##speedvar = max(0.0, min(speedvar, 1.0))
    
    except AttributeError:
        pass

def on_release(key):
    try:
#Forward Stop
        if key.char == 'w':
            print("Forward")
            run_motor(0, 0, False)#stop motor 0 on release
            run_motor(1, 0, False)#stop motor 1 on release
#Backward Stop
        elif key.char == 's':
            print("Backward")
            run_motor(0, 0, False)#stop motor 0 on release
            run_motor(1, 0, False)#stop motor 1 on release
#Left Turn Stop
        elif key.char == 'a':
            print("Left Turn")
            run_motor(0, 0, False) #stop motor 0 on release
            run_motor(1, 0, False) #stop motor 1 on release
#Right Turn Stop
        elif key.char == 'd':
            print("Right Turn")
            run_motor(0, 0, False) #stop motor 0 on release
            run_motor(1, 0, False) #stop motor 1 on release    
#LF Flip Up Halt
        elif key.char == 'u':
            print("LF Up")
            run_motor(2, 0, False) #M2 Halt
#LF Flip Down Halt
        elif key.char == 'j':
            print("LF Down")
            run_motor(2, 0, False) #M2 Halt 
#RF Flip Up Halt
        elif key.char == 'i':
            print("RF Up")
            run_motor(3, 0, False) #M3 Halt
#RF Flip Down Halt
        elif key.char == 'k':
            print("RF Down")
            run_motor(3, 0, False) # M3 Halt
#LR Flip Up Halt
        elif key.char == 'y':
            print("LR Up")
            run_motor(4, 0, False) # M4 Halt
#LR Flip Down Halt
        elif key.char == 'h':
            print("LR Down")
            run_motor(4, 0, False) #M4 halt
#RR Flip Up Halt
        elif key.char == 'o':
            print("RR Up")
            run_motor(5, 0, False) #M5 halt
#RR Flip Down Halt
        elif key.char == 'l':
            print("RR Down")
            run_motor(5, 0, False) #M5 halt
            
    except AttributeError:
        # Handle other keys
        pass
    
    # Stop the listener when 'Esc' is released
    if key == keyboard.Key.esc:
        print("Stopping Motors...")
        run_motor(MOTORS.index(motor), 0, False) #Stop all motors
        print("All Motors Halted")
        print("Safe to Stop Program")
        return False  # Returning False stops the listener
    


# Function to launch the Tkinter window
def open_window():
    global speedvar
    # Create a simple Tkinter window
    root = tk.Tk()
    root.title("Drive System")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}+0+0")
    
    # Add a StringVar to update the message dynamically
    message_var = tk.StringVar()

    #Explains Controls
    instructions_message = tk.Label(root, text="Welcome to the Robot Drive System!\nUse WASD to Steer\nFlipper Control As Follows\n(Up/Down)\nLeft Front: u/j Right Front: i/k\nLeft Rear:y/h Right Rear:o/l", font=("Arial", 14), anchor="center")
    instructions_message.pack(pady=10)
    
    # Define the message with the variable from the script
    def update_message():
        global speedvar
        message_var.set(f"Hit ESC for E-Stop.\nSpeed is set to: {speedvar*100:.0f}%")
        root.after(100, update_message) #refresh the message every 100ms

    update_message()

    # Add a multi-line message label that updates dynamically
    message_label = tk.Label(root, textvariable=message_var, font=("Arial", 12), justify="center", wraplength=250, fg="red")
    message_label.pack(pady=2)

    #Hidden Entry Bar
    entry = tk.Entry(root)
    entry.pack(pady=5)
    entry.bind("<Key>", on_key)
    
    #Release of liability
    lol_message = tk.Label(root, text="Owen Case denies all liability for damages caused by any potential sentience.\nIn Case of Sentience:\nA glass of water is not provieded", font=("Arial", 8), anchor="center", fg="gray")
    lol_message.pack(pady=5)
    
    # Center align all widgets in the window
    instructions_message.pack_configure(anchor="center")
    message_label.pack_configure(anchor="center")
    entry.pack_configure(anchor="center")
    lol_message.pack_configure(anchor="center")
    
    # Start the Tkinter event loop
    root.mainloop()
    


# Create and start the listener thread
listener_thread = threading.Thread(target=start_listener, daemon=True)
listener_thread.start()

# Open the Tkinter window
open_window()

