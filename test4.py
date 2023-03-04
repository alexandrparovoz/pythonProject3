import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl


max_page = 4
cur_page = 2
while cur_page < max_page:
    url = f'https://cars.av.by/filter?brands[0][brand]=6&brands[0][model]=5810&brands[0][generation]=4297&page={cur_page}'
    r = requests.get(url)
    ht = BeautifulSoup(r.content, 'html.parser')
    div = ht.find_all('div', class_="listing-item__wrap")
    #a = ht.find_all('a', class_='listing-item__link')
    for counter, a in enumerate(ht.find_all('div', class_='listing-item__wrap')):
        print(f'''{counter}. {a.text.strip()}''')
    cur_page += 1



# with open('test.html', 'w', encoding='utf-8') as file:
#   file.write(r.text)