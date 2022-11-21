import time
import requests

import db_sqlite


RETRY_TIME = 3600
API_KEY = 'fee216a41d060649c620d933b6545eea'

most_populated_cities = ['Tokyo', 'Delhi', 'Shanghai', 'São Paulo',
                         'Mexico City', 'Cairo', 'Mumbai', 'Beijing',
                         'Dhaka', 'Osaka', 'New York', 'Karachi',
                         'Buenos Aires', 'Chongqing', 'Istanbul',
                         'Kolkata', 'Manila', 'Lagos', 'Rio de Janeiro',
                         'Tianjin', 'Kinshasa', 'Guangzhou', 'Los Angeles',
                         'Moscow', 'Shenzhen', 'Lahore', 'Bangalore', 'Paris',
                         'Bogotá', 'Jakarta', 'Chennai', 'Lima', 'Bangkok',
                         'Seoul', 'Nagoya', 'Hyderabad', 'London', 'Tehran',
                         'Chicago', 'Chengdu', 'Nanjing', 'Wuhan',
                         'Ho Chi Minh City', 'Luanda', 'Ahmedabad',
                         'Kuala Lumpur', 'Hong Kong', 'Dongguan', 'Foshan',
                         'Hangzhou']
unit_of_measure = ('metric', 'standard', 'imperial')


def get_weather_from_site(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}&units={unit_of_measure[0]}'
    r = requests.get(url)
    timestamp = int(time.time())
    weather_in_city = r.json()['main']
    if len(weather_in_city) > 6:
        del weather_in_city['sea_level']
        del weather_in_city['grnd_level']
    weather = (city,) + (timestamp,) + tuple(weather_in_city.values())
    return weather

def main():
    db_sqlite.connection
    db_sqlite.create_table
    while True:
        try:
            for city in most_populated_cities:
                db_sqlite.create_weather_in_city(get_weather_from_site(city))
            time.sleep(RETRY_TIME)
        except Exception as error:
            raise error('Сервер не отвечает или что-то пошло не так')


if __name__ == '__main__':
    main()