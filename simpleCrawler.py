import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json

results = []
MAX_PAGE = 20
ROOT_URL = "http://miradetodo.io/page/{}"

for current_page in range(1,MAX_PAGE+1):
    print("Scraping the page {}".format(current_page), end='\t')
    content = requests.get(ROOT_URL.format(current_page))
    soup = BeautifulSoup(content.text, "html.parser")

    items_container = soup.find('div', {'class': 'item_1'})

    for cover in items_container.findAll('div', {'class': 'item'}):
        movie = {}
        movie["title"] = cover.find('span', {'class': 'tt'}).get_text()
        movie["description"] = cover.find('span', {'class': 'ttx'}).get_text()
        movie["rating"] = cover.find('span', {'class': 'imdb'}).get_text() if cover.find('span', {'class': 'imdb'}) is not None else ""
        movie["quality"] = cover.find('span', {'class': 'calidad2'}).get_text() if cover.find('span', {'class': 'calidad2'}) else ""
        movie["year"] = cover.find('span', {'class': 'year'}).get_text()
        movie["img"] = cover.find('img').get('src')
        movie["url"] = cover.find('a').get('href')
        results.append(movie)
    print("OK")

# pprint(results)

print("Done")

with open("results.json","w") as results_file:
    json.dump(results,results_file,indent=4,sort_keys=True)

