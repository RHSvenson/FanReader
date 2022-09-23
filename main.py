# Hovedmenu script

from msilib.schema import Font
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

def display():
    if (x.get()==1):
        print ("Ja, okay makker")
 

# Selve vinduet nevnet, størelsen og bagrunds farven. HOT!
window = Tk()

window.title('FanReader')

window.geometry("500x500")

window.config(background = "pink")

# Overskrift lablen, som er det menuen hedder.
label_file_explorer = Label(
    window,
    text = "File Explorer",
    font = ("Ariel",20,"bold"),
    width = 29, height = 3,
    fg = "white",
    bg = "blue",
    relief = RAISED,
    bd = 10
)

# En knap som skal gå til et directory med understøttede link på historier.
button_internetlink = Button(
    window,
    text = "Internet Link",
    width = 14, height = 1,
    font = ("Ariel",20),
    bg = "purple"
)

# En knap som browser filer og via, skal man kunne vælge en .txt file som loades ind i programmet.
button_explore = Button(
    window,
    text = "Browse Files",
    command = gennemgåFiler,
    width = 14, height = 1,
    font = ("Ariel",20),
    bg = ("Green")
)

# En knap som lukker programmet.
button_exit = Button(
    window,
    text = "Exit",
    command = exit,
    width = 14, height = 1,
    font = ("Ariel",20),
    bg = ("Red")
)

# En check box vi kan skule noget bag.

x = IntVar()

check_button = Checkbutton(
    window,
    text = "Jeg er over 18",
    variable = x,
    onvalue = 1,
    offvalue = 0,
    command = display,
    font = ("Ariel", 15),
    bg = ("pink"),
    activebackground = "pink"
)

# Hvor labes og buttons er i winduets grid.
label_file_explorer.grid(column = 1, row = 1)

button_internetlink.grid(column = 1, row = 2)

button_explore.grid(column = 1, row = 3)

button_exit.grid(column = 1, row = 4)

check_button.grid(column = 1, row = 5)

window.mainloop()