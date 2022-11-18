import requests
import db

most_populated_cities = ['Tokyo', 'Delhi', 'Shanghai']
unit_of_measure = ('metric', 'standard', 'imperial')
API_KEY = 'fee216a41d060649c620d933b6545eea'



def get_weather_from_site(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}&units={unit_of_measure[0]}'
    r = requests.get(url)
    weather_in_city = r.json()['main'] # {'temp': 14.72, 'feels_like': 13.97, 'temp_min': 11.14, 'temp_max': 17.53, 'pressure': 1024, 'humidity': 66}
    weather = (city,) + tuple(weather_in_city.values())
    return weather


def start_db():
    pass


def main(cities):
    db.connection
    weather_in_cities = []
    for city in cities:
        weather_in_cities.append(get_weather_from_site(city))
    print(weather_in_cities)

main(most_populated_cities)