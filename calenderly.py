import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="darkly")
# comtroller function
def datey():
     my_label.config(text=f"You Picked:{my_date.entry.get()}")

my_date = ttk.DateEntry(root, bootstyle="danger")
my_date.pack(pady=50)

my_button = ttk.Button(root, text="get date",
                       bootstyle="danger outline",
                       command=datey)
my_button.pack(pady=50)

my_label = ttk.Label(root, text="You Picked: ")
my_label.pack(pady=20)

 
root.mainloop()