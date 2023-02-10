# ++ MAIN TKINTER INSTANCE ++ #

import os
import tkinter as tk
from tkinter.tix import IMAGE
import customtkinter
from tkinter import filedialog as fd

# ++ LOCAL MODULES ++ #

from Components import Containers

# ++ CTK Constants ++ #

customtkinter.set_appearance_mode("Dark")

# ++ MAIN TKINTER OBJECT ++ #

class FanReader(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        customtkinter.CTk.__init__(self, *args, **kwargs)

        # Window appearance
        self.title("FanReader")
        self.geometry("860x480")
        self.minsize(640,480)

        self.prayer = "Må Herren den almægtige give at hans tjeneres skabning må fylde dem med samme fryd som dig ved tjenernes skabelse. Ved Kristus vor Herre, Amen."

        # Window Internal Layout
        self.grid_columnconfigure(1, weight = 1)
        self.grid_rowconfigure(0, weight = 1)

        # Logo
        self.logo = tk.tix.PhotoImage(file='Graphics/GarboIconWithBook100px.png')
        self.iconphoto(True, self.logo)

        # Instance Variables
        self.current_story_title = tk.StringVar(
            master = self,
            value = "No Story Currently Initialised",
            name = "currentStoryTitle"
        )

        self.app_directory = os.path.abspath(os.path.dirname(__file__))

        # Indholdsbeholdere
        self.sidebar = Containers.SidebarContainer(controller = self)
        self.main_window = Containers.MainContainer(controller = self)

        # Indhold


    # Metoder
    def close_fanreader(self):
        quit()

    def show_frame(self, frame):
        frame.update_frame()
        frame.tkraise()




fr = FanReader()

fr.mainloop()