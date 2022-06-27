# Modules

from bs4 import BeautifulSoup
from requests_html import HTMLSession
from datetime import datetime

# Variables

dateformat1 = datetime.today().strftime("%Y%m%d")

# Script

url = input("Enter URL Here: ")

session = HTMLSession()
r = session.get(url).text
soup = BeautifulSoup(r, 'lxml')

# Scrape HTML and create a .txt file with the data

print(f'\nGenerating data from {url}')

with open(f'data-{dateformat1}.txt', 'w') as f:
    f.write(str(soup.prettify()))

print('Script Complete!')
input('\nPress any key to exit ..')
