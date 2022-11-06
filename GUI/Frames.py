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
        customtkinter.CTkFrame.__init__(
            self,
            master = parent
        )
        self.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

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

