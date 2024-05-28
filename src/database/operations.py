from .connection_sqlite3 import connect, close

def create_table(table_name):
    """
    Creates a table in the SQLite database if it does not already exist.

    :param table_name: The name of the table to create.
    :return: None
    """
    connection = connect() # Establish database connection

    try:
        cursor = connection.cursor()
        # SQL statement to create table if it doesn't exist
        create_table = f'''CREATE TABLE IF NOT EXISTS {table_name} (
            transaction_id INTEGER,
            customer_id INTEGER,
            purchase_date DATE,
            sale_amount INTEGER,
            product_category TEXT
        )'''

        cursor.execute(create_table) # Execute the SQL statement

        connection.commit() # Commit the transaction
    except Exception as e:
        # Print an error message if an exception occurs
        print(f"An error occurred while creating the table: {e}")
    finally:
        # Close the database connection
        close(connection)

def insert_data(table_name, data):
    """
    Inserts data into the specified table in the SQLite database.

    :param table_name: The name of the table where data will be inserted.
    :param data: A list of tuples containing the data to be inserted.
    :return: None
    """
    connection = connect() # Establish database connection

    try:
        cursor = connection.cursor()
        # SQL statement to insert data into the table
        insert_data = f'''INSERT INTO {table_name} VALUES (?, ?, ?, ?, ?)'''
        cursor.executemany(insert_data, data) # Execute the SQL statement with multiple rows of data

        connection.commit() # Commit the transaction
    except Exception as e:
        # Print an error message if an exception occurs
        print(f"An error occurred while inserting the data: {e}")
    finally:
        # Close the database connection
        close(connection)