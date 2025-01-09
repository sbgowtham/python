from data_pipeline_helper.sql_builder import build_select_query, build_insert_query

def test_build_select_query():
    query = build_select_query("my_table", ["col1", "col2"], "col1 > 10")
    assert query == "SELECT col1, col2 FROM my_table WHERE col1 > 10"

def test_build_insert_query():
    query = build_insert_query("my_table", ["col1", "col2"], [1, 2])
    assert query == "INSERT INTO my_table (col1, col2) VALUES (1, 2)"
