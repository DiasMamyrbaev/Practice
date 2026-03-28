import psycopg2
from config import get_config

def get_connection():
    params = get_config()
    try:
        conn = psycopg2.connect(**params)
        return conn
    except psycopg2.DatabaseError as error:
        print(f"Ошибка подключения к базе данных: {error}")
        return None

