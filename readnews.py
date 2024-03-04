import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.bbc.com'

URL = BASE_URL+'/sport'
res = requests.get(URL)

soup = BeautifulSoup(res.text, 'html.parser')
links = soup.find_all(class_='ssrcss-vdnb7q-PromoLink exn3ah91')

for link in links:
    route = link.get('href')
    if not route.startswith('/sport'):
        continue
    subres = requests.get(BASE_URL+route)
    soup2 = BeautifulSoup(subres.text, 'html.parser')
    title = soup2.find(class_='gel-trafalgar-bold qa-story-headline gs-u-mv+')
    if title is None:
        continue
    print(title.text)





