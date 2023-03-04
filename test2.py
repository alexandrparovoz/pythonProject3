import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

max_page = 2
cur_page = 1
count = 1

d = {}
hr = []
text = []
while cur_page < max_page:
    req = requests.get(f'https://realt.by/sale/flats/?page={cur_page}')
    ht = BeautifulSoup(req.content, 'html.parser')
    prices = enumerate(ht.find_all('div', class_='text-truncate'))
    for counter, a in enumerate(ht.find_all('a', class_='teaser-title')):
        if 'article' in a['href'] or 'code' in a['href']:
            continue
        hr.append(a['href'])
        text.append(a.text.strip())
        count += 1
    cur_page += 1
d = {'название':text, 'cсылка':hr}
p = pd.DataFrame(d)
writer = pd.ExcelWriter('output.xlsx')
p.to_excel(writer, 'квартиры')
writer.save()