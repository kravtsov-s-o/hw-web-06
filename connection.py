import psycopg2
from psycopg2 import Error
from contextlib import contextmanager


@contextmanager
def create_connection():
    """Create a connection to a PostgreSQL database"""
    connection = None
    try:
        connection = psycopg2.connect(user="postgres", password="pass", host="localhost", port="5432",
                                      database="test_db")
        yield connection
        connection.commit()
    except Error as err:
        print(err)
        connection.rollback()
    finally:
        connection.close()
