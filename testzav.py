import requests
from pprint import pprint

most_populated_cities = ['Tokyo', 'Delhi', 'Shanghai']
unit_of_measure = ('metric', 'standard', 'imperial')
API_KEY = 'fee216a41d060649c620d933b6545eea'
CITY = most_populated_cities[0]


url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&APPID={API_KEY}&units={unit_of_measure[0]}'


r = requests.get(url)
weather_in_city = r.json()['main']
print(f'Погода в {CITY} {weather_in_city}')


def get_weather_from_site():
    pass


def start_db():
    pass


def get_api_weather():
    pass


def add_weather_in_city_to_db():
    pass
