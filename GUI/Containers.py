import imaplib
from tkinter import *
import tkinter.messagebox
from tkinter.tix import IMAGE
#CTk for progammet til at se mere prof ud!
import customtkinter
from tkinter import filedialog as fd
#from utils.LinkTester import LinkTester
import os, glob
from .Frames import *

class SidebarContainer(customtkinter.CTkFrame):
    def __init__(self, controller):
        # Dan containeren
        customtkinter.CTkFrame.__init__(
            self,
            master = controller,
            width = 100,
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

        self.title_text = tkinter.StringVar(
            value = "FanReader"
        )
        self.title_placement = customtkinter.CTkLabel(
            master = self,
            image = controller.unicon,
            textvariable = self.title_text,
            compound = 'top',
            text_font = ("Roboto Medium", 16),
            width = 84,
            height = 84,
            corner_radius = 8
        )
        self.title_placement.grid(
            row = 1,
            column = 0,
            pady = 10, padx = 10
        )

        #Fetcher knap
        self.nav_button_fetcher = customtkinter.CTkButton(
            master = self,
            text = "Fetcher",
            fg_color = ("purple"),
            command = lambda: controller.show_frame(controller.fetcher_frame)
        )
        self.nav_button_fetcher.grid(row=2, column=0, pady=10, padx=20)

        #Generator knap
        self.nav_button_generator = customtkinter.CTkButton(
            master = self,
            text = "Generator",
            fg_color = ("purple"),
            command = lambda: controller.show_frame(controller.generator_frame)
        )
        self.nav_button_generator.grid(row=3, column=0, pady=10, padx=20)

        #Reader knap
        self.nav_button_reader = customtkinter.CTkButton(
            master = self,
            text = "Reader",
            fg_color = ("purple"),
            command = lambda: controller.show_frame(controller.reader_frame)
        )
        self.nav_button_reader.grid(row=4, column=0, pady=10, padx=20)

        #History knap
        self.nav_button_history = customtkinter.CTkButton(
            master = self,
            text = "History",
            fg_color = ("purple"),
            command = lambda: controller.show_frame(controller.history_frame)
        )
        self.nav_button_history.grid(row=5, column=0, pady=10, padx=20)

        #Settings knap
        self.nav_button_settings = customtkinter.CTkButton(
            master = self,
            text = "Settings",
            fg_color = ("purple"),
            command = lambda: controller.show_frame(controller.settings_frame)
        )
        self.nav_button_settings.grid(row=6, column=0, pady=10, padx=20)

        #Exit knap
        self.nav_button_exit = customtkinter.CTkButton(
            master = self,
            text = "Exit",
            fg_color = ("purple"),
            command = controller.close_fr)
        self.nav_button_exit.grid(row=10, column=0, pady=10, padx=20)


        
class MainContainer(customtkinter.CTkFrame):
    def __init__(self, controller):
        customtkinter.CTkFrame.__init__(
            self,
            master = controller,
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

