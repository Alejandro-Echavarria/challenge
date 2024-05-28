import pandas as pd
import os
import time
from dotenv import load_dotenv
from generation_data.sales import sales_months, generate_one
from database.operations import create_table, insert_data

# Load environment variables from the .env file
load_dotenv()
data_path = os.getenv('DATA_PATH')

def main():
    """
    Main function to execute the ETL process.
    """
    validate_excel_data()
    validate_table()
    etl()

def etl():
    """
    Extract, Transform, Load (ETL) process to handle sales data.
    """
    start_time = time.time()

    for key, params in sales_months.items():
        excel_file_path = os.path.join(data_path, f"{key}.{params['type']}")

        if not os.path.isfile(excel_file_path):
            print(f"File '{excel_file_path}' not found.")
            continue

        # 1. Extract
        data = extract(excel_file_path)

        # 2. Transform
        data = transform(data)

        # 3. Load
        load(data)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.2f} seconds")

def extract(excel_file_path):
    """
    Extract data from a CSV file.
    
    :param excel_file_path: Path to the CSV file.
    :return: Data as a list of lists.
    """
    try:
        df = pd.read_csv(excel_file_path, delimiter=';')
        data = df.values.tolist()

        return data
    except Exception as e:
        print(f"An error occurred while extracting the data: {e}")

def transform(data):
    """
    Transform the data by multiplying the sale_amount by 100 and converting to integer.
    
    :param data: Data to be transformed.
    :return: Transformed data.
    """
    try:
        for row in data:
            row[3] = int(row[3] * 100)

        return data
    except Exception as e:
        print(f"An error occurred while transforming the data: {e}")

def load(data):
    """
    Load the data into the 'sales' table.
    
    :param data: Data to be inserted into the database.
    """
    try:
        insert_data('sales', data)
    except Exception as e:
        print(f"An error occurred while inserting the data: {e}")

def validate_table():
    """
    Validate or create the 'sales' table in the database.
    """
    try:
        create_table('sales')
    except Exception as e:
        print(f"An error occurred while validating the table: {e}")

def validate_excel_data():
    """
    Validate the presence of Excel files and generate missing ones.
    """
    try:
        for key, params in sales_months.items():
            excel_file_path = os.path.join(data_path, f"{key}.{params['type']}")

            if not os.path.isfile(excel_file_path):
                generate_one(key)
    except Exception as e:
        print(f"An error occurred while validating the excel data: {e}")

if __name__ == "__main__":
    main()