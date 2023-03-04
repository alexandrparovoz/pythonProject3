# пример построения таблицы на основе парсинга сайта
import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

url = 'https://webscraper.io/test-sites/e-commerce/static/computers/laptops'
res = requests.get(url)
ht = BeautifulSoup(res.content, 'html.parser')
# print(res)# если <Response [200]> то все ОК
# print(ht.text) # выводим текст всей страницы
# print(ht.h2)  #  выводим нужный нам тег
# print(ht.header.p) # выводим тег, вложный в больший тег
# print(ht.header.p.string) # выводим текст вложного тега
# print(ht.header.a.attrs) # выводим все атрибуты тега в виде словаря
#a_start = ht.header.a
# print(a_start.attrs)  # то же самое через перменую
#print(a_start['data-target']) # вывод элемента по ключу
# a = ht.find_all('h4', class_='pull-right price')
# for i in a:
#     print(i.text)  # перебираем список и вводим только текст
price = ht.find_all('h4', class_='pull-right price')
description = ht.find_all('p', class_='description')
name = ht.find_all('a', class_='title')
link = ht.find_all('a', class_='title')



product_price = []
product_desc = []
product_name = []
product_link = []

for i in price:
    price = i.text
    product_price.append(price)
for i in description:
    desc = i.text
    product_desc.append(desc)
for i in name:
    name = i.text
    product_name.append(name)

for count, a in enumerate(link):
    link = a['href']
    product_link.append(link)

table = pd.DataFrame({'Product  Name': product_name, 'Product  Price': product_price, 'Product  Description': product_desc,'Product  link': product_link})
#b = pd.DataFrame(d)
writer = pd.ExcelWriter('product.xlsx')
table.to_excel(writer, 'пример')
writer.save()
# print(product_price)
# print(product_name)
# print(product_desc)
