import sqlite3
from sqlite3 import Error


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


connection = create_connection("db.sqlite")


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


create_weather_table = """
CREATE TABLE IF NOT EXISTS weather (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  city TEXT NOT NULL,
  joiningDate timestamp,
  temp DECIMAL,
  feels_like DECIMAL,
  temp_min DECIMAL,
  temp_max DECIMAL,
  pressure DECIMAL,
  humidity DECIMAL
)
"""

create_table = execute_query(connection, create_weather_table)

def create_weather_in_city(weather):
    print(weather)
    create_weather = f"""
    INSERT INTO weather (city, joiningDate, temp, feels_like, temp_min, temp_max, pressure, humidity)
     VALUES
    {weather}
    """
    execute_query(connection, create_weather)