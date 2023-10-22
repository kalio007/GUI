import tkinter as tk 
from tkinter import messagebox

# declaring functions
def add():
    pass
def update():
    pass
def delete():
    pass 

root = tk.Tk()
root.title("CRUD APP")

entry = tk.Entry(root)
entry.pack(pady=20)
# creating a listbox to display the list
listbox = tk.Listbox(root)
listbox.pack()

# creating the crud opps
add_item = tk.Button(root, text="Add", command=add)
add_item.pack(pady=5)
update_item = tk.Button(root, text="Update", command=update)
update_item.pack(pady=5)
delete_item= tk.Button(root, text="Delete", command=delete)
delete_item.pack(pady=5)


root.mainloop()