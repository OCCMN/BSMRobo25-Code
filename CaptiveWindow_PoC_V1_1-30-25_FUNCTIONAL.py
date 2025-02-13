import os
import time

variable = 0  # This variable will change over time
script_content = """\
#!/bin/bash

while true; do
    clear
    echo "Welcome to the program!"
    echo "1. Follow the instructions carefully."
    echo "2. Do not close this window unless instructed."
    echo "3. Type your input below. Press Ctrl+C or type 'exit' to quit."
    echo "Current Variable Value: $(cat /tmp/var_value)"
    echo ""
    python3 -c 'import getpass; getpass.getpass("Hidden Input: ")'
done
"""

# Save the script to a temporary file                                          
script_path = "/tmp/live_terminal.sh"
with open(script_path, "w") as script_file:
    script_file.write(script_content)

# Make the script executable
os.system(f"chmod +x {script_path}")

# Start the terminal script
os.system(f'lxterminal -e "bash -c \\"{script_path}; exec bash\\"" &')

# Continuously update the variable in the background
while True:
    with open("/tmp/var_value", "w") as var_file:
        var_file.write(str(variable))
    time.sleep(1)  # Update every second
