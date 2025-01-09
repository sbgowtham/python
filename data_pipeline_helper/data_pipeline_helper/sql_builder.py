def build_select_query(table, columns, where_clause=None):
    """Generates a SELECT SQL query."""
    query = f"SELECT {', '.join(columns)} FROM {table}"
    if where_clause:
        query += f" WHERE {where_clause}"
    return query

def build_insert_query(table, columns, values):
    """Generates an INSERT SQL query."""
    columns_str = f"({', '.join(columns)})"
    values_str = f"({', '.join(map(str, values))})"
    query = f"INSERT INTO {table} {columns_str} VALUES {values_str}"
    return query
