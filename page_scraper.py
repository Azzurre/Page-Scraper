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



def main():
    options = Options()
    options.add_argument('--headless=new') # Run Chrome in headless mode
    driver = webdriver.Chrome(service=Service(), options=options)
    driver.get("https://blog.thepoon.fr")
    
    #Extract page and get screenshot
    print(driver.title)
    driver.save_screenshot("screenshot.png")
    
    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links[:5]:
        text = link.text.strip()
        href = link.get_attribute("href")
        print(text)
        print(href)
    
    driver.quit()
        
    
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

if __name__ == "__main__":
    main()
    

