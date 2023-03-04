import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

max_page = 4
cur_page = 1

d = {}
hr = []
text = []
price = []

while cur_page < max_page:
    req = requests.get(f'https://realt.by/sale/flats/?page={cur_page}')
    ht = BeautifulSoup(req.content, 'html.parser')
    for counter, a in enumerate(ht.find_all('a', class_="teaser-title")):
        if 'article' not in a['href'] and 'code' not in a['href']:
            hr.append(a['href'])
            text.append(a.text.strip())
            # print(f"""{a['href']} {a.text.strip()}""")
    for counter, div in enumerate(ht.find_all('div', class_="col-auto text-truncate")):
        if div.text.strip() != '':
            price.append(div.text.strip())
        else:
            continue
        # print(f"{div.text.strip()}")

    cur_page += 1


# for i in range(len(hr)):
#     print(hr[i])
# for j in range(len(text)):
#     print(text[j])
# for k in range(len(price)):
#     print(price[k])

d = {'продажа квартир': text, 'cсылка': hr, 'цена': price}
b = pd.DataFrame(d)
writer = pd.ExcelWriter('flats.xlsx')
b.to_excel(writer, 'квартиры')
writer.save()