import pandas as pd

def remove_null_values(df, columns):
    """Removes rows with null values from specified columns."""
    return df.dropna(subset=columns)

def remove_duplicates(df, subset=None):
    """Removes duplicate rows from the DataFrame."""
    return df.drop_duplicates(subset=subset)
