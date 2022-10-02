import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
import urllib.request

for url in ['https://www.fanfiction.net/']:
    try:
        response = requests.get(url)

        # Kontroller respons, giv eventuel fejlkode
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP fejl: {http_err}')
        exit()
    except Exception as err:
        print(f'Fejl: {err}')
        exit()
    else:
        print('Success')

# Generer soup og indhent hyperlinks, generer kapitelliste
urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:103.0) Gecko/20100101 Firefox/103.0'})
html_page = urllib.request.urlopen(url)
soup = BeautifulSoup(html_page, "html.parser")
for link in soup.findAll('a'):
    print(link.get('href'))