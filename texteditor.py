import tkinter.filedialog

def open_file(event=None):
 input_file_name = tkinter.filedialog.askopenfilename(defaultextension=".txt",
 filetypes=[("All Files", "*.*"), ("Text Documents",
 "*.txt")])

open_file()
