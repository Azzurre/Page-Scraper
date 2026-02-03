import asyncio
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
        if price.
        availability = book.select_one('p.instock.availability').text.strip()
        book.append({
            'title': title,
            'price': price,
            'availability': availability
        })