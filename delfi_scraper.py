from bs4 import BeautifulSoup
import requests
import csv

r = requests.get("https://www.delfi.lt/")

with open("delfi_naujienos.csv", 'w', encoding="UTF-8", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Category", "Title", "Link"])

    soup = BeautifulSoup(r.text, 'html.parser')
    blocks = soup.find_all("article")
    for block in blocks:
        try:
            try:
                category = block.find(class_='C-headline-labels__label').get_text().strip()
            except:
                category = ""

            title = block.find(class_='C-headline-title').a.get_text().strip()
            link = "https://www.delfi.lt" + block.find(class_='C-headline-title').a['href']
            csv_writer.writerow([category, title, link])
        except:
            pass