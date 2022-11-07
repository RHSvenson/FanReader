# Hovedmenu script

#=============================================================================================
#Import(s)
#=============================================================================================

import imaplib
from tkinter import *
import tkinter.messagebox
from tkinter.tix import IMAGE
#CTk for progammet til at se mere prof ud!
import customtkinter
from tkinter import filedialog as fd
#from utils.LinkTester import LinkTester
import os, glob
from director import director

from GUI.Containers import *
from GUI.Frames import FetcherFrame

#=============================================================================================
#Bavgrunds tema
#=============================================================================================

#Sætter vores appearance/theme
customtkinter.set_appearance_mode("Dark")

#=============================================================================================
#CTk Root/Main og title
#=============================================================================================

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
        self.unicon = PhotoImage(file='GarboIconWithBook100px.png')
        self.iconphoto(True, self.unicon)

        self.sidebar = SidebarContainer(controller = self)
        self.main_window = MainContainer(controller = self)

        self.fetcher_frame = FetcherFrame(parent = self.main_window)
        self.generator_frame = GeneratorFrame(parent = self.main_window)
        self.reader_frame = ReaderFrame(parent = self.main_window)
        self.history_frame = HistoryFrame(parent = self.main_window)
        self.settings_frame = SettingsFrame(parent = self.main_window)

        for self.frame_box in (
            self.fetcher_frame,
            self.generator_frame,
            self.reader_frame,
            self.history_frame,
            self.settings_frame
        ):
            self.frame_box.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")
            self.frame_box.rowconfigure(0, weight=1)
            self.frame_box.columnconfigure(0, weight=1)

        self.show_frame(self.fetcher_frame)

    def close_fr(self):
        quit()

    def show_frame(self, frame):
        frame.tkraise()


fr = ControllerWindow()



#Sørger for at fr.first_frame faktisk bliver vist når FR starter op
fr.show_frame(fr.fetcher_frame)

#=============================================================================================
#Skal slutte med main loop (so don't you dare put anything after this!)
#=============================================================================================

fr.mainloop()