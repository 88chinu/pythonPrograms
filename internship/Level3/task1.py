# Build a Web Scraper

import requests
from bs4 import BeautifulSoup

def fetchBooks():

    url = "https://books.toscrape.com/"

    limit = int(input("Enter number of books (1-10 at a time): "))
    limit = min(limit, 10)

    count = 0

    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    print("\n- Book List -\n")

    for book in books:

        if count >= limit:
            break

        title = book.find("h3").find("a")["title"]

        price = book.find("p", class_="price_color").text

        rating = book.find("p", class_="star-rating")["class"][1]

        availability = book.find("p", class_="availability").text.strip()

        print(f"Title  : {title}")
        print(f"Price  : {price}")
        print(f"Rating : {rating}")
        print(f"Stock  : {availability}")
        print("\n")

        count += 1

fetchBooks()