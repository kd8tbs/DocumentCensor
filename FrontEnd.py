import tkinter as tk
import os


def create_ui():
    # Create the main window
    window = tk.Tk()
    window.title("My UI")

    # Create the input fields
    input1_label = tk.Label(window, text="Input 1:")
    input1_label.pack()
    input1_entry = tk.Entry(window)
    input1_entry.pack()

    input2_label = tk.Label(window, text="Input 2:")
    input2_label.pack()
    input2_entry = tk.Entry(window)
    input2_entry.pack()

    # Create the output label
    output_label = tk.Label(window, text="Output:")
    output_label.pack()

    # Define the button click handler
    def button_click():
        input1_text = input1_entry.get()
        input2_text = input2_entry.get()
        output_text = input1_text + " " + input2_text
        output_label.config(text="Output: " + output_text)

    # Create the button
    button = tk.Button(window, text="Concatenate", command=button_click)
    button.pack()

    # Start the main event loop
    window.mainloop()
