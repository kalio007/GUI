import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="darkly")
# control functions
def starter():
    my_guage.start()
def stopper():
    my_guage.stop()
def increment():
    my_guage.step(10)
    my_label.config(text=f"Position: {my_guage.variable.get() +10 }")
my_guage = ttk.Floodgauge(root, bootstyle="success",
                          font=("Helvetica", 18),
                          mask="Pos: {}%",
                          maximum=80,
                          orient="horizontal",
                          value=0)
my_guage.pack(pady=50, fill=X, padx=20)
start_button = ttk.Button(root, text="start", bootstyle="danger outline", command=starter)
start_button.pack(pady=20)
stop_button = ttk.Button(root, text="stop", bootstyle="danger outline", command=stopper)
stop_button.pack(pady=20)
inc_button = ttk.Button(root, text="Increment", bootstyle="danger outline", command=increment)
inc_button.pack(pady=20)
my_label = ttk.Label(root)


root.mainloop()