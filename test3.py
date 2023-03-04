import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl


# страница куфар продажа животных страницы перечислять не могу (нет внятной сортировки)
url = 'https://www.kufar.by/l/zhivotnye?elementType=popular_categories'
resp = requests.get(url)
bs = BeautifulSoup(resp.content, 'html.parser')
a = bs.find_all('a', class_="styles_wrapper__yaLfq")
temp = bs.find_all('div', class_="styles_top__HNf3a")
for counter, a in enumerate(bs.find_all('a', class_="styles_wrapper__yaLfq")):
    if 'rank' not in a['href']:
        continue
#for counter, div in enumerate(bs.find_all('div', class_="styles_content__BDDGV")):
    print(f'''{counter}.{a['href']}. {a.text.strip()}''')
    #print(div.text.strip())
