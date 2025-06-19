import requests
from Weth_API_key import API_token

params = {'q': 'Moscow', 'appid': API_token, 'units': 'metric'}

response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)

print(response.json()['weather'][0]['main'])
