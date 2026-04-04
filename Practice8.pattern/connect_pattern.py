import psycopg2
from config_pattern import *

def connect():
    try:
        connection = psycopg2.connect(
            dbname="Students",
            user="postgres",
            password="Admin",
            host="localhost",
            port="5432"
        )
        return connection
    except Exception as e:
        print("Connection error:", e)
        return None