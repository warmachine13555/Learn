import tkinter as tk

def on_button_click():
    label.config(text="Button clicked!")

# Create the main window
window = tk.Tk()

# Set the window title
window.title("GUI Program")

# Create a label widget
label = tk.Label(window, text="Hello, GUI!")

# Create a button widget
button = tk.Button(window, text="Click Me", command=on_button_click)

# Place the label and button widgets in the window
label.pack()
button.pack()

# Start the main event loop
window.mainloop()
