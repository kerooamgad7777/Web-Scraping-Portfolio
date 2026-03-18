import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
response = requests.get(url, headers=headers)
print(f"status code: {response.status_code}")
soup= BeautifulSoup(response.text, "html.parser")
real_state_data = []
items = soup.find_all("div", class_="thumbnail")
for item in items:
    name= item.find("a", class_="title").text
    price= item.find("h4", class_="price").text
    description=item.find("p", class_="description").text

    relative_link = item.find("a", class_="title")["href"]
    full_link = f"https://webscraper.io{relative_link}"

    real_state_data.append({
        "property_name": name,
        "price": price,
        "description": description,
        "link": full_link
    })
df= pd.DataFrame(real_state_data)
df.to_excel("real_state_data.xlsx", index=False, engine='xlsxwriter')
print("done file saved")