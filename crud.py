import tkinter as tk 
from tkinter import messagebox

# declaring functions
items = []
def add():
    item = entry.get()
    if item:
        items.append(item)
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Please enter and Item")
def update():
    selected_index = listbox.curselection()
    if selected_index:
        new_item = entry.get()
        if new_item:
            items[selected_index[0]] = new_item
            listbox.delete(selected_index)
            listbox.insert(selected_index[0], new_item)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning")
    else:
        messagebox.showwarning("warning")
def delete():
    selected_index = listbox.curselection()
    if selected_index:
        listbox.delete(selected_index)
        del items[selected_index[0]]
        entry.delete(0,tk.END)
    else:
        messagebox.showwarning("Warning")

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