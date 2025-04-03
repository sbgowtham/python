import pandas as pd

# Load data
df = pd.read_csv('orders.csv')

# Find duplicate rows
duplicates = df[df.duplicated(keep=False)]

# Show duplicates
print("Duplicate Rows:")
print(duplicates)
