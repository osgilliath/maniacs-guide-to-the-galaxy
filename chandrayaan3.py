
import tkinter as tk
from tkinter import ttk, messagebox
from math import sqrt
import random

def calculate_time_dilation():
    try:
        v_fraction = float(speed_entry.get())
        if not 0 <= v_fraction < 1:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a number between 0 and 0.99 for the speed.")
        return

    if v_fraction == 0:
        gamma = 1.0
    else:
        gamma = 1 / sqrt(1 - v_fraction**2)

    result_label.config(text=f"At {v_fraction:.2f}c, 1 hour for you is {gamma:.2f} hours on Earth.")

# --- UI Setup ---
root = tk.Tk()
root.title("Maniac's Guide to the Galaxy")
root.geometry("500x700")
root.resizable(False, False)

# --- Style ---
style = ttk.Style()
style.theme_use('clam')

# --- Colors ---
BG_COLOR = '#0d1117' # GitHub Dark Background
FG_COLOR = '#c9d1d9' # GitHub Dark Foreground
ACCENT_COLOR = '#58a6ff' # GitHub Dark Accent
ENTRY_BG_COLOR = '#010409'
BUTTON_BG_COLOR = '#21262d'
BUTTON_ACTIVE_BG_COLOR = '#30363d'

root.configure(bg=BG_COLOR)

style.configure('TFrame', background=BG_COLOR)
style.configure('TLabel', background=BG_COLOR, foreground=FG_COLOR, font=('Segoe UI', 11))
style.configure('TButton', background=BUTTON_BG_COLOR, foreground=FG_COLOR, font=('Segoe UI', 12, 'bold'), borderwidth=0)
style.map('TButton', background=[('active', BUTTON_ACTIVE_BG_COLOR)])
style.configure('TEntry', fieldbackground=ENTRY_BG_COLOR, foreground=FG_COLOR, insertcolor=FG_COLOR, borderwidth=0)

# --- Main frame ---
main_frame = ttk.Frame(root, padding="20")
main_frame.pack(expand=True, fill=tk.BOTH)

# --- Space Canvas ---
canvas = tk.Canvas(main_frame, width=460, height=250, bg="#000000", highlightthickness=0)
canvas.pack(pady=20)

# Nebula effect
for _ in range(30):
    x1 = random.randint(-50, 500)
    y1 = random.randint(-50, 300)
    x2 = x1 + random.randint(100, 200)
    y2 = y1 + random.randint(100, 200)
    color = random.choice(["#4a0d66", "#3d0c5c", "#2c0a47"])
    canvas.create_oval(x1, y1, x2, y2, fill=color, outline="")

# Stars
for _ in range(150):
    x = random.randint(1, 459)
    y = random.randint(1, 249)
    size = random.uniform(0.5, 2)
    color = random.choice(["#ffffff", "#f0f0ff", "#e0e0ff"])
    canvas.create_oval(x, y, x + size, y + size, fill=color, outline="")

# Modern Rocket
# Body
canvas.create_polygon(225, 200, 235, 200, 245, 100, 215, 100, fill="#e0e0e0", outline="#b0b0b0")
# Cockpit
canvas.create_polygon(215, 100, 245, 100, 230, 80, fill="#58a6ff", outline="#c0c0c0")
# Wings
canvas.create_polygon(215, 180, 200, 210, 215, 190, fill="#c0c0c0")
canvas.create_polygon(245, 180, 260, 210, 245, 190, fill="#c0c0c0")
# Flame
for _ in range(50):
    x1 = random.randint(225, 235)
    y1 = random.randint(200, 220)
    x2 = x1 + random.randint(-2, 2)
    y2 = y1 + random.randint(5, 15)
    color = random.choice(["#ff4500", "#ffa500", "#ffd700"])
    canvas.create_line(x1, y1, x2, y2, fill=color, width=random.uniform(1, 3))


# --- UI Elements ---
title_label = ttk.Label(main_frame, text="Galactic Time Dilation", font=("Segoe UI", 18, "bold"), foreground=ACCENT_COLOR)
title_label.pack(pady=(0, 5))

description_label = ttk.Label(
    main_frame,
    text="You want to spend time with your girlfriend\nbut the time on Earth is not enough.\nSo you decide to go on a space trip!",
    wraplength=450,
    justify=tk.CENTER,
    font=('Segoe UI', 10)
)
description_label.pack(pady=(0, 25))

# Input Frame
input_frame = ttk.Frame(main_frame)
input_frame.pack(pady=10)

speed_label = ttk.Label(input_frame, text="Enter your speed (fraction of light speed, e.g., 0.5):")
speed_label.pack(side=tk.LEFT, padx=(0, 10))

speed_entry = ttk.Entry(input_frame, width=10, font=('Segoe UI', 11))
speed_entry.pack(side=tk.LEFT)
speed_entry.insert(0, "0.5")

# Calculate Button
calculate_button = ttk.Button(main_frame, text="Calculate Time Dilation", command=calculate_time_dilation, style='TButton', padding=(20, 10))
calculate_button.pack(pady=20)

# Result Frame
result_frame = ttk.Frame(main_frame, style='TFrame')
result_frame.pack(pady=(10, 20))

result_label = ttk.Label(result_frame, text="", font=("Segoe UI", 14, "bold"), foreground=ACCENT_COLOR, justify=tk.CENTER, wraplength=450)
result_label.pack(pady=10)

root.mainloop()
