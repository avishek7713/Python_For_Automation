import requests
import json

# EXAMPLE 1 - lemonade with raspberry
print("\nPRODUCT EXAMPLE 1\n")

# define base url
base_url = "https://api.upcitemdb.com/prod/trial/lookup"

#define parameters
parameters = {"upc": "028400516686"}

#make api request, passing in the base url and parameters
response = requests.get(base_url, params= parameters)

# parse the text from the api response using JSON schema
info = json.loads(response.text)

#extract the first item using index 0
item = info["items"][0]

#extract the product's title by indexing item
title = item["title"]

#extract the product's brand by indexing item
brand = item["brand"]

print("Title: ", title)
print("Brand: ", brand)