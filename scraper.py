from bs4 import BeautifulSoup
import requests
import pandas as pd

result = pd.read_html('https://youtube.com/')
print(result)
