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

import json
import string

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
            placeholder_text = "Enter URL Here"
        )
        self.url_field.grid(
            row = 0,
            column = 0,
            pady = 20, padx = 20,
            sticky = "we"
        )

        # Knap til at indlæse den indtastede URL
        self.fetch_button = customtkinter.CTkButton(
            master = self,
            text = "Fetch URL",
            text_font = ("times 35", 12),
            fg_color = ("purple"),
            command = lambda: self.fetch_chapters(parent)
        )
        self.fetch_button.grid(
            row = 0,
            column = 1,
            pady = 10, padx = 20,
            sticky = "we"
        )

        self.story_title_field = customtkinter.CTkLabel(
            master = self,
            width = 80,
            text = "No Story Initialized."
        )
        self.story_title_field.grid(
            row = 1,
            column = 0,
            pady = 10,
            padx = 20,
        )

        # Liste der indeholder de kapitler funktionen fandt.
        # Tom til at starte med.
        self.chapter_list = Listbox(
            master = self,
            bg = "purple",
            font = ("times 35", 12),
            selectmode = SINGLE
        )
        self.chapter_list.grid(
            row = 2,
            pady = 10,
            padx = 20, 
            sticky = "nsew",
            columnspan = 2
        )
        self.chapter_list.config(
            height=self.chapter_list.size()
        )

        # Knap til at gemme et kapitel
        self.save_one_chapter_button = customtkinter.CTkButton(
            master = self,
            text = "Save Individual Chapter",
            fg_color = ("purple"),
            command = lambda: self.save_chapter_from_web(parent, self.chapter_list.curselection())
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

    def fetch_chapters(self, parent):
        # Funktion til at samle de links vi skal bruge til de forskellige kapitler, og vise dem på skærmen

        # Hent den indtastede URL fra GUI feltet
        self.url = self.url_field.get()
        print("Starting Fetch...")

        # Indhent HTML siden fra linket til memory
        self.r = requests.get(self.url, allow_redirects=True,)
        print("Story fetched, scanning...")

        # Indsaml historien titel ved at formatere det fra linket.
        # TODO: Dette virker lige nu kun på FimFiction. Dette skal ændres når vi bliver bekendte med andre hjemmesider.
        self.story_title = re.search("(?<=\/\d{6}\/).+", self.url)
        self.story_title = self.story_title.group()
        self.story_title = re.sub("\-", " ", self.story_title)
        self.story_title = string.capwords(self.story_title, sep = None)
        self.story_title_field.configure(text = self.story_title)
        # NOTE: Alle variabler, såsom titlen på den nuværende indlæste historie opbevares i MainWindow (parent)
        parent.current_story_title = self.story_title

        # Find alle links til individuelle kapitler
        self.soup = BeautifulSoup(self.r.text, features="html.parser")
        self.txt_links = lambda tag: (
            getattr(tag, 'name', None) == 'a' and 'href' in tag.attrs and 'txt' in tag.get_text().lower()
        )
        self.results = self.soup.find_all(self.txt_links)
        self.results = re.findall("\/chapters\/download\/\d+\/txt",str(self.results))

        # Og indsæt dem i en liste
        # NOTE: Kapitel dictionary er også opbevaret i MainWindow, da den skal tilgås af andre objekter.
        i = 0
        for result in self.results:
            parent.chapters[f"Chapter {i+1}"] = "https://www.fimfiction.net"+result
            i += 1
        
        # Indsæt kapitlerne i GUI listen, så brugeren kan se og vælge dem
        for chapter in parent.chapters:
            self.chapter_list.insert(self.chapter_list.size(),chapter)

    def save_chapter_from_web(self, parent, chapter):
        # Metode til når man bruger 'Save Chapter' knapperne.

        # Fastlægger hvor vi er henne.
        # NOTE: Muligvis ikke cross-platform, dette skal kontrolleres.
        self.root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        # Og hvor vi skal hen
        self.target_directory = os.path.join(self.root_directory, f'Data/previousStories/{parent.current_story_title}')

        print("Attempting to print file " + f"Chapter{chapter[0]+1}.txt" + " to destination " + str(self.target_directory) +"...")

        # Hvis mappen findes, så skriv med det samme
        if os.path.exists(self.target_directory):
            with open (os.path.join(self.target_directory ,f"Chapter{chapter[0]+1}.txt"), "wb") as destination:
                destination.write(requests.get(parent.chapters[f"Chapter {chapter[0]+1}"]).content)
        
        # Ellers så lav mappen først.
        # NOTE: Koden kan virke redundant, men det er meget mere sandsynligt at mappen allerede findes, hvorfor denne
        # er længere nede i hierarkiet, så vi ikke spiller tid på et tjek der kun skal udføres en ud af 30 gange.
        else:
            os.makedirs(self.target_directory)
            with open (os.path.join(self.target_directory ,f"Chapter{chapter[0]+1}.txt"), "wb") as destination:
                destination.write(requests.get(parent.chapters[f"Chapter {chapter[0]+1}"]).content)


    # Funktion til brug ved tryk på Save Chapter knapperne. Bruges til begge.
    
            


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