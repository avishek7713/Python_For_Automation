import requests
from bs4 import BeautifulSoup

url = "https://www.goodreads.com/book/show/1137215.Boneshaker"

response = requests.get(url, headers={"Accept": "text/html"})

print(response)

parsed_response = BeautifulSoup(response.text, "html.parser")

print(parsed_response.prettify())