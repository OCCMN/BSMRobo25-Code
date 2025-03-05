import serial
import sys
sys.path.append(r"C:\Program Files\Python312\Lib\site-packages")
from pynput import keyboard
import threading
import time
import tkinter as tk


# Global flag for listener state
listener_valueone = False
listener_valuetwo = True

# Set up serial communication (update 'COM9' to your actual port)
try:
    ser = serial.Serial('COM3', 9600, timeout=1)
except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
    sys.exit(1)

# Function to prevent text entry in Tkinter
def on_key(event):
    return "break"

# Function to toggle the listener
def toggle_listener():
    global listener_valueone
    global listener_valuetwo
    listener_valueone = not listener_valueone
    listener_valuetwo = not listener_valuetwo
    print(f"Listener one {'Enabled' if listener_valueone else 'Disabled'}")
    print(f"Listener two {'Enabled' if listener_valuetwo else 'Disabled'}")


def on_press(key):
    global listener_valueone
    global listener_valuetwo
    try:
        if key.char == '/':  # Toggle listener with 'P'
            toggle_listener()
            return  # Ensure no other key is processed when toggling

        if not listener_valueone:
            if key.char == 'w':
                ser.write(b'<D:W>')
            elif key.char == 's':
                ser.write(b'<D:S>')
            elif key.char == 'a':
                ser.write(b'<D:A>')
            elif key.char == 'd':
                ser.write(b'<D:D>')
            elif key.char == 'q':
                ser.write(b'<D:Q>')
            elif key.char == 'e':
                ser.write(b'<D:E>')
            elif key.char == 'u':
                ser.write(b'<D:U>')
            elif key.char == 'j':
                ser.write(b'<D:J>')
            elif key.char == 'i':
                ser.write(b'<D:I>')
            elif key.char == 'k':
                ser.write(b'<D:K>')
            elif key.char == 'y':
                ser.write(b'<D:Y>')
            elif key.char == 'h':
                ser.write(b'<D:H>')
            elif key.char == 'o':
                ser.write(b'<D:O>')
            elif key.char == 'l':
                ser.write(b'<D:L>')
        if not listener_valuetwo:
            if key.char == 'w':
                ser.write(b'<A:W>')
            elif key.char == 's':
                ser.write(b'<A:S>')
            elif key.char == 'a':
                ser.write(b'<A:A>')
            elif key.char == 'd':
                ser.write(b'<A:D>')
            elif key.char == 'i':
                ser.write(b'<A:I>')
            elif key.char == 'k':
                ser.write(b'<A:K>')
            elif key.char == 'j':
                ser.write(b'<A:J>')
            elif key.char == 'l':
                ser.write(b'<A:L>')
            elif key.char == 'u':
                ser.write(b'<A:U>')
            elif key.char == 'o':
                ser.write(b'<A:O>')
            elif key.char == 'y':
                ser.write(b'<A:Y>')
            elif key.char == 'h':
                ser.write(b'<A:H>')
            elif key.char == 'q':
                ser.write(b'<A:Q>')
            elif key.char == 'e':
                ser.write(b'<A:E>')

        if key.char:
            return

    except AttributeError:
        pass  # Ignore special keys


def on_release(key):
    global listener_valueone
    global listener_valuetwo
    try:
        if not listener_valueone:
            if key.char == 'w':
                ser.write(b'<D:w>')
            elif key.char == 's':
                ser.write(b'<D:s>')
            elif key.char == 'a':
                ser.write(b'<D:a>')
            elif key.char == 'd':
                ser.write(b'<D:d>')
            elif key.char == 'q':
                ser.write(b'<D:q>')
            elif key.char == 'e':
                ser.write(b'<D:e>')
            elif key.char == 'u':
                ser.write(b'<D:u>')
            elif key.char == 'j':
                ser.write(b'<D:j>')
            elif key.char == 'i':
                ser.write(b'<D:i>')
            elif key.char == 'k':
                ser.write(b'<D:k>')
            elif key.char == 'y':
                ser.write(b'<D:y>')
            elif key.char == 'h':
                ser.write(b'<D:h>')
            elif key.char == 'o':
                ser.write(b'<D:o>')
            elif key.char == 'l':
                ser.write(b'<D:l>')
               
        if not listener_valuetwo:
            if key.char == 'w':
                ser.write(b'<A:w>')
            elif key.char == 's':
                ser.write(b'<A:s>')
            elif key.char == 'a':
                ser.write(b'<A:a>')
            elif key.char == 'd':
                ser.write(b'<A:d>')
            elif key.char == 'i':
                ser.write(b'<A:i>')
            elif key.char == 'k':
                ser.write(b'<A:k>')
            elif key.char == 'j':
                ser.write(b'<A:j>')
            elif key.char == 'l':
                ser.write(b'<A:l>')
            elif key.char == 'u':
                ser.write(b'<A:u>')
            elif key.char == 'o':
                ser.write(b'<A:o>')
            elif key.char == 'y':
                ser.write(b'<A:y>')
            elif key.char == 'h':
                ser.write(b'<A:h>')
            elif key.char == 'q':
                ser.write(b'<A:q>')
            elif key.char == 'e':
                ser.write(b'<A:e>')

        if key.char:
            return
            
    except AttributeError:
        pass

    # Emergency stop and exit
    if key == keyboard.Key.esc: 
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
