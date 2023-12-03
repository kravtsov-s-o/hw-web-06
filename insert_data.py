from datetime import datetime
from faker import Faker
from random import randint
from connection import create_connection

NUMBER_OF_STUDENTS = 50
NUMBER_OF_GROUPS = 3
NUMBER_OF_SUBJECTS = 8
NUMBER_OF_TEACHERS = 5
MAX_NUMBER_OF_MARKS = 20


def generate_data(count_groups: int = NUMBER_OF_GROUPS, count_students: int = NUMBER_OF_STUDENTS,
                  count_teachers: int = NUMBER_OF_TEACHERS, count_subjects: int = NUMBER_OF_SUBJECTS):
    group_id = 1
    groups = []
    students = []
    teachers = []
    subjects = []

    fake_data = Faker('uk_UA')

    for _ in range(count_groups):
        groups.append(f'Група {group_id}')
        group_id += 1

    for _ in range(count_students):
        students.append(fake_data.name())

    for _ in range(count_teachers):
        teachers.append(fake_data.name())

    for _ in range(count_subjects):
        subjects.append(fake_data.job())

    return groups, students, teachers, subjects


def prepare_data(groups, students, teachers, subjects):
    for_groups = []
    for_students = []
    for_teachers = []
    for_subjects = []
    for_marks = []

    for group in groups:
        for_groups.append((group,))

    for student in students:
        for_students.append((student, randint(1, len(groups)),))

    for teacher in teachers:
        for_teachers.append((teacher,))

    for subject in subjects:
        for_subjects.append((subject, randint(1, len(teachers)),))

    for i in range(len(students)):
        for j in range(len(subjects)):
            for _ in range(randint(10, MAX_NUMBER_OF_MARKS)):
                date = datetime(2022, randint(1, 12), randint(1, 28)).date()
                for_marks.append((i + 1, j + 1, randint(1, 10), date))

    return for_groups, for_students, for_teachers, for_subjects, for_marks


def insert_into_db(groups, students, teachers, subjects, marks):
    with create_connection() as conn:
        cur = conn.cursor()

        sql_to_groups = """INSERT INTO students_groups(name) VALUES(%s)"""
        sql_to_students = """INSERT INTO students(name, group_id) VALUES(%s, %s)"""
        sql_to_teachers = """INSERT INTO teachers(name) VALUES(%s)"""
        sql_to_subjects = """INSERT INTO subjects(name, teacher_id) VALUES(%s,%s)"""
        sql_to_marks = """INSERT INTO marks(student_id, subject_id, mark, date) VALUES(%s,%s,%s,%s)"""

        try:
            cur.executemany(sql_to_groups, groups)
            cur.executemany(sql_to_students, students)
            cur.executemany(sql_to_teachers, teachers)
            cur.executemany(sql_to_subjects, subjects)
            cur.executemany(sql_to_marks, marks)

            conn.commit()
            print("Success")

        except Exception as e:
            print("Error")
            print(e)
            conn.rollback()


if __name__ == "__main__":
    groups, students, teachers, subjects, marks = prepare_data(*generate_data())
    insert_into_db(groups, students, teachers, subjects, marks)
