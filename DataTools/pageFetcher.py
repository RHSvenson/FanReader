def pageFetcher(url):
    from bs4 import BeautifulSoup
    import requests


    # Lader brugere insert den url de ønsker
    r = requests.get(url, allow_redirects=True,)
    soup = BeautifulSoup(r.text, features="html.parser")

    return soup