import random
import tkinter as tk
from tkinter import messagebox

# Function to roll the dice and display the result
def roll_dice():
    faces = [chr(i) for i in range(ord('⚀'), ord('⚈') + 1)]
    rolled_faces = [random.choice(faces) for _ in range(num_dice.get())]
    result_label.config(text=''.join(rolled_faces))

# Function to validate the user input
def validate_input(input):
    if input.isdigit() and int(input) in range(1, 7):
        num_dice.set(int(input))
        return True
    else:
        messagebox.showerror("Error", "Please enter a number from 1 to 6.")
        return False

# Create the main window
window = tk.Tk()
window.title("Dice Roll Project")

# Configure the window size
window.geometry("300x150")

# Create the number of dice entry
num_dice = tk.StringVar()
num_dice.set("1")

entry_frame = tk.Frame(window)
entry_frame.pack(pady=20)

entry = tk.Entry(entry_frame, width=10, textvariable=num_dice, validate="key", validatecommand=(window.register(validate_input), '%P'))
entry.grid(row=0, column=0, padx=(0, 10))

# Create the roll button
roll_button = tk.Button(window, text="Roll Dice", command=roll_dice)
roll_button.pack(pady=(20, 0))

# Create the result label
result_label = tk.Label(window, text="")
result_label.pack()

# Start the main loop
window.mainloop()