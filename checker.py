import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="darkly")

my_label = ttk.Label(text="Click the checkbutton below", font=("san serif", 18))
my_label.pack(pady=(40,10))

def checker():
    pass
var1 = ttk.IntVar()
my_check = ttk.Checkbutton(bootstyle="primary",
                           text="Check Me Out",
                           variable=var1,
                           onvalue=1,
                           offvalue=0,
                           command=checker)
my_check.pack(pady=10)
var2 = ttk.IntVar()
my_check2 = ttk.Checkbutton(bootstyle="primary, toolbutton",
                           text="Check Me Out",
                           variable=var2,
                           onvalue=1,
                           offvalue=0,
                           command=checker)
my_check2.pack(pady=10)
var3 = ttk.IntVar()
my_check3 = ttk.Checkbutton(bootstyle="primary, toolbutton, outline",
                           text="Check Me Out",
                           variable=var3,
                           onvalue=1,
                           offvalue=0,
                           command=checker)
my_check3.pack(pady=10)
var4 = ttk.IntVar()
my_check4 = ttk.Checkbutton(bootstyle="primary, round-toggle",
                           text="toggle me",
                           variable=var4,
                           onvalue=1,
                           offvalue=0,
                           command=checker)
my_check4.pack(pady=10)
root.mainloop()
