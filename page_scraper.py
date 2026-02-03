import asyncio
import time
from wsgiref import headers
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
import random
from crawl4ai import *
import cmd

# Command Line Interface for the web scraper (AI powered)
class myCLI(cmd.Cmd):
    intro = 'Welcome to the web scraper CLI. Type help or ? to list commands.\n'
    prompt = '(scraper) '

    def do_scrape(self, url):
        'Scrape the given URL: scrape http://example.com'
        asyncio.run(main(url))

    def do_exit(self, arg):
        'Exit the CLI'
        print('Exiting...')
        return True 


async def main(url = "http://books.toscrape.com/"):
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url)
        print(result.markdown)

# async def scrape_books(url):
    
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    
#     URL = url
#     try:
#         response = requests.get(URL, headers=headers, timeout=10)
#         response.raise_for_status()  # Ensure we notice bad responses
#         soup = BeautifulSoup(response.content, 'html.parser')
        
#         books = []
        
#         for book in soup.select('article.product_pod'):
#             # Extract book details
#             title = book.h3.a['title'] # Book title
#             price = book.select_one('p.price_color').text.strip() # Book price
#             currency_symbol = None # Default currency symbol
#             match = re.search(r'[\$€£]', price) # Regex to find currency symbol
#             if match:  
#                 currency_symbol = match.group(0)           # Extract currency symbol if found 
#             availability = book.select_one('p.instock.availability').text.strip() # Availability status
#             star_rating = book.find('p', class_='star-rating')['class'][1] # Star rating class
#             star_rating = star_rating.lower()  # Convert to lowercase for consistency
#             converted_rating = {'one': '★', 'two': '★★', 'three': '★★★', 'four': '★★★★', 'five': '★★★★★'}.get(star_rating, '') # Convert
#             star_rating = converted_rating         
#             # Append book details to the list
#             books.append({
#                 'title': title,
#                 'price': price,
#                 'currency_symbol': currency_symbol if match else None,
#                 'availability': availability,
#                 'star_rating': star_rating
#             })
            
#             time.sleep(random.uniform(0.5, 2.5))  # Be polite and avoid overwhelming the server
#         return books
    
#     except requests.RequestException as e:
#         print(f"An error occurred: {e}")
#         return []
    
# def save_to_csv(books: List[dict], filename: str):
#     keys = books[0].keys()
#     with open(filename, 'w', newline='', encoding='utf-8') as output_file:
#         dict_writer = csv.DictWriter(output_file, fieldnames=keys)
#         dict_writer.writeheader()
#         dict_writer.writerows(books)


        
if __name__ == "__main__":
    # books = asyncio.run(scrape_books("http://books.toscrape.com/"))
    # save_to_csv(books, 'books.csv')
    asyncio.run(main())
    cli = myCLI()
    cli.cmdloop()
    
    # print(f"Scraped {len(books)} books and saved to books.csv")
    
