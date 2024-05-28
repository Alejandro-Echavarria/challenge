from .connection_sqlite3 import connect, close

def create_table(table_name):
    connection = connect()

    try:
        cursor = connection.cursor()
        create_table = f'''CREATE TABLE IF NOT EXISTS {table_name} (
            transaction_id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            purchase_date DATE,
            sale_amount INTEGER,
            product_category TEXT
        )'''

        cursor.execute(create_table)

        connection.commit()
    except Exception as e:
        print(f"An error occurred while creating the table: {e}")
    finally:
        # Close the database connection
        close(connection)