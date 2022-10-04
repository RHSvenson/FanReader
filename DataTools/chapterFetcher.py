def chapterFetcher(soup):
    from bs4 import BeautifulSoup
    import requests
    import re


    # Lader brugere insert den url de ønsker
    txt_links = lambda tag: (getattr(tag, 'name', None) == 'a' and 'href' in tag.attrs and 'txt' in tag.get_text().lower())
    results = soup.find_all(txt_links)


    results = re.findall("\/chapters\/download\/\d+\/txt",str(results))
    i = 0
    chapters = {}
    for result in results:
        chapters[f"Chapter {i+1}"] = "https://www.fimfiction.net"+result
        i += 1
    print(chapters)
    return(chapters)