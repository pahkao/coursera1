import requests
from bs4 import BeautifulSoup
import csv
import os
import time
import random

URL = 'https://www.avito.ru/sankt_peterburg_i_lo/kvartiry/prodam/novostroyka-ASgBAQICAUSSA8YQAUDmBxSOUg?cd=1&f=ASgBAQICAUSSA8YQAkDmBxSOUpC~DRSSrjU'
HOST = 'https://www.avito.ru'
FILE = 'zhks.csv'
HEADERS = {
    # ':authority:': 'www.avito.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,ru;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': paste your cookie here. 'f=' strongly recommended!
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_pages_count(html):
    soup = BeautifulSoup(html, 'lxml')
    pagination = soup.find_all('span', class_='pagination-item-1WyVp')
    if pagination:
        return int(pagination[-2].get_text())
    else:
        return 1


def save_file(items, path):
    with open(path, 'w', newline='', encoding='utf8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Тип', 'Название ЖК', 'Адрес ЖК', 'Город', 'Ссылка', 'Цена'])
        for item in items:
            writer.writerow([item['title'], item['zhk_name'], item['zhk_address'], item['zhk_city'], item['link'], item['price']])



def parse():
    html = get_html(URL)
    if html.status_code == 200:
        zhks = []
        pages_count = get_pages_count(html.text)
        for page in range(1, pages_count + 1):
            print(f'Парсинг страницы {page} из {pages_count}...')
            html = get_html(URL, params={'p': page})
            zhks.extend(get_content(html.text))
            save_file(zhks, FILE)
            time.sleep(random.randint(2, 5))
            print(f'Получено {len(zhks)} квартир')
        os.startfile(FILE)
    else:
        print('Error, status code not OK')



def get_content(html):
    soup = BeautifulSoup(html, 'lxml')
    cards = soup.find_all('div', class_='snippet-horizontal')

    zhks = []
    for card in cards:
        try:
            zhks.append({
                'title': card.find('a', class_='snippet-link').get_text(),
                'zhk_name': card.find('div', class_='address').find_next('div').get_text(strip=True),
                'zhk_address': card.find('span', class_='item-address__string').get_text(strip=True),
                'zhk_city': card.find('span', class_='item-address-georeferences-item__content').get_text(strip=True),
                'link': HOST + card.find('a', class_='snippet-link').get('href'),
                'price': card.find('span', class_='snippet-price').get_text(strip=True),
            })
        except AttributeError:
            print('Не удалось спарсить страницу')
            continue
    return zhks


parse()

