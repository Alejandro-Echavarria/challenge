import pandas as pd
import random as rd
from datetime import datetime, timedelta

# Se debe instalar pip, pandas, openpyxl
def generate_sales_data(month, year, number_records):
    try:
        if not 1 <= month <= 12:
            raise ValueError(f"Month '{month}' is not valid. It must be between 1 and 12.")

        start_date = datetime(year, month, 1)

        if month == 12:
            end_date = datetime(year + 1, 1, 1)
        else:
            end_date = datetime(year, month + 1, 1)

        data = []

        for _ in range(number_records):
            transaction_id = rd.randint(1000, 9999)
            customer_id = rd.randint(100, 999)
            purchase_date = random_date(start_date, end_date)
            sale_amount = round(rd.uniform(10.0, 1000.0), 2)
            product_category = rd.choice(['Electronics', 'Clothing', 'Groceries', 'Furniture'])

            data.append([transaction_id, customer_id, purchase_date, sale_amount, product_category])

        df = pd.DataFrame(data, columns=['transaction_id', 'customer_id', 'purchase_date', 'sale_amount', 'product_category'])
        return df

    except Exception as e:
        print(f"An error occurred while generating sales data: {e}")
        return None

# Función para generar una fecha aleatoria en un mes específico
def random_date(start, end):
    return start + timedelta(
        seconds = rd.randint(0, int((end - start).total_seconds()))
    )
