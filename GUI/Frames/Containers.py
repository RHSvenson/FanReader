import imaplib
from tkinter import *
import tkinter.messagebox
from tkinter.tix import IMAGE
#CTk for progammet til at se mere prof ud!
import customtkinter
from tkinter import filedialog as fd
#from utils.LinkTester import LinkTester
import os, glob

class SidebarContainer(customtkinter.CTkFrame):
    def __init__(self, parent):
        # Dan containeren
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
        
    