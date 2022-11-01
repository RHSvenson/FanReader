from tkinter import *
from tkinter import filedialog

def fileExplorer():
    filename = filedialog.askopenfilename(
        initialdir = "/",
        title = "Select a file",
        filetypes = (
            ("Text files",
            "*.txt"),
            ("HTML files",
            "*.html")
        )
    )

    return filename