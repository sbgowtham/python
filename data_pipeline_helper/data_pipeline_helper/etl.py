import pandas as pd

def load_csv_to_dataframe(file_path):
    """Loads a CSV file into a Pandas DataFrame."""
    return pd.read_csv(file_path)

def save_dataframe_to_csv(df, file_path, index=False):
    """Saves a DataFrame to a CSV file."""
    df.to_csv(file_path, index=index)
