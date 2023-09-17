import tkinter as tk
from tkinter import filedialog
import threading

import app

def save_to_file():
    filename = filedialog.asksaveasfilename(defaultextension=".gif", filetypes=[("GIF Files", "*.gif")])
    if filename:
        app.save(filename)

def start_calculation():
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)
    app.setDimensions(round(int(entry_num1.get())/2), round(int(entry_num2.get())/2))
    
    # Create a thread to run app.start()
    calculation_thread = threading.Thread(target=app.start)
    calculation_thread.start()

def stop_calculation():
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)
    app.stop()

# Create the main window
root = tk.Tk()
root.title("Swoosh Screen Recorder")

# Disable window resizing
root.resizable(False, False)

# Create and configure labels and entry widgets
label_num1 = tk.Label(root, text="Width:")
label_num2 = tk.Label(root, text="Height:")
entry_num1 = tk.Entry(root)
entry_num2 = tk.Entry(root)

# Create and configure buttons
start_button = tk.Button(root, text="Start Recording", command=start_calculation)
stop_button = tk.Button(root, text="Stop Recording", command=stop_calculation, state=tk.DISABLED)

# Create and configure a "Browse" button for file selection
browse_button = tk.Button(root, text="Save", command=save_to_file)

# Arrange widgets using grid layout
label_num1.grid(row=0, column=0, padx=10, pady=10)
entry_num1.grid(row=0, column=1, padx=10, pady=10)
label_num2.grid(row=1, column=0, padx=10, pady=10)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

start_button.grid(row=2, column=0, padx=10, pady=10)
stop_button.grid(row=2, column=1, padx=10, pady=10)

browse_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the main loop
root.mainloop()
