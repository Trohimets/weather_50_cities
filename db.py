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
  temp DECIMAL,
  feels_like DECIMAL,
  temp_min DECIMAL,
  temp_max DECIMAL,
  pressure DECIMAL,
  humidity DECIMAL
)
"""

execute_query(connection, create_weather_table)


def add_weather_in_city_to_db(weather):
    post_weather = ", ".join(["%s"] * len(weather))
    insert_query = (
    f"INSERT INTO weather_table (title, description, user_id) VALUES {post_records}")

connection.autocommit = True
cursor = connection.cursor()
# cursor.execute(insert_query, posts)