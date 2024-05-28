import sqlite3
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()
connection_string = os.getenv('CONNECTION_STRING')

def connect():
    try:
        connection = sqlite3.connect(connection_string)
        return connection
    except sqlite3.Error as error:
        print("Error connecting to sqlite: ", error)

def close(connection):
    try:
        connection.close()
    except sqlite3.Error as error:
        print("Error closing connection to sqlite: ", error)