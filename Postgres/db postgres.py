import psycopg2

from psycopg2 import OperationalError


def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


connection = create_connection(
    "postgres", "postgres", "1235813", "127.0.0.1", "5432"
)

def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


create_weather_table = """
CREATE TABLE IF NOT EXISTS weather (
  id SERIAL PRIMARY KEY,
  city TEXT NOT NULL,
  date time with time zone DEFAULT CURRENT_TIME,
  temp DECIMAL,
  feels_like DECIMAL,
  temp_min DECIMAL,
  temp_max DECIMAL,
  pressure DECIMAL,
  humidity DECIMAL
)
"""

create_table = execute_query(connection, create_weather_table)


def add_weather_in_city_to_db(weather):
    post_weather = ", ".join(["%s"] * len(weather))
    insert_query = (
    f"INSERT INTO weather (city, temp, feels_like, temp_min, temp_max, pressure, humidity) VALUES {post_weather}")
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute(insert_query, weather)

# Для проверки данных в БД можно воспользоваться кодом ниже

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")


select_cities = "SELECT * FROM weather"
cities = execute_read_query(connection, select_cities)
for city in cities:
    print(city)

# delete_all = "DELETE FROM weather"
# delete = execute_query(connection, delete_all)

