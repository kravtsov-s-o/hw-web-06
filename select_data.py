import sys
from pathlib import Path
from psycopg2 import DatabaseError
from connection import create_connection


def select_data(filename):
    try:
        with open(filename, 'r') as file:
            sql = file.read()
    except FileExistsError as e:
        print(e)

    try:
        with create_connection() as conn:
            cur = conn.cursor()
            cur.execute(sql)
            return cur.fetchall()
    except DatabaseError as err:
        print(err)


if __name__ == "__main__":
    path = sys.argv[1]
    arg = Path(path)
    print(select_data(arg))
