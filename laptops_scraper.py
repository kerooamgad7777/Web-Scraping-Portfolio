import requests
from bs4 import BeautifulSoup
import pandas as pd
url = " https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
response = requests.get(url)
print(f"status code: {response.status_code}")
soup = BeautifulSoup(response.text, "html.parser")
all_laptops = soup.find_all("div", class_="caption")
laptops_data = []
print(f"Found {len(all_laptops)} laptops on the page.")
for laptop in all_laptops:
    name = laptop.find("a", class_="title").text
    price = laptop.find("h4", class_="price").text
    description = laptop.find("p", class_="description").text
    laptops_data.append({
        "name": name,
        "price": price,
        "description": description
    })

df = pd.DataFrame(laptops_data)
df.to_excel("Laptops_data.xlsx", index=False)
print("done file saved")
