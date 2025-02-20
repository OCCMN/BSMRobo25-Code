import serial
import sys
sys.path.append(r"C:\Program Files\Python312\Lib\site-packages")
from pynput import keyboard

# Set up serial communication (update 'COM3' to your actual port)
ser = serial.Serial('COM10', 9600)

def on_press(key):
    try:
        if key.char == 't':  # Change 'a' to whatever key you want
            ser.write(b'H')  # Send 'H' to turn LED ON
    except AttributeError:
        pass  # Ignore special keys

def on_release(key):
    try:
        if key.char == 't':  # Change 'a' to match the key in on_press
            ser.write(b'h')  # Send 'L' to turn LED OFF
    except AttributeError:
        pass

# Listen for key events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
