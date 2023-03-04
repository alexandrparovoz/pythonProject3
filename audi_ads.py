# пример построения таблицы на основе парсинга сайта yandex.com/weather
import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://cars.av.by/filter?brands[0][brand]=6&brands[0][model]=5810&transmission_type=1'
res = requests.get(url)
ht = BeautifulSoup(res.content, 'html.parser')
param = ht.find_all('div', class_='listing-item__params')
description = ht.find_all('div',  class_="listing-item__message")
price = ht.find_all('div', class_='listing-item__price')
link = ht.find_all('a', class_='listing-item__link')
# for i in link:
#     link = i['href']
#     print(f'https://cars.av.by/{link}')

audi_param = []
audi_description = []
audi_price = []
audi_link = []

for i in param:
    param1 = i.text
    audi_param.append(param1)

for i in description:
    description = i.text
    audi_description.append(description)

for i in price:
    price = i.text
    audi_price.append(price)

for i in link:
    link = i['href']  # важноо брать не текст а саму ссылку href
    audi_link.append(f'https://cars.av.by/{link}')
# в словарь не влез description (слишком длинный)
dict = {'AUDI parameters': audi_param, 'AUDI price': audi_price, 'AUDI  link': audi_link}
table = pd.DataFrame(dict)
writer = pd.ExcelWriter('AUDI.xlsx')
table.to_excel(writer, 'audi_ads')
writer.save()