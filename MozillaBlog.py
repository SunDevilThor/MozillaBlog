# Webpress Scraper - Mozilla Blog
# Tutorial from John Watson Rooney YouTube channel

import requests 
from bs4 import BeautifulSoup
import pandas as pd
import time

article_list = []

def request(x):
    url = f'https://blog.mozilla.org/latest/page/{x}/'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, features='lxml')
    return soup.find_all('section', class_= 'mzp-c-card mzp-has-aspect-1-1')

def parse(articles):
    for item in articles: 
        title = item.find({'h2': 'mzp-c-card-title'}).text
        link = item.find({'a': 'mzp-c-card-block-link'})
        link = link['href']
        # print(title, link['href'])

        article = {
            'title': title,
            'link': link,
        }

        article_list.append(article)

def output():
    df = pd.DataFrame(article_list)
    df.to_csv('MozillaBlog.csv')
    print('Saved items to CSV file.')

x = 1

while True: 
    print(f'Page {x}')
    articles = request(x)
    x += 1
    # time.sleep(3)
    if len(articles) != 0:
        parse(articles)
    else: 
        break

print('Completed. Total articles is ', len(article_list))
output()




