import requests

#defining the base url
base_url = "http://api.openweathermap.org/data/2.5/forecast"

#define parameters
parameters = {"q": "Paris, FR", "appid": "6654b4226dc9a11a9b7ea7112f8c6af7"}

#make api request, parsing in the base url and parameters
response = requests.get(base_url, params= parameters)

print(response.text)