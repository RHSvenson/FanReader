# Hovedmenu script

from tkinter import *
from tkinter import filedialog as fd

def gennemgåFiler():
    filnavn = fd.askopenfilename(
        initialdir = "~",
        title = "Select a file",
        filetypes = (
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        )
    )

    label_file_explorer.configure(text="File Opened: "+filename)

window = Tk()

window.title('FanReader')

window.geometry("500x500")

window.config(background = "black")

label_file_explorer = Label(
    window,
    text = "File Explorer",
    width = 100, height = 4,
    fg = "blue"
)

button_explore = Button(
    window,
    text = "Browse Files",
    command = gennemgåFiler
)

button_exit = Button(
    window,
    text = "Exit",
    command = exit
)

label_file_explorer.grid(column = 1, row = 1)

button_explore.grid(column = 1, row = 2)

button_exit.grid(column = 1, row = 3)

window.mainloop()