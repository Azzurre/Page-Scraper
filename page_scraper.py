import asyncio
import time
from mdurl import URL
import requests
from bs4 import BeautifulSoup
from typing import List
from urllib.parse import urljoin
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re


def scrape_books():
    URL = "http://books.toscrape.com/"
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    books = []
    
    for book in soup.select('article.product_pod'):
        title = book.h3.a['title']
        price = book.select_one('p.price_color').text.strip()
        match = re.search(r'[\$€£]', price)
        if match:
            currency_symbol = match.group(0)            
        availability = book.select_one('p.instock.availability').text.strip()
        books.append({
            'title': title,
            'price': price,
            'currency_symbol': currency_symbol if match else None,
            'availability': availability
        })
        
        time.sleep(1)  # Be polite and avoid overwhelming the server
    return books
def save_to_csv(books: List[dict], filename: str):
    keys = books[0.].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(books)
        
if __name__ == "__main__":
    books = scrape_books()
    save_to_csv(books, 'books.csv')
