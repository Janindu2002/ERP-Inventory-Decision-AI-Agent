import pandas as pd

def load_inventory_data(file_path):
    """
    Load inventory data from CSV file
    """

    try:
        data = pd.read_csv(file_path)
        return data

    except Exception as e:
        print("Error loading inventory data:", e)
        return None