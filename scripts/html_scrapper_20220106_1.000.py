# Modules

from bs4 import BeautifulSoup
import requests
import os
import datetime

# Variables

user = os.getlogin()
path = fr"C:\Users\{user}\Dropbox\Coding\Git\HTML-scrapper\logs"
url = input("Enter URL Here: ")
dt = datetime.datetime.today().strftime("%Y%m%d_%H%M%S")
filename = f"WS_{dt}.txt"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
print(doc)

print("\n---")
print(f"\nHTML has been scrapped from: {url}")

# Write HTML to notepad

file = open(rf"{path}\{filename}", "a")
file.write(str(doc.encode("utf-8")))
file.close()

print(f"\nOutpit file has been created - {path}")

input("\nPress any key to exit .. ")