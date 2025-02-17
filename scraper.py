import requests as req
from bs4 import BeautifulSoup as bs
import json

url = "http://books.toscrape.com/"
def scrape_books(url):
    response = req.get(url)
    print(response)

    if response.status_code != 200:
        print("failed to fetch page")
        return

    response.encoding = response.apparent_encoding
    print(response.text)

    soup = bs(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    books_list = []
    for book in books:
        title = book.h3.a["title"]
        price_text = book.find("p", class_="price_color").text    
        currency = price_text[0]
        price = price_text[1:]

        # convert into list of dictionaries
        books_list.append({
            "title": title,
            "price": price,
            "currency": currency
        })
    return books_list
books = scrape_books(url)
print(books)
with open("books.json", "w") as f:
    json.dump(books, f, ensure_ascii=False)



