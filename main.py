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
from DataTools.chapterFetcher import *
from DataTools.pageFetcher import *

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

fr = ControllerWindow()

#=============================================================================================
#Logo/Icon
#=============================================================================================

#Definer PNG som PhotoImage så det kan bruges icon nu og logo senere
unicon = PhotoImage(file='GarboIconWithBook100px.png')
#mini icon
fr.iconphoto(True, unicon)

#=============================================================================================
#Grids
#=============================================================================================

#Definer venstre side af Menuen
fr.frame_left = Container(
    parent = fr, 
    type = "sidebar"
)
fr.frame_right = Container(
    parent = fr,
    type = "main"
)

#=============================================================================================
#Command/def(s)
#=============================================================================================

#Test command for at tjekke knapperne under debugging og bliver useless i det færdige build
def click():
    print("Test Click")

#Ændre frame vinduet i højre side af FR
def show_frame(frame):
    print("Button Clicked")
    frame.tkraise()

#Tager den url som man intaster og inserter den i chapter_list

#Lukker FR
def close_fr():
    print("FR Window Quit")
    quit()

#=============================================================================================
#Left Side Logo
#=============================================================================================

#FanReader Txet og Logo
text_var = tkinter.StringVar(value="FanReader")
fr.sidebar_title = customtkinter.CTkLabel(master=fr.frame_left,
                               image=unicon,
                               textvariable=text_var,
                               compound='top',
                               text_font=("Roboto Medium", 16),
                               width=84,
                               height=84,
                               corner_radius=8)
fr.sidebar_title.grid(row=1, column=0, pady=10, padx=10)

#=============================================================================================
#Venstre side knapper(s)
#=============================================================================================

#Fetcher knap
fr.nav_button_fetcher = customtkinter.CTkButton(
    master=fr.frame_left,
    text="Fetcher",
    fg_color=("purple"),
    command=lambda:show_frame(fr.fetcher_frame)
)
fr.nav_button_fetcher.grid(row=2, column=0, pady=10, padx=20)

#Generator knap
fr.nav_button_generator = customtkinter.CTkButton(
    master=fr.frame_left,
    text="Generator",
    fg_color=("purple"),
    command=lambda:show_frame(fr.generator_frame)
)
fr.nav_button_generator.grid(row=3, column=0, pady=10, padx=20)

#Reader knap
fr.nav_button_reader = customtkinter.CTkButton(
    master=fr.frame_left,
    text="Reader",
    fg_color=("purple"),
    command=lambda:show_frame(fr.reader_frame)
)
fr.nav_button_reader.grid(row=4, column=0, pady=10, padx=20)

#History knap
fr.nav_button_history = customtkinter.CTkButton(
    master=fr.frame_left,
    text="History",
    fg_color=("purple"),
    command=lambda:show_frame(fr.history_frame)
)
fr.nav_button_history.grid(row=5, column=0, pady=10, padx=20)

#Settings knap
fr.nav_button_settings = customtkinter.CTkButton(
    master=fr.frame_left,
    text="Settings",
    fg_color=("purple"),
    command=lambda:show_frame(fr.settings_frame)
)
fr.nav_button_settings.grid(row=6, column=0, pady=10, padx=20)

#Exit knap
fr.nav_button_exit = customtkinter.CTkButton(
    master=fr.frame_left,
    text="Exit",
    fg_color=("purple"),
    command=close_fr)
fr.nav_button_exit.grid(row=10, column=0, pady=10, padx=20)

#=============================================================================================
#Højre side vindu
#=============================================================================================

#Den første Frame der visses i højre side af vinduet når du starter FR
fr.first_frame = customtkinter.CTkFrame(master=fr.frame_right)
fr.first_frame.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

fr.first_frame.rowconfigure(0, weight=1)
fr.first_frame.columnconfigure(0, weight=1)

#Styrer hvar der visses i fr.first_frame
fr.first_frame_info = customtkinter.CTkLabel(master=fr.first_frame,
                                           text="Place Holder",
                                           text_font=("Roboto Medium", 48),
                                           height=1260,
                                           corner_radius=6,
                                           fg_color=("white", "gray38"),
                                           justify=tkinter.LEFT)
fr.first_frame_info.pack(fill='both', expand=True)
#fr.first_frame_info.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

#Definere de forskellige frame vinduer (% fr.first_frame) til højre side af FR
fr.fetcher_frame = FetcherFrame(parent = fr.frame_right)
fr.generator_frame = customtkinter.CTkFrame(master=fr.frame_right)
fr.reader_frame = customtkinter.CTkFrame(master=fr.frame_right)
fr.history_frame = customtkinter.CTkFrame(master=fr.frame_right)
fr.settings_frame = customtkinter.CTkFrame(master=fr.frame_right)

#låmber de forskellige frames sammen i en boks
for fr.frame_box in (fr.fetcher_frame,
                     fr.generator_frame,
                     fr.reader_frame,
                     fr.history_frame,
                     fr.settings_frame):
    fr.frame_box.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

fr.frame_box.rowconfigure(0, weight=1)
fr.frame_box.columnconfigure(0, weight=1)

#Styrer hvar der visses i fr.fetcher_frame
#URL entry boks

#Save Individual Chapter knap
fr.fetcher_b_sic = customtkinter.CTkButton(master=fr.fetcher_frame,
                                            text="Save Individual Chapter",
                                            text_font=("times 35", 12),
                                            fg_color=("purple"),
                                            command=click)
fr.fetcher_b_sic.grid(row=7, column=0, pady=10, padx=20, sticky="w")
#Save All Chapters knap
fr.fetcher_b_sac = customtkinter.CTkButton(master=fr.fetcher_frame,
                                            text="Save All Chapters",
                                            text_font=("times 35", 12),
                                            fg_color=("purple"),
                                            command=click)
fr.fetcher_b_sac.grid(row=7, column=1, pady=10, padx=20, sticky="w")

#Styrer hvar der visses i fr.generator_frame
from GUI.fileBrowseUtils import fileExplorer

fr.generator_manual_button = customtkinter.CTkButton(
    master = fr.generator_frame,
    command = lambda: fileExplorer(),
    text_font=("times 35", 12),
    fg_color=("purple"),
    text = "Manual (Browse Files)"
)
fr.generator_manual_button.grid(row = 0, column = 0, pady = 10, padx = 20, sticky = "w")

fr.generator_manual_file_display = customtkinter.CTkTextbox(
    master = fr.generator_frame,
    text_font = ("times 35", 12),
    fg_color = ("purple"),
)

fr.generator_manual_file_display.insert("0.0", "No file selected.")
fr.generator_manual_file_display.configure(state="disabled")

fr.generator_manual_file_display.grid(row = 1, column = 0, pady = 10, padx = 20, sticky = "w")


#fr.generator_frame_info = customtkinter.CTkLabel(fr.generator_frame,
#                                                text="Generator",
#                                                text_font=("times 35", 48),
##                                                height=1260,
#                                               corner_radius=6,
#                                                fg_color=("white", "blue"),
#                                                justify=tkinter.LEFT)
#fr.generator_frame_info.pack(fill='both', expand=True)
#fr.generator_frame_info.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

#Styrer hvar der visses i fr.reader_frame
fr.reader_frame_info = customtkinter.CTkLabel(fr.reader_frame,
                                                text="Reader",
                                                text_font=("times 35", 48),
                                                height=1260,
                                                corner_radius=6,
                                                fg_color=("white", "orange"),
                                                justify=tkinter.LEFT)
fr.reader_frame_info.pack(fill='both', expand=True)
#fr.reader_frame_info.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

#Styrer hvar der visses i fr.history_frame
fr.history_frame_info = customtkinter.CTkLabel(fr.history_frame,
                                                text="History",
                                                text_font=("times 35", 48),
                                                height=1260,
                                                corner_radius=6,
                                                fg_color=("white", "red"),
                                                justify=tkinter.LEFT)
fr.history_frame_info.pack(fill='both', expand=True)
#fr.history_frame_info.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

#Styrer hvar der visses i fr.settings_frame
fr.settings_frame_info = customtkinter.CTkLabel(fr.settings_frame,
                                                text="Settings",
                                                text_font=("times 35", 48),
                                                height=1260,
                                                corner_radius=6,
                                                fg_color=("white", "black"),
                                                justify=tkinter.LEFT)
fr.settings_frame_info.pack(fill='both', expand=True)
#fr.settings_frame_info.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)
#valg1 test
fr.settings_Server = customtkinter.CTkLabel(fr.settings_frame_info,
                         text="Server settings",
                         text_font=("times 35", 16),
                         height=36,
                         corner_radius=6,
                         fg_color=("white", "black"),
                         justify=tkinter.LEFT)
fr.settings_Server.grid(column=0, row=1, sticky="nwe", padx=15, pady=15)
#valg2 test
fr.settings_Reader = customtkinter.CTkLabel(fr.settings_frame_info,
                         text="Reader choices",
                         text_font=("times 35", 16),
                         height=36,
                         corner_radius=6,
                         fg_color=("white", "black"),
                         justify=tkinter.LEFT)
fr.settings_Reader.grid(column=0, row=2, sticky="nwe", padx=15, pady=15)

#Sørger for at fr.first_frame faktisk bliver vist når FR starter op
show_frame(fr.first_frame)

#=============================================================================================
#Skal slutte med main loop (so don't you dare put anything after this!)
#=============================================================================================

fr.mainloop()