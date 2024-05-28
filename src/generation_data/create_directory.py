import os

def create(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except Exception as e:
        print(f"An error occurred while creating the directory: {e}")