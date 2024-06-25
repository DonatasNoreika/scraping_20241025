
from bs4 import BeautifulSoup
import requests
import csv

r = requests.get("https://www.telia.lt/prekes/telefonai-ir-priedai/mobilieji-telefonai/apple")

soup = BeautifulSoup(r.text, 'html.parser')

blocks = soup.find_all(class_='mobiles-product-card card card__product card--anim js-product-compare-product')

with open("telia_apple_telefonai.csv", 'w', encoding="UTF-8", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Phone", "Price per Month", "Price"])

    for block in blocks:
        name = block.find(class_="mobiles-product-card__title js-open-product").get_text().strip()
        price_per_month = block.find_all(class_="mobiles-product-card__price-marker")[0].get_text().strip()
        price = block.find_all(class_="mobiles-product-card__price-marker")[1].get_text().strip()
        print(name)
        print(price_per_month)
        print(price)
        csv_writer.writerow([name, price_per_month, price])