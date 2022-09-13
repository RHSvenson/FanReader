import time
import urllib
from bs4 import BeautifulSoup
import requests
import re


url = "https://www.fimfiction.net/story/25125/the-keepers-of-discord"
r = requests.get(url, allow_redirects=True)
soup = BeautifulSoup(r.text)
txt_links = lambda tag: (getattr(tag, 'name', None) == 'a' and 'href' in tag.attrs and 'txt' in tag.get_text().lower())
results = soup.find_all(txt_links)
print(results)






# Side hvor links til alle kapitlerne er og skal findes
# Links som ikke slutter med .txt skal ignoreres
#https://www.fimfiction.net/story/25125/the-keepers-of-discord

# Link til individuelle kapitler
#https://www.fimfiction.net/chapters/download/184009/txt
#https://www.fimfiction.net/chapters/download/192610/txt
#https://www.fimfiction.net/chapters/download/192665/txt

# Link til alle kapitler samlet
#https://www.fimfiction.net/story/download/25125/txt

