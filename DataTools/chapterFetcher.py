def chapterFetcher(url):
    from bs4 import BeautifulSoup
    import requests
    import re


    # Lader brugere insert den url de ønsker
    r = requests.get(url, allow_redirects=True,)
    soup = BeautifulSoup(r.text, features="html.parser")
    txt_links = lambda tag: (getattr(tag, 'name', None) == 'a' and 'href' in tag.attrs and 'txt' in tag.get_text().lower())
    results = soup.find_all(txt_links)


    results = re.findall("\/chapters\/download\/\d+\/txt",str(results))
    i = 0
    while i <= 2:
        results[i] = "https://www.fimfiction.net"+results[i]
        i += 1
    print(results)
    return(results)