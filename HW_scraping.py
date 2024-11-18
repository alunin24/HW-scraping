import json
from pprint import pprint

import requests
import bs4
import re

response = requests.get('https://habr.com/ru/articles/')
soup = bs4.BeautifulSoup(response.text, features='lxml')
articles_list = soup.findAll('div', class_='tm-article-snippet')
# print(articles_list)


KEYWORDS = {'дизайн', 'фото', 'web', 'python'}

pars_data = []
for articles in articles_list:
    link = f"https://habr.com{articles.find('a', class_='tm-title__link')['href']}"#добываем ссылки на текст
    # print(link)
    response = requests.get(link)
    soup = bs4.BeautifulSoup(response.text, features='lxml')

    title = soup.find('h1', class_='tm-title').text.strip()
    # print(title)
    time = soup.find('time')['datetime']
    text = soup.find('div', class_='article-formatted-body').text
    if KEYWORDS & set(text.rstrip().split()):
        pars_data.append({
            'time': time,
            'title': title,
            'link': link
        })
pprint(pars_data)