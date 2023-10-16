import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="darkly")

# creating an entry box
my_entry = ttk.Entry(root, bootstyle="success", 
                    font=("Helvetica", 18),
                    foreground="green",
                    show="*" )
my_entry.pack()

my_label = ttk.Label(text="Click the button below to reveal your password", font=("san serif", 18))
my_label.pack(pady=(40,10))

def speak():
    my_label.config(text=f'Your Password is: {my_entry.get()}')

my_check = ttk.Button(bootstyle="primary",
                           text="Check Me Out",
                           command=speak)
my_check.pack(pady=10)

root.mainloop()
