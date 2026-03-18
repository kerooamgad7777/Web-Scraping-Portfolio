import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "http://quotes.toscrape.com/"
response = requests.get(url)
print(f"status code: {response.status_code}")
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")
all_data = []
print(f"Found {len(quotes)} quotes on the page.")
for i in range(len(quotes)):
    all_data.append({
        "quote": quotes[i].text,
        "author": authors[i].text
    })
    
df = pd.DataFrame(all_data)
df.to_excel("Quotes_with_Authors.xlsx", index=False)
print("done file saved")
