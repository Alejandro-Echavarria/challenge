import sqlite3
import os
from generation_data.create_directory import create as create_directory
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()
db_path = os.getenv('DB_PATH')
connection_string = os.getenv('CONNECTION_STRING')

def connect():
    try:
        create_directory(db_path)

        connection = sqlite3.connect(connection_string)
        return connection
    except sqlite3.Error as error:
        print("Error connecting to sqlite: ", error)

def close(connection):
    try:
        connection.close()
    except sqlite3.Error as error:
        print("Error closing connection to sqlite: ", error)