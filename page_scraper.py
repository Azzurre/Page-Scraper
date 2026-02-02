import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup

async def main():
    
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://example.com')
    await page.screenshot({'path': 'example.png'})
    await browser.close()
asyncio.get_event_loop().run_until_complete(main())