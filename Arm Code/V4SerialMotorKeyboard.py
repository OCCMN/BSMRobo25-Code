import serial
import sys
sys.path.append(r"C:\Program Files\Python312\Lib\site-packages")
from pynput import keyboard
import time
import threading
import tkinter as tk

#Function captures inputy sans displaying it
def on_key(event):
    return "break"

# Set up serial communication (update 'COM3' to your actual port)
ser = serial.Serial('COM9', 9600)

def on_press(key):
    try:
        if key.char == 't':  # Change 'a' to whatever key you want
            ser.write(b'T')  # Send 'H' to turn LED ON
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
        elif key.char == 'u':
            ser.write(b'U')
        elif key.char == 'o':
            ser.write(b'O')
        elif key.char == 'y':
            ser.write(b'Y')
        elif key.char == 'h':
            ser.write(b'H')
    except AttributeError:
        pass  # Ignore special keys

def on_release(key):
    try:
        if key.char == 't':  # Change 'a' to match the key in on_press
            ser.write(b't')  # Send 'L' to turn LED OFF
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
        elif key.char == 'y':
            ser.write(b'y')
        elif key.char == 'h':
            ser.write(b'h')
    except AttributeError:
        pass
    
    #Stop Program and stop motors
    if key == keyboard.Key.esc:
        ser.write(b'Z')
        ser.write(b'T')
        time.sleep(0.1)
        ser.write(b't')
        time.sleep(0.01)
        return False #stops program

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
    instructions_message = tk.Label(root, text="Welcome to the Robot Drive System!\nUse WASD to Steer\nFlipper Control As Follows\n(Up/Down)\nLeft Front: u/j Right Front: i/k\nLeft Rear:y/h Right Rear:o/l", font=("Arial", 14), anchor="center")
    instructions_message.pack(pady=10)
    
    #E-Stop Message
    estop_message = tk.Label(root, text="Hit ESC for E-Stop", font=("Arial", 12), justify="center", wraplength=250, fg="red")
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
    
#Creat and start listener thread
listener_thread = threading.Thread(target=start_listener, daemon=True)
listener_thread.start()
    
# Open the Tkinter window
open_window()