import sqlite3

# A more organized way to handle database connections is to use a context manager
# This ensures that the connection is properly closed after use
def get_db_connection(db_path='yt_manager.db'):
    return sqlite3.connect(db_path)

with get_db_connection() as connection:
    cursor = connection.cursor()
    # execute queries here
