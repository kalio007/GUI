import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="darkly")
counter = 0
def changer():
    global counter
    counter += 1
    if counter % 2 == 0:
        my_label.config(text="Hello World")
    else:
        # .config changes a feature later on on the app
        my_label.config(text="Goodbye World")
# for a label

# danger colored label style
my_label = ttk.Label(text="Hello world!", font=("Helvetica", 29), bootstyle="orange")
my_label.pack(pady=50)

# for a button
b1 = ttk.Button(root, text="Welcome", bootstyle="primary, outline", command=changer)
# button positioning
b1.pack()



root.mainloop()
