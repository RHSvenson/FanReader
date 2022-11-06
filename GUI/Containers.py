import imaplib
from tkinter import *
import tkinter.messagebox
from tkinter.tix import IMAGE
#CTk for progammet til at se mere prof ud!
import customtkinter
from tkinter import filedialog as fd
#from utils.LinkTester import LinkTester
import os, glob

class ControllerWindow(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        customtkinter.CTk.__init__(self, *args, **kwargs)

        # Basis udseende
        self.title("FanReader")
        self.geometry("860x480")
        self.minsize(640,480)

        # Basis grids
        self.grid_columnconfigure(1, weight = 1)
        self.grid_rowconfigure(0, weight = 1)

        # Ikon
        unicon = PhotoImage(file='GarboIconWithBook100px.png')
        self.iconphoto(True, unicon)
 

class Container(customtkinter.CTkFrame):
    def __init__(self, parent, type):
        # Dan containeren
        if type == "sidebar":
            customtkinter.CTkFrame.__init__(
                self,
                master = parent,
                width = 180,
                corner_radius = 0)

            self.grid(
                row = 0,
                column = 0,
                sticky = "nswe"
            )
            ## Afgrænsing
            # Toppen af rammen
            self.grid_rowconfigure(0, minsize = 10)
            self.grid_rowconfigure(8, weight = 1)

            # Bunden af rammen
            self.grid_rowconfigure(9, minsize = 20)
            self.grid_rowconfigure(11, minsize = 15)
        
        elif type == "main":
            customtkinter.CTkFrame.__init__(
                self,
                master = parent,
            )
            self.grid(
                row = 0,
                column = 1,
                sticky = "nswe",
                padx = 20, pady = 20)

            #kontrollerer toppen af frame_right
            self.rowconfigure((0, 1, 2, 3), weight=1)
            self.rowconfigure(7, weight=10)
            #kontrollerer bunden af frame_right
            self.columnconfigure((0, 1), weight=1)
            self.columnconfigure(2, weight=0)