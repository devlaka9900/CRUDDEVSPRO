import sqlite3
from contextlib import contextmanager

import config

def get_connection(db_path=None):
    """Open a new SQLite connection. Rows behave like dicts (row["title"])."""
    conn = sqlite3.connect(db_path or config.DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@contextmanager
def connection(db_path=None):
    """Commit on success, roll back on error, always close."""
    conn = get_connection(db_path)
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()