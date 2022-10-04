def chapterFetcher(url):
    from bs4 import BeautifulSoup
    import requests
    import re


    # Lader brugere insert den url de ønsker
    r = requests.get(url, allow_redirects=True,)
    soup = BeautifulSoup(r.text, features="html.parser")
    storyContentBox = soup.find("div", class_="story_content_box")
    children = storyContentBox.children

    for child in children:
        print(child)

chapterFetcher("https://www.fimfiction.net/story/164364/how-to-court-alicorns-a-humans-guide")