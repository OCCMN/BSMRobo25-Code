import serial
import sys
sys.path.append(r"C:\Users\robo\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages")
from pynput import keyboard
import threading
import time
import tkinter as tk


# Global flag for listener state
listener_active = True

# Set up serial communication (update 'COM9' to your actual port)
try:
    ser = serial.Serial('COM5', 9600, timeout=1)
except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
    sys.exit(1)

# Function to prevent text entry in Tkinter
def on_key(event):
    return "break"

# Function to toggle the listener
def toggle_listener():
    global listener_active
    listener_active = not listener_active
    print(f"Listener {'Enabled' if listener_active else 'Disabled'}")

# Key mappings for commands
key_map = {
    't': b'T', 'j': b'J', 'l': b'L', 'i': b'I', 'k': b'K',
    'a': b'A', 'd': b'D', 'w': b'W', 's': b'S',
    'u': b'U', 'o': b'O', 'y': b'Y', 'h': b'H'
}

release_map = {k: v.lower() for k, v in key_map.items()}  # Lowercase for release

def on_press(key):
    global listener_active

    try:
        if key.char == '/':  # Toggle listener with 'P'
            toggle_listener()
            return  # Ensure no other key is processed when toggling

        if not listener_active:
            return  # Ignore all other input if listener is off

        if key.char in key_map:
            ser.write(key_map[key.char])

    except AttributeError:
        pass  # Ignore special keys


def on_release(key):
    global listener_active
    if not listener_active:
        return  # Ignore input if listener is off

    try:
        if key.char in release_map:
            ser.write(release_map[key.char])
    except AttributeError:
        pass

    # Emergency stop and exit
    if key == keyboard.Key.esc:
        ser.write(b'Z')
        ser.write(b'T')
        time.sleep(0.1)
        ser.write(b't')
        time.sleep(0.01)
        return False  # Stop program

def start_listener():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

def open_window():
       # Create a simple Tkinter window
    root = tk.Tk()
    root.title("Arm System")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}+0+0")
    
    
    #Explains Controls
    instructions_message = tk.Label(root, text="Welcome to the Robot Arm System!\nW/S moves the shoulder forward/back\nA/D mosve the turret Left/Right\nI/K moves the elbow up/down\nJ/L revolves the wrist joint\nY/H articulates the wrist up/down\nU give the elbow power to hold it in place\n if U is too strong use O", font=("Arial", 14), anchor="center")
    instructions_message.pack(pady=10)
    
    #E-Stop Message
    estop_message = tk.Label(root, text="Hit / to pause listening to inputs and switch to drive system\nHit ESC for E-Stop", font=("Arial", 12), justify="center", wraplength=250, fg="red")
    estop_message.pack(pady=2)

    #Hidden Entry Bar
    entry = tk.Entry(root)
    entry.pack(pady=5)
    entry.bind("<Key>", on_key)
    
    #Release of liability
    lol_message = tk.Label(root, text="Owen Case denies all liability for damages caused by any potential sentience.\nIn Case of Sentience:\nA glass of water is not provieded", font=("Arial", 8), anchor="center", fg="gray")
    lol_message.pack(pady=5)
    
    # Center align all widgets in the window
    instructions_message.pack_configure(anchor="center")
    estop_message.pack_configure(anchor="center")
    entry.pack_configure(anchor="center")
    lol_message.pack_configure(anchor="center")
    
    # Start the Tkinter event loop
    root.mainloop()

# Start listener in a separate thread
listener_thread = threading.Thread(target=start_listener, daemon=True)
listener_thread.start()

# Open the Tkinter window
open_window()