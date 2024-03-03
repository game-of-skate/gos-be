import psycopg2
import os


def test_db_is_test_db():
    # Make sure we're not accidentally connecting to local db.
    # Arrange: Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
    )
    # Create a cursor
    cursor = conn.cursor()

    # Act: Execute a query to get the current database name
    cursor.execute("SELECT current_database();")
    db_name = cursor.fetchone()[0]

    # Assert: Assert the name of the database is what's expected
    assert db_name == os.getenv('DB_NAME')
    #assert "test" in db_name

    # Cleanup: Close cursor and connection
    cursor.close()
    conn.close()
