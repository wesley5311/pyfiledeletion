'''
Created on Oct 3, 2023

@author: Wesley
'''
import os
import tkinter as tk
from tkinter import filedialog
from damages import obfuscation
import sys

all_files = []
folder_paths = ["No files are selected"]

def get_files():
    files = []
    for folder_path in folder_paths:
        # check if current folder_path is a file
        if os.path.isfile(folder_path):
            # adds filename to list
            files.append(folder_path)
    return files

def get_folders():
    global folder_paths
    folder_paths = filedialog.askopenfilenames(
        initialdir="/",
        title="Select Protected Files:",
        filetypes=[],  
        multiple=True
    )
    if folder_paths:
        print("Selected Files:")
        for folder in folder_paths:
            print(folder)
    return folder_paths

def delete_click():
    for file_path in get_files():
        obfuscation([file_path])
    folder_paths = ["No files are selected"]

def pick_click():
    root.withdraw() 
    get_folders()
    root.deiconify() 

def show_click():
    if folder_paths:
        print("Selected Files:")
        print(folder_paths)
        return folder_paths
    else:
        print("No files selected")


root = tk.Tk()
root.title("File deletion tool")

window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

root.configure(bg="black")

button1 = tk.Button(root, text="Delete selected files", width=15, height=2)
button2 = tk.Button(root, text="Pick files", width=15, height=2)
button3 = tk.Button(root, text="Selected files", width=15, height=2)

button1.pack(pady=20)
button2.pack()
button3.pack()

button1.config(command=delete_click)
button2.config(command=pick_click)
button3.config(command=show_click)



console_output = tk.Text(root, height=5, width=45, fg="white", bg="black")
console_output.pack(pady=10)

# console output to text box
original_stdout = sys.stdout

def stdout_to_console_output(message):
    console_output.insert(tk.END, message + '\n')
    console_output.see(tk.END)

sys.stdout.write = stdout_to_console_output




root.mainloop()

# gui.py


