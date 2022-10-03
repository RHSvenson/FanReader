def tagFetcher(url):
    from bs4 import BeautifulSoup
    import requests
    import re
    import json


    # Lader brugere insert den url de ønsker
    r = requests.get(url, allow_redirects=True,)
    soup = BeautifulSoup(r.text, features="html.parser")
    for tag in soup.find_all("a", class_="tag-character"):
        for parent in tag.parents:
            if parent.name == "story_content_box":
                print(tag)
    #results = re.findall("(?<=data-tag=\")([a-z]|-)+(?=\")", str(storybox))
    

tagFetcher("https://www.fimfiction.net/story/25125/the-keepers-of-discord")