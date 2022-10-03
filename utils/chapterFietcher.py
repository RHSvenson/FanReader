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

chapterFetcher("https://www.fimfiction.net/story/164364/how-to-court-alicorns-a-humans-guide")


# Side hvor links til alle kapitlerne er og skal findes
# Links som ikke slutter med .txt skal ignoreres
#https://www.fimfiction.net/story/25125/the-keepers-of-discord

# Link til individuelle kapitler
#https://www.fimfiction.net/chapters/download/184009/txt
#https://www.fimfiction.net/chapters/download/192610/txt
#https://www.fimfiction.net/chapters/download/192665/txt

# Link til alle kapitler samlet skal også ignoreres
#https://www.fimfiction.net/story/download/25125/txt

