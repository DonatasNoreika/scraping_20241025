
import requests
from bs4 import BeautifulSoup
import pickle

quotes = []

url = "https://quotes.toscrape.com/"

page = 1

while True:
    r = requests.get(f"{url}page/{page}/")
    page += 1
    soup = BeautifulSoup(r.text, 'html.parser')


    blocks = soup.find_all(class_="quote")

    if len(blocks) < 1:
        break

    for block in blocks:
        quote = block.find(class_="text").get_text().strip()
        author = block.find(class_="author").get_text().strip()
        author_href = block.find("a")['href']

        author_r = requests.get(url + author_href)
        author_soup = BeautifulSoup(author_r.text, 'html.parser')
        author_born = author_soup.find(class_="author-details").p.get_text().strip()
        quote_dict = {
            "quote": quote,
            "author": author,
            "author_born": author_born,
        }
        quotes.append(quote_dict)
        print(quote)
        print(author)
        print(author_born)
        print("--------------------------------------------------------")

print(quotes)
with open("quotes.pkl", 'wb') as file:
    pickle.dump(quotes, file)
