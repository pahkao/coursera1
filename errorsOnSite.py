# #### Импорты
import re
from pprint import pprint

#!pip install pyaspeller

from pyaspeller import Word
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--headless")

browser = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())


# #### Парсинг




check_url = 'http://station-l.ru/'
browser.get(check_url)





all_urls = [check_url]

for a in browser.find_elements_by_tag_name('a'):
    a = a.get_attribute('href')

    if type(a) == str and 'jivosite' not in a and re.match('.+\.(jpg|pdf|png)$', a) == None:
        domain = re.sub('https:\/\/(w{3}\.)?(.+?)\/.*', r'\2', check_url )


        a = re.sub('(.*)(\?|\#)', r'\1', a)

        try:
            if domain in a and a not in all_urls:
                all_urls.append(a)

        except:
            continue

all_urls





def get_words(body):
    unique_words_list = []

    for frase in body.split('\n'):
        frase = frase.split(' ')
        for word in frase:
            word = re.sub('[^ёЁа-яА-Яa-zA-Z0-9-–—]', '', word)
            if word not in unique_words_list and re.match('(^\d+$)|(^\W+$)|(^$)', word) == None:
                unique_words_list.append(word)

    return sorted(unique_words_list)





body = {}

for url in all_urls:
    print(url)
    browser.get(url)
    browser.find_element_by_tag_name('body').send_keys(Keys.END) # scroll page to bottom

    body[url] = ''
    body[url] += ' ' + browser.find_element_by_tag_name('body').text
    if len(browser.find_elements_by_tag_name('div')) != 0:
        for div in browser.find_elements_by_tag_name('div'):
            try:
                body[url] += ' ' + div.text
            except:
                continue

    print(f'Слов для проверки на странице {url}: {len(get_words(body[url]))}\n')


# #### Проверка




for url in body:

    errors = {}
    print(url)
    for clean_word in get_words(body[url]):
        try:
            check = Word(clean_word)
            if check.correct == False:
                if clean_word not in errors:
                    errors[clean_word] = {}
                    errors[clean_word]['variants'] = check.variants
                    errors[clean_word]['count'] = 1
                else:
                    errors[clean_word]['count'] += 1
        except Exception as e:
            print(f'Что-то пошло не так: {e}, слово: {clean_word}')
            continue

    pprint(errors)
    print('\n')





browser.quit()
