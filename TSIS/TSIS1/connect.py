import psycopg2
from config import *

def connect():
    try:
        connection = psycopg2.connect(
            dbname = "diasmamyrbaev",
            user = "postgres",
            password = "Admin",
            host = "localhost",
            port = "5432"
        )
        return connection 
    except Exception as error:
        print("Connection error:", error)
