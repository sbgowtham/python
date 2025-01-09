import pandas as pd
from data_pipeline_helper.cleaning import remove_null_values, remove_duplicates

def test_remove_null_values():
    data = {'col1': [1, None, 3], 'col2': [4, 5, None]}
    df = pd.DataFrame(data)
    result = remove_null_values(df, ['col1'])
    assert len(result) == 2

def test_remove_duplicates():
    data = {'col1': [1, 2, 2], 'col2': [3, 4, 4]}
    df = pd.DataFrame(data)
    result = remove_duplicates(df)
    assert len(result) == 2
