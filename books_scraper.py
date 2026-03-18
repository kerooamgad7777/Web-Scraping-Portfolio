import requests
from bs4 import BeautifulSoup
import pandas as pd

all_books = []

for page in range(1,4):
    url = f"http://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    for book in books:
        title = book.find("h3").find("a")["title"]
        price = book.find("p", class_="price_color").text
        all_books.append({"title": title, "price": price})

df = pd.DataFrame(all_books)
df.to_excel("Books_data.xlsx", index=False)
print("done file saved")