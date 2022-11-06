import imaplib
from tkinter import *
import tkinter.messagebox
from tkinter.tix import IMAGE
#CTk for progammet til at se mere prof ud!
import customtkinter
from tkinter import filedialog as fd
#from utils.LinkTester import LinkTester
import os, glob

from bs4 import BeautifulSoup
import requests
import re

class FetcherFrame(customtkinter.CTkFrame):
    
    def __init__(self, parent):
        # Indlæser den egentlige frame
        customtkinter.CTkFrame.__init__(
            self,
            master = parent
        )
        self.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

        # Feldt til at indtaste URL
        self.url_field = customtkinter.CTkEntry(
            master = self,
            width = 120,
            placeholder_text = "Enter URL Here"
        )
        self.url_field.grid(
            row = 0,
            column = 0,
            columnspan = 2,
            pady = 20, padx = 20,
            sticky = "we"
        )

        # Knap til at indlæse den indtastede URL
        self.fetch_button = customtkinter.CTkButton(
            master = self,
            text = "Fetch URL",
            text_font = ("times 35", 12),
            fg_color = ("purple"),
            command = lambda: self.fetch_chapters()
        )
        self.fetch_button.grid(
            row = 0,
            column = 2,
            pady = 10, padx = 20,
            sticky = "w"
        )

        # Liste der indeholder de kapitler funktionen fandt.
        # Tom til at starte med.
        self.chapter_list = Listbox(
            master = self,
            bg = "purple",
            font = ("times 35", 12)
        )
        self.chapter_list.grid(
            row = 2,
            column = 0,
            pady = 10,
            padx = 20, 
            sticky = "nsew"
        )
        self.chapter_list.config(
            height=self.chapter_list.size()
        )

        # Knap til at gemme et kapitel
        self.save_one_chapter_button = customtkinter.CTkButton(
            master = self,
            text = "Save Individual Chapter",
            fg_color = ("purple"),
            command = self.click
        )
        self.save_one_chapter_button.grid(
            row=7,
            column=0,
            pady=10, padx=20,
            sticky="w"
        )

        # Knap til at gemme alle kapitler
        self.save_all_chapters_button = customtkinter.CTkButton(
            master = self,
            text = "Save All Chapters",
            fg_color = ("purple"),
            command = self.click
        )
        self.save_all_chapters_button.grid(row=7, column=1, pady=10, padx=20, sticky="w")

    def fetch_chapters(self):
        url = self.url_field.get()
        print("Starting Fetch...")
        r = requests.get(url, allow_redirects=True,)

        soup = BeautifulSoup(r.text, features="html.parser")
        txt_links = lambda tag: (getattr(tag, 'name', None) == 'a' and 'href' in tag.attrs and 'txt' in tag.get_text().lower())
        results = soup.find_all(txt_links)
        print("Story fetched, scanning...")

        results = re.findall("\/chapters\/download\/\d+\/txt",str(results))
        i = 0
        chapters = {}
        for result in results:
            chapters[f"Chapter {i+1}"] = "https://www.fimfiction.net"+result
            i += 1
        
        for chapter in chapters:
            self.chapter_list.insert(self.chapter_list.size(),chapter)

    def click(self):
        print("Test Click")


class GeneratorFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        # Initialiserer objektet som en CTkFrame
        customtkinter.CTkFrame.__init__(
            self,
            master = parent
        )

        # Knap til manuel filvalg
        self.generator_manual_button = customtkinter.CTkButton(
            master = self,
            command = self.click,
            text_font = ("times 35", 12),
            fg_color = ("purple"),
            text = "Manual (Browse Files)"
        )
        self.generator_manual_button.grid(
            row = 0,
            column = 0,
            pady = 10, padx = 20,
            sticky = "w"
        )

    def click(self):
        print("Test button")

class ReaderFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        customtkinter.CTkFrame.__init__(
            self,
            master = parent
        )

        self.placeholder_info = customtkinter.CTkLabel(
            master = self,
            text = "Reader",
            text_font = ("times 35", 48),
            height = 1260,
            corner_radius = 6,
            fg_color = ("white", "orange"),
            justify = tkinter.LEFT
        )
        self.placeholder_info.pack(
            fill = 'both',
            expand = True
        )

class HistoryFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        customtkinter.CTkFrame.__init__(
            self,
            master = parent
        )

        self.placeholder_info = customtkinter.CTkLabel(
            master = self,
            text = "History",
            text_font = ("times 35", 48),
            height = 1260,
            corner_radius = 6,
            fg_color = ("white", "orange"),
            justify = tkinter.LEFT
        )
        self.placeholder_info.pack(
            fill = 'both',
            expand = True
        )

class SettingsFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        customtkinter.CTkFrame.__init__(
            self,
            master = parent
        )

        self.settings_server = customtkinter.CTkLabel(
            master = self,
            text="Server settings",
            text_font=("times 35", 16),
            height=36,
            corner_radius=6,
            fg_color=("white", "black"),
            justify=tkinter.LEFT)
        self.settings_server.grid(column=0, row=1, sticky="nwe", padx=15, pady=15)
        #valg2 test
        self.settings_reader = customtkinter.CTkLabel(
            master = self,
            text="Reader choices",
            text_font=("times 35", 16),
            height=36,
            corner_radius=6,
            fg_color=("white", "black"),
            justify=tkinter.LEFT)
        self.settings_reader.grid(column=0, row=2, sticky="nwe", padx=15, pady=15)