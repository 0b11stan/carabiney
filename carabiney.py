#!/bin/python

from requests import get
from bs4 import BeautifulSoup
from urllib.parse import unquote
from pathlib import Path
from os import mkdir

BASE = 'https://www.carabinsbordeaux.fr/'


def fetch(route):
    r = get(BASE + route)
    return BeautifulSoup(r.text, 'html.parser').find_all('a')[5:]


outdir = Path('./roneos/')
if not outdir.exists():
    outdir.mkdir()

categories = fetch('wp-content/uploads/roneos')

print('Liste des matières :')
for index, category in enumerate(categories):
    print(f"  {index}. " + unquote(category['href'][:-1]))

pick = int(input("\nChoisis une matière à télécharger : "))

category = categories[pick]['href']
roneos = fetch('wp-content/uploads/roneos/' + category)

for roneo in roneos:
    roneo = roneo['href']
    print('  fetching ' + unquote(roneo[:-1]) + ' ...')
    try:
        files = fetch('wp-content/uploads/roneos/' + category + roneo)
        filename = [f['href'] for f in files if '.pdf' in f['href']][0]
        r = get(BASE+'wp-content/uploads/roneos/'+category+roneo+filename)
        outdir.joinpath(unquote(roneo[:-1]) + '.pdf').write_bytes(r.content)
    except:
        print('    FAILED')
