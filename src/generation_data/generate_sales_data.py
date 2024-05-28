import pandas as pd
import random as rd
from datetime import datetime, timedelta

def generate_sales_data(month, year, number_records):
    """
    Generates a DataFrame containing sales data for a given month, year, and number of records.

    :param month: The month for which to generate sales data (1-12).
    :param year: The year for which to generate sales data.
    :param number_records: The number of sales records to generate.
    :return: A DataFrame containing the generated sales data.
    """
    try:
        # Check if the month is valid
        if not 1 <= month <= 12:
            raise ValueError(f"Month '{month}' is not valid. It must be between 1 and 12.")

        # Define the start date as the first day of the given month and year
        start_date = datetime(year, month, 1)

        # Define the end date as the first day of the next month
        if month == 12:
            end_date = datetime(year + 1, 1, 1)
        else:
            end_date = datetime(year, month + 1, 1)

        data = []

        # Generate the specified number of sales records
        for _ in range(number_records):
            transaction_id = rd.randint(1000, 9999)
            customer_id = rd.randint(100, 999)
            purchase_date = random_date(start_date, end_date)
            sale_amount = round(rd.uniform(10.0, 1000.0), 2)
            product_category = rd.choice(['Alpha FWD', 'Alpha Plus', 'Alpha Margen', 'Alpha Mutuo'])

            data.append([transaction_id, customer_id, purchase_date, sale_amount, product_category])

        # Create a DataFrame from the generated data
        df = pd.DataFrame(data, columns=['transaction_id', 'customer_id', 'purchase_date', 'sale_amount', 'product_category'])
        return df

    except Exception as e:
        print(f"An error occurred while generating sales data: {e}")
        return None

def random_date(start, end):
    """
    Generates a random date between the start and end dates.

    :param start: The start date.
    :param end: The end date.
    :return: A randomly generated date between start and end.
    """
    return start + timedelta(
        seconds = rd.randint(0, int((end - start).total_seconds()))
    )
