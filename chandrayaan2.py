import tkinter as tk
from tkinter import messagebox
from math import sqrt
import random

def calculate_time_dilation():
    try:
        v_fraction = float(speed_entry.get())
        if v_fraction < 0 or v_fraction >= 1:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid input", "Enter a number between 0 and 0.99 for speed (fraction of c).")
        return

    gamma = 1 / sqrt(1 - v_fraction**2)
    earth_time = gamma * 1  # 1 hour traveler time corresponds to gamma hours on Earth

    result_label.config(
        text=f"At {v_fraction:.2f}x speed of light,\n1 hour for you equals {earth_time:.4f} hours on Earth."
    )

root = tk.Tk()
root.title("Maniac's Guide to the Galaxy")

win_width = 500
win_height = 400
root.geometry(f"{win_width}x{win_height}")

background_canvas = tk.Canvas(root, width=win_width, height=win_height, bg="black", highlightthickness=0)
background_canvas.place(x=0, y=0)

frame = tk.Frame(root, bg="black")
frame.place(relwidth=1, relheight=1)

greeting = tk.Label(frame, text="You want to spend time with your girlfriend\nbut the time on Earth is not enough.\nSo you decide to go on a space trip!", pady=10, fg="white", bg="black", font=("Helvetica", 12))
greeting.pack(pady=(20, 10))

speed_frame = tk.Frame(frame, bg="black")
speed_frame.pack(pady=10)

speed_label = tk.Label(speed_frame, text="Enter your speed (fraction of light speed, e.g., 0.5): ", fg="white", bg="black", font=("Helvetica", 10))
speed_label.pack(side=tk.LEFT)

speed_entry = tk.Entry(speed_frame, width=5, font=("Helvetica", 10))
speed_entry.pack(side=tk.LEFT)
speed_entry.insert(0, "0.5")

calc_btn = tk.Button(frame, text="Calculate Time Dilation", command=calculate_time_dilation, bg="gray20", fg="white", activebackground="gray40", activeforeground="white")
calc_btn.pack(pady=15)

result_label = tk.Label(frame, text="", fg="white", bg="black", font=("Helvetica", 14))
result_label.pack(pady=10)

root.mainloop()

