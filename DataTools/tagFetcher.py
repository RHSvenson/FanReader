from pageFetcher import pageFetcher

def tagFetcher(soup):
    import json
    import re
    from bs4 import BeautifulSoup

    allTags = soup.find_all("a", class_="tag-character")
    relevantTags = []
    
    for tag in allTags:
        for parent in tag.parents:
            print(parent.attrs)

    #print(allTags)

soup = pageFetcher("https://www.fimfiction.net/story/25125/the-keepers-of-discord")
tagFetcher(soup)