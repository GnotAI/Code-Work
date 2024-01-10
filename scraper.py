import pandas as pd

url = input("Enter the url: ")

result = pd.read_html(url)
print(result)

