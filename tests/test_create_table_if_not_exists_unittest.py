
# Generated by CodiumAI

import unittest

class TestCreateTableIfNotExists(unittest.TestCase):

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
        self.assertIsNotNone(result)

    #  Commits the changes to the database after creating the table
    def test_commits_changes_to_database(self):
        # Arrange
        conn = sqlite3.connect(":memory:")
        table_name = "test_table"
        columns = ["id INTEGER", "name TEXT", "age INTEGER"]

        # Act
        create_table_if_not_exists(conn, table_name, columns)

        # Assert
        conn.close()
        conn = sqlite3.connect(":memory:")
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        result = cursor.fetchone()
        self.assertIsNone(result)

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
            self.fail(f"An exception occurred: {str(e)}")

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
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        result = cursor.fetchall()
        self.assertEqual(len(result), 0)

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
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        result = cursor.fetchall()
        self.assertEqual(len(result), 0)

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
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        result = cursor.fetchall()
        self.assertEqual(len(result), 0)
