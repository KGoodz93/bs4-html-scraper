# Modules

from bs4 import BeautifulSoup
import requests
import sys

# Variables

path = r"../logs/"

# Webpage URL

url = input("Enter URL Here: ")

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
print(doc)

print(f"\nHTML has now been scrapped from {url}")

# Write HTML to notepad

file = open(f"{path}newfile.txt", "a")
file.write(str(doc))
file.close()

print(f"Log file has been created - {path}")

input("Press any Key to exit .. ")
sys.exit()