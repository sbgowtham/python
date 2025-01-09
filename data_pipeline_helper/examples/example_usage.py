# Import functions from the data_pipeline_helper package
from data_pipeline_helper import remove_null_values, load_csv_to_dataframe, build_select_query

# Example 1: Load data and clean it
print("Example 1: Data Cleaning")
file_path = "sample_data.csv"
df = load_csv_to_dataframe(file_path)
print("Original DataFrame:")
print(df)

cleaned_df = remove_null_values(df, ['column1'])
print("\nDataFrame after removing null values:")
print(cleaned_df)

# Example 2: Build a SQL query
print("\nExample 2: SQL Query Builder")
query = build_select_query("my_table", ["column1", "column2"], "column1 > 10")
print("Generated SQL Query:")
print(query)
