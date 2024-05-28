import sqlite3
import os
from generation_data.create_directory import create as create_directory
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()
db_path = os.getenv('DB_PATH')
connection_string = os.getenv('CONNECTION_STRING')

def connect():
    """
    Establishes a connection to the SQLite database and ensures the database directory exists.

    :return: SQLite connection object if successful, None otherwise.
    """
    try:
        # Ensure the database directory exists
        create_directory(db_path)

        # Establish the database connection
        connection = sqlite3.connect(connection_string)
        return connection
    except sqlite3.Error as error:
        # Print an error message if an exception occurs
        print("Error connecting to sqlite: ", error)
        return None

def close(connection):
    """
    Closes the connection to the SQLite database.

    :param connection: The SQLite connection object to be closed.
    :return: None
    """
    try:
        # Close the database connection
        connection.close()
    except sqlite3.Error as error:
        # Print an error message if an exception occurs
        print("Error closing connection to sqlite: ", error)