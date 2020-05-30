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
    'cookie': 'u=2k2nckh9.uimfo2.ge503t04ox; buyer_selected_search_radius4=0_general; buyer_location_id=107621; luri=sankt_peterburg_i_lo; __cfduid=d4c1149a07c388028619a0dcd9c3d87271590785447; sessid=4d68db581d70a7d76a861957f6679366.1590785447; buyer_tooltip_location=0; f=5.0c4f4b6d233fb90636b4dd61b04726f147e1eada7172e06c47e1eada7172e06c47e1eada7172e06c47e1eada7172e06cb59320d6eb6303c1b59320d6eb6303c1b59320d6eb6303c147e1eada7172e06c8a38e2c5b3e08b898a38e2c5b3e08b890df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b9ad42d01242e34c7968e2978c700f15b6c5033da27bc46070d94b4f04f9554cf0c772035eab81f5e146b8ae4e81acb9fad99271d186dc1cd087829363e2d856a246b8ae4e81acb9fa143114829cf33ca734d62295fceb188dd50b96489ab264edf88859c11ff00895f88859c11ff00895f88859c11ff00895e2415097439d40471a2a574992f83a924124a64270d264e8f25f46baee4a3e2fea53f715ccf12793940f446d53389faf2985db2d99140e2d37522ba77017b09df3149a1a5471b7d038f0f5e6e0d2832edd6910c879f616322da10fb74cac1eab8f1786dad6fd98129e82118971f2ed64956cdff3d4067aa58ff5d551b162c7dafeebcd958348fe023de19da9ed218fe23de19da9ed218fe2dc4f5790d1ff098fb0ecb2e6b8bbd99dc9002564ccba9497; v=1590839683; sx=H4sIAAAAAAACA1WTS3KjQAyG78J6FgKrG5Hb2ALasQxKLGLFmcrdRz1Vzgwb2LS%2B%2Bh%2FS7%2BZyJbuf2kEHK4SFipORF25efjf35qUZl%2FGIb9bekwGIs6AXADQBQi7W%2FGqm5qVNA1AfH%2Fj%2B1Ryz9%2B92nFMpggbxiqGwmz6RQ9vNh7wdcWVkMnBiKWhqQkii%2FyNbSl0gWT5ez3jN7soFWZRKDDLAEym3r9ta7nKbkdlVzdUZQioWJaI9Mlfk6U48Xq8ZDoYc1swFhGPqiex5mPoyru%2FOKlSKKQcVWE2lKP5DDl0GOgSyu3Q%2BnUr6fHUXFa1KwQF%2BjI9ysGF5LBwJQ3gv7n9DVFAkk12Wfd8GcjwOj7flAo%2BzFVQji5LMzfGJPJQJN5izt1nDRDRTzKM%2BEUZg%2BB%2BJhy7VekaImNROFByviUaVFtk%2FkRMh5llgCxQx1Q5JQ6dHBgy%2BQyJWlW2Pl%2FGWeDtfECS2J%2FxRzMgTef6aqbutCV%2B1iETe6BFj7TFkYtkhE1aVxCnfB5za2IkoJeSFnyj2J0t9LFOirj%2FeUGMXIm3hGjtxRMSyR3a18XY9YXTT3q6rOkmpbyVk%2FEN%2BdeM8iPmKLobm4SUsq3D8yPbGBwzksOGtpK1dYr0hmgFjp6rkiWy9fKblfD33ByygjHETFmUjaImcdsiM9Xqmiy66bB%2Frm0ThLLHOkVjIfSK39Hi%2FbAuPOVYC44DcUCXyrJtp%2B3py6qvx6%2BM%2Brm%2F5Y%2FkM3zER16iA8mN8G6ZcTls5A5DH3UCEgwDRePB1f%2BN9qvXk05aWZV7gFIcW7%2BNTvLj%2BLNFQ5sm6fLTkseBQt8wBo8q4CXLcIzN%2Bf%2F8B0Le5AIoEAAA%3D; so=1590839684; dfp_group=96; no-ssr=1; buyer_from_page=catalog',
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

