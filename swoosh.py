import tkinter as tk
from tkinter import filedialog
import threading

import app

def save_to_file():
    filename = filedialog.asksaveasfilename(defaultextension=".gif", filetypes=[("GIF Files", "*.gif")])
    if filename:
        app.save(filename, float(entry_num3.get()))

calculation_thread = 0
def start_calculation():
    global calculation_thread
    try:
        app.setDimensions(round(int(entry_num1.get())/2), round(int(entry_num2.get())/2))
        app.setSmoothing((101 - int(entry_num4.get()))/101)
        
        # Create a thread to run app.start()
        calculation_thread = threading.Thread(target=app.start)
        calculation_thread.start()
        start_button.config(state=tk.DISABLED)
        stop_button.config(state=tk.NORMAL)
    except:
        tk.messagebox.showerror(title="Error", message="Invalid Input")

def stop_calculation():
    app.stop()
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Swoosh Screen Recorder")

# Disable window resizing
root.resizable(False, False)

# Create and configure labels and entry widgets
label_num1 = tk.Label(root, text="Width:")
label_num2 = tk.Label(root, text="Height:")
label_num3 = tk.Label(root, text="FPS Multiplier:")
label_num4 = tk.Label(root, text="Smoothing:")
entry_num1 = tk.Entry(root)
entry_num2 = tk.Entry(root)
entry_num3 = tk.Entry(root)
entry_num3.insert(0, "1.5")
entry_num4 = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)

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
label_num3.grid(row=2, column=0, padx=10, pady=10)
entry_num3.grid(row=2, column=1, padx=10, pady=10)
label_num4.grid(row=3, column=0, padx=10, pady=10)
entry_num4.grid(row=3, column=1, padx=10, pady=10)

start_button.grid(row=4, column=0, padx=10, pady=10)
stop_button.grid(row=4, column=1, padx=10, pady=10)

browse_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Start the main loop
root.mainloop()
