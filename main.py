import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl


d = {}
hr = []
text = []

max_page = 2
cur_page = 0
# count = 1

while cur_page < max_page:
    req = requests.get(f'https://realt.by/sale/flats/?page={cur_page}')
    ht = BeautifulSoup(req.content, 'html.parser')
    prices = enumerate(ht.find_all('div', class_='col-auto text-truncate'))
    for counter, a in enumerate(ht.find_all('a', class_='teaser-title')):
        print(f'''{counter}. {a['href']} {a.text.strip()}''')
        if 'article' in a['href'] or 'code' in a['href']:
            continue
        # hr.append(a['href'])
        # text.append(a.text.strip())
        # count += 1
    cur_page += 1
# d = {'название': text ,'сcылка': hr}
# p = pd.DataFrame(a)
# writer = pd.ExcelWriter('output.xlsx')
# p.to_excel(writer, 'квартиры')
# writer.save()