import tkinter as tk
from tkinter import messagebox
from math import sqrt

def calculate_time_dilation():
    try:
        v_fraction = float(speed_entry.get())
        if v_fraction < 0 or v_fraction >= 1:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid input", "Enter a number between 0 and 0.99 for speed (fraction of c).")
        return

    gamma = 1 / sqrt(1 - v_fraction**2)

    result_label.config(
        text=f"At {v_fraction:.2f} x speed of light,\n1 hour for you equals {gamma:.4f} hours on Earth."
    )

def draw_artwork(canvas):
    # Starss
    import random
    for _ in range(60):
        x = random.randint(10, 380)
        y = random.randint(10, 180)
        canvas.create_oval(x, y, x + 2, y + 2, fill="white", outline="")
    # Rocket body
    canvas.create_rectangle(180, 150, 220, 110, fill="white", outline="gray")
    # Rocket nose
    canvas.create_polygon(180, 110, 220, 110, 200, 80, fill="red", outline="black")
    # Rocket ke kone wali cheeze
    canvas.create_polygon(180, 150, 170, 170, 190, 150, fill="blue")
    canvas.create_polygon(220, 150, 230, 170, 210, 150, fill="blue")
    # Rocket window
    canvas.create_oval(195, 120, 205, 130, fill="skyblue", outline="black")

root = tk.Tk()
root.title("Maniac's Guide to the Galaxy")

# Canvas
canvas = tk.Canvas(root, width=400, height=200, bg="black")
canvas.grid(row=0, column=0, columnspan=2)
draw_artwork(canvas)

# Message
greeting = tk.Label(root, text="You want to spend time with your girlfriend\nbut the time on Earth is not enough.\nSo you decide to go on a space trip!", pady=10)
greeting.grid(row=1, column=0, columnspan=2)

# Input speed
tk.Label(root, text="Enter your speed (as a fraction of light speed, e.g., 0.5): ").grid(row=2, column=0, sticky=tk.E)
speed_entry = tk.Entry(root)
speed_entry.grid(row=2, column=1, sticky=tk.W)
speed_entry.insert(0, "0.5")

# Calculate button
calc_btn = tk.Button(root, text="Calculate Time Dilation", command=calculate_time_dilation)
calc_btn.grid(row=3, column=0, columnspan=2, pady=10)

# Result display
result_label = tk.Label(root, text="", fg="green", pady=10)
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()

