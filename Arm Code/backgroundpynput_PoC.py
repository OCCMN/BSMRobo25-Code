from pynput import keyboard
import threading
import tkinter as tk

# Function to handle key presses in the background
def on_press(key):
    try:
        print(f"Key {key.char} pressed")
    except AttributeError:
        print(f"Special key {key} pressed")

def on_release(key):
    if key == keyboard.Key.esc:
        print("Exiting...")
        return False  # Stop listener when ESC is pressed

# Start the listener in a separate thread
def start_listener():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

def on_key(event):
    return "break"

# Function to launch the Tkinter window
def open_window():
    # Create a simple Tkinter window
    root = tk.Tk()
    root.title("Input Window")

    # Add a label and entry field for user input
    label = tk.Label(root, text="Type something:")
    label.pack(pady=10)

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
