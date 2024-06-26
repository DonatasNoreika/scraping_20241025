from bs4 import BeautifulSoup
import requests
import csv
from random import shuffle

r = requests.get("https://www.delfi.lt/")
titles = []
titles1 = []
titles2 = []

bad_words = ["Karas", "karas", "mirt", "rus", "apšaud"]

soup = BeautifulSoup(r.text, 'html.parser')
blocks = soup.find_all("article")

for block in blocks:
    try:
        title = block.find(class_='C-headline-title').a.get_text().strip()
        titles.append(title)
    except:
        pass

for title in titles:
    if ":" in title:
        if not any(word in title for word in bad_words):
            titles1.append(title.split(":", maxsplit=1)[0])
            titles2.append(title.split(":", maxsplit=1)[1])

shuffle(titles2)

for index in range(len(titles1)):
    print(f"{titles1[index]}:{titles2[index]}")