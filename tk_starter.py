import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="darkly")

# for a label

# danger colored label style
my_label = ttk.Label(text="Hello world!", font=("Helvetica", 29), bootstyle="orange")
my_label.pack(pady=50)

# for a button
b1 = ttk.Button(root, text="Welcome", bootstyle="primary, outline")
# button positioning
b1.pack()



root.mainloop()
