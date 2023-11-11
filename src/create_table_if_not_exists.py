def create_table_if_not_exists(conn, table_name, columns):
    cursor = conn.cursor()
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)});")
    conn.commit()
