import time
import requests

import db_sqlite


RETRY_TIME = 10
API_KEY = 'fee216a41d060649c620d933b6545eea'
most_populated_cities = ['Tokyo', 'Delhi', 'Shanghai', 'São Paulo', 'Mexico City', 'Cairo',
'Mumbai', 'Beijing', 'Dhaka', 'Osaka', 'New York', 'Karachi', 'Buenos Aires', 'Chongqing', 'Istanbul',
'Kolkata', 'Manila', 'Lagos', 'Rio de Janeiro', 'Tianjin', 'Kinshasa', 'Guangzhou', 'Los Angeles', 'Moscow',
'Shenzhen', 'Lahore', 'Bangalore', 'Paris', 'Bogotá', 'Jakarta', 'Chennai', 'Lima', 'Bangkok', 'Seoul', 'Nagoya',
'Hyderabad', 'London', 'Tehran', 'Chicago', 'Chengdu', 'Nanjing', 'Wuhan', 'Ho Chi Minh City', 'Luanda', 'Ahmedabad',
'Kuala Lumpur', 'Hong Kong', 'Dongguan', 'Foshan', 'Hangzhou']
unit_of_measure = ('metric', 'standard', 'imperial')



def get_weather_from_site(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}&units={unit_of_measure[0]}'
    r = requests.get(url)
    timestamp = int(time.time())
    weather_in_city = r.json()['main']
    if len(weather_in_city) > 6:
        del weather_in_city['sea_level']
        del weather_in_city['grnd_level']
    weather = (city,) + tuple(weather_in_city.values())
    return weather

def main():
    db_sqlite.connection
    db_sqlite.create_table
    weather_in_cities = []
    for city in most_populated_cities:
        weather_in_cities.append(get_weather_from_site(city))
        db_sqlite.add_weather_in_city_to_db(weather_in_cities)
    # time.sleep(RETRY_TIME)


if __name__ == '__main__':
    main()

# def main(cities):
#     db.connection
#     db.create_table
#     weather_in_cities = []
#     for city in cities:
#         weather_in_cities.append(get_weather_from_site(city))
#         # db.add_weather_in_city_to_db(weather_in_cities)
#     print(weather_in_cities)
# main(most_populated_cities)

# ('Beijing', 2.94, 0.88, 2.94, 2.94, 1024, 72, 1024, 1018)
#  ('Mumbai', 22.99, 22.26, 22.99, 22.99, 1010, 35)