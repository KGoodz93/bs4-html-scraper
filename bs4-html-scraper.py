# Modules

from bs4 import BeautifulSoup
from requests_html import HTMLSession
import datetime

# Variables
dateformat1 = datetime.datetime.today().strftime("%Y%m%d")
file = f'data-{dateformat1}.txt'

# Script

url = input("Enter URL Here: ")

session = HTMLSession()
r = session.get(url).text
soup = BeautifulSoup(r, 'lxml')

# Scrape HTML and create a .txt file with the data

print(f'\nScraping data from {url}')

with open(f'{file}', 'w') as f:
    f.write(str(soup.prettify()))

print(f'\nProcess complete! File saved as: {file}')
input('\nPress any key to exit ..')
