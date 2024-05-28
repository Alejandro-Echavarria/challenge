from generate_sales_data import generate_sales_data
from create_file import create_file

# Data of sales per month ( January, February, March )
sales_months = {
    "df_january": {
        "month": 1,
        "year": 2024,
        "number_records": 3599
    },
    "df_february": {
        "month": 2,
        "year": 2024,
        "number_records": 1000
    },
    "df_march": {
        "month": 5,
        "year": 2024,
        "number_records": 5693
    },
}

for filename, params in sales_months.items():
    try:
        df = generate_sales_data(
            params["month"],
            params["year"],
            params["number_records"]
        )

        create_file(df = df, name = filename, path = 'excel', type = 'csv', sep = ';')
    except Exception as e:
        print(f"An error occurred while creating sales: {e}")

