import os

def create_file(df, name, path, type, sep = ','):
    try:
        if not os.path.exists(f'data/{path}'):
            os.makedirs(f'data/{path}')

        if type == 'csv':
            return df.to_csv(f'data/{path}/{name}.csv', sep = sep, index = False)

        if type == 'xlsx':
            return df.to_excel(f'data/{path}/{name}.xlsx', index = False)

        raise NotImplementedError(f"File type '{type}' is not supported yet. Only 'xlsx' is implemented.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")
        return None
