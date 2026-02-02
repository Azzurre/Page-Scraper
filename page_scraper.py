import asyncio
import requests
from bs4 import BeautifulSoup
from typing import List
from urllib.parse import urljoin

URL = "https://automatetheboringstuff.com/3e/chapter12.html"

with requests.get(URL) as response:
    soup = BeautifulSoup(response.content, 'lxml')


for section in soup.find_all('section', attrs={'type': 'division'}):
    
    match = soup.find_all('section', attrs={'type': 'division', 'aria-labelledby': 'sec1'})
    for i in range(len(match)):
        print (match[i].h3.text)

    summary = match[i].p.text
    print(summary)