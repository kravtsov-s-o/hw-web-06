from psycopg2 import DatabaseError
from connection import create_connection

sql_create_students_groups_table = """
    DROP TABLE IF EXISTS students_groups;
    CREATE TABLE students_groups (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

sql_create_students_table = """
    DROP TABLE IF EXISTS students;
    CREATE TABLE students (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        group_id INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (group_id) REFERENCES students_groups (id)
            ON DELETE SET NULL
            ON UPDATE CASCADE
    );
    """

sql_create_teachers_table = """
    DROP TABLE IF EXISTS teachers;
    CREATE TABLE teachers (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

sql_create_subjects_table = """
    DROP TABLE IF EXISTS subjects;
    CREATE TABLE subjects (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        teacher_id INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (teacher_id) REFERENCES teachers (id)
            ON DELETE SET NULL
            ON UPDATE CASCADE
    );
    """

sql_create_marks_table = """
    DROP TABLE IF EXISTS marks;
    CREATE TABLE marks (
        id SERIAL PRIMARY KEY,
        student_id INTEGER,
        subject_id INTEGER,
        mark SMALLINT CHECK (mark >= 1 AND mark <= 10) NOT NULL,
        date DATE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (student_id) REFERENCES students (id) 
            ON DELETE SET NULL
            ON UPDATE CASCADE,
        FOREIGN KEY (subject_id) REFERENCES subjects (id) 
            ON DELETE SET NULL
            ON UPDATE CASCADE        
    );
    """


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except DatabaseError as err:
        print(err)


if __name__ == "__main__":
    with create_connection() as conn:
        if conn is not None:
            create_table(conn, sql_create_students_groups_table)
            create_table(conn, sql_create_students_table)
            create_table(conn, sql_create_teachers_table)
            create_table(conn, sql_create_subjects_table)
            create_table(conn, sql_create_marks_table)
        else:
            print("Error: Could not create table")
