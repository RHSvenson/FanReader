import os
import re
import requests
import string
from bs4 import BeautifulSoup

class Story(local_file, external_link):
    def __init__(self):
        # If a link is provided, fetch it from the URL
        if external_link:
            # ++ Get necessary variable inputs ++ #
            # For FimFiction
            if re.match("fimfiction\.net",external_link):
                # Get Title
                self.title = re.search("(?<=\d{3}\/).+", self.external_link)
                self.title = self.title.group()
                self.title = re.sub("\-", " ", self.title)
                self.title = string.capwords(self.title, sep = None)

                # Get Download Link
                self.fimfiction_id = re.search("\d{6}",self.external_link)
                self.download_link = f'https://www.fimfiction.net/story/download/{self.fimfiction_id}/html'

                # Get Soup
                self.page = requests.get(self.external_link, allow_redirects = true)
                self.soup = BeautifulSoup(self.page.text, features="html.parser")

                # Get Tags
                self.soup_tags = soup.article.story_container.find_all("a", class_=(re.compile("^b(tag-)")))
                self.tags = []
                for tag in soup_tags:
                    self.tags.append(tag.title)


            # ++ Create Folder for permanent storage ++ #
            # Navigate to Library directory
            self.storage_directory = os.path.join(os.path.dirname(__file__), os.pardir)
            self.storage_directory = os.path.join(self.storage_directory, 'Library', 'Unsorted', f'{self.title}')
            self.storage_path = os.path.abspath(os.path.join(self.storage_directory, f'{self.title}.json'))

            # Create storage directory if it's not there yet.
            if not os.path.exists(self.storage_path):
                os.makedirs(self.storage_directory)

            # Mark the story as not downloaded. Disables various methods.
            self.downloaded = False
            self.file_path = ""

            # Write all of these variables down in a .json
            self.story_properties = {
                "title": self.title,
                "download_link": self.download_link,
                "download_status": self.downloaded,
                "path": self.storage_path,
                "tags": self.tags,
                "file_path": self.file_path
            }
            with open(self.storage_path, "wb") as destination:
                json.dump(story_properties, destination)

        # ++ If it's from storage, then fetch it from existing .json ++ #
        if json:
            self.story_properties = json.load(self.local_file)
            # Initialise variables from json
            self.title = self.story_properties["title"]
            self.tags = self.story_properties["tags"]
            self.downloaded = self.story_properties["download_status"]
            self.download_link = self.story_properties["download_link"]
            self.storage_path = self.story_properties["path"]
            self.storage_directory = os.path.dirname(self.storage_path)

    def download_content():
        self.file = requests.get(download_link)
        self.downloaded = True
        self.file_path = os.path.join(self.storage_directory,f'{self.title}.html')
        with open(self.file_path, "wb") as destination:
            destination.write(self.file.content)

        update_json()

    def update_json():
        self.story_properties = {
                "title": self.title,
                "download_link": self.download_link,
                "download_status": self.downloaded,
                "path": self.storage_path,
                "tags": self.tags,
                "file_path": self.file_path
            }
        with open(self.storage_path, "wb") as destination:
            json.dump(story_properties, destination)


            


        

        