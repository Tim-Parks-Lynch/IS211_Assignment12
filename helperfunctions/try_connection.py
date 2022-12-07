import sqlite3
import sys
import os


def is_sql_file(db_filename: str) -> bool:
    """Tests if the file you are connecting to is a SQLite file.

    Args:
       db_filename (str) : The file location of the sqlite db file

     Returns:
       boolean: returns True if the file is a SQLite file or False if not
    """

    if not os.path.isfile(db_filename):
        return False
    if os.path.getsize(db_filename) < 100:
        return False

    with open(db_filename, "rb") as fd:
        header = fd.read(100)

    return header[0:16] == b"SQLite format 3\000"


def try_connection(db_name):
    """Tests the connection to a sqlite database

    Args:
        db_name (str) : The file location of the sqlite db file

    Returns:
        boolean: returns True if the file is a SQLite file or False if not
    """
    con = None
    cur = None
    if os.path.exists(db_name) and is_sql_file(db_name):
        try:
            print("Trying to connect to database...")
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            cur.execute("SELECT SQLITE_VERSION()")
            data = cur.fetchone()[0]
            if data:
                print(f"Connected to database {db_name}")
                return True
        except sqlite3.Error as e:
            print(f"Error {e.args[0]}")
            sys.exit(1)
        finally:
            if cur:
                cur.close()
            if con:
                con.close()
    else:
        print(
            "Database either does not exist at this location, or is not a database file"
        )
        return False
