import asyncio
import requests
from bs4 import BeautifulSoup
from typing import List
from urllib.parse import urljoin

URL = "https://blog.thepoon.fr"

with requests.get(URL) as response:
    soup = BeautifulSoup(response.content, 'lxml')


match = soup.find('div', class_='posts')
#print(match)

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)
    
    summary = article.find('div', class_='entry').p.text
    print(summary)
    
    href = article.h2.a['href']
    print(urljoin(URL, href))
    
    print()

#for headline in match.find_all('h2'):
#    headline = headline.a.text
#    print(headline)
    
#headline = match.h2.a.text
#print(headline)