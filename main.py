# Hovedmenu script

#================================================================
#Import(s)
#================================================================

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

#================================================================
#Bavgrunds tema
#================================================================

#Sætter vores appearance/theme
customtkinter.set_appearance_mode("Dark")

#================================================================
#CTk Root/Main og title
#================================================================

#Root/Main (der skal bruges CTk og ikke Tk)
fr = customtkinter.CTk()
#Program Title
fr.title("FanReader")

#================================================================
#Windows difinacioner
#================================================================

#window start størrelse
fr.geometry("860x480")
#Window min størrelse
fr.minsize(640,480)

#================================================================
#Logo/Icon
#================================================================

#Definer PNG som PhotoImage så det kan bruges icon nu og logo senere
icon = PhotoImage(file='GarboIconWithBook.png')
#mini icon
fr.iconphoto(True, icon)

#================================================================
#Grids
#================================================================

#En masse Fancy Grids som jeg lige skal læse lidt meget mere op på før det kommer til at se godt ud :/
fr.grid_columnconfigure(1, weight=1)
fr.grid_rowconfigure(0, weight=1)

fr.frame_left = customtkinter.CTkFrame(master=fr,
                                         width=180,
                                         corner_radius=0)
fr.frame_left.grid(row=0, column=0, sticky="nswe")

fr.frame_right = customtkinter.CTkFrame(master=fr)
fr.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

fr.frame_left.grid_rowconfigure(0, minsize=10)
fr.frame_left.grid_rowconfigure(5, weight=1)
fr.frame_left.grid_rowconfigure(8, minsize=20)
fr.frame_left.grid_rowconfigure(11, minsize=10)

#================================================================
#Command/def(s)
#================================================================

#Command for at tjekke knapperne under debugging og bliver useless i det færdige build
def click():
    print("Click")

#================================================================
#Left Side Logo
#================================================================

#FanReader Txet og Logo
text_var = tkinter.StringVar(value="FanReader")
fr.label_1 = customtkinter.CTkLabel(master=fr.frame_left,
                               image=icon,
                               textvariable=text_var,
                               compound='top',
                               text_font=("Roboto Medium", -16),
                               width=84,
                               height=84,
                               corner_radius=8)
fr.label_1.grid(row=1, column=0, pady=10, padx=10)

#================================================================
#Left Side Buttom(s)
#================================================================

#Fetcher knap
fr.button_1 = customtkinter.CTkButton(master=fr.frame_left,
                                        text="Fetcher",
                                        fg_color=("purple"),
                                        command=click)
fr.button_1.grid(row=2, column=0, pady=10, padx=20)

#Generator knap
fr.button_2 = customtkinter.CTkButton(master=fr.frame_left,
                                        text="Generator",
                                        fg_color=("purple"),
                                        command=lambda: director())
fr.button_2.grid(row=3, column=0, pady=10, padx=20)

#Reader knap
fr.button_3 = customtkinter.CTkButton(master=fr.frame_left,
                                        text="Reader",
                                        fg_color=("purple"),
                                        command=click)
fr.button_3.grid(row=4, column=0, pady=10, padx=20)

#History knap
fr.button_4 = customtkinter.CTkButton(master=fr.frame_left,
                                        text="History",
                                        fg_color=("purple"),
                                        command=click)
fr.button_4.grid(row=5, column=0, pady=10, padx=20)

#Settings knap
fr.button_5 = customtkinter.CTkButton(master=fr.frame_left,
                                        text="Settings",
                                        fg_color=("purple"),
                                        command=click)
fr.button_5.grid(row=6, column=0, pady=10, padx=20)

#Exit knap
fr.button_6 = customtkinter.CTkButton(master=fr.frame_left,
                                        text="Exit"
                                        ,fg_color=("purple"),
                                        command=click)
fr.button_6.grid(row=7, column=0, pady=10, padx=20)

#================================================================
#Højre side vindu
#================================================================

fr.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
fr.frame_right.rowconfigure(7, weight=10)
fr.frame_right.columnconfigure((0, 1), weight=1)
fr.frame_right.columnconfigure(2, weight=0)

fr.frame_info = customtkinter.CTkFrame(master=fr.frame_right)
fr.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

fr.frame_info.rowconfigure(0, weight=1)
fr.frame_info.columnconfigure(0, weight=1)

fr.label_info_1 = customtkinter.CTkLabel(master=fr.frame_info,
                                           text="Place Holder",
                                           text_font=("Roboto Medium", 48),
                                           height=1260,
                                           corner_radius=6,
                                           fg_color=("white", "gray38"),
                                           justify=tkinter.LEFT)
fr.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

#================================================================
#Skal slutte med main loop (so don't you dare put anything after this!)
#================================================================

fr.mainloop()