import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

req = requests.get('https://realt.by/sale/flats/') # в пременую пишм адрес стрницы
ht = BeautifulSoup(req.content, 'html.parser')  # в другую пременую грузим удобоваримый вид html файла
#print(ht.find_all('a', class_='teaser-title')) # здесь выводим ссылки А по классу teaser-title,
                                              # найденному в коде страницы
for counter, a in enumerate(ht.find_all('a', class_='teaser-title')):
    if 'news' in a['href'] or 'code' in a['href']:
        continue
    print(f'''{counter}. {a['href']} {a.text.strip()}''')

# выводим номер позиции, ссылку и текст объявления