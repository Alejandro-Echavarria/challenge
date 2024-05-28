from .create_directory import create as create_directory

def create_file(df, name, path, type, sep = ','):
    """
    Creates a file from the given DataFrame and saves it in the specified format and path.

    :param df: DataFrame to be saved as a file.
    :param name: Name of the file to be created.
    :param path: Directory path where the file will be saved.
    :param type: Type of file to be created ('csv' or 'xlsx').
    :param sep: Separator to be used if the file type is 'csv'. Default is ','.
    :return: None
    """
    try:
        # Ensure the target directory exists or create it
        create_directory(f'data/{path}')

        # Save the DataFrame as a CSV file
        if type == 'csv':
            return df.to_csv(f'data/{path}/{name}.csv', sep = sep, index = False)

        # Save the DataFrame as an Excel file
        if type == 'xlsx':
            return df.to_excel(f'data/{path}/{name}.xlsx', index = False)

        # Raise an error if the file type is not supported
        raise NotImplementedError(f"File type '{type}' is not supported yet. Only 'xlsx' is implemented.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")
        return None
