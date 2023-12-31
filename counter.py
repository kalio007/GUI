import tkinter as tk

def increment_count():
    current_count = int(label["text"])
    new_count = current_count + 1
    label["text"] = str(new_count)

def reset_count():
    label["text"] = "0"
def close_window():
    root.destroy()  


#the main window
root = tk.Tk()
root.title("Simple Counter")

#Label to display the count
label = tk.Label(root, text="0", font=("Arial", 24))
label.pack(pady=20)

# "Increment" button
increment_button = tk.Button(root, text="Increment", command=increment_count)
increment_button.pack()

# Reset button
reset_button = tk.Button(root, text="Reset", command=reset_count)
reset_button.pack()

# In-app close Button
close_button = tk.Button(root, text="Close", command=close_window)
close_button.pack()

# Tkinter main loop
root.mainloop()
