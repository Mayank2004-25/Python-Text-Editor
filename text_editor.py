import tkinter as tk
from tkinter import filedialog, messagebox

filename = None

def new_file():
    global filename
    filename = None
    text.delete("1.0", tk.END)

def save_file():
    global filename
    if not filename:  # If filename is None or empty, call saveAs
        save_as()
    else:
        try:
            with open(filename, 'w') as f:
                f.write(text.get("1.0", tk.END).rstrip())
        except:
            messagebox.showerror("Oops!", "Unable to save file...")

def save_as():
    global filename
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f:  # If a file was selected
        filename = f.name
        save_file()  # Save the file after getting the name

def open_file():
    global filename
    f = filedialog.askopenfile(mode='r')
    if f:  # If a file was selected
        filename = f.name
        text.delete("1.0", tk.END)
        text.insert("1.0", f.read())

root = tk.Tk()
root.title("Python Text Editor")
root.geometry("400x400")

text = tk.Text(root)
text.pack(expand=True, fill=tk.BOTH)

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new_file)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_command(label="Save As", command=save_as)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()
