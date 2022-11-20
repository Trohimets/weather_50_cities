import requests
import db

most_populated_cities = ['Tokyo', 'Delhi', 'Shanghai', 'São Paulo', 'Mexico City', 'Cairo',
'Mumbai', 'Beijing', 'Dhaka', 'Osaka', 'New York', 'Karachi', 'Buenos Aires', 'Chongqing', 'Istanbul',
'Kolkata', 'Manila', 'Lagos', 'Rio de Janeiro', 'Tianjin', 'Kinshasa', 'Guangzhou', 'Los Angeles', 'Moscow',
'Shenzhen', 'Lahore', 'Bangalore', 'Paris', 'Bogotá', 'Jakarta', 'Chennai', 'Lima', 'Bangkok', 'Seoul', 'Nagoya',
'Hyderabad', 'London', 'Tehran', 'Chicago', 'Chengdu', 'Nanjing', 'Wuhan', 'Ho Chi Minh City', 'Luanda', 'Ahmedabad',
'Kuala Lumpur', 'Hong Kong', 'Dongguan', 'Foshan', 'Hangzhou']
unit_of_measure = ('metric', 'standard', 'imperial')
API_KEY = 'fee216a41d060649c620d933b6545eea'



def get_weather_from_site(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}&units={unit_of_measure[0]}'
    r = requests.get(url)
    weather_in_city = r.json()['main'] # {'temp': 14.72, 'feels_like': 13.97, 'temp_min': 11.14, 'temp_max': 17.53, 'pressure': 1024, 'humidity': 66}
    weather = (city,) + tuple(weather_in_city.values())
    return weather


def main(cities):
    db.connection
    db.create_table
    weather_in_cities = []
    for city in cities:
        weather_in_cities.append(get_weather_from_site(city))
        # db.add_weather_in_city_to_db(weather_in_cities)
    print(weather_in_cities)
main(most_populated_cities)

('Beijing', 2.94, 0.88, 2.94, 2.94, 1024, 72, 1024, 1018)
 ('Mumbai', 22.99, 22.26, 22.99, 22.99, 1010, 35)