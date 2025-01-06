import requests

# define base url
base_url = "https://api.upcitemdb.com/prod/trial/lookup"

#define parameters
parameters = {"upc": "025000044908"}

#make api request, passing in the base url and parameters
response = requests.get(base_url, params= parameters)

#print out the response
print(response.url)