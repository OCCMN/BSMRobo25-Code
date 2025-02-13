# Create a tkinter window with hidden input
def create_input_window():
    # Create the main window
    root = tk.Tk()
    root.title("User Input Window")

    # Add a StringVar to update the message dynamically
    message_var = tk.StringVar()

    # Define the message with the variable from the script
    def update_message():
        message_var.set(f"This is a multi-line message.\nSpeed is set to: {speeddis:.0f}%\nFeel free to interact.")

    update_message()

    # Add a multi-line message label that updates dynamically
    message_label = tk.Label(root, textvariable=message_var, font=("Arial", 12), justify="left", wraplength=250)
    message_label.pack(pady=10)

    # Start the Tkinter event loop
    root.mainloop()

# Start the input window in a separate thread or before the main program loop
create_input_window()