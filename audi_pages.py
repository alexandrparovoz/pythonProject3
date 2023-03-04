# пример построения таблицы на основе парсинга сайта av.by с пересчетом страниц
import requests
from bs4 import BeautifulSoup
import pandas as pd

max_page = 5
cur_page = 1
count = 1

while cur_page < max_page:
    url = f'https://cars.av.by/filter?brands[0][brand]=6&brands[0][model]=5810&transmission_type=1&page={cur_page}'
    res = requests.get(url)
    ht = BeautifulSoup(res.content, 'html.parser')
    param = ht.find_all('div', class_='listing-item__params')
    description = ht.find_all('div',  class_="listing-item__message")
    price = ht.find_all('div', class_='listing-item__price')
    link = ht.find_all('a', class_='listing-item__link')
    for count, a in enumerate(ht.find_all('div', class_='listing-item__price')):
        price1 = a.text
        print(f'{count}. price - {price1}')
    cur_page += 1