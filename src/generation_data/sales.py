from .generate_sales_data import generate_sales_data
from .create_file import create_file

# Data of sales per month ( January, February, March )
# Dictionary containing sales data parameters for each month
sales_months = {
    "df_january": {
        "month": 1, # Month number
        "year": 2024, # Year
        "number_records": 33599, # Number of records to generate
        "type": "csv", # File type
    },
    "df_february": {
        "month": 2,
        "year": 2024,
        "number_records": 11000,
        "type": "csv",
    },
    "df_march": {
        "month": 3,
        "year": 2024,
        "number_records": 55693,
        "type": "csv",
    },
}

def generate_one(month_miss):
    """
    Generates sales data for a specific month if it is missing and creates a corresponding file.
    
    :param month_miss: The key for the month to generate sales data for.
    """
    try:
        # Get the parameters for the specified month
        params = sales_months[month_miss]

        # Generate the sales data using the parameters
        df = generate_sales_data(
                params["month"],
                params["year"],
                params["number_records"]
            )

        # Create a file with the generated sales data
        create_file(df = df, name = month_miss, path = 'excel', type = params['type'], sep = ';')
    except KeyError:
        print(f"Month {month_miss} not found in sales_months")
    except Exception as e:
        print(f"An error occurred while creating sales: {e}")

def generate_sales():
    """
    Generates sales data for all months defined in the sales_months dictionary and creates corresponding files.
    """
    for filename, params in sales_months.items():
        try:
            # Generate the sales data using the parameters for each month
            df = generate_sales_data(
                params["month"],
                params["year"],
                params["number_records"]
            )

            # Create a file with the generated sales data
            create_file(df = df, name = filename, path = 'excel', type = params['type'], sep = ';')
        except Exception as e:
            print(f"An error occurred while creating sales: {e}")
