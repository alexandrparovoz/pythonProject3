import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

max_page = 4 #  до какой страницы листаем
cur_page = 0  # с какой страницы начинаеем
counter = 0
while cur_page < max_page:
    reg = requests.get(f'https://realt.by/sale/flats/?page={cur_page}') # после каждого цикла идем на следщую страницу
    ht = BeautifulSoup(reg.content,'html.parser')
    for counter, a in enumerate(ht.find_all('a', class_='teaser-title')):
        if 'news' in a['href'] or 'code' in a['href']:
            continue
        print(f'''{counter+1}. {a['href']} {a.text.strip()}''')
        counter += 1
    cur_page += 1
