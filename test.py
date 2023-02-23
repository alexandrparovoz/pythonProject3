import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

max_page = 100
cur_page = 0
counter = 0
while cur_page < max_page:
    reg = requests.get('https://realt.by/sale/flats/?page=1{cur_page}')
    ht = BeautifulSoup(reg.content,'html.parser')
    for counter, a in enumerate(ht.find_all('a', class_='teaser-title')):
        if 'news' in a['href'] or 'code' in a['href']:
            continue
        print(f'''{counter+1}. {a['href']} {a.text.strip()}''')
        counter += 1
    cur_page += 1
