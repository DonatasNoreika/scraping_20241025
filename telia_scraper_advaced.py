
from bs4 import BeautifulSoup
import requests
import csv


with open("telia_samsung_telefonai.csv", 'w', encoding="UTF-8", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Phone", "Price per Month", "Price"])

    page_num = 1

    while True:
        r = requests.get(f"https://www.telia.lt/prekes/telefonai-ir-priedai/mobilieji-telefonai/samsung?page={page_num}")
        page_num += 1

        soup = BeautifulSoup(r.text, 'html.parser')

        blocks = soup.find_all(class_='mobiles-product-card card card__product card--anim js-product-compare-product')

        if not blocks:
            print("No more pages")
            break

        for block in blocks:
            name = block.find(class_="mobiles-product-card__title js-open-product").get_text().strip()
            price_per_month = float(block.find_all(class_="mobiles-product-card__price-marker")[0].get_text().strip().split()[0].replace(",", "."))
            price = float(block.find_all(class_="mobiles-product-card__price-marker")[1].get_text().strip().rsplit(maxsplit=1)[0].replace("\xa0", ""))
            print(name)
            print(price_per_month)
            print(price)
            csv_writer.writerow([name, price_per_month, price])

