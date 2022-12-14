from tkinter import *
from tkinter import filedialog

def fileExplorer():
    global fileName
    fileName = filedialog.askopenfilename(
        initialdir = "~",
        title = "Select a file",
        filetypes = (
            ("Text files",
            "*.txt"),
            ("HTML files",
            "*.html")
        )
    )

    generator_manual_file_display.insert("0.0", filename)
