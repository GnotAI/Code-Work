from bs4 import BeautifulSoup
import requests

url = "#"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
print(doc.prettify())