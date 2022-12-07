from flask import Flask
import sqlite3


app = Flask(__name__)


def init():
    """
    Used to seed the hw13 database with seed data from schema.sql
    """

    sql_script = None

    with open("schema.sql", "r") as sql_file:
        sql_script = sql_file.read()

    db = sqlite3.connect("hw13.db")
    cursor = db.cursor()
    cursor.executescript(sql_script)

    db.commit()
    db.close()


init()
