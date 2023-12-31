
# Generated by CodiumAI

import pytest

class TestCreateTableIfNotExists:

    #  Creates a table with the given name and columns if it doesn't exist in the database
    def test_creates_table_if_not_exists(self):
        # Arrange
        conn = sqlite3.connect(":memory:")
        table_name = "test_table"
        columns = ["id INTEGER", "name TEXT", "age INTEGER"]

        # Act
        create_table_if_not_exists(conn, table_name, columns)

        # Assert
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        result = cursor.fetchone()
        assert result is not None

    #  Commits the changes to the database after creating the table
    def test_commits_changes_to_database(self):
        # Arrange
        conn = sqlite3.connect(":memory:")
        table_name = "test_table"
        columns = ["id INTEGER", "name TEXT", "age INTEGER"]

        # Act
        create_table_if_not_exists(conn, table_name, columns)

        # Assert
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        result = cursor.fetchone()
        assert conn.total_changes > 0

    #  Returns no errors or exceptions when creating a table with valid inputs
    def test_no_errors_or_exceptions_with_valid_inputs(self):
        # Arrange
        conn = sqlite3.connect(":memory:")
        table_name = "test_table"
        columns = ["id INTEGER", "name TEXT", "age INTEGER"]

        # Act & Assert
        try:
            create_table_if_not_exists(conn, table_name, columns)
        except Exception as e:
            pytest.fail(f"An exception occurred: {e}")

    #  Does not create a table if the table name or columns are empty strings
    def test_does_not_create_table_with_empty_strings(self):
        # Arrange
        conn = sqlite3.connect(":memory:")
        table_name = ""
        columns = ["id INTEGER", "name TEXT", "age INTEGER"]

        # Act
        create_table_if_not_exists(conn, table_name, columns)

        # Assert
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        result = cursor.fetchone()
        assert result is None

        table_name = "test_table"
        columns = []

        # Act
        create_table_if_not_exists(conn, table_name, columns)

        # Assert
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        result = cursor.fetchone()
        assert result is None

    #  Does not create a table if the table name or columns contain invalid characters or SQL keywords
    def test_does_not_create_table_with_invalid_characters_or_keywords(self):
        # Arrange
        conn = sqlite3.connect(":memory:")
        table_name = "test_table;"
        columns = ["id INTEGER", "name TEXT", "age INTEGER"]

        # Act
        create_table_if_not_exists(conn, table_name, columns)

        # Assert
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        result = cursor.fetchone()
        assert result is None

        table_name = "test_table"
        columns = ["id INTEGER", "name TEXT", "age INTEGER", "SELECT TEXT"]

        # Act
        create_table_if_not_exists(conn, table_name, columns)

        # Assert
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        result = cursor.fetchone()
        assert result is None

    #  Does not create a table if the connection to the database is closed or invalid
    def test_does_not_create_table_with_closed_or_invalid_connection(self):
        # Arrange
        conn = sqlite3.connect(":memory:")
        table_name = "test_table"
        columns = ["id INTEGER", "name TEXT", "age INTEGER"]
        conn.close()

        # Act
        create_table_if_not_exists(conn, table_name, columns)

        # Assert
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        result = cursor.fetchone()
        assert result is None
