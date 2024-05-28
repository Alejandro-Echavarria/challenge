import os

def create(path):
    """
    Creates a directory if it does not already exist.

    :param path: The directory path to create.
    :return: None
    """
    try:
        # Check if the directory does not exist
        if not os.path.exists(path):
            # Create the directory
            os.makedirs(path)
    except Exception as e:
        print(f"An error occurred while creating the directory: {e}")