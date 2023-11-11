def import_csv_to_sqlite(csv_file_path, db_name, table_name):
    conn = sqlite3.connect(db_name)
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        columns = next(csv_reader)
        total_rows = sum(1 for _ in csv_reader)
    create_table_if_not_exists(conn, table_name, [f"{col} TEXT" for col in columns])
    update_interval = max(1, total_rows // 20)  # 5%
    with tqdm(total=total_rows, unit="row") as progress_bar:
        rows_inserted = 0
        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Omitir la primera fila
            cursor = conn.cursor()
            for row in csv_reader:
                placeholders = ', '.join(['?'] * len(row))
                cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", row)
                rows_inserted += 1
                if rows_inserted % update_interval == 0:
                    conn.commit()
                    rows_inserted = 0
                progress_bar.update(1)
        conn.commit()
    conn.close()
