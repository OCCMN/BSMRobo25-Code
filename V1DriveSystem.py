import sys
sys.path.append("/home/robo24/myenv/lib/python3.11/site-packages")
from pynput import keyboard
import ioexpander
import time
import threading

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
key_states = {}

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

#drives robot forward
def forward_drive():
    while True:
        key_states.get('up', False) #loop while up arrow key is held
        print("Forward")
        threading.Thread(target=run_motor, args=(0, speedvar, True)).start()  # Run Left Drive motor
        threading.Thread(target=run_motor, args=(1, speedvar, True)).start()  # Run Right Drive motor
        time.sleep(0.1)
    
#drives robot backward
def backward_drive():
    while True:
        key_states.get('down', False) #loop while key is held
        print("Backward")
        threading.Thread(target=run_motor, args=(0, speedvar, False)).start()  # Run Left Drive motor
        threading.Thread(target=run_motor, args=(1, speedvar, False)).start()  # Run Right Drive motor
        time.sleep(0.1)

#left turn at pre-set speed
def left_turn():
    while True:
        key_states.get('left', False) #loop while key is held
        print("Turning Left")
        threading.Thread(target=run_motor, args=(0, 0.3, True)).start()  # Run Left Drive motor
        threading.Thread(target=run_motor, args=(1, 0.2, False)).start()  # Run Right Drive motor
        time.sleep(0.1)

#right turn at pre-set speed
def right_turn():
    while True:
        key_states.get('right', False) #loop while key is held
        print("Turning Right")
        threading.Thread(target=run_motor, args=(0, 0.2, False)).start()  # Run Left Drive motor
        threading.Thread(target=run_motor, args=(1, 0.3, True)).start()  # Run Right Drive motor
        time.sleep(0.1)

#actuate left front flipper up
def LF_up():
    while True:
        key_states.get('w', False) #loop while key is held
        print("Raising Left Front Flipper")
        run_motor(2, 0.4, True) #run LF motor up
        time.sleep(0.1)

#actuate left front flipper down
def LF_down():
    while True:
        key_states.get('s', False) #loop while key is held
        print("Lowering Left Front Flipper")
        run_motor(2, 0.4, False) #run LF motor down
        time.sleep(0.1)

#actuate left rear flipper up
def LR_up():
    while True:
        key_states.get('q', False) #loop while key is held
        print("Raising Left Rear Flipper")
        run_motor(3, 0.4, True) #run LF motor up
        time.sleep(0.1)

#actuate left rear flipper down
def LR_down():
    while True:
        key_states.get('a', False) #loop while key is held
        print("Lowering Left Rear Flipper")
        run_motor(3, 0.4, False) #run LR motor down
        time.sleep(0.1)
        
#actuate right front flipper up
def RF_up():
    while True:
        key_states.get('e', False) #loop while key is held
        print("Raising Right Front Flipper")
        run_motor(4, 0.4, True) #run RF motor up
        time.sleep(0.1)

#actuate right front flipper down
def RF_down():
    while True:
        key_states.get('d', False) #loop while key is held
        print("Lowering Right Front Flipper")
        run_motor(4, 0.4, False) #run RF motor down
        time.sleep(0.1)

#actuate right rear flipper up
def RR_up():
    while True:
        key_states.get('r', False) #loop while key is held
        print("Raising Right Rear Flipper")
        run_motor(5, 0.4, True) #run RR motor up
        time.sleep(0.1)

#actuate right rear flipper down
def RR_down():
    while True:
        key_states.get('f', False) #loop while key is held
        print("Lowering Right Rear Flipper")
        run_motor(5, 0.4, False) #run RR motor down
        time.sleep(0.1)

#what happens on key press
def on_press(key):
    global speedvar
    global speeddis
    try:
        #Adjusts speed
        if key.char == '=':  # = is presed increase speed by 5%
            speedvar += 0.05
            print(f"Speed: {speeddis}%")
        elif key.char == '-':  # - is presed decrease speed by 5%
            speedvar -= 0.05
            print(f"Speed: {speeddis}%")
        elif key.char.isdigit(1): #If 1 is pressed set speed to 25%
            speedvar = 0.25
            print(f"Speed: {speeddis}%")
        elif key.char.isdigit(2): #If 2 is pressed set speed to 50%
            speedvar = 0.50
            print(f"Speed: {speeddis}%")
        elif key.char.isdigit(3): #If 3 is pressed set speed to 75%
            speedvar = 0.75
            print(f"Speed: {speeddis}%")
        #Forward Drive
        elif key == keyboard.Key.up and not key_states.get('up', False):  # Start if not already running
            key_states['up'] = True
        #Backward Dive
        elif key == keyboard.Key.down and not key_states.get('down', False):  
            key_states['down'] = True
        #Left Turn
        elif key == keyboard.Key.left and not key_states.get('left', False):  
            key_states['left'] = True
        #Right Turn
        elif key == keyboard.Key.right and not key_states.get('right', False):  
            key_states['right'] = True
        #Left Front Flipper
        elif key.char == 'w' and not key_states.get('w', False):
            key_states['w'] = True
            threading.Thread(target=LF_up).start()
        elif key.char == 's' and not key_states.get('s', False):
            key_states['s'] = True
            threading.Thread(target=LF_down).start()
        #Left Rear Flipper
        elif key.char == 'q' and not key_states.get('q', False):
            key_states['q'] = True
            threading.Thread(target=LR_up).start()
        elif key.char == 'a' and not key_states.get('a', False):
            key_states['a'] = True
            threading.Thread(target=LR_down).start()
        #Right Front Flipper
        elif key.char == 'e' and not key_states.get('e', False):
            key_states['e'] = True
            threading.Thread(target=RF_up).start()
        elif key.char == 'd' and not key_states.get('d', False):
            key_states['d'] = True
            threading.Thread(target=RF_down).start()
        #Right Rear Flipper
        elif key.char == 'r' and not key_states.get('r', False):
            key_states['r'] = True
            threading.Thread(target=RR_up).start()
        elif key.char == 'f' and not key_states.get('f', False):
            key_states['f'] = True
            threading.Thread(target=RR_down).start()
        #OH SHIT!
        elif key == keyboard.Key.esc:
            print("All Stop")
            for i in range(len(MOTORS)):
                run_motor(i, 0.0, True)  # Ensure all motors are stopped on exit

    except AttributeError:
        pass

#what happens on key release
def on_release(key):
    try:
        #Forward Halt
        if key == keyboard.Key.up:
            key_states['up'] = False
            print("Halted")
        #Backward Halt
        elif key == keyboard.Key.down:
            key_states['down'] = False
            print("Halted")
        #Left Turn Halt
        elif key == keyboard.Key.left:
            key_states['left'] = False
            print("Halted")
        #Right Turn Halt
        elif key == keyboard.Key.right:
            key_states['right'] = False
            print("Halted")
        #Left Front Flipper Halt
        elif key.char == 'w':
            key_states['w'] = False
            print("Halted")
        elif key.char == 's':
            key_states['s'] = False
            print("Halted")
        #Left Rear Flipper Halt
        elif key.char == 'q':
            key_states['q'] = False
            print("Halted")
        elif key.char == 'a':
            key_states['a'] = False
            print("Halted")
        #Right Front Flipper Halt
        elif key.char == 'e':
            key_states['e'] = False
            print("Halted")
        elif key.char == 'd':
            key_states['d'] = False
            print("Halted")
        #Right Rear Flipper Halt
        elif key.char == 'r':
            key_states['r'] = False
            print("Halted")
        elif key.char == 'f':
            key_states['f'] = False
            print("Halted")
    except AttributeError:
        # Handle other keys
        pass
    
    # Stop the listener when 'Esc' is released
    if key == keyboard.Key.esc:
        print("Program Stopped")
        return False  # Returning False stops the listener


# Start listening to key events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
    
