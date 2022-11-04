import imaplib
from tkinter import *
import tkinter.messagebox

import customtkinter
from tkinter import filedialog as fd

import os, glob

customtkinter.set_appearance_mode("dark")

class ControllerWindow(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        customtkinter.CTk.__init__(self, *args, **kwargs)

        # Basis udseende
        self.set_appearance_mode("dark")
        self.title("FanReader")
        self.geometry("860x480")
        self.minsize(640,480)

        # Basis grids
        self.grid_columnconfigure(1, weight = 1)
        self.grid_rowconfigure(0, weight = 1)

        # Ikon
        unicon = PhotoImage(file='GarboIconWithBook100px.png')
        self.iconphoto(True, unicon)



        
