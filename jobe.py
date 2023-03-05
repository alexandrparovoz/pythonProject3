# пример построения таблицы на основе парсинга сайта rabota.by с пересчетом страниц
import requests
from bs4 import BeautifulSoup
import pandas as pd

urls = 'https://praca.by/catalogue/vacancies/programmist/'
# res = requests.get(url)
# ht = BeautifulSoup(res.content, 'html.parser')
# job_message = ht.find_all('div', class_='vacancy__search-description')
# job_name = ht.find_all('a', class_='vac-small__title-link')
# job_salary = ht.find_all('div', class_='vac-small__salary')
# #for c, a in enumerate(ht.find_all('div', class_='vacancy__search-description')):
#    # print(c,a)
# for c, a in enumerate(ht.find_all('div', class_='vac-small__salary')):
#     print(c,a)
# for c, a in enumerate(ht.find_all('a', class_='vac-small__title-link')):
#     print(c,a)

def parse(url):
    result_list = {'NAME': [], 'EXPERIENCE': [], "LINK": []}
    res = requests.get(url)
    ht = BeautifulSoup(res.content, 'html.parser')
    job_name = ht.find_all('a', class_='vac-small__title-link')
    job_experience = ht.find_all('div', class_='vac-small__experience')
    for name in job_name:
        result_list['NAME'].append(name.text)
        result_list['LINK'].append(name['href'])
    for experience in job_experience:
        result_list['EXPERIENCE'].append(experience.text)
    return result_list


table = pd.DataFrame(data=parse(urls))
writer = pd.ExcelWriter('JOB.xlsx')
table.to_excel(writer, 'job_ads')
writer.save()
