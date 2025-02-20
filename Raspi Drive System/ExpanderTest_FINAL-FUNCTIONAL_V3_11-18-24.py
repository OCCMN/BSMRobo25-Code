import ioexpander
import time

# Initialize the IO Expander
expander = ioexpander.IOE(i2c_addr=0x18)  # Default I2C address of the IO Expander

# Define pin assignments
PWM_PIN = 1 # Replace with the IO Expander PWM pin connected to motor control
DIR_PIN = 7 # Replace with the IO Expander GPIO pin for direction control

# Set up the pins
expander.set_mode(PWM_PIN, ioexpander.PWM)  # Set PWM_PIN as PWM output
expander.set_mode(DIR_PIN, ioexpander.OUT)  # Set DIR_PIN as digital output

#set PWM freq
expander.set_pwm_frequency(1000) #Frequency in Hz (ajust to motor)

#define PWM resolution
PWM_MAX = 65535

# Define a function to control the motor
def run_motor(speed, direction):
    """
    Controls the motor speed and direction.
    
    :param speed: Motor speed (0.0 to 1.0 for 0% to 100% duty cycle).
    :param direction: Motor direction (True for forward, False for reverse).
    """
    # Set the direction
    expander.output(DIR_PIN, direction)
    
    # Set the PWM duty cycle
    speed = int(max(0.0, min(1.0, speed)) * PWM_MAX) # Clamp speed to range [0.0, 1.0]
    expander.output(PWM_PIN, speed)

# Example Usage
try:
    print("Motor running forward at 50% speed")
    run_motor(0.5, True)  # Forward at 50% speed
    time.sleep(2)
    
    print("Motor running reverse at 75% speed")
    run_motor(0.75, False)  # Reverse at 75% speed
    time.sleep(2)
    
    print("Stopping motor")
    run_motor(0.0, True)  # Stop the motor
except KeyboardInterrupt:
    print("Exiting program")
    run_motor(0.0, True)  # Ensure motor is stopped on exit



