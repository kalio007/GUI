import tkinter as tk

def convert():
    try:
        celsius = float(entry.get())
        fahr = (celsius * 1.8 ) + 32
        result_label["text"] = f"{celsius}C is {fahr}F"
    except ValueError:
        result_label["text"] = "Invalid Input"

root = tk.Tk()
root.title("Celsius to Fahrenheit Converter")

# label for input 
enter_instruction = tk.Label(root, text="Enter temperature in Celsuis")
enter_instruction.pack(pady=10)

#input box for entry
entry = tk.Entry(root)
entry.pack(pady=5)

#button to carry out the conversion
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack(pady=10)

# To display result
result_label =tk.Label(root, text="")
result_label.pack()



root.mainloop()