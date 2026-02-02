import asyncio
import requests
from bs4 import BeautifulSoup
from typing import List
from urllib.parse import urljoin
import csv

URL = "https://blog.thepoon.fr"

with requests.get(URL) as response:
    soup = BeautifulSoup(response.content, 'lxml')


match = soup.find('div', class_='posts')
#print(match)

csv_file = open('cms_scrape.csv', 'w', newline='', encoding='utf-8')
writer = csv.writer(csv_file)
writer.writerow(['Headline', 'Summary', 'URL'])

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)
    
    summary = article.find('div', class_='entry').p.text
    print(summary)
    
    try:
        href = article.h2.a['href']
        print(urljoin(URL, href))
    except KeyError:
        print("No href found for article")

    print()
    
    writer.writerow([headline, summary, urljoin(URL, href)])
csv_file.close()
