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
        elif key.char == 'j':
            ser.write(b'J')
        elif key.char == 'l':
            ser.write(b'L')
        elif key.char == 'i':
            ser.write(b'I')
        elif key.char == 'k':
            ser.write(b'K')
        elif key.char == 'a':
            ser.write(b'A')
        elif key.char == 'd':
            ser.write(b'D')
        elif key.char == 'w':
            ser.write(b'W')
        elif key.char == 's':
            ser.write(b'S')
    except AttributeError:
        pass  # Ignore special keys

def on_release(key):
    try:
        if key.char == 't':  # Change 'a' to match the key in on_press
            ser.write(b'h')  # Send 'L' to turn LED OFF
        elif key.char == 'j':
            ser.write(b'j')
        elif key.char == 'l':
            ser.write(b'l')
        elif key.char == 'i':
            ser.write(b'i')
        elif key.char == 'k':
            ser.write(b'k')
        elif key.char == 'a':
            ser.write(b'a')
        elif key.char == 'd':
            ser.write(b'd')
        elif key.char == 'w':
            ser.write(b'w')
        elif key.char == 's':
            ser.write(b's')
    except AttributeError:
        pass

# Listen for key events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()